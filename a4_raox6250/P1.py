"""
CP 312 - Assignment 4
P1.py

@author Nausher Rao (190906250)
@author Will Roberts (191023880)
"""
import sys;

def main():
    args = sys.argv;
    if(len(args) == 0):
        raise Exception("Program needs a file to run!");
        exit();

    numbers, pluses, minuses = processFile(str(args[1]));
    numbers.sort();
    result = [];
    sum = 0;
    
    for x in numbers:
        if(minuses > 0):
            sum -= x;
            minuses -= 1;
            result.append("-");
            result.append(x);

        else:
            sum += x;
            pluses -= 1;
            result.append("+");
            result.append(x);

    return sum, result;


def processFile(fileName):
    file = open(fileName, "r+");
    lines = file.readlines();
    print(lines);
    if(len(lines) < 3):
        raise Exception("File must have atleast three lines!");
        exit();

    numbers = lines[0].strip().split(",");
    positives = int(lines[1].strip());
    negatives = int(lines[2].strip());
    return [int(x) for x in numbers], positives, negatives;


if(__name__ == "__main__"):
    print(main());