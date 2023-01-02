class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val


class LinkedList:
    def __init__(self):
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')

        self.head.next = self.tail
        self.tail.prev = self.head

    def get_head(self):
        return self.head.next

    def add(self, node: Node):
        prev = self.tail.prev
        prev.next = node

        node.prev = prev
        node.next = self.tail

        self.tail.prev = node

    def remove(self, node: Node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.dict = {}
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.linked_list.remove(node)
            self.linked_list.add(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            exit_node:Node = self.dict[key]
            exit_node.val = value
            self.linked_list.remove(exit_node)
            self.linked_list.add(exit_node)

        else:
            node = Node(key, value)
            self.linked_list.add(node)
            self.dict[key] = node

        if len(self.dict) > self.capacity:
            expirated_node = self.linked_list.get_head()
            self.linked_list.remove(expirated_node)
            if expirated_node.key in self.dict:
                del self.dict[expirated_node.key]



lru_cache = LRUCache(2)
expected=[None,None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,-1,None,None,18,None,None,-1,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,-1,None,None,None,None,29,None,None,None,None,17,22,18,None,None,None,-1,None,None,None,20,None,None,None,-1,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
for i, val in enumerate([[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]):

    if i==0:
        lru_cache=LRUCache(val[0])
    elif len(val)==2:
        put = lru_cache.put(val[0], val[1])
        if put != expected[i]:
            print(f'put i={i},put={put}')
    else:
        print(i)
        get = lru_cache.get(val[0])
        if get != expected[i]:
            print(f'i={i} get({val[0]})={get} expect={expected[i]}')