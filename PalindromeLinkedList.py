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


    #recursive approach

    # Store the head in as a class property, so that it can be accessed and changed it the last recursion step
    self.frontpointer = head

    def recursive_approach(current_node = head):
       
        # Recurse to the end of the Linked List and return a False so that the next lines can be executed
        if not (recursive_approach(current_node.next)) :
            return False
        
        # Check if the current_node val is equal to the frontpointer value if they are move the frontpointer forward.
        # If they aren't equal return False to the upper stack which will perpetuate to the upper function calls
        if current_node.val  != self.frontpointer.val :
            return False

        self.frontpointer = self.frontpointer.next

        return True
    
    return recursive_approach()
