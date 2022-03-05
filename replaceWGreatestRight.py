def replaceElements(arr):
    greatest = -1
    for i in range(len(arr)-1, -1, -1):
        temp = arr[i]
        arr[i] = greatest
        greatest = max(temp, greatest)
    return arr

if __name__ = "__main__":
    arr = [1,2,3,4,5]
    print(replaceElements(arr))