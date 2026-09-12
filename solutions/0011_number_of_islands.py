"""
LeetCode Problem 200: Number of Islands
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from typing import List
from collections import deque

def num_islands(grid: List[List[str]]) -> int:
    """
    Count the number of islands in a 2D grid.
    
    Approach: BFS (Breadth-First Search)
    - Iterate through each cell in the grid
    - When we find land ('1'), initiate BFS to mark all connected land as visited
    - Each BFS initiation counts as one island
    - Mark visited land as '0' to avoid revisiting
    
    Time Complexity: O(m * n) - each cell visited at most once
    Space Complexity: O(min(m, n)) - queue size in worst case (checkerboard pattern)
    
    Args:
        grid: 2D list representing the map ('1' = land, '0' = water)
        
    Returns:
        Number of islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def bfs(r: int, c: int) -> None:
        """Perform BFS to mark all connected land as visited."""
        queue = deque([(r, c)])
        grid[r][c] = '0'  # Mark as visited
        
        while queue:
            row, col = queue.popleft()
            
            # Check all 4 adjacent directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == '1'):
                    grid[nr][nc] = '0'  # Mark as visited
                    queue.append((nr, nc))
    
    # Iterate through each cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                bfs(r, c)
    
    return islands

def num_islands_dfs(grid: List[List[str]]) -> int:
    """
    Count the number of islands using DFS (Depth-First Search).
    
    Approach: Similar to BFS but using recursion/stack
    - Iterate through each cell
    - When finding land, initiate DFS to mark all connected land
    - Each DFS initiation counts as one island
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n) - worst case recursion stack (all land)
    
    Args:
        grid: 2D list representing the map
        
    Returns:
        Number of islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r: int, c: int) -> None:
        """Perform DFS to mark all connected land as visited."""
        # Base case: out of bounds or water
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'):
            return
        
        # Mark current land as visited
        grid[r][c] = '0'
        
        # Recursively visit all 4 adjacent directions
        dfs(r - 1, c)  # up
        dfs(r + 1, c)  # down
        dfs(r, c - 1)  # left
        dfs(r, c + 1)  # right
    
    # Iterate through each cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
    
    return islands

def num_islands_union_find(grid: List[List[str]]) -> int:
    """
    Count the number of islands using Union-Find (Disjoint Set Union).
    
    Approach:
    - Initialize each land cell as its own set
    - Union adjacent land cells
    - Count unique root parents
    
    Time Complexity: O(m * n * α(m*n)) - where α is inverse Ackermann (nearly constant)
    Space Complexity: O(m * n) - for parent and rank arrays
    
    Args:
        grid: 2D list representing the map
        
    Returns:
        Number of islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.rank = [0] * size
            self.count = 0  # Number of disjoint sets
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return
            
            # Union by rank
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px] += 1
            
            self.count -= 1
    
    # Initialize UnionFind
    uf = UnionFind(rows * cols)
    
    # First pass: count initial land and set up unions
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                uf.count += 1  # Each land starts as its own island
                # Check right and down neighbors to avoid double counting
                if r + 1 < rows and grid[r + 1][c] == '1':
                    uf.union(r * cols + c, (r + 1) * cols + c)
                if c + 1 < cols and grid[r][c + 1] == '1':
                    uf.union(r * cols + c, r * cols + (c + 1))
    
    return uf.count

# Test cases
if __name__ == "__main__":
    test_case_1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    
    test_case_2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    
    test_case_3 = [
        ["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]
    ]
    
    test_cases = [
        (test_case_1, 1),
        (test_case_2, 3),
        (test_case_3, 1),
        ([], 0),
        ([[]], 0),
        ([["0"]], 0),
        ([["1"]], 1),
        ([["1","0","1"],["0","1","0"],["1","0","1"]], 5),
    ]
    
    print("Testing num_islands() function (BFS):")
    for i, (grid, expected) in enumerate(test_cases):
        # Make a deep copy since the function modifies the grid
        import copy
        grid_copy = copy.deepcopy(grid)
        result = num_islands(grid_copy)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: num_islands(grid) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing num_islands_dfs() function (DFS):")
    for i, (grid, expected) in enumerate(test_cases):
        import copy
        grid_copy = copy.deepcopy(grid)
        result = num_islands_dfs(grid_copy)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: num_islands_dfs(grid) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing num_islands_union_find() function (Union-Find):")
    for i, (grid, expected) in enumerate(test_cases):
        import copy
        grid_copy = copy.deepcopy(grid)
        result = num_islands_union_find(grid_copy)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: num_islands_union_find(grid) = {result}")
        print(f"         Expected: {expected}")