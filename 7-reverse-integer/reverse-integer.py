class Solution:
    def reverse(self, x: int) -> int:
        isneg=x<0
        x=abs(x)
        s=0
        while x>0:
            r=x%10
            s=s*10+r
            x=x//10
        if isneg:
            s=-s
        if s<-2**31 or s>2**31-1:
            return 0
        return s
