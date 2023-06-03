class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(ch for ch in s if ch.isalnum()).lower()
        n = len(clean_s)
        for i in range(n // 2):
            if clean_s[i] != clean_s[n - 1 - i]:
                return False
        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama")) 
print(sol.isPalindrome("race a car")) 
print(sol.isPalindrome(" ")) 

