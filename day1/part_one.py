if __name__ == '__main__':
    with open('./data.txt') as file:
        sum = 0
        for item in file:
            numbers = [None]*2
            for idx in range(len(item)):
                if item[idx].isdigit():
                    if numbers[0] is None:
                        numbers[0] = item[idx]
                    numbers[1] = item[idx]
            sum += int(f"{numbers[0]}{numbers[1]}")
        print(sum)