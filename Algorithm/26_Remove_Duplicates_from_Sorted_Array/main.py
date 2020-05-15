class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize two pointers
        i, j = 0, 1
        
        '''
        loop the list
        if i-th emelemt is equal to j-th element then increase j to skip the duplicate
        if i-th emelemt is not equal to j-th element then assign (i+1)-th element to j-th element j and  increase j 
        '''
        
        while j < len(nums):
            if(nums[i] != nums[j]):
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1
                