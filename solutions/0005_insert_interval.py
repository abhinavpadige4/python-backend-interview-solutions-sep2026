"""
LeetCode Problem 57: Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,6],[8,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    Insert a new interval into a list of non-overlapping intervals and merge if necessary.
    
    Approach:
    1. Add all intervals that end before newInterval starts
    2. Merge all intervals that overlap with newInterval
    3. Add the merged newInterval
    4. Add all remaining intervals
    
    Time Complexity: O(n) - single pass through intervals
    Space Complexity: O(n) - for the result list
    
    Args:
        intervals: List of non-overlapping intervals sorted by start time
        newInterval: Interval to insert
        
    Returns:
        List of intervals after insertion and merging
    """
    if not intervals:
        return [newInterval[:]]
    
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i][:])
        i += 1
    
    # Merge all overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    # Add the merged newInterval
    result.append(newInterval[:])
    
    # Add remaining intervals
    while i < n:
        result.append(intervals[i][:])
        i += 1
    
    return result

# Alternative approach: add new interval, then merge all
def insert_alternative(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    Alternative approach: insert new interval then merge all intervals.
    """
    # Insert new interval in the correct position
    merged_intervals = intervals + [newInterval[:]]
    merged_intervals.sort(key=lambda x: x[0])
    
    # Now merge overlapping intervals
    if not merged_intervals:
        return []
    
    result = [merged_intervals[0][:]]
    for interval in merged_intervals[1:]:
        if interval[0] <= result[-1][1]:
            # Overlapping intervals, merge them
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval[:])
    
    return result

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,6],[8,10],[12,16]]),
        ([], [5,7], [[5,7]]),
        ([[1,5]], [2,3], [[1,5]]),
        ([[1,5]], [2,7], [[1,7]]),
        ([[1,5]], [6,8], [[1,5],[6,8]]),
        ([[1,5]], [0,0], [[0,0],[1,5]]),
        ([[1,5]], [0,6], [[0,6]]),
    ]
    
    print("Testing insert() function:")
    for i, (intervals, newInterval, expected) in enumerate(test_cases):
        result = insert(intervals, newInterval)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: insert({intervals}, {newInterval}) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing insert_alternative() function:")
    for i, (intervals, newInterval, expected) in enumerate(test_cases):
        result = insert_alternative(intervals, newInterval)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: insert_alternative({intervals}, {newInterval}) = {result}")