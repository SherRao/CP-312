import sys

def main():
    args = sys.argv;
    if(len(args) == 0):
        raise Exception("Program needs a file to run!");
        exit();

    numbers, pluses, minuses = processFile(str(args[0]));
    maxNumbers = pluses + minuses;
    numbers.sort();

    result = "";
    sum = 0;
    i = len(numbers) - 1;
    for n in positives:
        if(i == len(numbers)):
            break;

        result += numbers[i];
        if(i >= 1):
            result += " + ";

        sum += numbers[i];
        i -= 1;

    for n in negatives:
        if(i == len(numbers)):
            break;

        result += f"({numbers[i]})";
        if(i >= 1):
            result += " - ";

        sum -= numbers[i];
        i -= 1;

    result += " = " + sum;
    return result;



def processFile(fileName):
    file = open(fileName, "r+");
    lines = file.readlines();
    if(len(lines) < 3):
        raise Exception("File must have atleast three lines!");
        exit();

    numbers = lines[0];
    positives = int(lines[1]);
    negatives = int(lines[2]);

    return ([int(x) for x in numbers], positives, negatives);
