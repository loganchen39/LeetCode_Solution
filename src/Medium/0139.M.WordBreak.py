# Algo. 1, Failed
b_res = False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        :
        :\Algo. 1, first thought try different combinations/paths, sth like backtrace and recursion. If there exists one
        : (True) combination case which equals to s, then returns True, otherwise all cases failed, returns False. 
        : Here for Example 1, why it printed out "setting b_res = True", but in the end b_res is still False? 
        : b_res is not like a global or member variable? Python functions pass parameters as references, right?
        """
        if not s: return True
        
        n = len(wordDict)
        for v in wordDict:
            if v not in s:
                wordDict.remove(v)
        if not wordDict: return False
        # b_res = False
        
        def recur_func(s: str, wordDict: List[str], b_res):
            if b_res: return
            
            print("In recur_func, s = " + s)
            lst_str_st = []
            for v in wordDict:
                print("In recur_func, s = " + s + ", v = " + v)
                if v == s: 
                    print("In recur_func, v == s, setting b_res = True")
                    b_res = True
                    #return
                elif len(v) <= len(s) and v == s[0:len(v)]: 
                    lst_str_st.append(v)
            print(lst_str_st)
            if not lst_str_st: 
                return
            
            for v in lst_str_st:
                recur_func(s[len(v):], wordDict, b_res)
        
        
        print("s = " + s)
        print("wordDict = ")
        print(wordDict)
        recur_func(s, wordDict, b_res)
        print("After recur_func, b_res = " + str(b_res))
        return b_res


# For example 1, part of the print-out is as follows:
# s = leetcode
# wordDict = 
# ['leet', 'code']
# In recur_func, s = leetcode, v = code
# ['leet']
# In recur_func, s = code, v = code
# In recur_func, v == s, setting b_res = True
# []
# After recur_func, b_res = False  # why b_res is still False since above it's been set to True?!




# Algo. 1, Failed because of Time Limit Exceeded.
class Solution:
    def __init__(self):
        self.b_res = False
                
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        :
        :\Still Algo. 1, set b_res as class member variable, which solved the previous problem. Once self.b_res is set to True, it's been kept.
        : but it got error of Time Limit Exceeded, for test case 30/36, and it passed test cases 29/36, and later it passed test cases 32/36. 
        : Need better algo. The input of failed test case below:
        : "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        : ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"], 
        : which becomes ['aa', 'aaa', 'aaaaa', 'aaaaaaa', 'ba'] after removal.
        """
        if not s: return True
        
        for v in wordDict:
            if v not in s:
                wordDict.remove(v)
        if not wordDict: return False
        n = len(wordDict)
        
        # special pre-process for certain test case 30/36, or it has error of Time Limit Exceeded.
        char_set_s = set(s)
        char_set_dict = set()
        for v in wordDict:
            char_set_dict |= set(v)  # NOT char_set_dict += set(v)!
        if not char_set_s <= char_set_dict: 
            return False
        
        
        def numTimesBetweenStr(s0, s1):
            # return the number of times n that s1 is n times of s0, it not, return -1. 
            # in order to remove those redundent element string in the list, to improve the TC. 
            # not working for some test cases.
            # It has to be defined before been called below. 
            if not s0: return -1
            if len(s1)%len(s0) != 0: return -1
            
            n = 1
            while True:
                if s0 == s1: 
                    return n           
                if s0 != s1[0:len(s0)]:
                    return -1
                else:
                    s1 = s1[len(s0):]
                    n += 1
            return n
        
        
        for i in range(n-1):
            for j in range(i+1, n):
                if numTimesBetweenStr(wordDict[i], wordDict[j]) != -1:
                    wordDict[j] = ""
                elif numTimesBetweenStr(wordDict[j], wordDict[i]) != -1:
                    wordDict[i] = ""
        wordDict = [v for v in wordDict if v != ""]
        n = len(wordDict)
        # print(wordDict)

        
        def recur_func(s: str, wordDict: List[str]):
            if self.b_res: return
            
            lst_str_st = []
            for v in wordDict:
                if v == s: 
                    self.b_res = True
                    return
                elif len(v) <= len(s) and v == s[0:len(v)]: 
                    lst_str_st.append(v)
            if not lst_str_st: 
                return
            
            for v in lst_str_st:
                recur_func(s[len(v):], wordDict)
        

        recur_func(s, wordDict)
        return self.b_res




# Algo. 2, Failed because of Time Limit Exceeded,
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        : TC: Time Limit Exceeded with 29/36 test cases passed, O(n^n) for recursion tree in worst cases.
        : SC: NA, O(n) for recursion;
        :
        :\Algo. 2 as A1 BF, still use recursion to try all combinations/paths, and if in the middle there exists one
        : right combination, then return True, else return False. Here it avoided my Algo. 1 where even if you 
        : found one right combination and needs to return True, you still can NOT stop the whole recursion. You
        : have to try out ALL of the combinations and set the bool b_res class member variable to keep the result.
        : Algo. 2 is more clever and concise. Use set for query efficiency. 
        """
        def word_break(s: str, wordDict: set, st: int) -> bool:
            if st == len(s): return True
            
            for end in range(st+1, len(s)+1):  # it's not just len(s);
                if s[st:end] in wordDict and word_break(s, wordDict, end):
                    return True
            else:
                return False
        
        
        return word_break(s, set(wordDict), 0)




# Algo. 3, Succeeded
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        : TC: 75.82%, O(n^2)?, The size of recursion tree can go up to n**2? See ref. <<CtCI>> p.133;  
        : SC: 5.55%, O(n) for worst case, where the depth of recursion tree goes up to n; 
        :
        :\Algo. 3 as A2 examined by Ligang, recursion with memoization. Here memo[st] (take memo[8] as example) stores the
        : bool result of word_break for substring s[8:], it's needed because there might be several combinations/paths 
        : that reach to evaluate s[8:], so you don't need to do redundent computation for s[8:], see below for a detailed 
        : explanation for examples. You can comment or remove the "print" statements. 
        """
        def word_break(s: str, wordDict: set, st: int, memo: List[bool]) -> bool:
            if st < len(s):
                print("st = " + str(st) + ", memo[st] = " + str(memo[st]))
            else:
                print("st = " + str(st))
            
            if st == len(s): 
                # if it's True, finally it'll reach here and return True as final result.
                return True
            
            if memo[st] != None: 
                # No need to re-do the redundent computation, improve TC greatly in general.
                return memo[st]
            
            for end in range(st+1, len(s)+1):  # Be ware it's len(s)+1, not len(s)!
                if s[st:end] in wordDict and word_break(s, wordDict, end, memo):
                    print("st = " + str(st) + ", setting memo[st] to True ...")
                    memo[st] = True
                    return True
            else:
                print("stt = " + str(st) + ", setting memo[st] to False ...")
                memo[st] = False
                return False
        
        
        memo = [None]*len(s)
        return word_break(s, set(wordDict), 0, memo)


# check the example and its output below. Pay attension of how the (order of) recursion works.
# "aaaaaaabaabaaaaaaaaa"
# ["aa","aaa","ba"]
#
# st = 0, memo[st] = None
# st = 2, memo[st] = None
# st = 4, memo[st] = None
# st = 6, memo[st] = None
## the above 3-recursion works as: "aa" + "aa" + "aa", all exist;
## since s[6:] starts with "ab" which does not exist in wordDict, at the end of the for-loop, 
## the word_break(..., st=6) set memo[6]=False, and returns False, so the above-level of 
## recursion where st=4 will continue with end = 7, since s[4:7] = "aaa" exist in the wordDict, 
## so it will enter recursion func word_break with st = 7. 
# st = 6, setting memo[st] to False ...   
# st = 7, memo[st] = None  # end = 8, s[7:8] = "b" not exist, continue the for-loop with end = 9; 
## s[7:9] = "ba" exist, enter recursion with st=9, 
# st = 9, memo[st] = None
## again s[9:] starts with "ab" which does not exist in wordDict, at the end of for-loop, 
## set memo[9]=False and return False
# st = 9, setting memo[st] to False ...
## at the end of for-loop in word_break with st=7, since not found any right case, 
## set memo[7]=False and return False
# st = 7, setting memo[st] to False ...
## at the end of for-loop in word_break with st=4, set memo[4]=False and return False;
# st = 4, setting memo[st] to False ...
## Back to upper-level recursion where st=2, now end=st+3, and s[2:5]="aaa" also exist in wordDict,  
## (previously end=st+2, and s[2:4]="aa", which corresponds to st=4, that has been processed and returned False)
# st = 5, memo[st] = None
## Now it enters recursion again with st=7, which has already been processed before, 
## No need to re-do the redundent computation. 
## Previously the path is: "aa" + "aa" + "aaa", 
## now        the path is: "aa" + "aaa" + "aa", 
# st = 7, memo[st] = False
## Back to recursion with st=5
# st = 5, setting memo[st] to False ...
## Back to recursion with st=2
# st = 2, setting memo[st] to False ...
## Back to recursion with st=0, now enters recursion st=3 with "aaa" in wordDict.
# st = 3, memo[st] = None
## st=5 already processed, previously "aa" + "aaa", now "aaa" + "aa"
# st = 5, memo[st] = False
# st = 6, memo[st] = False
## After failed with recursion on st=5 and st=6, back to upper-level recursion on st=3
# st = 3, setting memo[st] to False ...
## Back to the toppest level of recursion on st=0, at the end of for-loop, where all the rest
## substring s[0:m] not exist in the wordDict, it returns False as the final result. 
# st = 0, setting memo[st] to False ...


# Here the use of memo[] to store the intermediate results for later use, and thus to avoid the redundent 
# computation is absolutely necessary. The original test case of the above is as follows:
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
# It is a lot more redundent, and the memo[] is more necessary here with this bigger case. 
# Another idea is that we can shrink the wordDict here, without affecting the result.
# if we have "aa", we do not need "aaaa" which equals to "aa"+"aa", so it can be equally 
# shrinked to ["aa", "aaa", "ba"]. This shrink should also improve TC. 


# Another example with True result, see how recursion works.
# "applepenapple", ["apple", "pen"]
# st = 0, memo[st] = None
# st = 5, memo[st] = None
# st = 8, memo[st] = None
# st = 13
# st == len(s), returning True
# st = 8, setting memo[st] to True ...
# st = 5, setting memo[st] to True ...
# st = 0, setting memo[st] to True ...




# Algo. 4
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        : TC: 53.33%, O(n^2) with 2 for-loop;   
        : SC: 5.55%, O(n) for dp;  
        :
        :\Algo. 4 as A4 using DP, The idea is to scan all possible substrings, and mark True for dp[i] if s[0:i] can be
        : broken, and i gradually increase from 1 to n, the order matters. 
        """
        setWordDict = set(wordDict)
        n     = len(s)
        dp    = [False] * (n+1)
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(0, i):
                print("i = " + str(i) + ", j = " + str(j) + ", dp[j] = " + str(dp[j]) +", s[j:i] = " + s[j:i])
                if dp[j] and s[j:i] in setWordDict:
                    print("dp[j] = " + str(dp[j]) + ", s[j:i] = " + s[j:i] + " in setWordDict, setting dp[i] to True ...")
                    dp[i] = True
                    break
        
        print(dp)
        return dp[n]


# Check the following example which returns True.
# "applepenapple", ["apple", "pen"]
# 
# i = 1, j = 0, dp[j] = True, s[j:i] = a
# i = 2, j = 0, dp[j] = True, s[j:i] = ap
# i = 2, j = 1, dp[j] = False, s[j:i] = p
# i = 3, j = 0, dp[j] = True, s[j:i] = app
# i = 3, j = 1, dp[j] = False, s[j:i] = pp
# i = 3, j = 2, dp[j] = False, s[j:i] = p
# i = 4, j = 0, dp[j] = True, s[j:i] = appl
# i = 4, j = 1, dp[j] = False, s[j:i] = ppl
# i = 4, j = 2, dp[j] = False, s[j:i] = pl
# i = 4, j = 3, dp[j] = False, s[j:i] = l
# i = 5, j = 0, dp[j] = True, s[j:i] = apple
# dp[j] = True, s[j:i] = apple in setWordDict, setting dp[i] to True ...
# i = 6, j = 0, dp[j] = True, s[j:i] = applep
# i = 6, j = 1, dp[j] = False, s[j:i] = pplep
# i = 6, j = 2, dp[j] = False, s[j:i] = plep
# i = 6, j = 3, dp[j] = False, s[j:i] = lep
# i = 6, j = 4, dp[j] = False, s[j:i] = ep
# i = 6, j = 5, dp[j] = True, s[j:i] = p
# i = 7, j = 0, dp[j] = True, s[j:i] = applepe
# i = 7, j = 1, dp[j] = False, s[j:i] = pplepe
# i = 7, j = 2, dp[j] = False, s[j:i] = plepe
# i = 7, j = 3, dp[j] = False, s[j:i] = lepe
# i = 7, j = 4, dp[j] = False, s[j:i] = epe
# i = 7, j = 5, dp[j] = True, s[j:i] = pe
# i = 7, j = 6, dp[j] = False, s[j:i] = e
# i = 8, j = 0, dp[j] = True, s[j:i] = applepen
# i = 8, j = 1, dp[j] = False, s[j:i] = pplepen
# i = 8, j = 2, dp[j] = False, s[j:i] = plepen
# i = 8, j = 3, dp[j] = False, s[j:i] = lepen
# i = 8, j = 4, dp[j] = False, s[j:i] = epen
# i = 8, j = 5, dp[j] = True, s[j:i] = pen
# dp[j] = True, s[j:i] = pen in setWordDict, setting dp[i] to True ...
# i = 9, j = 0, dp[j] = True, s[j:i] = applepena
# i = 9, j = 1, dp[j] = False, s[j:i] = pplepena
# i = 9, j = 2, dp[j] = False, s[j:i] = plepena
# i = 9, j = 3, dp[j] = False, s[j:i] = lepena
# i = 9, j = 4, dp[j] = False, s[j:i] = epena
# i = 9, j = 5, dp[j] = True, s[j:i] = pena
# i = 9, j = 6, dp[j] = False, s[j:i] = ena
# i = 9, j = 7, dp[j] = False, s[j:i] = na
# i = 9, j = 8, dp[j] = True, s[j:i] = a
# i = 10, j = 0, dp[j] = True, s[j:i] = applepenap
# i = 10, j = 1, dp[j] = False, s[j:i] = pplepenap
# i = 10, j = 2, dp[j] = False, s[j:i] = plepenap
# i = 10, j = 3, dp[j] = False, s[j:i] = lepenap
# i = 10, j = 4, dp[j] = False, s[j:i] = epenap
# i = 10, j = 5, dp[j] = True, s[j:i] = penap
# i = 10, j = 6, dp[j] = False, s[j:i] = enap
# i = 10, j = 7, dp[j] = False, s[j:i] = nap
# i = 10, j = 8, dp[j] = True, s[j:i] = ap
# i = 10, j = 9, dp[j] = False, s[j:i] = p
# i = 11, j = 0, dp[j] = True, s[j:i] = applepenapp
# i = 11, j = 1, dp[j] = False, s[j:i] = pplepenapp
# i = 11, j = 2, dp[j] = False, s[j:i] = plepenapp
# i = 11, j = 3, dp[j] = False, s[j:i] = lepenapp
# i = 11, j = 4, dp[j] = False, s[j:i] = epenapp
# i = 11, j = 5, dp[j] = True, s[j:i] = penapp
# i = 11, j = 6, dp[j] = False, s[j:i] = enapp
# i = 11, j = 7, dp[j] = False, s[j:i] = napp
# i = 11, j = 8, dp[j] = True, s[j:i] = app
# i = 11, j = 9, dp[j] = False, s[j:i] = pp
# i = 11, j = 10, dp[j] = False, s[j:i] = p
# i = 12, j = 0, dp[j] = True, s[j:i] = applepenappl
# i = 12, j = 1, dp[j] = False, s[j:i] = pplepenappl
# i = 12, j = 2, dp[j] = False, s[j:i] = plepenappl
# i = 12, j = 3, dp[j] = False, s[j:i] = lepenappl
# i = 12, j = 4, dp[j] = False, s[j:i] = epenappl
# i = 12, j = 5, dp[j] = True, s[j:i] = penappl
# i = 12, j = 6, dp[j] = False, s[j:i] = enappl
# i = 12, j = 7, dp[j] = False, s[j:i] = nappl
# i = 12, j = 8, dp[j] = True, s[j:i] = appl
# i = 12, j = 9, dp[j] = False, s[j:i] = ppl
# i = 12, j = 10, dp[j] = False, s[j:i] = pl
# i = 12, j = 11, dp[j] = False, s[j:i] = l
# i = 13, j = 0, dp[j] = True, s[j:i] = applepenapple
# i = 13, j = 1, dp[j] = False, s[j:i] = pplepenapple
# i = 13, j = 2, dp[j] = False, s[j:i] = plepenapple
# i = 13, j = 3, dp[j] = False, s[j:i] = lepenapple
# i = 13, j = 4, dp[j] = False, s[j:i] = epenapple
# i = 13, j = 5, dp[j] = True, s[j:i] = penapple
# i = 13, j = 6, dp[j] = False, s[j:i] = enapple
# i = 13, j = 7, dp[j] = False, s[j:i] = napple
# i = 13, j = 8, dp[j] = True, s[j:i] = apple
# dp[j] = True, s[j:i] = apple in setWordDict, setting dp[i] to True ...
# [True, False, False, False, False, True, False, False, True, False, False, False, False, True]


# Check the following example which returns False.
# "catsandog", ["cats", "dog", "sand", "and", "cat"]
# 
# i = 1, j = 0, dp[j] = True, s[j:i] = c
# i = 2, j = 0, dp[j] = True, s[j:i] = ca
# i = 2, j = 1, dp[j] = False, s[j:i] = a
# i = 3, j = 0, dp[j] = True, s[j:i] = cat
# dp[j] = True, s[j:i] = cat in setWordDict, setting dp[i] to True ...
# i = 4, j = 0, dp[j] = True, s[j:i] = cats
# dp[j] = True, s[j:i] = cats in setWordDict, setting dp[i] to True ...
# i = 5, j = 0, dp[j] = True, s[j:i] = catsa
# i = 5, j = 1, dp[j] = False, s[j:i] = atsa
# i = 5, j = 2, dp[j] = False, s[j:i] = tsa
# i = 5, j = 3, dp[j] = True, s[j:i] = sa
# i = 5, j = 4, dp[j] = True, s[j:i] = a
# i = 6, j = 0, dp[j] = True, s[j:i] = catsan
# i = 6, j = 1, dp[j] = False, s[j:i] = atsan
# i = 6, j = 2, dp[j] = False, s[j:i] = tsan
# i = 6, j = 3, dp[j] = True, s[j:i] = san
# i = 6, j = 4, dp[j] = True, s[j:i] = an
# i = 6, j = 5, dp[j] = False, s[j:i] = n
# i = 7, j = 0, dp[j] = True, s[j:i] = catsand
# i = 7, j = 1, dp[j] = False, s[j:i] = atsand
# i = 7, j = 2, dp[j] = False, s[j:i] = tsand
# i = 7, j = 3, dp[j] = True, s[j:i] = sand
## dp[7] will be set to True, by either "cat"+"sand", or later "cats"+"and", which does not execute because of "break". 
# dp[j] = True, s[j:i] = sand in setWordDict, setting dp[i] to True ...
# i = 8, j = 0, dp[j] = True, s[j:i] = catsando
# i = 8, j = 1, dp[j] = False, s[j:i] = atsando
# i = 8, j = 2, dp[j] = False, s[j:i] = tsando
# i = 8, j = 3, dp[j] = True, s[j:i] = sando
# i = 8, j = 4, dp[j] = True, s[j:i] = ando
# i = 8, j = 5, dp[j] = False, s[j:i] = ndo
# i = 8, j = 6, dp[j] = False, s[j:i] = do
# i = 8, j = 7, dp[j] = True, s[j:i] = o
# i = 9, j = 0, dp[j] = True, s[j:i] = catsandog
# i = 9, j = 1, dp[j] = False, s[j:i] = atsandog
# i = 9, j = 2, dp[j] = False, s[j:i] = tsandog
# i = 9, j = 3, dp[j] = True, s[j:i] = sandog
# i = 9, j = 4, dp[j] = True, s[j:i] = andog
# i = 9, j = 5, dp[j] = False, s[j:i] = ndog
# i = 9, j = 6, dp[j] = False, s[j:i] = dog
# i = 9, j = 7, dp[j] = True, s[j:i] = og
# i = 9, j = 8, dp[j] = False, s[j:i] = g
# [True, False, False, True, True, False, False, True, False, False]


