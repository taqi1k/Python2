#1863528
#taqi syed

def selection_sort_descend_trace(numbers):
    for index in range(len(numbers) - 1):
        value = index
        for k in range(index + 1, len(numbers)):
            if numbers[value] < numbers[k]:
                value = k
        numbers[index], numbers[value] = numbers[value], numbers[index]
        for value in numbers:
            print(value, end=" ")
        print()
    return numbers

if __name__ == "__main__":
    numbers = []
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)