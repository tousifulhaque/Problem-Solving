def checkIfExist(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        j = i + 1
        isDouble = False
        
        while i < len(arr):
            while j < len(arr):
                if arr[j] == (arr[i] * 2):
                    isDouble = True 
                    return isDouble 
                j += 1

            i += 1
            j  = i + 1
        
        return isDouble

if __name__ == "__main__":
    arr = [1,3,5,7,9]
    print(checkIfExist(arr))