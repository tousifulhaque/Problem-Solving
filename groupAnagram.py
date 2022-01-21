from tokenize import group


def groupAnagrams(strs):
    all_maps = {}
    group_anagrams = []
    l = 0
    r = 0
    for word in strs:
        single_map ={}
        for char in word:
            single_map[char] = 1 + single_map.get(char,0)

        all_maps[word] = single_map
    
     


    #[""
    while len(strs) >= 1 :
        a = strs.pop(l)
        tmp_array = [a] #[eat]

        while r < len(strs): # r = 0
            if all_maps[a] == all_maps[strs[r]]: # eat == tea
                tmp_array.append(strs.pop(r)) #[eat,tea, ate]
            else:
                r += 1 # r = 1
        group_anagrams.append(tmp_array) #[[eat, tea, ate], []]
        r = 0
    return group_anagrams        
    



strs = ["a"]
print(groupAnagrams(strs))