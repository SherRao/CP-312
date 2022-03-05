"""
A and B are lists of 2-element vectors. The first subelement is the coefficient, and the second is the x term.

Example:
    A = [ [1, 2], [3, 1] ]
    B = [ [7, 2], [9, 1] ]
"""
def efficientPolynomialMultiplication(A, B):
    A1 = []; # Stores the first half of the co-efficients of A.
    A2 = []; # Stores the second half of the co-efficients of A.
    B1 = []; # Stores the first half of the co-efficients of B.
    B2 = []; # Stores the second half of the co-efficients of B.

    # The degree of the polynomials - assumes both polynomials are the same degree.
    n = len(A) - 1; 

    # If the polynomials are of degree 1, then we can just simply multiply them.
    # (A_00*x^A_01 + A_10*x^A_11) (B_00*x^B_01 + B_10*x^B_11)
    if n == 1:
        result = [];
        result[0][0] = A[0][0] * B[0][0];
        result[0][1] = A[0][1] + B[0][1];  
        result[1][0] = A[1][0] * B[0][0] + A[0][0] * B[1][0];
        result[1][1] = A[1][1] + B[0][1] + A[0][1] * B[1][1];
        result[2][0] = A[1][0] * B[1][0];
        result[2][1] = A[1][1] + B[1][1];
        return result;

    # Calculates the midpoint of A.
    mid = n // 2;

    # Calculates the values for the first half of A and B.
    for i in range(0, mid):
        A1[i][0] = A[i][0];
        A1[i][1] = A[i][1];
        B1[i][0] = B[i][0];
        B1[i][1] = B[i][1];

    # Calculate the values for the second half of A and B.
    for i in range(mid + 1, n):
        A2[i][0] = A[i][0];
        A2[i][1] = x^(i - mid + 1);
        B2[i][0] = B[i][0];
        B2[i][1] = x^(i - mid + 1);

    # Recursively call the function on the two halves of A and B.
    Q = efficientPolynomialMultiplication(A1+A2, B1+B2);
    X = efficientPolynomialMultiplication(A1, B1);
    W = efficientPolynomialMultiplication(A2, B2);
    return X + (Q - X - W) * X^(n/2) + W*X^n;





    