class Solution:
    def interpretRecursive(self, command, res):
        if not command:
            return res
        if command.startswith("G"):
            return self.interpretRecursive(command[1:], res + "G")
        if command.startswith("()"):
            return self.interpretRecursive(command[2:], res + "o")
        if command.startswith("(al)"):
            return self.interpretRecursive(command[4:], res + "al")
        else:
            return ""

    def interpret(self, command):
        return self.interpretRecursive(command, "")

