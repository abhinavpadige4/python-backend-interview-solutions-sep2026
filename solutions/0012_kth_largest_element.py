"""
LeetCode Problem 215: Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

from typing import List
import heapq

def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find the kth largest element in an array.
    
    Approach 1: Min Heap of size k
    - Maintain a min heap of size k
    - Iterate through array, adding elements to heap
    - If heap size exceeds k, remove smallest element
    - At the end, the heap root is the kth largest element
    
    Time Complexity: O(n log k) - each heap operation is O(log k)
    Space Complexity: O(k) - heap stores at most k elements
    
    Args:
        nums: List of integers
        k: The kth position to find (1-indexed from largest)
        
    Returns:
        The kth largest element
    """
    # Min heap to store the k largest elements
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        # If heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # The root of the min heap is the kth largest element
    return min_heap[0]

def find_kth_largest_sorting(nums: List[int], k: int) -> int:
    """
    Find the kth largest element using sorting.
    
    Approach: Sort the array and pick the kth element from the end
    
    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(1) or O(n) depending on sorting algorithm
    
    Args:
        nums: List of integers
        k: The kth position to find
        
    Returns:
        The kth largest element
    """
    nums.sort()
    return nums[-k]

def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    """
    Find the kth largest element using QuickSelect algorithm.
    
    Approach: QuickSelect (based on QuickSort partition)
    - Find the (n-k)th smallest element (which is kth largest)
    - Average case: O(n), Worst case: O(n^2)
    
    Time Complexity: Average O(n), Worst O(n^2)
    Space Complexity: O(1) - in-place partitioning
    
    Args:
        nums: List of integers
        k: The kth position to find
        
    Returns:
        The kth largest element
    """
    def partition(left: int, right: int, pivot_index: int) -> int:
        """Partition the array and return the final pivot position."""
        pivot_value = nums[pivot_index]
        # Move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # Move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # Move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        
        return store_index
    
    def select(left: int, right: int, k_smallest: int) -> int:
        """
        Returns the k-th smallest element of list within left..right
        """
        if left == right:  # Only one element
            return nums[left]
        
        # Select a random pivot_index
        import random
        pivot_index = random.randint(left, right)
        
        # Find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)
        
        # The pivot is in its final sorted position
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            # Go left
            return select(left, pivot_index - 1, k_smallest)
        else:
            # Go right
            return select(pivot_index + 1, right, k_smallest)
    
    # kth largest is (n-k)th smallest
    return select(0, len(nums) - 1, len(nums) - k)

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([1, 2, 3, 4, 5], 1, 5),
        ([1, 2, 3, 4, 5], 5, 1),
        ([5, 5, 5, 5, 5], 3, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6], 4, 7),
    ]
    
    print("Testing find_kth_largest() function (Min Heap):")
    for i, (nums, k, expected) in enumerate(test_cases):
        # Make a copy since some methods modify the input
        nums_copy = nums[:]
        result = find_kth_largest(nums_copy, k)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: find_kth_largest({nums}, {k}) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing find_kth_largest_sorting() function:")
    for i, (nums, k, expected) in enumerate(test_cases):
        nums_copy = nums[:]
        result = find_kth_largest_sorting(nums_copy, k)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: find_kth_largest_sorting({nums}, {k}) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing find_kth_largest_quickselect() function:")
    for i, (nums, k, expected) in enumerate(test_cases):
        nums_copy = nums[:]
        result = find_kth_largest_quickselect(nums_copy, k)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: find_kth_largest_quickselect({nums}, {k}) = {result}")
        print(f"         Expected: {expected}")