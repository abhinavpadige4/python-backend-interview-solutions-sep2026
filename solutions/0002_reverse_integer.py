"""
LeetCode Problem 7: Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-2^31 <= x <= 2^31 - 1
"""

def reverse(x: int) -> int:
    """
    Reverse the digits of a signed 32-bit integer.
    
    Approach:
    - Handle the sign separately
    - Convert absolute value to string, reverse it, convert back to int
    - Apply the original sign
    - Check for 32-bit integer overflow
    
    Time Complexity: O(log(n)) - number of digits in x
    Space Complexity: O(1) - constant extra space
    
    Args:
        x: Signed 32-bit integer
        
    Returns:
        Reversed integer or 0 if overflow occurs
    """
    # Define 32-bit integer bounds
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    # Handle sign
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    
    # Reverse the digits
    reversed_str = str(x_abs)[::-1]
    reversed_int = int(reversed_str)
    
    # Apply sign
    result = sign * reversed_int
    
    # Check for overflow
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

# Alternative mathematical approach (no string conversion)
def reverse_math(x: int) -> int:
    """
    Reverse integer using mathematical operations only.
    
    Time Complexity: O(log(n))
    Space Complexity: O(1)
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    result = 0
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    
    while x_abs != 0:
        digit = x_abs % 10
        # Check for overflow before actually adding the digit
        if result > (INT_MAX - digit) // 10:
            return 0
        result = result * 10 + digit
        x_abs //= 10
    
    return sign * result

# Test cases
if __name__ == "__main__":
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # Overflow case
        (-2147483412, -2147483412),  # Edge case
    ]
    
    print("Testing reverse() function:")
    for x, expected in test_cases:
        result = reverse(x)
        status = "✓" if result == expected else "✗"
        print(f"{status} reverse({x}) = {result}, expected = {expected}")
    
    print("\nTesting reverse_math() function:")
    for x, expected in test_cases:
        result = reverse_math(x)
        status = "✓" if result == expected else "✗"
        print(f"{status} reverse_math({x}) = {result}, expected = {expected}")