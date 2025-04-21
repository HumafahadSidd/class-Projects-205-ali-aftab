"""Problem 1: Reverse a String
Write a function that takes a string as input and returns the reversed string.
Example:
🔹 Input: "hello"
🔹 Output: "olleh"
💡 Hint: Use Python's slicing feature."""

def reverse_string(s: str) -> str:
     return s[::-1]             #- The first colon : means "start at the beginning" (no start value is provided).
#- The second colon : means "go all the way to the end" (no stop value is provided).
#- The -1 indicates the step size, which is negative, meaning the slice will progress in reverse order.



if __name__ == "__main__":
    print(reverse_string('hello there'))

# Test cases
