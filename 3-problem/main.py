"""Problem 1: Reverse a String
Write a function that takes a string as input and returns the reversed string.
Example:
🔹 Input: "hello"
🔹 Output: "olleh"
💡 Hint: Use Python's slicing feature."""

def reverse_string(s: str) -> str:
     return s[::-1]
if __name__ == "__main__":
    print(reverse_string('hello there'))

# Test cases
