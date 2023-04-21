from typing import List

"""
Given a string array words, 
return an array of all characters that show up in all strings 
within the words (including duplicates). 

You may return the answer in any order.


Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""
class Solution:
    def commonChars(self, wordss: List[str]) -> List[str]:
        res = []
        for char in wordss[0]:
            if all(char in word for word in wordss):
                res.append(char)
                wordss = [word.replace(char, '', 1) for word in wordss]
        return res


print(Solution().commonChars(["bella", "label", "roller"]))
print(Solution().commonChars(["cool", "lock", "cook"]))


