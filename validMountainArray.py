from modulefinder import packagePathMap


def validMountainArray(arr):

    # find the index of the peak
    i = 1
    j = 1

    max_value = max(arr)
    max_index = arr.index(max_value)
        
    
    if (len(arr) >= 3) and (0 < max_index < len(arr)-1) :
        while j < len(arr):
            if j <= max_index and (arr[j] <= arr[j-1]):
                return False
            elif j > max_index and (arr[j] >= arr[j-1]):
                return False
            else:
                j += 1
        return True
    
    else:
        return False

if __name__ == "__main__":
    arr = [1,3,3,3,1]
    print(validMountainArray(arr))