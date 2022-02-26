def duplicateZeros(arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Find out the zero
        # Replace the number after 0 with a zero 
        # Keep replace the numbers until we hit the end
        #[1,0,2,3,0,4,5,0]
        index = 0
        while index < len(arr): #1
            if arr[index]  == 0 :
                c_index = index+1 #2 
                tmp = arr[index] #0
                while c_index < len(arr):#[1,0,0,2,0,4,5,0]
                    #store
                    
                    tmp_1 = arr[c_index] #3
                    #change
                    arr[c_index] = tmp
                    #store
                    tmp = tmp_1
                    c_index += 1 #3
                index = index + 2
            else:
                index += 1
            


if __name__ == "__main__":
    arr = [1,0,2,3,0,4,5,0]
    duplicateZeros(arr)
    print(arr)
