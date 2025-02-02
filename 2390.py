class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        for ch in s:
            if ch == "*":
                arr and arr.pop()
            else:
                arr.append(ch)
        return "".join(arr)
