def checkIfExist(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        exists = set()
        for i in arr:
            if i in exists:
                return True
            exists.add(i*2)
            exists.add(i/2)
        return False
        
if __name__ == "__main__":
    arr = [1,3,5,7,9]
    print(checkIfExist(arr))