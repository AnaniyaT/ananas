class Solution:
    def interpret(self, command: str) -> str:
        goal = []
        for ind, lett in enumerate(command):
            if lett == "G":
                goal.append("G")
            elif lett == "(":
                    if command[ind+1] == ")":
                        goal.append("o")
                    else:
                        goal.append("al")
        return "".join(goal)