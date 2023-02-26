class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        added = set()
        stack = []
        
        for letter in s:
            counter[letter] -= 1
            if letter not in added:
                while stack and counter[stack[-1]] and stack[-1] > letter:
                    added.remove(stack.pop())

                stack.append(letter)
                added.add(letter)
            
        return "".join(stack)
                