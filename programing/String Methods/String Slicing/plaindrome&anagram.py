# --- 1. STRING SLICING CHEAT SHEET ---

word = "python"

print(word[0:2])
print(word[1:7])
print(word[:-4])
print(word[::-1])

# --- 2. PALINDROME AND ANAGRAM FUNCTIONS ---

def is_palindrome(text):
    cleaned = text.lower().replace(" ","")
    return cleaned == cleaned [::-1]

def is_anagram(str1,str2):
    cleaned1 = str1.lower().replace(" ","")
    cleaned2 = str2.lower().replace(" ","")
    return sorted(cleaned1) == sorted(cleaned2)

# --- 3. TESTING THE PRACTICE FUNCTIONS ---

# Palindrome Checks
print("--- Palindrome Tests ---")
print(is_palindrome("radar"))       # Output: True
print(is_palindrome("Nurses Run"))  # Output: True (Handles casing and spaces)
print(is_palindrome("python"))      # Output: False

# Anagram Checks
print("\n--- Anagram Tests ---")
print(is_anagram("listen", "silent"))      # Output: True
print(is_anagram("Dormitory", "Dirty Room")) # Output: True (Handles casing and spaces)
print(is_anagram("cat", "rat"))           # Output: False