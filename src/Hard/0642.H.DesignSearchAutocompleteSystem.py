# Algo. 1
class AutocompleteSystem:
    """
    : TC: NA, How to sort according to the ASCII code for same hot degree? 
    : SC: NA, 
    :
    :\Keep list of string sorted according to times? Keep a list of current hit strings (or their indices)?
    : How to sort according to the hot degree AS WELL AS the ASCII code, is a problem! 
    :\Another solution is to use a Trie structure, the real question is, what data structure you will use to 
    : implement the Trie? See Chinese ref. book, p.248.  
    :\Algo. 1 from Ligang, failed, How to sort according to the ASCII code for same hot degree? Sth like 
    : 2-level sorting? 
    """
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.dict_his = {}
        for i in range(len(sentences)):
            self.dict_his[sentences[i]] = times[i]
        
        self.str_curr = ""
        self.matches = []
        

    def input(self, c: str) -> List[str]:
        if c != "#":
            self.str_curr += c
            if self.matches:
                for i in range(len(self.matches)):
                    if self.matches[i][len(self.str_curr)-1] != c:
                        self.matches[i] = ""
                else:
                    self.matches = [s for s in self.matches if s != ""]
            else:
                if self.str_curr != c:  # self.matches empty from the beginning;
                    return []
                else:  # 1st character of the current sentence
                    for str_his in self.dict_his:
                        if str_his[0] == c:
                            self.matches.append(str_his)
                    if self.matches:  # sorting
                        #print(self.matches)
                        self.matches.sort(key=self.dict_his.get, reverse=True)
                        #print(self.matches)
            
            if len(self.matches) <= 3:
                return self.matches
            else:
                return self.matches[0:3]
        else:  # c == "#", end of the sentence
            if self.str_curr in self.dict_his:
                self.dict_his[self.str_curr] += 1
            else:
                self.dict_his[self.str_curr]  = 1
            
            self.str_curr = ""
            self.matches  = []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)




# Algo. 2
from collections import defaultdict

class AutocompleteSystem:
    """
    : TC: 99.29%, O(n) for __init__, and input; 
    : SC: 100%, O(n)
    :  
    :\Algo. 2 from Discuss "Fast and simple explained, no trie, no priority queue", the idea is normal,
    : the key is how to sort the current matches at the beginning of the current sentence, according to each 
    : of the two dims. Need to implement by myself again! 
    """
    
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.partial = []           # previously seen chars of current sentence
        self.matches = []           # matching sentences in decreasing frequency order
        
        self.counts  = defaultdict(int)     # map from sentence to its frequency
        for sentence, count in zip(sentences, times):
            self.counts[sentence] = count

    def input(self, c):
        if c == "#":
            sentence = "".join(self.partial)
            # What if not exist? defaultdict can do like this?
            # O(1) time to locate the "sentence" with defaultdict,
            # See ref. about defaultdict at: 
            # https://docs.python.org/2/library/collections.html#collections.defaultdict
            self.counts[sentence] += 1  
            self.partial = []       # reset partial and matches
            self.matches = []
            return []
        
        # first char of sentence
        # This is the key! 
        # matches = [(-3, "dd", 5), (-3, "aa", 1), (-3, "dd", 4), (-3, "aa", 2), (-2, "bb", 9), (-2, "cc", 7)]
        # matches.sort()  # it will sort the list matches according to each dimension, with dim 0 having the top priority
        # and the last dim having the least priority! here it uses -count so all dims will be sorted from smallest
        # to largest!
        if not self.partial: 
            self.matches = [(-count, sentence) for sentence, count in self.counts.items() if sentence[0] == c]
            self.matches.sort()
            self.matches = [sentence for _, sentence in self.matches]   # drop the counts
        else:
            i = len(self.partial)   # filter matches for c
            self.matches = [sentence for sentence in self.matches if len(sentence) > i and sentence[i] == c]
            
        self.partial.append(c)
        return self.matches[:3]  # it's ok even if self.matches only has 1 or 0 element.




# Still Algo. 2
from collections import defaultdict
class AutocompleteSystem:
    """
    : TC: 99.29%, O(n) for __init__, and input; 
    : SC: 100%, O(n)
    :  
    :\Still Algo. 2 from Discuss "Fast and simple explained, no trie, no priority queue", re-implemented
    : by Ligang. 
    """
    
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.str_curr    = ""
        self.lst_matches = []
        
        self.dict_his = defaultdict(int)
        for sentence, time in zip(sentences, times):
            self.dict_his[sentence] = time
        

    def input(self, c):
        if c == "#":
            self.dict_his[self.str_curr] += 1
            self.str_curr                 = ""
            self.lst_matches              = []
            return []
        
        if not self.str_curr:  # 1st character
            self.lst_matches = [(-time, sentence) for sentence, time in self.dict_his.items() if sentence[0] == c]
            self.lst_matches.sort()
            self.lst_matches = [sentence for _, sentence in self.lst_matches]
          # return self.lst_matches[:3]
        else:
            n = len(self.str_curr)
            self.lst_matches = [sentence for sentence in self.lst_matches if len(sentence) >= n+1 and sentence[n] == c]
        
        self.str_curr += c
        return self.lst_matches[:3]


