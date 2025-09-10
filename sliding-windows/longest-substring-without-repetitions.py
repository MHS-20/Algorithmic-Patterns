from typing import DefaultDict

def longest_substrings_without_repetitions(s: str) -> int : 
    longest = 0
    left = 0
    counter: dict[str , int] = DefaultDict(int)
    for right in range(len(s)):
        counter[s[right]] += 1
        while counter[s[right]] > 1:
            counter[s[left]] -= 1
            left += 1
        longest = max(longest, right - left +  1)
    return longest
