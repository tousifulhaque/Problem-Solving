def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


nums = [3, 3, 1, 15]
print(twoSum(nums, 6))
