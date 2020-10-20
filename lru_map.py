from typing import Optional, Dict, Any


class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache = dict()
        self.key_to_node: Dict[Any, Node] = dict()
        self.lru_list: Optional[Node] = None

    def get(self, key):
        if key not in self.cache:
            return None
        val = self.cache[key]
        self._move_to_head(key)
        return val

    def set(self, key, value):
        if key in self.cache:
            self._move_to_head(key)
            return
        self.cache[key] = value
        evac_key = None
        if len(self.cache) >= self.capacity:
            evac_key = self.lru_list.data
        new_node = Node(key)
        new_node.next = self.lru_list
        self.lru_list = new_node
        self.lru_list = self.lru_list.next
        self.key_to_node[key] = new_node
        if evac_key:
            del self.cache[evac_key]
            del self.key_to_node[evac_key]
            self.lru_list.next = self.lru_list.next.next

    def _move_to_head(self, key):
        key_node: Node = self.key_to_node[key]
        if key_node.prev:
            key_node.prev.next = key_node.next
        new_node = Node(data=key)
        new_node.next = self.lru_list
        self.lru_list = new_node
