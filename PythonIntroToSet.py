# Python introduction to Set
def average(array):
    # your code goes here
    array = set(array)
    narr = (sum(array))/len(array)
    return round(narr, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
