class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile(r'[A-Za-z0-9]')
        matches = pattern.findall(s)
        s = "".join(matches).lower()
        n = len(s)
        for i in range(n//2):
            ptr1 = i
            ptr2 = -i - 1
            a = s[ptr1]
            b = s[ptr2]
            if a != b:
                return False
        return True