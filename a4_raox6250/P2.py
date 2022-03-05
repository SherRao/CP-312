import sys

def main(num_list, value):
    list_len = len(num_list);

    # Keys = sum value 
    # Values = minimum number of items to sum (base case 0)
    value_table = [0];

    # Initialize all table values to MAX
    for i in range(1, value + 1):
        value_table.append(sys.maxsize);

    # try every combination that is smaller than <value>
    for i in range(1, value+1):
        for j in range(0, list_len):
            if (num_list[j] <= i):
                tmp = value_table[i-num_list[j]]
                if ((tmp != sys.maxsize) and (tmp + 1 < value_table[i])):
                    value_table[i] = tmp + 1

    return value_table;



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
    fileName = str(sys.argv[1]);
    numbers, sum = processFile(fileName);
    print(main(numbers, sum));