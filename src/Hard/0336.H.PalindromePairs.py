# Algo. 1
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        : type words: List[str]
        : rtype: List[List[int]]
        :
        : TC: O(n^2*k), Time Limit Exceeded with 66/134 test cases passed. 2 for-loop and 1 for-loopto check if it's palindrome
        : SC: O(n+k)? for lst_res and s parameter for function isPalindrome.
        :\Algo. 1 BF with 2 for-loop and 1 for-loop to check if it's palindrome. Any improvement room? 
        : Is it wasteful or redundent to check all pairs? One word can be formed Palindrome with many other words, 
        : so you need to check with all other words! One improvement is that when determine whether 2 words
        : concatenation is palindrome, one word should be a subset of the other. 
        :\Be aware of the case ["a", ""], my output is [], while the expected output is [[0,1], [1,0]]
        """
        def isPalindrome(s:str) -> bool:
            n = len(s)
            if n <= 1: return True
            
            for i in range(int(n/2)):
                if s[i] != s[n-1-i]: return False
            
            return True
                
        
        n = len(words)
        if n <= 1: return []
        
        lst_res = []
        for i in range(n):
            for j in range(n):
                if j == i: continue
                if isPalindrome(words[i]+words[j]): lst_res.append([i, j])
        
        return lst_res




# Algo. 2
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        : type words: List[str]
        : rtype: List[List[int]]
        :
        : TC: O(n*k), 48.02%, 
        : SC: O(n)? 8.20%, 
        :\Algo. 2 Using dict as HashTable. First be clear about the problem, for s1+s2 to be palin, 2 cases,
        : 1. len(s1)>=len(s2), e.g. ["abcded", "cba"], here reverse "cba" which becomes "abc", which is the 
        : hashtable key; 2. len(s1)<=len(s2), e.g. ["abc", "dedcba"], here reverse "abc" which becomes "cba",
        : which is also the hashtable (dict) key, except we start to compare from the last characters of 
        : "dedcba"; so the reversed string with shorter length will always be the key. 
        :\THE IDEA OF USING HASHTABLE, is to store the processed and wanted information into HashTable so that
        : we can retrieve the info. (by key) in constant O(1) time!
        """
        def isPalin(s:str) -> bool:
            n = len(s)
            if n <= 1: return True
            for i in range(int(n/2)):
                if s[i] != s[n-1-i]: return False
            return True
                
            
        n = len(words)
        if n <= 1: return []
        
        dict_rev = {}
        for i in range(n):
            dict_rev[words[i][::-1]] = i
        # key can be "", for ["a",""], dict_rev = ["a":0, "":1]!
        # print(dict_rev)
        
        set_res = set()
        for i in range(n):
            word = words[i]
            # 2 cases, here with word at first, and the HashTable key at second.
            for j in range(len(word)+1):
                pref = word[:j]  # pref can be "", while j==0; 
                rmdr = word[j:]  # rmdr can be "", while j==len(word);
                if pref in dict_rev and isPalin(rmdr) and dict_rev[pref] != i:
                    set_res.add((i, dict_rev[pref]))
            # 2nd case, with word at right, and the HashTable key at left. 
            for j in range(len(word), -1, -1):
                surf = word[j:]  # surf can be "", while j==len(word);
                rmdr = word[:j]  # rmdr can be "", while j==0;
                if surf in dict_rev and isPalin(rmdr) and dict_rev[surf] != i:
                    set_res.add((dict_rev[surf], i))
        
        return list(set_res)




# Still Algo. 2
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        : type words: List[str]
        : rtype: List[List[int]]
        :
        : TC: O(n*k), 48.02%, 
        : SC: O(n)? 8.20%, 
        :\Still Algo. 2 Using HashTable, with a little coding improvement. 
        """
        def isPalin(s:str) -> bool:
            return s == s[::-1]
                
        n = len(words)
        if n <= 1: return []
        
        dict_rev = {word[::-1]:i for i, word in enumerate(words)}
        
        set_res = set()
        for i in range(n):
            word = words[i]
            # 2 cases, here with word at first, and the HashTable key at second.
            for j in range(len(word)+1):
                pref, rmdr = word[:j], word[j:] 
                if pref in dict_rev and isPalin(rmdr) and dict_rev[pref] != i:
                    set_res.add((i, dict_rev[pref]))
            # 2nd case, with word at right, and the HashTable key at left. 
            for j in range(len(word), -1, -1):
                surf, rmdr = word[j:], word[:j] 
                if surf in dict_rev and isPalin(rmdr) and dict_rev[surf] != i:
                    set_res.add((dict_rev[surf], i))
        
        return list(set_res)


