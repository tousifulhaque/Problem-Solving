def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j = 0
        res = []
        missing = []

        for i in range(len(nums)):
            res.append(False)

        for i in nums:
            res[i-1] = True
        
        for i  in res :
            if i == False:
                missing.append(j+1)
            j += 1

        return missing
        

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))