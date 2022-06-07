class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_string = s.rstrip().lstrip()
        counter = 0
        new_list = list(new_string)
        for item in range(len(new_list) - 1):
            if item[counter] != item[counter + 1]:
                counter += 1
            else:
                break
        return counter
