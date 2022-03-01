def mergeTwoLists(nums1, nums2,m, n):
  
        l=0
        r = 0

        if m  == 0:
            while r < n:
                nums1.append(nums2[r])
                r += 1
            return
        #[1,2,3,0,0,0]
        #[2,5,6]

        while l < (m+n) and r <= (len(nums2) - 1):
             #2
            if l < (m+n-1) and (nums1[l] <= nums2[r]) and (nums1[l+1] >= nums2[r]):
                num = nums2.pop(0) #2
                tmp_itr = l+1 #1
                while tmp_itr < m+n: 
                    tmp = nums1[tmp_itr] #0
                    nums1[tmp_itr] = num #[1,2,2,3,0,0]
                    num = tmp #0
                    tmp_itr +=1 #4
                
                l = l + 2
                continue                
                    
            if l == (len(nums1)-len(nums2)):
                nums1[l] = nums2.pop(0)
                
            l += 1
            

if __name__ == '__main__':
    nums1 = [2, 3,4]
    nums2 = []
    m = 3
    n = 0
    mergeTwoLists(nums1, nums2, m, n)
    print(nums1)