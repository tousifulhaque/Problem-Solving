
def sub_lists(nums):
    current_sum = nums[0]
    best_sum = nums[0]
    for item in nums[1:]:
        print(item)
        print(f'Sum {item+current_sum}')
        current_sum = max(item, current_sum + item)
        best_sum = max(best_sum, current_sum)
    return best_sum


print(sub_lists([-2, 1, -3, -1, 2]))
