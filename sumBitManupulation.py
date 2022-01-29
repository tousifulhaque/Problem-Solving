def sum(a, b):
    # bit wise addtion
    # if 2 one's and carry = 1 , result 1 , carry 1
    # if 2 zeros and carry = 1 result 0 , carry 0
    # if 1 zero and 1 one and carry = 1, resutl = 0, carry = 1

    # if 1 and 0 , result 1, carry 0 

    # How to represent summation using add or xor
    while b != 0:
        tmp = (a&b) << 1
        a = a^b
        b = tmp
    return a
    

print(sum(2, 3))