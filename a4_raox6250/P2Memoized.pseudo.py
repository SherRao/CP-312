from cgitb import lookup


def main():
    args = sys.argv;
    if(len(args) == 0):
        raise Exception("Program needs a file to run!");
        exit();

    numbers, sum = processFile(str(args[1]));
    numbers.reverse();

    for x in numbers:
        if(sum % x == 0):
            print(sum // x, "packages of size", x);
            exit(0);
        
    print("-1 -> No solution found!");

# The key for this dictionary is a tuple of the sizes and the sum
lookupTable = {};

def minPack(sizes, m):
    key = (sizes, m);
    if(key in lookupTable):
        return lookupTable[(sizes, m)];

    elif(len(sizes) == 0):
        return -1;

    elif(m % sizes[-1] == 0):
        result = m // sizes[-1];
        lookupTable[key] = result
        
        return result;

    else:
        return minPack(sizes[:-1], m)
