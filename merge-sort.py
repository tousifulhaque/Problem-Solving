def mergeTwoLists(nums1, nums2,m, n):
    for i in range(len(nums2)):
        nums1[m + i] = nums2[i]
    list.sort()


