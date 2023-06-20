'''
@file   sorvspoisson.py
@author Thanasis Mattas, 2019

Produces different scenarios for further meta-analysis of the solution
parameters selection.

SORvsPoisson is free software; you may redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

import numpy as np
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
from timeit import default_timer as timer
import pandas as pd
import warnings


warnings.filterwarnings("error")


"""
                            X                   i-1        i
                    L       ►
           0 1 2 3 4 5 6 7 8 9        j+1   ○         ○         ○
           ===================
        0  G G G G G G G G G G                   ■   ◄ S2  ■         j
        1  G - - - - - - - - G
      W 2  G - - - - - - - - G         j    ○    S3   ○    ▲    ○
        3  G - - - - - - - - G                   ▼         S1
        4  G - - - - - - - - G                   ■   S4 ►  ■        j-1
     Y▼ 5  G G G G G G G G G G
           ===================        j-1   ○         ○         ○

                                           i-1        i        i+1


G: ghost node - boundary conditions        ○ : basic mesh       m * h
                                           ■ : staggered mesh   (2m + 1) * h
"""


def mesh(L, W, h):
    """
    generates a cartetian (stuctured) mesh
    --------------------------------------
    @L             : length along x axis
    @W             : width along y axis
    @h             : descritization step
    returns X, Y   : np.meshgrid
    """
    x = np.arange(0, L + h, h)
    y = np.arange(0, W + h, h)
    return np.meshgrid(x, y)


def permittivity(a, b, c, h, *meshgrid):
    """
    populates the permittivity function on the grid
    -----------------------------------------------
              perm(x,y) = ax^2 + by^2 + c
    """
    # permittivity populates the staggered mesh
    X, Y = meshgrid
    X = X + h / 2
    Y = Y + h / 2
    X = X[:-1, :-1]
    Y = Y[:-1, :-1]
    return a * X**2 + b * Y**2 + c


def source(p, q, r, *meshgrid):
    """
    populates the source function distribution on the grid
    ------------------------------------------------------
               f(x,y) = ax^2 + by^2 + c
    """
    X, Y = meshgrid
    return p * X**2 + q * Y**2 + r


def combinations(*args):
    """
    It takes all the feature-lists, where each feature-list contains the
    different values
    that the corresponding feature takes, and creates all possible combinations.
    Namely,
    every combination (simulation configuration) will have one value of each
    feature-list.

    @param *args         : iterable of iterables (list of feature-lists)
    returns comb_list    : iterable of iterables (list of combinations)
    """
    comb_list = []
    for values in itertools.product(*args):
        comb_list.append([value for value in values])
    return comb_list


def boundaryConditions(u, f):
    """
    applies Neumann boundary conditions
    -----------------------------------
    The rate of change of the function u at the borders of the domain is equal
    to the rate of change of the source function f. The rates are evaluated,
    using 1st order central differences.

    currently: left and right borders
    """

    # - top    (du/dy = df/dy)
    #   (u(i, 0) - u(i, 2)) / 2h = (f(i, 0) - f(i, 2)) / 2h
    # u[0, :] = u[2, :] + f[0, :] - f[2, :]
    # - bot    (du/dy = df/dy)
    #   (u(i, Ny) - u(i, Ny-2)) / 2h = (f(i, Ny) - f(i, Ny-2)) / 2h
    # u[-1, :] = u[-3, :] + f[-1, :] - f[-3, :]
    # - left   (du/dx = df/dx)
    #   (u(0, j) - u(2, j)) / 2h = (f(0, j) - f(2, j)) / 2h
    u[:, 0] = u[:, 2] + f[:, 0] - f[:, 2]
    # - right  (du/dx = df/dx)
    #   (u(Nx, j) - u(Nx-2, j)) / 2h = (f(Nx, j) - f(Nx-2, j)) / 2h
    u[:, -1] = u[:, -3] + f[:, -1] - f[:, -3]


def initialization(L, W, Nx, Ny, u_top, u_bot, f, *meshgrid):
    """
    populates the function u on the mesh and initializes it to the \
    interpolation of the values on the boundaries
    """
    X, Y = meshgrid

    # populate the mesh with function u
    u = np.zeros_like(X)
    # apply Dirichlet boundary conditions
    u[0, :] = u_top
    u[-1, :] = u_bot
    # u[:, 0] = u_left
    # u[:, -1] = u_right
    boundaryConditions(u, f)

    # vertical interpolation
    y_borders_values = np.array([0, W])
    u_vert_borders_values = np.array([[u[0, i], u[-1, i]] for i in range(Nx)])
    yvals = np.linspace(0, W, Ny)

    uy_inter = np.zeros_like(u)
    for column in range(Nx):
        uy_inter[:, column] = np.interp(yvals, y_borders_values,
                                        u_vert_borders_values[column])

    """
    # horizontal interpolation
    x_borders_values = np.array([0, L])
    u_hor_borders_values = np.array([[u[i, 0], u[i, -1]] for i in range(Ny)])
    xvals = np.linspace(0, L, Nx)

    ux_inter = np.zeros_like(u)
    for row in range(Ny):
        ux_inter[row, :] = np.interp(xvals, x_borders_values,
                                     u_hor_borders_values[row])


    # final interpolation as the mean of verical and horizontal
    u[1:-1, 1:-1] = (uy_inter[1:-1, 1:-1] + ux_inter[1:-1, 1:-1]) / 2
    """
    u[1:-1, 1:-1] = uy_inter[1:-1, 1:-1]

    return u


def factors(perm):
    """
    generates the factors of the 5-point Liebmann scheme
    ----------------------------------------------------
    @param perm                 : permittivity distribution on the mesh
    returns a0, a1, a2, a3, a4  : the factors
    """
    # a0 = e_r(i-1, j) + e_r(i, j) + e_r(i, j-1) + e_r(i-1, j-1)
    a0 = perm[1:, :-1] + perm[1:, 1:] + perm[:-1, 1:] + perm[:-1, :-1]
    # a1 = 1/2 * (e_r(i, j-1) + e_r(i, j))
    a1 = 0.5 * (perm[:-1, 1:] + perm[1:, 1:])
    # a2 = 1/2 * (e_r(i-1, j) + e_r(i, j))
    a2 = 0.5 * (perm[1:, :-1] + perm[1:, 1:])
    # a3 = 1/2 * (e_r(i-1, j-1) + e_r(i-1, j))
    a3 = 0.5 * (perm[:-1, :-1] + perm[1:, :-1])
    # a4 = 1/2 * (e_r(i, j-1) + e_r(i-1, j-1))
    a4 = 0.5 * (perm[:-1, 1:] + perm[:-1, :-1])
    return a0, a1, a2, a3, a4


def main():
    # Simulation termination criteria
    # - tolerance
    # - max iterations
    __TOL__ = 10**-5
    __ITER_MAX__ = 2 * 10**5

    # features (dimensions) of the problem (9)
    # --------
    # (expressed with ranges, in order to later produce the different
    # compinations, that will constitute the data-set)
    # {
    #
    # grid boundaries
    # L: length, along the x axis
    # W: width, along the y axis
    L = np.array([1])
    W = np.array([1])

    # spatial descritization step
    h = np.array([0.005, 0.01, 0.02])

    # Dirichlet boundary conditions
    u_top = np.linspace(10, 20, 3)
    u_bot = np.linspace(10, 20, 3)
    # u_right = np.linspace(10, 20, 2)
    # u_left = np.linspace(10, 20, 2)

    # assuming permittivity is not constant, but a function of x, y:
    #            perm = ax^2 + by^2 + c
    a = np.linspace(-0.2, 0.3, 3)
    b = np.linspace(-0.2, 0.3, 3)
    c = np.linspace(1.5, 2.5, 3)

    # source or forcing function, f(x,y) = px^2 + qy^2 + r
    p = np.linspace(-10, -2, 3)
    q = np.linspace(-10, -2, 3)
    r = np.linspace(-20, -5, 3)
    #
    # }

    # create the combinations, that will constitute the design matrix
    dataset = combinations(L, W, h, a, b, c, p, q, r, u_top, u_bot)
    print(len(dataset))

    # print dataset in pandas DataFrame format
    test_indices = [0, 1000, 2000, 10000, 15000]
    df = pd.DataFrame(
        [dataset[point] for point in test_indices],
        columns=['L', 'W', 'h', 'a', 'b', 'c', 'p', 'q', 'r', 'u_top', 'u_bot']
    )
    # print(df[:1])

    # this will hold the optimum omega for all datapoints and it will constitute
    # the y-vector of the dataset
    optimum_omega_array = np.array([])

    iters_array = np.array([])
    time_array = np.array([])
    tolerance_array = np.array([])

    # iterate through each data-point, to find its optimum relaxation factor
    for datapoint in test_indices:
        # time each datapoint
        start = timer()

        # unpack the datapoint-list to features
        L, W, h, a, b, c, p, q, r, u_top, u_bot = dataset[datapoint]

        # number of nodes at x and y axis
        Nx = int(L / h + 1)
        Ny = int(W / h + 1)

        # generate mesh
        X, Y = mesh(L, W, h)

        # source function distribution
        f = source(p, q, r, X, Y)

        # permittivity distribution
        perm = permittivity(a, b, c, h, X, Y)

        # initialization
        u = initialization(L, W, Nx, Ny, u_top, u_bot, f, X, Y)

        # generate the factors of the 5-point iterative scheme
        a0, a1, a2, a3, a4 = factors(perm)

        # this will hold the number of the iterations needed with the previous
        # relaxation factor, in order to compare it with the current one and,
        # thus, to perform a binary research of the optimum omega
        iterations = __ITER_MAX__

        # this will hold the optimum_omega for the binary research
        optimum_omega = 1.0

        tol = __TOL__

        # iterate through the values of the relaxation factor, omega
        for omega in np.arange(0.2, 1.2, 0.2):
            # solution
            iter = 0
            tolerance = 2
            while tolerance > __TOL__ and iter < __ITER_MAX__:
                try:
                    iter += 1

                    # update boundary conditions
                    # --------------------------
                    # borders of the rectangular domain:
                    # - top and bot    : Dirichlet (set at initialization)
                    # - left and right : Neumann   (du/dx = df/dx)
                    boundaryConditions(u, f)

                    # Successive Over Relaxation scheme
                    # ---------------------------------
                    #                                      a2
                    # u_new(i,j) = u(i,j) + omega/a0 [{a3 -a0 a1} u(i,j)
                    #                                      a4
                    #                                 - h^2 f(i,j)]
                    #
                    u_new = u[1:-1, 1:-1] + omega / a0 * (
                        a3 * u[1:-1, :-2]
                        + a2 * u[2:, 1:-1]
                        + a1 * u[1:-1, 2:]
                        + a4 * u[:-2, 1:-1]
                        - a0 * u[1:-1, 1:-1]
                        - h**2 * f[1:-1, 1:-1]
                    )
                    # mean residual of the nodes
                    tolerance = (np.sum(np.abs(u_new - u[1:-1, 1:-1]))
                                 / ((Nx - 2) * (Ny - 2)))

                    u[1:-1, 1:-1] = u_new
                    print('iter: ', iter, '  tol: {0:.7f}'.format(tolerance))

                except RuntimeWarning:
                    break
            if tolerance > 1:
                pass
            else:
                if iter < iterations:
                    iterations = iter
                    omega_optimum = omega
                    tol = tolerance

        end = timer()
        min = str(int(np.floor((end - start)) / 60))
        sec = str(int((end - start) % 60))
        min_zeros = (2 - len(str(min))) * '0'
        sec_zeros = (2 - len(str(sec))) * '0'
        dtpoint_duration = min_zeros + min + ':' + sec_zeros + sec

        # append values to the corresponding arrays
        optimum_omega_array = np.append(optimum_omega_array, omega_optimum)
        iters_array = np.append(iters_array, iterations)
        time_array = np.append(time_array, dtpoint_duration)
        tolerance_array = np. append(tolerance_array, tol)

    # print(optimum_omega_array)
    # print(iters_array)
    # print(time_array)
    # print(tolerance_array)

    # append columns to the dataset matrix
    df['omega_opt'] = optimum_omega_array
    df['iterations'] = iters_array
    df['time'] = time_array
    df['tolerance'] = tolerance_array

    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None):
        print(df)

    fig = plt.figure()

    sub1 = fig.add_subplot(121, projection='3d')
    sub1.plot_surface(X[1:-1, 1:-1], Y[1:-1, 1:-1], u[1:-1, 1:-1])
    sub1.title.set_text('u')
    sub1.set_xlabel('x')
    sub1.set_ylabel('y')
    sub1.set_zlabel('u')

    sub2 = fig.add_subplot(122, projection='3d')
    sub2.plot_surface(X[1:-1, 1:-1], Y[1:-1, 1:-1], f[1:-1, 1:-1])
    sub2.title.set_text('f')
    sub2.set_xlabel('x')
    sub2.set_ylabel('y')
    sub2.set_zlabel('f')

    # sub3 = fig.add_subplot(133, projection='3d')
    # sub3.plot_surface(X[1:,1:], Y[1:,1:], perm)
    # sub3.title.set_text('perm')

    plt.show()


if __name__ == '__main__':
    main()
