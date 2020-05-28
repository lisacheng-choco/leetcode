class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ''' solution 1: brute method '''
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
        
        ''' solution 2: cycle '''
        cycle = nums + nums
        length = len(nums)
        for i in range(length):
            nums[i] = cycle[i+(length-k)]
        
        ''' solution 3: reverse 3 steps '''
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)