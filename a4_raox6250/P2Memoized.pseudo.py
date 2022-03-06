# The key for this dictionary is a tuple of the sizes and the sum
lookupTable = {};

def main(packageSizes, totalSize):
    # The key for the lookup table for this pair of arguments.
    key = (packageSizes, totalSize);

    # Returns the value in the lookup table that has already been calculated.
    if(key in lookupTable):
        return lookupTable[key];

    # If there is no solution.
    elif(len(packageSizes) == 0):
        return -1;

    # If the total size is a factor of the last package size, then the last package is the solution.
    elif(totalSize % packageSizes[-1] == 0):
        result = totalSize // packageSizes[-1];
        lookupTable[key] = result;
        
        return result;

    # The last package is not the solution -> Lets go to the next last package size.
    else:
        return main(packageSizes[:-1], totalSize);