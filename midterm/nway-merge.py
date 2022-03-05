import math;

"""
A is a list of lists. Each sublist is a list of integers.
"""
def nway_merge(A):
    if len(A) <= 1:
        return A[0];

    else:
        B = nway_merge(A[0:len(A)//2]);
        C = nway_merge(A[len(A)//2:len(A)]);
        return merge(B, C);

def merge(A, B):
    return A + B;


def main():
    A = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ];
    print(nway_merge(A));

main();