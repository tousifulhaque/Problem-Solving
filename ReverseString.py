class Solution():

    def reverseString(self, s):
        self.string = s
        self.fronpointer = 0

        i = 0
        def recursiveReverse(i):

            if i == len(self.string):
                return 
            
            else: 
                recursiveReverse(i+1)
            
            if self.fronpointer < i:
                self.string[self.fronpointer] ,self.string[i] = self.string[i], self.string[self.fronpointer] 
                self.fronpointer = self.fronpointer + 1
            
            return self.string
        
        return recursiveReverse(0)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))