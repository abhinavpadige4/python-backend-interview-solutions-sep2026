"""
LeetCode Problem 127: Word Ladder
A transformation sequence from word beginWord to endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which has 5 words.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

from typing import List
from collections import deque, defaultdict

def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Find the length of the shortest transformation sequence from beginWord to endWord.
    
    Approach: BFS (Breadth-First Search)
    - Treat each word as a node in a graph
    - Two words are connected if they differ by exactly one character
    - Use BFS to find the shortest path from beginWord to endWord
    - Optimization: Preprocess wordList to create adjacency list using generic states
    
    Time Complexity: O(M^2 * N) where M = word length, N = number of words
                    In practice, with optimization: O(M * N)
    Space Complexity: O(M^2 * N) for the generic states dictionary
    
    Args:
        beginWord: Starting word
        endWord: Target word
        wordList: List of available words for transformation
        
    Returns:
        Number of words in the shortest transformation sequence, or 0 if not possible
    """
    if endWord not in wordList:
        return 0
    
    # Preprocess wordList to create generic states dictionary
    # e.g., "hot" -> "*ot", "h*t", "ho*"
    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    
    for word in wordList:
        for i in range(L):
            # Create generic state by replacing i-th character with '*'
            generic_state = word[:i] + "*" + word[i+1:]
            all_combo_dict[generic_state].append(word)
    
    # BFS initialization
    queue = deque([(beginWord, 1)])  # (current_word, level)
    visited = {beginWord: True}
    
    while queue:
        current_word, level = queue.popleft()
        
        # Generate all possible generic states for current word
        for i in range(L):
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            
            # Check all words that share this generic state
            for word in all_combo_dict[intermediate_word]:
                if word == endWord:
                    return level + 1
                
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            
            # Optimization: Clear the list to prevent revisiting
            all_combo_dict[intermediate_word] = []
    
    return 0

def ladder_length_bidirectional(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Find the length of the shortest transformation sequence using Bidirectional BFS.
    
    Approach: Bidirectional BFS
    - Search simultaneously from beginWord and endWord
    - Meet in the middle approach reduces search space significantly
    
    Time Complexity: O(M^2 * N) but much faster in practice
    Space Complexity: O(M^2 * N)
    
    Args:
        beginWord: Starting word
        endWord: Target word
        wordList: List of available words for transformation
        
    Returns:
        Number of words in the shortest transformation sequence, or 0 if not possible
    """
    if endWord not in wordList:
        return 0
    
    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
    
    # Bidirectional BFS
    queue_begin = deque([beginWord])
    queue_end = deque([endWord])
    
    visited_begin = {beginWord: True}
    visited_end = {endWord: True}
    
    level_begin = 1
    level_end = 1
    
    while queue_begin and queue_end:
        # Always expand the smaller queue for efficiency
        if len(queue_begin) > len(queue_end):
            queue_begin, queue_end = queue_end, queue_begin
            visited_begin, visited_end = visited_end, visited_begin
            level_begin, level_end = level_end, level_begin
        
        # Process one level from the beginning side
        for _ in range(len(queue_begin)):
            current_word = queue_begin.popleft()
            
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                
                for word in all_combo_dict[intermediate_word]:
                    if word in visited_end:
                        return level_begin + level_end
                    
                    if word not in visited_begin:
                        visited_begin[word] = True
                        queue_begin.append(word)
                
                # Clear to prevent revisiting
                all_combo_dict[intermediate_word] = []
        
        level_begin += 1
    
    return 0

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
        ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
        ("a", "c", ["a","b","c"], 2),
        ("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"], 4),
        ("leet", "code", ["lest","leet","lose","code","lode","rode","lost"], 0),
    ]
    
    print("Testing ladder_length() function (Standard BFS):")
    for i, (beginWord, endWord, wordList, expected) in enumerate(test_cases):
        result = ladder_length(beginWord, endWord, wordList)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: ladder_length('{beginWord}', '{endWord}', {wordList}) = {result}")
        print(f"         Expected: {expected}")
        print()
    
    print("Testing ladder_length_bidirectional() function (Bidirectional BFS):")
    for i, (beginWord, endWord, wordList, expected) in enumerate(test_cases):
        result = ladder_length_bidirectional(beginWord, endWord, wordList)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: ladder_length_bidirectional('{beginWord}', '{endWord}', {wordList}) = {result}")
        print(f"         Expected: {expected}")