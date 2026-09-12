"""
LeetCode Problem 21: Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists.
    
    Approach: Iterative with dummy head
    - Use a dummy head to simplify edge cases
    - Compare nodes from both lists and attach the smaller one
    - Move forward in the list from which we took the node
    - Attach remaining nodes from non-empty list
    
    Time Complexity: O(n + m) - where n and m are lengths of the two lists
    Space Complexity: O(1) - constant extra space (excluding output)
    
    Args:
        list1: Head of first sorted linked list
        list2: Head of second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
    """
    # Create a dummy head to simplify edge cases
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach the remaining nodes
    current.next = list1 if list1 else list2
    
    return dummy.next

def merge_two_lists_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists using recursion.
    
    Approach:
    - Base case: if either list is empty, return the other
    - Recursive case: compare heads, attach smaller one, recurse on remainder
    
    Time Complexity: O(n + m) - each node processed once
    Space Complexity: O(n + m) - due to recursion stack
    
    Args:
        list1: Head of first sorted linked list
        list2: Head of second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Recursive case
    if list1.val < list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2

# Helper functions for testing
def create_linked_list(values: list) -> Optional[ListNode]:
    """Create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ]
    
    print("Testing merge_two_lists() function:")
    for i, (list1_vals, list2_vals, expected) in enumerate(test_cases):
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        merged_head = merge_two_lists(list1, list2)
        result = linked_list_to_list(merged_head)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: merge_two_lists({list1_vals}, {list2_vals}) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing merge_two_lists_recursive() function:")
    for i, (list1_vals, list2_vals, expected) in enumerate(test_cases):
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        merged_head = merge_two_lists_recursive(list1, list2)
        result = linked_list_to_list(merged_head)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: merge_two_lists_recursive({list1_vals}, {list2_vals}) = {result}")