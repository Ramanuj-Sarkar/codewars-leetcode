# implement x ** n
# it works recursively
class Solution:
    def myPow(self, x: float, n: int) -> float:
        cheating = False

        if cheating:
            return self.myCheatingPow(x, n)
        else:
            return self.mySeriousPow(x, n)

    def mySeriousPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, abs(n)
        elif n == 0:
            return 1.0
        
        if n % 2 == 0:
            # do binary trick
            return self.mySeriousPow(x * x, n // 2)
        else:
            # set it up to do binary trick
            return x * self.mySeriousPow(x, n - 1)

    def myCheatingPow(self, x: float, n: int) -> float:
        # cheating
        return x ** n
