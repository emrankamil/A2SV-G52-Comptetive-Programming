class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (pow(10,9)+7)
        def power(x,n):
            if n==0:
                return 1
            k = n//2
            if n%2==0:
                return pow(power(x%mod, k)%mod, 2)%mod
            else:
                return (x%mod * pow(power(x%mod, k)%mod, 2))%mod

        if n%2==0:
            return power(20,n//2)%mod
        return 5*power(20,n//2)%mod





        # if n==1:
        #     return 5
        # k = n//2
        # if n%2==0:
        #     if k%2==1:
        #         return ((self.countGoodNumbers(k)%mod) * (4*self.countGoodNumbers(k)//5)%mod)%mod
        #     else:
        #         return pow(self.countGoodNumbers(k)%mod,2) %mod
        # else:
        #     return ((self.countGoodNumbers(k)%mod) * (self.countGoodNumbers(k+1)%mod))%mod
        
        # k = n//2
        # if n%2==0:
        #     return ((4**k)*(5**k))%(10**9+7)
        # return( 5**(k+1)*(4**k))%(10**9+7)