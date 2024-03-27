import numpy as np 

def innerMat(A, B):
    rowA, colA = A.shape 
    rowB, colB = B.shape 

    if colA != rowB:
        print("행렬곱 불가")
        return None 
    
    C = np.ndarray([rowA, colB])

    for i in range(rowA):
        for j in range(colB):
            C[i, j] = 0.0
            for k in range(colA):
                C[i, j] += A[i, k] * B[k, j]

    return C 

if __name__ == "__main__":
    A = np.array([[1.1, 1.2, 1.3], [2.1, 2.2, 2.3]])
    B = np.array([[1.1, 1.2], [2.1, 2.2], [3.1, 3.2]])

    C = innerMat(A, B)
    print(C)