class Solution(object):
    # from collections import deque

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        word_set = set(wordList)

        queue = deque([(beginWord, 1)])

        visited = {beginWord}

        while queue:
            current_word, level = queue.popleft()

            #change each position in word
            for i in range(len(current_word)):
                # try each letter of the alphabet
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # create a new word with the changed letter
                    next_word = current_word[:i] + c + current_word[i+1:]

                    # if we found the target word
                    if next_word == endWord:
                        return level + 1
                    
                    # if the new word is in our word list and hasnt been visited
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

        return 0 # if no path is found

        