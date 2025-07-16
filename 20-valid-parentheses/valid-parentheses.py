class Solution:
    def isValid(self, s: str) -> bool:
        t=[]
        d={'()','[]','{}'}
        for c in s:
            if c in '({[':
                t.append(c)
            elif not t or t.pop()+c not in d:
                return False
        return not t