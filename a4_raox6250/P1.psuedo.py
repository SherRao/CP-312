def main():
    p = getPositiveAmount();
    n = getNegativeAmount()
    numbers = getNumbersList();

    # sort the numbers in ascending order.
    numbers.sort();

    sum = 0;
    result = [];

    for x in numbers:
        if(n > 0):
            sum = sum - x;
            n = n - 1;

            # record that this number was a negative.
            result.add("-");
            result.add(x);

        else:
            sum = sum + x;
            p = p - 1;

            # record that this number was a positive.
            result.add("+");
            result.add(x);

    return sum, result;

def getPositiveAmount():
    pass;

def getNegativeAmount():
    pass;

def getNumbersList():
    pass;