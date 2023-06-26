def firstUniqChar(s):
    char_freq = {}  # Dictionary to store character frequencies

    # Count the frequency of each character in the string
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Find the first non-repeating character and return its index
    for i in range(len(s)):
        if char_freq[s[i]] == 1:
            return i

    return -1  # No non-repeating character found


# Test the function
s = "leetcode"
print(firstUniqChar(s))  # Output: 0

s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2

s = "aabb"
print(firstUniqChar(s))  # Output: -1
