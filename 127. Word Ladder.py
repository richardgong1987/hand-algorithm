from collections import deque, defaultdict
from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord, [beginWord])])

        while q:
            wd, path = q.popleft()

            if wd == endWord:
                return len(path)

            for i in range(len(wd)):
                # ascii_lowercase is [a-z] lowercase letters
                for char in ascii_lowercase:
                    next_wd = wd[:i] + char + wd[i + 1:]

                    if next_wd in wordList:
                        wordList.remove(next_wd)
                        q.append((next_wd, path + [next_wd]))

        return 0


class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0


        L = len(beginWord)

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0


solution = Solution2()
solution.ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"])
