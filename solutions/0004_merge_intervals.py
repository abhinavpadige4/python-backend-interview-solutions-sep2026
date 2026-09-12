"""
LeetCode Problem 56: Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.
    
    Approach:
    1. Sort intervals by their start time
    2. Iterate through sorted intervals
    3. If current interval overlaps with the last merged interval, merge them
    4. Otherwise, add current interval to the result
    
    Two intervals [a,b] and [c,d] overlap if b >= c (when sorted by start time)
    
    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(n) - for the result list
    
    Args:
        intervals: List of intervals where each interval is [start, end]
        
    Returns:
        List of merged non-overlapping intervals
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        # If merged list is empty or current interval doesn't overlap with last merged interval
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval[:])  # Append a copy
        else:
            # Overlapping intervals, merge them
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Alternative approach using stack-like behavior
def merge_alternative(intervals: List[List[int]]) -> List[List[int]]:
    """
    Alternative implementation using explicit stack-like approach.
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    stack = []
    
    for interval in intervals:
        if not stack or interval[0] > stack[-1][1]:
            stack.append(interval[:])
        else:
            stack[-1][1] = max(stack[-1][1], interval[1])
    
    return stack

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,4],[0,4]], [[0,4]]),
        ([[1,4],[2,3]], [[1,4]]),
        ([[2,3],[4,5],[6,7],[8,9],[1,10]], [[1,10]]),
        ([], []),
        ([[1,4]], [[1,4]]),
    ]
    
    print("Testing merge() function:")
    for i, (intervals, expected) in enumerate(test_cases):
        result = merge(intervals)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: merge({intervals}) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing merge_alternative() function:")
    for i, (intervals, expected) in enumerate(test_cases):
        result = merge_alternative(intervals)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: merge_alternative({intervals}) = {result}")