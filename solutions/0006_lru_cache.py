"""
LeetCode Problem 146: LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2],     [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 3, evicts key 3, cache is {4=4, 1=1}
lRUCache.get(1);    // return 1
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
"""

class Node:
    """Doubly linked list node for LRU Cache."""
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRU Cache implementation using hash map and doubly linked list.
    
    Approach:
    - Use a hash map for O(1) access to nodes by key
    - Use a doubly linked list to maintain order of usage
    - Most recently used items are near the head
    - Least recently used items are near the tail
    - get(key): O(1) - lookup in hash map, move node to head
    - put(key, value): O(1) - update/insert, move to head, evict tail if over capacity
    
    Time Complexity: O(1) for both get and put operations
    Space Complexity: O(capacity) - stores at most capacity elements
    """
    
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity.
        
        Args:
            capacity: Maximum number of items the cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Create dummy head and tail nodes for easier edge case handling
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: Node) -> None:
        """Add node right after head (most recently used position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        """
        Return the value of the key if the key exists, otherwise return -1.
        
        Args:
            key: Key to look up
            
        Returns:
            Value associated with key, or -1 if not found
        """
        if key in self.cache:
            node = self.cache[key]
            # Move accessed node to head (most recently used)
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the key-value pair 
        to the cache. If the number of keys exceeds the capacity, evict the least recently used key.
        
        Args:
            key: Key to insert or update
            value: Value to associate with the key
        """
        if key in self.cache:
            # Key exists, update value and move to head
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Key doesn't exist, create new node
            if len(self.cache) >= self.capacity:
                # Cache is full, remove least recently used item (before tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

# Alternative implementation using OrderedDict (Python 3.7+ maintains insertion order)
from collections import OrderedDict

class LRUCacheOrderedDict:
    """
    LRU Cache implementation using OrderedDict.
    
    OrderedDict maintains insertion order and provides O(1) operations for:
    - move_to_end(key): O(1)
    - popitem(last=False): O(1) - removes first item
    """
    
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        # If over capacity, remove least recently used (first item)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Test cases
if __name__ == "__main__":
    # Test case from the problem description
    print("Testing LRUCache with example from problem:")
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(f"get(1): {lru_cache.get(1)}")  # returns 1
    lru_cache.put(3, 3)                  # evicts key 2
    print(f"get(2): {lru_cache.get(2)}")  # returns -1 (not found)
    lru_cache.put(4, 4)                  # evicts key 3
    print(f"get(1): {lru_cache.get(1)}")  # returns 1
    print(f"get(3): {lru_cache.get(3)}")  # returns 3
    print(f"get(4): {lru_cache.get(4)}")  # returns 4
    print()
    
    # Additional test cases
    print("Additional test cases:")
    lru_cache2 = LRUCache(1)
    lru_cache2.put(2, 1)
    print(f"get(2): {lru_cache2.get(2)}")  # returns 1
    lru_cache2.put(3, 2)                  # evicts key 2
    print(f"get(2): {lru_cache2.get(2)}")  # returns -1 (not found)
    print(f"get(3): {lru_cache2.get(3)}")  # returns 2