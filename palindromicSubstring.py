def countSubstrings(s):
    count = 0
    def addPalindrom(s, l, r):
       
        while (l>=0 and r <len(s)) and (s[l]==s[r]):
            nonlocal count
            count  += 1
            l -= 1
            r += 1

    for i in range(len(s)):
        l= i #0
        r = i #
        addPalindrom(s, l, r)

    for i in range(len(s)):
        l = i
        r = i + 1     
        addPalindrom(s, l, r)

    return count     

print(countSubstrings(s = "aaa"))

