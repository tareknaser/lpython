from ltypes import i32, f64
from copy import deepcopy

def check_mat_and_vec(mat: list[list[f64]], vec: list[f64]):
    rows: i32 = len(mat)
    cols: i32 = len(vec)
    i: i32
    j: i32

    for i in range(rows):
        for j in range(cols):
            assert mat[i][j] == float(i + j)

    for i in range(cols):
        assert vec[i] == 2.0 * float(i)

def test_list_of_lists():
    tensors: list[list[list[list[f64]]]] = []
    tensor: list[list[list[f64]]] = []
    mat: list[list[f64]] = []
    vec: list[f64] = []
    rows: i32 = 10
    cols: i32 = 5
    i: i32
    j: i32
    k: i32
    l: i32

    for i in range(rows):
        for j in range(cols):
            vec.append(float(i + j))
        mat.append(deepcopy(vec))
        vec.clear()

    for i in range(cols):
        vec.append(2.0 * float(i))

    check_mat_and_vec(mat, vec)

    for k in range(rows):
        tensor.append(deepcopy(mat))
        for i in range(rows):
            for j in range(cols):
                mat[i][j] += float(1)

    for k in range(rows):
        for i in range(rows):
            for j in range(cols):
                assert mat[i][j] - tensor[k][i][j] == f64(rows - k)

    for l in range(2 * rows):
        tensors.append(deepcopy(tensor))
        for i in range(rows):
            for j in range(rows):
                for k in range(cols):
                    tensor[i][j][k] += float(1)

    for l in range(2 *  rows):
        for i in range(rows):
            for j in range(rows):
                for k in range(cols):
                    assert tensor[i][j][k] - tensors[l][i][j][k] == f64(2 * rows - l)

test_list_of_lists()
