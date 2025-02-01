# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    """
    Linked List Node. Contains key-value pair and links to neighbor elements.
    """
    def __init__(self, key: int, value: int, prev=None, next=None):
        self.key: int = key
        self.value: int = value
 
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next

class LinkedList:
    """
    Linked List. Represents usage history of cache items
    """
    head: Optional[Node] = None
    tail: Optional[Node] = None

    def add_to_head(self, item: Node) -> None:
        """
        Add node to the very top of the list
        """
        if not self.head:
            self.head = self.tail = item
            return
        item.next = self.head
        self.head.prev = item
        self.head = item

    def unlink(self, item: Node) -> None:
        """
        Remove references to the node from other nodes on the list
        """
        if item is None:
            return
 
        prev_item: Node = item.prev
        next_item: Node = item.next

        if prev_item is not None:
            prev_item.next = next_item
        if next_item is not None:
            next_item.prev = prev_item
        
        if self.head == item:
            self.head = next_item
 
        if self.tail == item:
            self.tail = prev_item

        item.prev = item.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lruCache = {}
        self.capacity = capacity
        self.linkedList = LinkedList()

    def get(self, key: int) -> int:
        if key in self.lruCache:
            node = self.lruCache[key]
            if node != self.linkedList.head:
                self.linkedList.unlink(node)
                self.linkedList.add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lruCache:
            node = self.lruCache[key]
            node.value = value
            self.linkedList.unlink(node)
            self.linkedList.add_to_head(node)

        elif len(self.lruCache) < self.capacity:
            node = Node(key, value)
            self.lruCache[key] = node
            self.linkedList.add_to_head(node)
        else:
            lru_node = self.linkedList.tail
            del self.lruCache[lru_node.key]
            self.linkedList.unlink(lru_node)
            lru_node.key = key
            lru_node.value = value
            self.linkedList.add_to_head(lru_node)
            self.lruCache[key] = lru_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)