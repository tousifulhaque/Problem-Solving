from DSA import linked_list

class LinkList(linked_list.LinkedList):
    def __init__(self):
        super(LinkList, self).__init__()
    
    def remove_element(self, head, val):

        if head == None :
            return
        
        elif head.val == val:
            head = self.remove_element(head.next,val)
        
        else:
            head.next = self.remove_element(head.next, val)
        
        return head
    
    def remove_element_itr(self, head, val):
        
        p = head = linked_list.Node(-1, head)

        while p and p.next:

            if p.next.val == val:
                p.next = p.next.next
            
            else:
                p = p.next
            
        return head.next

