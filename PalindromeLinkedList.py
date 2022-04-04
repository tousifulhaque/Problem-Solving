def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        rev_ll = None
        
        itr = head

        #Reversing the linked list
        while itr :
            rev_ll = ListNode(itr.val, rev_ll)
            itr = itr.next
        
        rev_itr = rev_ll
        itr = head 

        #Iterating through the head and reversed linked list to match them
 
        while rev_itr:
            if itr.val != rev_itr.val :
                return False
            else:
                itr = itr.next
                rev_itr = rev_itr.next
        return True