def sortArrayByParity(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        oddPointer = 0
        evenPointer = len(nums) - 1 
        
        while oddPointer < evenPointer:
            if nums[oddPointer] % 2 != 0 and nums[evenPointer] % 2 == 0:
                nums[oddPointer] , nums[evenPointer] = nums[evenPointer] , nums[oddPointer]
                evenPointer -= 1 
                oddPointer += 1

            elif nums[oddPointer] % 2 == 0 and nums[evenPointer] % 2 != 0:
                evenPointer -= 1 
                oddPointer += 1
            elif nums[oddPointer] % 2 == 0 and nums[evenPointer] % 2 == 0:
                oddPointer +=1
            else:
                evenPointer -= 1
            
if __name__ == "__main__":
    nums = [3,2,1,4]
    sortArrayByParity(nums)
    print(nums)