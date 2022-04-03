# return true if a number is a power of two otherwise return false 


import math
class Solution(object):
    def powerOfTwo(self, num):
        # res = None  #4

        # if (num) > 1 and num % 2 == 0:
        #     res = powerOfTwo(num/2)

        # elif ((num) > 1 and num % 2 != 0) or num < 1:
        #     return False
        
        # else: 
        #     return True

        # return res

        ####### Solution without any loop ########

        if bin(num).count("1") == 1 and num > 0:
            return True
        
        else:
            return False


    

if __name__ == '__main__':
    num = -29
    solution = Solution()
    print(solution.powerOfTwo(num))