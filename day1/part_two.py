import re

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        result = 0
        for line in file:
            numbers = []
            for i, c in enumerate(line):
                if c.isdigit():
                    numbers.append(c)
                for d, val in enumerate([
                    'one',
                    'two',
                    'three',
                    'four',
                    'five',
                    'six',
                    'seven',
                    'eight',
                    'nine'
                ]):
                    if line[i:].startswith(val):
                        numbers.append(str(d + 1))
            result += int(numbers[0] + numbers[-1])
        print(result)
