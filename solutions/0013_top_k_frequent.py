"""
LeetCode Problem 347: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
"""

from typing import List
import heapq
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements in an array.
    
    Approach: Min Heap of size k
    - Count frequency of each element using Counter
    - Maintain a min heap of size k based on frequency
    - For each element, if heap size < k, push it
    - If heap size == k and current frequency > heap root frequency, replace root
    - Extract elements from heap
    
    Time Complexity: O(n + m log k) where n = len(nums), m = number of unique elements
    Space Complexity: O(m) for counter + O(k) for heap = O(m)
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Min heap to store k most frequent elements
    # We store (-frequency, element) to simulate max heap behavior with min heap
    min_heap = []
    
    for num, freq in freq_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        else:
            # If current frequency is greater than the smallest in heap, replace it
            if freq > min_heap[0][0]:
                heapq.heappushpop(min_heap, (freq, num))
    
    # Extract elements from heap (ignore frequencies)
    return [num for freq, num in min_heap]

def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements using bucket sort.
    
    Approach: Bucket Sort by Frequency
    - Count frequency of each element
    - Create buckets where index = frequency
    - Place each element in bucket corresponding to its frequency
    - Collect elements from highest frequency buckets downwards
    
    Time Complexity: O(n) - linear time
    Space Complexity: O(n) - for frequency map and buckets
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Create buckets: index = frequency, value = list of elements with that frequency
    max_freq = max(freq_map.values()) if freq_map else 0
    buckets = [[] for _ in range(max_freq + 1)]
    
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Collect elements from highest frequency downwards
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

def top_k_frequent_sorting(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements using sorting.
    
    Approach: Sort by frequency
    - Count frequency of each element
    - Sort elements by frequency in descending order
    - Take first k elements
    
    Time Complexity: O(n + m log m) where m = number of unique elements
    Space Complexity: O(m)
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Sort by frequency (descending) and then by value (for deterministic output)
    sorted_items = sorted(freq_map.items(), key=lambda x: (-x[1], x[0]))
    
    # Extract first k elements
    return [num for num, freq in sorted_items[:k]]

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 2], 2, [1, 2]),
        ([1, 1, 2, 2, 2, 3], 2, [2, 1]),
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
        ([3, 0, 1, 0], 1, [0]),
    ]
    
    print("Testing top_k_frequent() function (Min Heap):")
    for i, (nums, k, expected) in enumerate(test_cases):
        result = top_k_frequent(nums, k)
        # Sort both for comparison since order doesn't matter
        status = "✓" if sorted(result) == sorted(expected) else "✗"
        print(f"{status} Test {i+1}: top_k_frequent({nums}, {k}) = {result}")
        print(f"         Expected: {expected} (order doesn't matter)")
        print()
    
    print("Testing top_k_frequent_bucket_sort() function:")
    for i, (nums, k, expected) in enumerate(test_cases):
        result = top_k_frequent_bucket_sort(nums, k)
        status = "✓" if sorted(result) == sorted(expected) else "✗"
        print(f"{status} Test {i+1}: top_k_frequent_bucket_sort({nums}, {k}) = {result}")
        print(f"         Expected: {expected} (order doesn't matter)")
        print()
    
    print("Testing top_k_frequent_sorting() function:")
    for i, (nums, k, expected) in enumerate(test_cases):
        result = top_k_frequent_sorting(nums, k)
        status = "✓" if sorted(result) == sorted(expected) else "✗"
        print(f"{status} Test {i+1}: top_k_frequent_sorting({nums}, {k}) = {result}")
        print(f"         Expected: {expected} (order doesn't matter)")