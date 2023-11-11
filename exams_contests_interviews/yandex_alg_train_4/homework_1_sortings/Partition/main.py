def partition(arr, x):
    result = 0
    for element in arr:
        if element < x:
            result += 1
    return result


if __name__ == "__main__":
    N = int(input())
    array = [int(elm) for elm in input().split()]
    x = int(input())
    number_of_less = partition(array, x)
    print(f"{number_of_less}\n{N-number_of_less}")
