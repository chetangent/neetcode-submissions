class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        words = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                words[pattern].append(word)
        visit = set()
        q = deque()
        visit.add(beginWord)
        q.append(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for nei in words[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res+=1
        return 0