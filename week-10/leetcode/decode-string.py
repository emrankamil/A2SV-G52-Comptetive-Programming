class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def decoded(start):
            nonlocal i
            cur = []
            while i<len(s):
                if s[i].isnumeric():
                    val = 0
                    for k in range(4):
                        if not s[i+k].isnumeric():
                            val = int(s[i:i+k])
                            i += k+1
                            break
                    cur.extend(val*decoded(i))
                    i += 1
                elif s[i]=="]":
                    return cur
                else:
                    cur.append(s[i])
                    i += 1
            return cur
        return "".join(decoded(0))

