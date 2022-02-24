arr = [ -7, -2, 12, 13]
index = 0
for i  in arr :
    arr[index] = i * i
    index += 1

arr.sort()

print(arr)