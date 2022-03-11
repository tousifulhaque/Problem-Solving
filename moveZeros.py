def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        readPointer = 0
        numberPointer = 0

        if 0 in nums:
            while readPointer < len(nums) :
                if nums[readPointer] != 0:
                    nums[numberPointer] =  nums[readPointer]
                    numberPointer += 1 #1

                readPointer += 1 #1

            while numberPointer < len(nums):
                nums[numberPointer] = 0
                numberPointer += 1