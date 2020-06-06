class Solution:
    def reverse(self, x: int) -> int: 
        sign = 1 if x>=0 else -1
        digit, ans = 1, 0
        for d in str(x*sign):
            ans += digit * int(d)
            digit *= 10
        return sign*ans if -(2**31)-1 < sign*ans < (2**31) else 0
   