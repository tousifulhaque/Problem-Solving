from DSA import linked_list

class ReorderingLinkedList(linked_list.LinkedList):
        def __init__(self):
            super(ReorderingLinkedList, self).__init__()


        def reorderingLinkedList(self):       
                len_pointer = self.head
                pointer_1 = self.head
                pointer_2 = self.head.next
                length = 0
                i = 1
                node_dic = {}
                
                while len_pointer:
                    node_dic[length] = len_pointer 
                    len_pointer = len_pointer.next
                    length += 1 
  
                while i-1 < ((length)//2):
                    pointer_1.next = node_dic[length - i] 
                    node_dic[length-i-1].next = None 
                    pointer_1.next.next = pointer_2 
                    pointer_1 = pointer_1.next.next 
                    pointer_2 = pointer_2.next
                    i += 1 

if __name__ == "__main__":
    ll = ReorderingLinkedList()
    arr = [1, 2, 3, 4, 5,6]
    for i in arr:
        ll.insert_at_begining(i)
    
    ll.reorderingLinkedList()
    ll.print()

