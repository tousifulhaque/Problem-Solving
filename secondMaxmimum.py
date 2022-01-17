def secondMax(list):
    max_num = - float('inf')
    max_itr = []

    for num in list:
        if num > max_num:
            max_itr.append(num)
            max_num = num

    if len(max_itr) > 1:
        return max_itr[-2]
    else:
        return max_itr[-1]

