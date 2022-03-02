def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
                
            i +=1


if __name__ = "__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    val = 1
    removeElement(nums, val)
    print(nums)