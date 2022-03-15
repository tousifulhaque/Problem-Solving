from jinja2 import Undefined


def thirdMaximumNumber(nums):
    maxi = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')

    for num in nums:
        if num > maxi:
            third_max = second_max
            second_max = maxi
            maxi = num
        
        elif num < maxi:
            if third_max < num < second_max :
                third_max = num
            if num > second_max:
                third_max = second_max
                second_max = num

        else:
            pass

    if third_max == float('-inf'):
        return maxi
    
    else:
        return third_max

     
if __name__ == "__main__":
    nums = [3,2,1]
    print(thirdMaximumNumber(nums))