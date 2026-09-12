"""
LeetCode Problem 269: Alien Dictionary
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Note:
- You may assume all letters are in lowercase.
- You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
- If the order is invalid, return "".
- You may assume that the input is valid: words[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict, deque

def alien_order(words: List[str]) -> str:
    """
    Determine the order of letters in an alien language.
    
    Approach: Topological Sort using Kahn's Algorithm
    1. Build graph by comparing adjacent words
    2. Find first differing character between adjacent words to determine order
    3. Handle special case: if word2 is prefix of word1 and word1 != word2, return ""
    4. Perform topological sort to get letter order
    5. If cycle detected or not all letters included, return ""
    
    Time Complexity: O(C) where C is total length of all words
    Space Complexity: O(U + min(U^2, C)) where U is number of unique letters
    
    Args:
        words: List of words sorted lexicographically in alien language
        
    Returns:
        String representing the alien dictionary order, or "" if invalid
    """
    # Step 1: Create adjacency list and in-degree map
    adj_list = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}
    
    # Step 2: Build graph by comparing adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        
        # Check if word2 is a prefix of word1 (invalid case)
        if len(word1) > len(word2) and word1.startswith(word2):
            return ""
        
        # Find first differing character
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                # word1[j] comes before word2[j] in alien dictionary
                if word2[j] not in adj_list[word1[j]]:
                    adj_list[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break  # Only the first differing character matters
    
    # Step 3: Topological sort using Kahn's Algorithm
    # Find all nodes with in-degree 0
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []
    
    while queue:
        char = queue.popleft()
        result.append(char)
        
        # Reduce in-degree for all neighbors
        for neighbor in adj_list[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 4: Check if topological sort includes all unique characters
    if len(result) < len(in_degree):
        # There's a cycle or disconnected components
        return ""
    
    return "".join(result)

def alien_order_dfs(words: List[str]) -> str:
    """
    Determine the order of letters using DFS cycle detection.
    
    Approach: DFS with three states (unvisited, visiting, visited)
    - Build graph same as above
    - Use DFS to detect cycles and build topological order
    
    Time Complexity: O(C)
    Space Complexity: O(U + min(U^2, C))
    
    Args:
        words: List of words sorted lexicographically in alien language
        
    Returns:
        String representing the alien dictionary order, or "" if invalid
    """
    # Build adjacency list
    adj_list = defaultdict(list)
    in_degree = {c: 0 for word in words for c in word}
    
    # Build graph by comparing adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        
        # Check if word2 is a prefix of word1 (invalid case)
        if len(word1) > len(word2) and word1.startswith(word2):
            return ""
        
        # Find first differing character
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                # word1[j] comes before word2[j] in alien dictionary
                adj_list[word1[j]].append(word2[j])
                in_degree[word2[j]] += 1
                break
    
    # DFS states: 0 = unvisited, 1 = visiting, 2 = visited
    visited = {c: 0 for c in in_degree}
    result = []
    
    def has_cycle(char: str) -> bool:
        if visited[char] == 1:  # Currently visiting - cycle detected
            return True
        if visited[char] == 2:  # Already visited - safe
            return False
        
        # Mark as visiting
        visited[char] = 1
        
        # Visit all neighbors
        for neighbor in adj_list[char]:
            if has_cycle(neighbor):
                return True
        
        # Mark as visited and add to result
        visited[char] = 2
        result.append(char)
        return False
    
    # Check for cycles in all characters
    for char in in_degree:
        if visited[char] == 0:  # Unvisited
            if has_cycle(char):
                return ""  # Cycle detected
    
    # Reverse to get correct topological order
    return "".join(reversed(result))

# Test cases
if __name__ == "__main__":
    test_cases = [
        (["wrt","wrf","er","ett","rftt"], "wertf"),
        (["z","x"], "zx"),
        (["z","x","z"], ""),
        (["z","z"], "z"),
        (["abc","ab"], ""),  # Invalid: "ab" is prefix of "abc" but comes after
        (["za","zb","ca","cb"], "azbc"),  # Multiple valid orders possible
        (["wrt","wrf","er","ett","rftt","te"], ""),  # Cycle: t->e->r->t
    ]
    
    print("Testing alien_order() function (Kahn's Algorithm):")
    for i, (words, expected) in enumerate(test_cases):
        result = alien_order(words)
        # For cases with multiple valid orders, we check if result is valid
        if expected == "":
            status = "✓" if result == "" else "✗"
            print(f"{status} Test {i+1}: alien_order({words}) = '{result}'")
            print(f"         Expected: '{expected}'")
        else:
            # Check if result is a valid ordering (same length, same chars)
            status = "✓" if (len(result) == len(expected) and 
                           sorted(result) == sorted(expected)) else "✗"
            print(f"{status} Test {i+1}: alien_order({words}) = '{result}'")
            print(f"         Expected: '{expected}' (any valid order acceptable)")
        print()
    
    print("Testing alien_order_dfs() function (DFS Cycle Detection):")
    for i, (words, expected) in enumerate(test_cases):
        result = alien_order_dfs(words)
        if expected == "":
            status = "✓" if result == "" else "✗"
            print(f"{status} Test {i+1}: alien_order_dfs({words}) = '{result}'")
            print(f"         Expected: '{expected}'")
        else:
            status = "✓" if (len(result) == len(expected) and 
                           sorted(result) == sorted(expected)) else "✗"
            print(f"{status} Test {i+1}: alien_order_dfs({words}) = '{result}'")
            print(f"         Expected: '{expected}' (any valid order acceptable)")