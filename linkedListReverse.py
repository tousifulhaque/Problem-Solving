from DSA import linked_list

class ReversedLinkedList(linked_list.LinkedList):
    def __init__(self):
        super(ReversedLinkedList, self).__init__()
        self.reversed_head = None

    def reverse_link_list(self):
        itr = self.head
        while itr != None:
            self.reversed_head = linked_list.Node(itr.data, self.reversed_head)
            itr = itr.next
            print(id(itr))

        # return self.reversed_head
    
    def print_reverse(self):

        if self.reversed_head is None:
            print('Linked list empty')
            return
        itr = self.reversed_head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = ReversedLinkedList()
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.reverse_link_list()


