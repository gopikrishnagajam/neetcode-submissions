class Solution:
    def encode(self, strs: List[str]) -> str:
        separator = "\u001F"

        if not strs:
            return "\u001E"  # or some special marker

        return separator.join(strs)

    def decode(self, s: str) -> List[str]:
        separator = "\u001F"

        if s == "\u001E":
            return []

        return s.split(separator)