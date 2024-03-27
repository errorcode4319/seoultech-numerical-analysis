import numpy as np

def isPositiveDefinite(mat):
    row, col = mat.shape

    if row != col:
        return False 
    
    for i in range(1, row+1):
        am = mat[:i,:i]
        if np.linalg.det(am) <= 0.0:
            return False 
    
    return False


if __name__ == '__main__':
    mat = np.array([[1.0, 2.0, 3.0], 
                    [1.0, 2.0, 1.0], 
                    [0.0, 1.0, 2.0]])

    if isPositiveDefinite(mat):
        print("정부호")
    else:
        print("정부호 아님")