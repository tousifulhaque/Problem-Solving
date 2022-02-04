    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        self.result_head = None
        pointer_1 = head
        pointer_2 = head
        i = 0
        
        while i <= 2:
            if pointer_2.next != None:
                pointer_2 = pointer_2.next
                i += 1
        while pointer_2.next != None:
            if self.result_head == None:
                self.result_head = ListNode(pointer_1.val, None)#[1,2,None]
                itr = self.result_head.next #itr
            else:
                itr = ListNode(pointer_1.val, None)
                itr = itr.next #None
            
            pointer_1 = pointer_1.next #3
            pointer_2 = pointer_2.next #5
            i += 1
        
        if i != n:
            itr = pointer_1.next.next
            
        return self.result_head