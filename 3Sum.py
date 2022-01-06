def threeSum(nums):

    value_map = {}
    result = []
    for index, value in enumerate(nums):
        value_map[value] = index
    if len(nums) <= 2 :
        return result

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if j != i :
                value = -(i+j)
                if value in value_map and value_map[value] != i and value_map[value] != j:
                    result.append([nums[i], nums[j], value])
    return result

print(threeSum([-1,0,1,2,-1,-4]))

