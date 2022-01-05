def findMin(nums):
    l = 0
    r = len(nums)-1
    res = nums[l]
    while l<=r: #4 #6

        if nums[l] <= nums[r]:
            return min(res, nums[l])
            break

        mid = (l+r) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid +1

        else :
            r = mid -1
    return res


ans = [4,5,6,7,0,1,2]
print(findMin(ans))