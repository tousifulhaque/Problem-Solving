def findMin(nums):
    l = 0
    r = len(nums)-1

    while l<=r: #4 #6

        if l == r :
            return nums[l]
        m = (l+r) // 2 #5
        print(nums[l], nums[m], nums[r])
        if   nums[l] > nums[m] and nums[m] < nums[r] : #4 #7
            print('if')
            print(nums[l], nums[m], nums[r])
            l = m
        elif nums[l] <= nums[m] and nums[m] <= nums[r]:
            return nums[l]
        else:
            print('else')
            print(nums[l], nums[m], nums[r])
            r = m

ans = [4,5,6,7,0,1,2]
print(findMin(ans))