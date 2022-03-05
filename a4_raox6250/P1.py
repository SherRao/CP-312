import sys

def main():
    args = sys.argv;
    if(len(args) == 0):
        raise Exception("Program needs a file to run!");
        exit();

    numbers, pluses, minuses = processFile(str(args[1]));
    numbers.sort();
    
    result = [];
    sum = 0;
    i = 0;
    for i in range(len(numbers)):
        if(minuses > 0):
            sum -= numbers[i];
            minuses -= 1;
            result.append("-");
            result.append(numbers[i]);

        else:
            sum += numbers[i];
            pluses -= 1;
            result.append("+");
            result.append(numbers[i]);

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
