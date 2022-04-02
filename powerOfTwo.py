# return true if a number is a power of two otherwise return false 

def powerOfTwo(num):

    res = None  #4

    if (num) > 1 and num % 2 == 0:
        res = powerOfTwo(num/2)

    elif ((num) > 1 and num % 2 != 0) or num < 1:
        return False
    
    else: 
        return True

    return res
    

if __name__ == '__main__':
    num = 9
    print(powerOfTwo(num))