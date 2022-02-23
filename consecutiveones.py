def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=1
        l= 0
        max_size = 0
        
        #[1,0,1,1,0,1]
        if len(nums) > 1:
            while r < len(nums):
                if nums[r] == 1 and nums[r-1] != 1:
                    l = r # 2
                    max_size = max(r-l+1, max_size)
                
                if nums[r] == 1 and nums[r-1] == 1:
                    max_size = max(r-l+1, max_size)
                    
                if nums[r] != 1 and nums[r-1] == 1:  
                    max_size = max(r-l, max_size)
                    
                r +=1
        else:
            if nums[l] == 1:
                return 1
            
            else:
                return 0
            
        return max_size