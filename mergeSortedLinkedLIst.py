class mergeLL:
        def __init__(self):
            self.head = None

        def mergeSortLL(self):
            self.merged_head = None #(1, None)
            self.rev_merge = None
            itr_1 = list1
            itr_2 = list2
            
            while itr_1 != None and itr_2 != None:
                if itr_1.val <= itr_2.val: # 1 , 1
                    self.merged_head = ListNode(itr_1.val, self.merged_head)
                    itr_1 = itr_1.next #2
                
                else:
                    self.merged_head = ListNode(itr_2.val, self.merged_head)
                    itr_2 = itr_2.next 
            
            while itr_1 != None:
                self.merged_head = ListNode(itr_1.val, self.merged_head)
                itr_1 = itr_1.next
            
            while itr_2 != None:
                self.merged_head = ListNode(itr_2.val, self.merged_head)
                itr_2 = itr_2.next
            
            rev = self.merged_head
            
            while rev != None:
                self.rev_merge = ListNode(rev.val, self.rev_merge)
                rev = rev.next
                
            return self.rev_merge