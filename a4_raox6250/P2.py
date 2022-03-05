import sys

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
        
    print("No solution found!");


def processFile(fileName):
    file = open(fileName, "r+");
    lines = file.readlines();
    if(len(lines) < 2):
        raise Exception("File must have atleast two lines!");
        exit();

    numbers = lines[0].split(",");
    sum = int(lines[1]);
    return [int(x) for x in numbers], sum;


if(__name__ == "__main__"):
    print(main());