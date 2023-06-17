class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


s = Solution()
nums1 = [1, 2, 0, 0]
m = 2
nums2 = [2, 3]
n = 2
s.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1,2,2,3]

# PR(A) = PR(B) = PR(C) = 1.0
# PR(A) = 0.15 + 0.85 * (PR(C))
# PR(B) = 0.15 + 0.85 * (PR(A) / 2)
# PR(C) = 0.15 + 0.85 * (PR(B) + PR(A) / 2)
