def heightChecker( heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights = sorted(heights)
        
        i = 0 
        count = 0
        
        while i < len(heights):
            
            if sorted_heights[i] != heights[i]:
                count +=1
            
            i  += 1
        
        return count

if __name__ == "__main__":
    heights = [5,1,2,3,4]
    heightChecker(heights)
    print(heightChecker(heights))