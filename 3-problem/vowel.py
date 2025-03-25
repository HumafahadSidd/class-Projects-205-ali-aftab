""" Problem 2: Count Vowels in a String
Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
Example:
🔹 Input: "Apple"
🔹 Output: 2
💡 Hint: Use a loop and check if each character is in a set of vowels."""

def count_vowels(s: str) -> int:
    vowels = set('aeiou')
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    print(count_vowels('Apple'))
    print(count_vowels('Hello there!'))