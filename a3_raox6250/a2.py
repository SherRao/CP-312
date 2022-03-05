def sortEvenOdd(array, low, high):
    curr = low - 1;
    for i in range(low, high):
        if(array[i] < 0):
            curr += 1;
            array[curr], array[i] = array[i], array[curr];
    
    return;
