def search(nums, target):

    l = 0
    r = len(nums) -1

    while l <= r : #4 6
         m =  (l + r) // 2  # 5
         if nums[m] == target:
             return m
         # left sorted portion

         if nums[l] <= nums[m]: # 0  3  7
             if target < nums[l] or target > nums[m]:
                 l = m +1

             else:
                 r = m -1

         else:
             if target < nums[m] or target > nums[r]:
                 r = m - 1
             else :
                 l = m + 1
    return -1



nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))
