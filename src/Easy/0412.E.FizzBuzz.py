# Algo. 1
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        : TC: 61.57%, O(n)
        : SC: 6.38%, O(n) for lst_res
        :
        :\1st idea, should be easy? loop over, but be aware there's an order to process,first %15, then %3 and %5, then the rest. 
        :\Algo. 1 BF from Ligang, easy loop-process.
        """
        lst_res = []
        for i in range(1, n+1):
            if i%15==0: lst_res.append("FizzBuzz")
            elif i%3==0: lst_res.append("Fizz")
            elif i%5==0: lst_res.append("Buzz")
            else: lst_res.append(str(i))
        
        return lst_res




