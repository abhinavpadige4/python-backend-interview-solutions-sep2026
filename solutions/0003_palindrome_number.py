"""
LeetCode Problem 9: Palindrome Number
Given an integer x, return true if x is a palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-2^31 <= x <= 2^31 - 1
Follow up: Could you solve it without converting the integer to a string?
"""

def is_palindrome(x: int) -> bool:
    """
    Check if an integer is a palindrome.
    
    Approach 1: String conversion (simple and readable)
    - Convert integer to string
    - Check if string equals its reverse
    
    Time Complexity: O(log(n)) - number of digits
    Space Complexity: O(log(n)) - for string storage
    
    Args:
        x: Integer to check
        
    Returns:
        True if x is palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Convert to string and check if it equals its reverse
    s = str(x)
    return s == s[::-1]

def is_palindrome_no_string(x: int) -> bool:
    """
    Check if an integer is a palindrome without converting to string.
    
    Approach: Reverse half of the number
    - Special cases: negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
    - Reverse the second half of the number
    - Compare the first half with the reversed second half
    
    Time Complexity: O(log(n)) - number of digits
    Space Complexity: O(1) - constant extra space
    
    Args:
        x: Integer to check
        
    Returns:
        True if x is palindrome, False otherwise
    """
    # Special cases:
    # As mentioned above, when x < 0, x is not a palindrome.
    # Also if the last digit of x is 0, in order to be a palindrome,
    # the first digit of x also needs to be 0.
    # Only 0 satisfies this property.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
    # For example when the input is 12321, at the end of the while loop we get x = 12, reversed_half = 123,
    # since the middle digit doesn't matter in palindrome (it will always equal to itself), we can simply get rid of it.
    return x == reversed_half or x == reversed_half // 10

# Test cases
if __name__ == "__main__":
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (12321, True),
        (123321, True),
        (12345, False),
        (1, True),
        (1001, True),
        (1000021, False),
    ]
    
    print("Testing is_palindrome() function:")
    for x, expected in test_cases:
        result = is_palindrome(x)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_palindrome({x}) = {result}, expected = {expected}")
    
    print("\nTesting is_palindrome_no_string() function:")
    for x, expected in test_cases:
        result = is_palindrome_no_string(x)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_palindrome_no_string({x}) = {result}, expected = {expected}")