"""
LeetCode Problem 207: Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should 
also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import deque, defaultdict

def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if it's possible to finish all courses given prerequisites.
    
    Approach: Topological Sort using Kahn's Algorithm (BFS)
    - Build adjacency list and in-degree count for each course
    - Add all courses with in-degree 0 to queue (no prerequisites)
    - Process queue: remove course, reduce in-degree of neighbors
    - If we can process all courses, return True; otherwise False
    
    Time Complexity: O(V + E) - where V = numCourses, E = len(prerequisites)
    Space Complexity: O(V + E) - for adjacency list and in-degree array
    
    Args:
        numCourses: Total number of courses
        prerequisites: List of prerequisite pairs [course, prerequisite]
        
    Returns:
        True if all courses can be finished, False otherwise
    """
    # Build adjacency list and in-degree array
    adj_list = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1
    
    # Initialize queue with courses having no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    courses_taken = 0
    
    # Process courses in topological order
    while queue:
        course = queue.popleft()
        courses_taken += 1
        
        # Reduce in-degree for all dependent courses
        for dependent in adj_list[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    # If we took all courses, it's possible to finish
    return courses_taken == numCourses

def can_finish_dfs(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if it's possible to finish all courses using DFS cycle detection.
    
    Approach: DFS with cycle detection
    - Build adjacency list
    - Use three states: unvisited (0), visiting (1), visited (2)
    - If we encounter a node in 'visiting' state during DFS, there's a cycle
    
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    
    Args:
        numCourses: Total number of courses
        prerequisites: List of prerequisite pairs [course, prerequisite]
        
    Returns:
        True if all courses can be finished, False otherwise
    """
    # Build adjacency list
    adj_list = defaultdict(list)
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    visited = [0] * numCourses
    
    def has_cycle(course: int) -> bool:
        if visited[course] == 1:  # Currently visiting - cycle detected
            return True
        if visited[course] == 2:  # Already visited - no cycle from this path
            return False
        
        # Mark as visiting
        visited[course] = 1
        
        # Visit all neighbors
        for neighbor in adj_list[course]:
            if has_cycle(neighbor):
                return True
        
        # Mark as visited
        visited[course] = 2
        return False
    
    # Check for cycles in all courses
    for course in range(numCourses):
        if visited[course] == 0:  # Unvisited
            if has_cycle(course):
                return False
    
    return True

# Test cases
if __name__ == "__main__":
    test_cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (1, [], True),
        (3, [[0, 1], [0, 2], [1, 2]], True),
        (3, [[0, 1], [1, 2], [2, 0]], False),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
        (5, [[1, 0], [2, 1], [3, 2], [4, 3]], True),
        (5, [[1, 0], [0, 1], [2, 3], [3, 4], [4, 2]], False),
    ]
    
    print("Testing can_finish() function (BFS/Kahn's Algorithm):")
    for i, (numCourses, prerequisites, expected) in enumerate(test_cases):
        result = can_finish(numCourses, prerequisites)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: can_finish({numCourses}, {prerequisites}) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing can_finish_dfs() function (DFS Cycle Detection):")
    for i, (numCourses, prerequisites, expected) in enumerate(test_cases):
        result = can_finish_dfs(numCourses, prerequisites)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: can_finish_dfs({numCourses}, {prerequisites}) = {result}")