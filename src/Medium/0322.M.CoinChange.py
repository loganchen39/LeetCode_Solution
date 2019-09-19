# Algo. 1
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :\TC: NA, O(amount^n) = (a/c0)*(a/c1)...(a/cn_1) = a^n/(c0*c1*...cn_1), 
        :     Time Limit Exceeded with case: [3,7,405,436] 8839; 32/182 test cases passed.
        :\SC: NA, O(n) in worst cases for recursion stack.
        :
        :\First thought, recursion, start with largest coins? DP? No idea! Do NOT even know the BF algo.! 
        :\BF from A. 1, to try all combinations, there's a limit of the number for each coin type, which is 
        : (amount/coins[i]). In this kind of cases, normally we can use recursion for backtrace, to try all 
        : combinations, the problem is the TC is usually the WORST!
        """
        def recur_backtrace(idx: int, coins: List[int], amount: int) -> int:
            if amount == 0: # Base case, 0 coins needed, succeeded, not necessarily fewest coins.
                return 0
            
            if idx < len(coins) and amount > 0:
                maxNum  = int(amount/coins[idx])
                minCoin = sys.maxsize  # float("inf")
                for i in range(maxNum+1):
                    res = recur_backtrace(idx+1, coins, amount-i*coins[idx])
                    if res != -1:
                        if res + i < minCoin:
                            minCoin = res + i
                    else:
                        pass  # do nothing
                if minCoin != sys.maxsize:
                    return minCoin
                else: 
                    return -1
            else:  # failed, not found, recursion return case and end condition!
                return -1
        
        
        # if not coins or amount <= 0: return 0
        n_res = recur_backtrace(0, coins, amount)
        return n_res




# Algo. 2
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :\TC: NA, O(amount^n) = (a/c0)*(a/c1)...(a/cn_1) = a^n/(c0*c1*...cn_1), 
        :     Time Limit Exceeded with case: [186,419,83,408]  6249; 31/182 test cases passed, even worse than previous one.
        :     Previous algo. which has maximum limit of a/c0 etc, but this algo. goes until amt < 0, deeper.
        :\SC: NA, O(?), recursion and dictionary. 
        :
        :\A.2, in order to understand the algo., check the picture of recursion tree at Approach #2, and you'll understand!  
        : DP TopDown using Memoization and recursion implemented by Ligang, TC worse than Algo. 1 and still Time Limit Exceeded. 
        : Sth must be wrong. Using dict to store intermediate result and for checkup. 
        """
        def recur_dp_topdown(coins: List[int], amt: int, d: dict()) -> int:
            if amt == 0: return 0
            if amt <  0: return -1
            
            #print("amt = " + str(amt) + ", d = ")
            #print(d)
            
            n       = len(coins)
            minCoin = sys.maxsize
            for i in range(n):
                if amt-coins[i] in d:
                    res = d[amt-coins[i]]
                else:
                    res = recur_dp_topdown(coins, amt-coins[i], d)
                    if res > 0:
                        d[amt-coins[i]] = res
                # print("i = " + str(i) + ", res = " + str(res) + ", minCoin = " + str(minCoin))
                    
                if res == -1:
                    pass
                    #return -1
                elif res+1 < minCoin:
                    minCoin = res+1
            else:
                if minCoin != sys.maxsize:
                    return minCoin
                else:
                    return -1
        
        
        d = {}
        res = recur_dp_topdown(coins, amount, d)
        return res




# Still Algo. 2
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :\TC: 34.92%, O(S), S=amount,
        :\SC: 8.33%, O(S+n)=O(S), recursion and dictionary. 
        :
        :\A.2 again with more similar to Solution 2, except here use dictionary, while A.2 uses array.
        """
        def recur_dp_topdown(coins: List[int], amt: int, d: dict()) -> int:
            if amt == 0: return 0
            if amt <  0: return -1 
            if amt in d: return d[amt]
            
            minCoin = sys.maxsize
            for coin in coins:
                res = recur_dp_topdown(coins, amt-coin, d)
                if 0 <= res and res < minCoin:
                    minCoin = res
            else:
                # Previously forgot this, then TC is bad, and Time Limit Exceeded.
                d[amt] = minCoin + 1 if minCoin != sys.maxsize else -1
                return d[amt]
        
        
        d = {}
        res = recur_dp_topdown(coins, amount, d)
        return res




# Still Algo. 2
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :\TC: 27.49%, O(S*n), S=amount, 
        :\SC: 8.33%, O(S), for memoization, TopDown DP. 
        :
        :\A.2 using array to store memo, exactly the same as A.2, succeeded!
        """
        def recur_dp_topdown(coins: List[int], amt: int, d: List[int]) -> int:
            if amt == 0: return 0
            if amt <  0: return -1 
            if d[amt-1] >= -1: return d[amt-1]
            
            minCoin = sys.maxsize  # Here the value is: 9223372036854775807.
            for coin in coins:
                res = recur_dp_topdown(coins, amt-coin, d)
                if 0 <= res and res < minCoin:
                    minCoin = res
            else:
                # Previously forgot this, then still Time Limit Exceeded.
                d[amt-1] = minCoin + 1 if minCoin != sys.maxsize else -1
                return d[amt-1]
        
        d = [-2]*amount
        res = recur_dp_topdown(coins, amount, d)
        return res


