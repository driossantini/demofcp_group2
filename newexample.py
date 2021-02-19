import sys
import statistics
from collections import Counter

def average(n):
    aver = sum(n)/len(n)
    return aver

def mode(n):

    return Counter(n).most_common(1)[0][0]


def median(n):
    return statistics.median(n)

def main(args):
    NUMBERS = []
    for x in args:
        try:
            NUMBERS.append(float(x))
        except:
            pass
    
    if '--average' in args:
        print(f'Average: {average(NUMBERS)}')

    if '--mode' in args:
        print(f'Mode: {mode(NUMBERS)}')

    if '--median' in args:
        print(f'Median: {median(NUMBERS)}')

    if len (NUMBERS) == len(args):
        print(f'Average: {average(NUMBERS)}')
        print(f'Mode: {mode(NUMBERS)}')
        print(f'Median: {median(NUMBERS)}')

    print("My name is David RS example")


if __name__ == "__main__":
    main(sys.argv[1:])