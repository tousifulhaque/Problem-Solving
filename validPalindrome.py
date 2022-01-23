def isPalindrome(s):
    s = s.lower()
    stack = []
    l = 0
    
    for letter in s:
        if (97 <= ord(letter)<= 122) or (48 <= ord(letter) <= 57):
            stack.append(letter)
    r = len(stack)-1
    while l < r:
        if stack[l] != stack[r]:
            return False
        l += 1 # 1
        r -= 1 # 
    
    return True

s = ' '
print(isPalindrome(s))