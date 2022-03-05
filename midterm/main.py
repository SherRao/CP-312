import math;
import time

def maximum(A, i, j):
    if j-i <= 1:
        return max(A[i], A[j])

    else:
        m1 = maximum(A, i, math.floor((i + j)/2));
        m2 = maximum(A, math.floor((i+j)/2)+1, j);

    return( max(m1, m2) );

start_time = time.time()
result = maximum(list(range(0, 1000)), 0, 999);
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
result = maximum(list(range(0, 2000)), 0, 1999);
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
result = maximum(list(range(0, 4000)), 0, 3999);
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
result = maximum(list(range(0, 8000)), 0, 7999);
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
result = maximum(list(range(0, 16000)), 0, 15999);
print("--- %s seconds ---" % (time.time() - start_time))
