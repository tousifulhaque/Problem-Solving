def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                continue
            
            i += 1

if __name__ == "__main__":
    nums = [1,1,2,3,3,3,4,5,6,6,6,7,7,7,8,8,8,8,9,9,9,9,9]
    removeDuplicates(nums)
    print(nums)