class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = 0
        if word[0].isupper():
            for ind, char in enumerate(word[1:]):
                if char.isupper():
                    caps += 1
                if caps != 0 and ind != caps - 1:
                    return False
        else:
            for char in word[1:]:
                if char.isupper():
                    return False
        return True