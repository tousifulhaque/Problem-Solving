def containsDuplicate(nums) -> bool:
    num_dic = {}
    contains_dup = False
    for num in nums :
        if num in num_dic:
            contains_dup = True
            break
        else :
            num_dic[num] = 1
    return contains_dup