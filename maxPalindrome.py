def longestPalindrome(s):
    l = 0
    r = 1 
    maxLen = 0
    maxPalindrome = ""
    if len(s) == 1:
        return s

    
    for i in range(len((s))):
            l = i - 1  # 2
            r = i + 1 #4 
            while (l >= 0) and (r < len(s)) : #l = 0  r = 2 
                if (s[l].lower() == s[r].lower()) : #ba
                    if (r-l+1 >= maxLen):
                            maxPalindrome = s[l : r+1] #bab
                            maxLen = r-l+1 
                else: 
                    break

                l -= 1 
                r += 1

    for i in range(len((s))):   
            l = i
            r = i+1
            while (l >= 0) and (r < len(s)) : #l = 0  r = 2 
                if (s[l].lower() == s[r].lower()) : #ba
                    if (r-l+1 >= maxLen):
                            maxPalindrome = s[l : r+1] #bab
                            maxLen = r-l+1 
                else: 
                    break

                l -= 1 
                r += 1   
    return maxPalindrome

s = "abbc"
print(longestPalindrome(s))