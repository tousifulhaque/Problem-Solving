def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        self.result_head = None
        pointer_1 = head
        pointer_2 = head.next
        it = head
        length = 0
        i = 1
        while it != None:
            it = it.next
            length += 1 #5
    
        while pointer_2.next != None and (i <= (length-n)): #i = 4,  #len-n = 4
            if self.result_head == None:
                self.result_head = ListNode(pointer_1.val, self.result_head)#[1,2,3(4,None)]
                itr =self.result_head
                itr = itr.next 
            else:
                print(id(itr))
                new_node = ListNode(pointer_1.val, itr) 
                itr = new_node
                itr = itr.next #None
                
            
            pointer_1 = pointer_1.next #5
            pointer_2 = pointer_2.next #None
            i += 1 #5
        
        if length == 1:
            return self.result_head
        else:
            itr = pointer_1.next
        
        return self.result_head
            