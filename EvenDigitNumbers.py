def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digit_count = 0
        even_digits = 0
        
        for num in nums:
            while num != 0:
                num = num // 10 
                digit_count += 1
            
            if digit_count % 2 == 0:
                even_digits += 1
            
            digit_count = 0
            
        return even_digits