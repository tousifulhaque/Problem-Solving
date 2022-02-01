

def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        i = 0 
        hmap = {}
        pointer_1 = head
        
        
        while True: 
            if pointer_1 == None :
                return False
            
            else:
                if (pointer_1 in hmap.values()):
                    return True 
                else:
                    hmap[i] = pointer_1
                    pointer_1 = pointer_1.next
            
            i += 1