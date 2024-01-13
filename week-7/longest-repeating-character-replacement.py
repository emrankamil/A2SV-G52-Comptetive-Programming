class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26  # A list to store frequency of each character
        rst, max_freq, left = 0, 0, 0

        for i in range(len(s)):
            char_index = ord(s[i]) - ord('A')
            freq[char_index] += 1
            max_freq = max(max_freq, freq[char_index])
            
            # Check if the number of characters to change (k) is sufficient
            if (i - left + 1 - max_freq) <= k:
                rst = max(rst, i - left + 1)
            else:
                # Adjust the sliding window by moving the left pointer
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

        return rst
