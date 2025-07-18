class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast(base,exp):
            if exp==0:
                return 1.0
            h=fast(base,exp//2)
            if exp%2==0:
                return h*h
            else:
                return h*h*base
        if n<0:
            x=1/x
            n=-n
        return fast(x,n)
        