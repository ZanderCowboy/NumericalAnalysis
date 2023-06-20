'''
@file   sorvspoisson_test.py
@author Thanasis Mattas, 2019

tests of sorvspoisson.py

SORvsPoisson is free software; you may redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

import sorvspoisson as sor
import numpy as np


# permittivity of the void
__e0__ = 8.854 * 10**-12


# def test_h():
#     assert(np.round(sor.h(300), 3) == np.array([1., 1.333, 1.667, 2.])


def test_mesh():
    X = [[0, 1, 2, 3],
         [0, 1, 2, 3],
         [0, 1, 2, 3],
         [0, 1, 2, 3]]

    Y = [[0, 0, 0, 0],
         [1, 1, 1, 1],
         [2, 2, 2, 2],
         [3, 3, 3, 3]]
    assert sor.mesh(3, 3, 1) == X, Y


def test_e_r():
    X = [[0, 1, 2, 3],
         [0, 1, 2, 3],
         [0, 1, 2, 3],
         [0, 1, 2, 3]]

    Y = [[0, 0, 0, 0],
         [1, 1, 1, 1],
         [2, 2, 2, 2],
         [3, 3, 3, 3]]

    a, b, c = 1, 2, 1

    result = [[1, 1, 1, 1],
              [4, 4, 4, 4],
              [11, 11, 11, 11],
              [22, 22, 22, 22]]
    assert(sor.e_r(a, b, c, X, Y) == result)


def test_source():
    p, q, r = -1, -2, -3

    X = [[0, 1, 2],
         [0, 1, 2],
         [0, 1, 2]]

    Y = [[0, 0, 0],
         [1, 1, 1],
         [2, 2, 2]]

    result = [[- 3, - 4, - 7],
              [- 5, - 6, - 9],
              [-11, -12, -15]]

    assert(sor.charge_density(p, q, r, X, Y) == result)


def test_combinations():
    L = np.array([1, 2])
    d = np.array([11, 22])
    w = np.array([111, 222])

    result = [[1, 11, 111],
              [1, 11, 222],
              [1, 22, 111],
              [1, 22, 222],
              [2, 11, 111],
              [2, 11, 222],
              [2, 22, 111],
              [2, 22, 222]]

    assert(sor.combinations(L, d, w) == result)
