
def groupAnagrams(strs):
#     all_maps = {}
    group_anagrams = []
    sorted_array = []
    l = 0
    r = 0
    
    for word in strs:
        sorted_array.append("".join(sorted(word)))

    while len(strs) >= 1 :
        a = strs.pop(l)
        a_sorted = sorted_array.pop(l)
        tmp_array = [a] #[eat]

        while r < len(strs):# r = 0
            if a_sorted == sorted_array[r]: # eat == tea
                tmp_array.append(strs.pop(r)) #[eat,tea, ate]
                sorted_array.pop(r)
            else:
                r += 1 # r = 1
        group_anagrams.append(tmp_array) #[[eat, tea, ate], []]
        r = 0
    return group_anagrams        
    



strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))