class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split("/")
        stack = []
        for i in pathList:
            if (not stack and i == "..") or i == "." or i == "":
                continue
            elif i == "..":
                stack.pop()
            else:
                stack.append("/"+i)
        if stack:
            return "".join(stack)
        else:
            return "/"