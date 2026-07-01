class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sendout = []
        sizes = []
        for string in strs:
            sendout.append(str(len(string)))
            sendout.append(",")
        sendout.append("#")
        sendout.extend(strs)
        return ''.join(sendout)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        finaler = []
        sizes = []
        i = 0
        while s[i] != "#":
            j = i
            while s[j] != ",":
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for num in sizes:
            finaler.append(s[i:i + num])
            i += num
        return finaler


