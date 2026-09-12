"""
LeetCode Problem 138: Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list 
such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def __repr__(self):
        return f"Node({self.val})"

def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    """
    Create a deep copy of a linked list with random pointers.
    
    Approach: Hash Map (Three-pass solution)
    1. First pass: Create copy of each node and map original -> copy
    2. Second pass: Assign next and random pointers for copy nodes
    3. Return the head of copied list
    
    Time Complexity: O(n) - three passes through the list
    Space Complexity: O(n) - hash map stores n mappings
    
    Args:
        head: Head of the original linked list
        
    Returns:
        Head of the copied linked list
    """
    if not head:
        return None
    
    # Step 1: Create copy of each node and map original -> copy
    old_to_new = {}
    current = head
    while current:
        copy = Node(current.val)
        old_to_new[current] = copy
        current = current.next
    
    # Step 2: Assign next and random pointers for copy nodes
    current = head
    while current:
        copy = old_to_new[current]
        copy.next = old_to_new.get(current.next)
        copy.random = old_to_new.get(current.random)
        current = current.next
    
    # Return the head of copied list
    return old_to_new[head]

def copy_random_list_optimized(head: Optional[Node]) -> Optional[Node]:
    """
    Create a deep copy using O(1) space (interweaving method).
    
    Approach:
    1. Interweave copy nodes with original nodes: A -> A' -> B -> B' -> C -> C'
    2. Assign random pointers for copy nodes: A'.random = A.random.next
    3. Separate the interweaved list into original and copy lists
    
    Time Complexity: O(n) - three passes through the list
    Space Complexity: O(1) - constant extra space
    
    Args:
        head: Head of the original linked list
        
    Returns:
        Head of the copied linked list
    """
    if not head:
        return None
    
    # Step 1: Interweave copy nodes with original nodes
    current = head
    while current:
        copy = Node(current.val)
        copy.next = current.next
        current.next = copy
        current = copy.next
    
    # Step 2: Assign random pointers for copy nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Step 3: Separate the interweaved list
    current = head
    copy_head = head.next
    while current:
        copy = current.next
        current.next = copy.next
        current = current.next
        if current:
            copy.next = current.next
    
    return copy_head

# Helper functions for testing
def create_linked_list_with_random(values: list, random_indices: list) -> Optional[Node]:
    """
    Create a linked list with random pointers from values and random indices.
    
    Args:
        values: List of node values
        random_indices: List of indices for random pointers (None for null)
        
    Returns:
        Head of the linked list
    """
    if not values:
        return None
    
    # Create all nodes
    nodes = [Node(val) for val in values]
    
    # Set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Set random pointers
    for i, rand_idx in enumerate(random_indices):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    
    return nodes[0] if nodes else None

def linked_list_to_list_with_random(head: Optional[Node]) -> list:
    """
    Convert a linked list with random pointers to list representation.
    
    Returns:
        List of [val, random_index] pairs
    """
    if not head:
        return []
    
    # First, collect all nodes and create a mapping
    nodes = []
    node_to_index = {}
    current = head
    index = 0
    while current:
        nodes.append(current)
        node_to_index[current] = index
        current = current.next
        index += 1
    
    # Now create the result list
    result = []
    current = head
    while current:
        random_index = node_to_index.get(current.random) if current.random else None
        result.append([current.val, random_index])
        current = current.next
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1 from problem description
    print("Testing copy_random_list() function:")
    head1 = create_linked_list_with_random([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copied_head1 = copy_random_list(head1)
    result1 = linked_list_to_list_with_random(copied_head1)
    expected1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    status1 = "✓" if result1 == expected1 else "✗"
    print(f"{status1} Test 1: {result1}")
    print(f"         Expected: {expected1}")
    print()
    
    # Test case 2
    head2 = create_linked_list_with_random([1, 2], [1, 1])
    copied_head2 = copy_random_list(head2)
    result2 = linked_list_to_list_with_random(copied_head2)
    expected2 = [[1, 1], [2, 1]]
    status2 = "✓" if result2 == expected2 else "✗"
    print(f"{status2} Test 2: {result2}")
    print(f"         Expected: {expected2}")
    print()
    
    # Test case 3
    head3 = create_linked_list_with_random([3, 3, 3], [None, 0, None])
    copied_head3 = copy_random_list(head3)
    result3 = linked_list_to_list_with_random(copied_head3)
    expected3 = [[3, None], [3, 0], [3, None]]
    status3 = "✓" if result3 == expected3 else "✗"
    print(f"{status3} Test 3: {result3}")
    print(f"         Expected: {expected3}")
    print()
    
    # Test optimized version
    print("Testing copy_random_list_optimized() function:")
    head4 = create_linked_list_with_random([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copied_head4 = copy_random_list_optimized(head4)
    result4 = linked_list_to_list_with_random(copied_head4)
    status4 = "✓" if result4 == expected1 else "✗"
    print(f"{status4} Optimized Test 1: {result4}")