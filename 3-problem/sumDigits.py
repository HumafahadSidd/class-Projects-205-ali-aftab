""" Problem 3: Sum of Digits
Write a function that takes a non-negative integer and returns the sum of its digits.
Example:
🔹 Input: 1234
🔹 Output: 10
💡 Hint: Convert the number to a string and iterate over each digit or use modulus and division.""
"""
def sum_digits(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

if __name__ == "__main__":
    sum = sum_digits(1234455666)
    print(sum) # 10