class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        node = Doubly_Linked_List_Node(x)  # new node
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_last(self, x):
        node = Doubly_Linked_List_Node(x)
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def delete_first(self):
        assert self.head
        x = self.head.item
        if self.head == self.tail: # one node
            self.head = None
            self.tail = None
            return x
        self.head = self.head.next
        self.head.prev = None
        return x

    def delete_last(self):
        assert self.tail
        x = self.tail.item
        if self.head == self.tail: # one node
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
        return x

    def remove(self, x1, x2):
        assert self.head
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2
        if self.head is x1 and self.tail != x2:
            self.head = x2.next
            self.head.prev = None
            x2.next = None
        elif self.head is x1 and self.tail is x2:
            self.head = None
            self.tail = None
        elif self.head != x1 and self.tail is x2:
            self.tail = x1.prev
            self.tail.next = None
            x1.prev = None
        else:
            x1.prev.next = x2.next
            x2.next.prev = x1.prev
        return L2

    def splice(self, x, L2):
        if L2.head is None:
            return
        if self.tail is x:  # if x is the tail of linklist
            x.next = L2.head
            L2.head.prev = x
            self.tail = L2.tail
            L2.head = None
            L2.tail = None
        else:              # splice L2 to linklist
            p = x.next
            x.next = L2.head
            L2.head.prev = x
            L2.head = None
            L2.tail.next = p
            p.prev = L2.tail
            L2.tail = None
        return