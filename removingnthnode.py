def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #
        l1 = head
        l2 = head
        count = 1
        while(l2.next):
            l2 = l2.next
            if(count>n):
                l1 = l1.next
            count += 1
        if(count == n):
            return head.next
        l1.next = l1.next.next
        return head
            