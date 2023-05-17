class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = [[] for _ in range(len(parent) + 1)]
        
        for child, p in enumerate(parent):
            self.children[p].append(child)
            
        self.locked = [0 for _ in range(len(parent))]

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        
        self.locked[num] = 0
        return True
    
    def parentsUnlocked(self, num):
        cur = num
        while cur:
            cur = self.parent[cur]
            if self.locked[cur]:
                return False
            
        if self.locked[cur]:
            return False
        
        return True
    
    def lockedDecendants(self, num):
        flag = False
        for child in self.children[num]:
            locked = self.locked[child]
            lockedDec = self.lockedDecendants(child)
            
            if locked or lockedDec:
                self.locked[child] = 0
                flag = True
            
        return flag

    def upgrade(self, num: int, user: int) -> bool:
        
        if self.locked[num]:
            return False

        if not self.parentsUnlocked(num):
            return False

        if self.lockedDecendants(num):
            self.locked[num] = user
            return True

        return False
        
        
        
         


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
