"""
LeetCode Problem 206: Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list.
    
    Approach: Iterative with three pointers
    - Use prev, current, and next pointers
    - Iterate through the list, reversing pointers as we go
    - Time Complexity: O(n) - single pass through the list
    - Space Complexity: O(1) - constant extra space
    
    Args:
        head: Head of the singly linked list
        
    Returns:
        Head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        # Store next node
        next_temp = current.next
        # Reverse current node's pointer
        current.next = prev
        # Move pointers one step forward
        prev = current
        current = next_temp
    
    # prev will be the new head
    return prev

def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list using recursion.
    
    Approach:
    - Base case: empty list or single node
    - Recursively reverse the rest of the list
    - Make the next node point to current node
    - Set current node's next to None
    
    Time Complexity: O(n) - each node visited once
    Space Complexity: O(n) - due to recursion stack
    
    Args:
        head: Head of the singly linked list
        
    Returns:
        Head of the reversed linked list
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    # Make the next node point to current node
    head.next.next = head
    # Set current node's next to None
    head.next = None
    
    return new_head

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
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
    ]
    
    print("Testing reverse_list() function:")
    for i, (input_values, expected) in enumerate(test_cases):
        head = create_linked_list(input_values)
        reversed_head = reverse_list(head)
        result = linked_list_to_list(reversed_head)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: reverse_list({input_values}) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing reverse_list_recursive() function:")
    for i, (input_values, expected) in enumerate(test_cases):
        head = create_linked_list(input_values)
        reversed_head = reverse_list_recursive(head)
        result = linked_list_to_list(reversed_head)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: reverse_list_recursive({input_values}) = {result}")