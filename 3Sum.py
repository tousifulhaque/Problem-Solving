def threeSum(nums):
    value_map = {}
    result = set()
    for index , value in enumerate(nums):
        value_map[value] = index
    if len(nums) >= 2 :
        return result

    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i:

    return value_map

print(threeSum([1,2]))

