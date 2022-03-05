import sys

def main():
    args = sys.argv;
    if(len(args) == 0):
        raise Exception("Program needs a file to run!");
        exit();

    numbers, pluses, minuses = processFile(str(args[1]));
    maxNumbers = pluses + minuses;
    numbers.sort();

    result = "";
    sum = 0;
    i = len(numbers) - 1;
    for n in range(pluses):
        if(i == len(numbers)):
            break;

        result += str(numbers[i]);
        if(i >= 1):
            result += " + ";

        sum += numbers[i];
        i -= 1;

    for n in range(minuses):
        if(i == len(numbers)):
            break;

        result += f"({numbers[i]})";
        if(i >= 1):
            result += " - ";

        sum -= numbers[i];
        i -= 1;

    result += " = " + str(sum);
    return result;


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
