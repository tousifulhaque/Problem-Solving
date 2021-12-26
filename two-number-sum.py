def two_number_sum(array, targetSum):
    hashmap = {}
    output = []
    for i,num in enumerate(array):
        hashmap[num] = i

    for i,num in enumerate(array):
        compliment = targetSum - num
        if compliment in hashmap and hashmap[compliment] != i:
            output = [num, compliment]
            return output



a = [3, 5, -4, 8, 11,1,-1,6]
two_number_sum(a, 10)