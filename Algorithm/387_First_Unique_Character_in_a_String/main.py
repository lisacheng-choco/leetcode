class Solution:
    def firstUniqChar(self, s: str) -> int:
        ''' solution 1 '''
        dic = {}
        for e in s :
            if e in dic:
                dic[e] = dic[e]+1
            else:
                dic[e] = 1
        for key in dic:
            if(dic[key]==1):
                return s.index(key)
        return -1
        
        ''' solution 2  '''
        alphabet='abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in alphabet if s.count(l) == 1]
        return min(index) if len(index) else -1
    