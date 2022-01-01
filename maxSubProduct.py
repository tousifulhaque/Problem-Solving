def maxProduct( nums):
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum = curr_sum + num
        max_sum = max(curr_sum, max_sum)
    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum = curr_sum + num
        max_sum = max(curr_sum, max_sum)
    return max_sum
