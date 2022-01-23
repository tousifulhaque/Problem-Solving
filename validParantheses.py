def isValid(s):
    paran_dic = {
            '(' : ')',
            '{' : '}',
            '[' : ']'

        }
    res = True
    l = 0
    stack = []
    if len(s)% 2 != 0:
        res = False #([])
        return res

    while l < len(s): #[
        if s[l] not in paran_dic.keys():
            if len(stack) == 0 :
                res = False
                return res
            
            if paran_dic[stack[-1]] != s[l]:
                res = False
                return res
            else:
                stack.pop(-1)
                l = l + 1
        else:
                stack.append(s[l]) #[{]
                l = l+1
    if len(stack) != 0:
        return False
    return res
        
print(isValid(s = "{[]}"))