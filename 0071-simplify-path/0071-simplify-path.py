class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("/", " ").split()
        stack = []
        
        for p in path:
            if p == ".." and stack:
                stack.pop()
            elif p != "." and p != "..":
                stack.append(p)
                    
        return "/" + "/".join(stack)
            