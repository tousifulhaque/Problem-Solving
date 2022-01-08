def threeSum(nums):

    nums.sort()
    print(nums)
    value_map = {}
    result = []
    print(nums)
    for index, value in enumerate(nums):
        value_map[value] = index
    if len(nums) <= 2 :
        return result

    for i in range(len(nums)):
        if i >=1 and nums[i]  == nums[i-1]:
            print(f'skipping{i}')
            continue
        else:
            for j in range(i+1, len(nums)):
                if j >= 2 and nums[j] == nums[j - 1]:
                    continue
                value = -(nums[i]+nums[j])
                if value in value_map and value_map[value] > i and value_map[value] > j:
                    result.append([nums[i], nums[j], value])
    return result

print(threeSum([0, 0 , 0 , 0]))

