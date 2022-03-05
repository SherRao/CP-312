"""
Applies an improved merge-sort algorithm by using an iterative solution.
"""
def mergeSort(A):
    sorted = [];
    while(len(A) > 0):
        i = 0;
        min = A[i];

        for j in range(len(A)):
            if A[j][1] < min:
                min = A[i];
                i = j;

        sorted.append(A.pop(i));
    
    return sorted;