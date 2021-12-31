def subArrayMaxSum(list):
    max_sum = 0
    curr_sum = 0
    for num in list:
        if num >= 0 and curr_sum >= 0 :#-2 0
            curr_sum = curr_sum + num
            max_sum = max(curr_sum, max_sum)
        elif num <= 0 and curr_sum >= 0 :
            curr_sum = curr_sum + num #-2
            max_sum = max(curr_sum, max_sum)
        elif num <= 0 and curr_sum <= 0 :
            curr_sum = curr_sum + num #-2
            max_sum = max(curr_sum, max_sum)
        else:
            curr_sum = num
    return max_sum
list = [-2,1,-3,4,-1,2,1,-5,4]
print(subArrayMaxSum(list))
