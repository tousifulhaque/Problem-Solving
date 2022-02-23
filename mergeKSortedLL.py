from DSA import linked_list
from DSA.mergeSort import merge_sort

class MergeKSortedLL(linked_list.LinkedList):
    def __init__(self):
        super(MergeKSortedLL, self).__init__()
        self.merged_head = None
    
    # def mergeKSortedLL(self, k):
    #     self.merged_head = None
    #merge k sorted linked list
    def merge(element):
        

    def merge_sorted_ll(self,arr, l, r):
        if l < r :
            m = r - ((r-l)//2)
            merge_sort_ll(arr, l, m)
            merge_sort_ll(arr, m+1, r)
            merge(arr,l,m,r)




