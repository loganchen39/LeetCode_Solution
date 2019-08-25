# Algo. 1.0
# not used, originally I wanted to use list to store adjacet list to represent the directed graph.
#class VNode:  
#    def __init__(self, c, inDe):
#        self.ch            = c
#        self.inDegree      = inDe
#        self.lst_adjVertex = []
    

class Solution:
    def __init__(self):
        self.lst_ordered1stLtr = []  # should be [[]]
        self.lst_words         = []
        #self.lst_VNode        = []
        self.dict_VNode        = {}
    
    
    #def charIndexInVNode(self, c):
    #    for i in range(len(self.lst_VNode)):
    #        if lst_VNode[i].ch == c: return i
    #    else: 
    #        return -1
    
    
    def alienOrder(self, words: List[str]) -> str:
        """
        : type words: List[str]
        : rtype: str
        :
        : TC: 74.78%, O(n*m+n*m) = O(n*m), 
        : SC: 12.50%, O(n*m) = total number of letters from all words;
        :\Algo. 1 from Ligang, use Example 1 as illustration, the idea is obvious, the problem lies in implementation!
        : The solution consists of 3 steps: 
        :\The 1st step is to construct the sliced ordered letters, i.e. the self.lst_ordered1stLtr[[]], which is a list
        : of lists. If you check Example 1, the process is kind like "recursion", with running a same function 
        : (i.e. def getOrdered1stLtr(words: List[str]) -> bool:) over and over again. You implement it, and then use 
        : a queue of "words" to loop over, to get final self.lst_ordered1stLtr[[]].
        :\Then you know it's a directed graph and Topological Sort problem. The 2nd step is to create the Adjacent List
        : as the graph representation, so later you can implement the Topological Sort algo. My original thought is to
        : use array (i.e. List) to store the adjacent list (see ref. Chinese book <<Data Structure>>, p. 164), then for 
        : each single letter, most likely you'll need to search the whole list to get its index, and you'll also need 
        : to dynamically add a new letter to the list, which make the process more compliated. Here you can use a dictionary
        : as hash table (i.e. self.dict_VNode) to avoid all of those processes. For each dict element, the key is the 
        : letter x, and the value is a list of 2 elements, one is the letter's InDegree, and the other is a set of adjacent
        : letters. One point here is that, the order info. of the array (list) to store the adjacent list is of no use,
        : and the order of one letter's adjacent letters is also of no use, the only thing you need to know is whether 
        : the letter exists in the adjacent list or the adjacent elements, and if it exist, where it is. Then Dictionary 
        : is a perfect choice. 
        :\The 3rd step is to implement the Topological Sort algo., with a stack (or maybe queue) and the InDegree info.
        : see ref. Chinese book <<Data Structure>>, p. 182. 
        :\ Use class member (i.e. self.lst_ordered1stLtr, self.lst_words, self.dict_VNode) as global variables to store 
        : immediate and final info. Any other ways to implement? What about real global variables? 
        : here the comment "\ U" will make a problem of 
        : "SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2208-2209: truncated \ UXXXXXXXX escape",
        : use "\ U" will solve the problem. 
        :\How about define the function getOrdered1stLtr out of function alienOrder? and its interaction with local/global
        : variables.
        """
        n = len(words)
        if n == 0: return ""
        #if n == 1: return words[0][0]  # wrong!
        if n == 1: return words[0]
        
        self.lst_ordered1stLtr = []
        self.lst_words         = [words]
        
        
        def getOrdered1stLtr(words: List[str]) -> bool:
            n = len(words)
            # if n == 0 or words[0] == "": return
            
            lst_ltr = [words[0][0]]
            # be aware words[0][1:] might be empty ""
            lst_wds = [[words[0][1:]]]  
            #print(words)
            for i in range(1, n):
                #print("i = " + str(i))
                #print(lst_ltr)
                #print(lst_wds)
                
                if words[i][0] == words[i-1][0]:
                    #lst_wds[len(self.lst_words)-1].append(words[i][1:])  # wrong!
                    lst_wds[len(lst_wds)-1].append(words[i][1:])
                else:
                    if words[i][0] in lst_ltr: return False  # invalid
                    lst_ltr.append(words[i][0])
                    lst_wds.append([words[i][1:]])
                #print(lst_ltr)
                #print(lst_wds)
                
            #print(lst_ltr)
            self.lst_ordered1stLtr.append(lst_ltr)
            
            # process lst_wds
            # bad idea to modify a list during a for-loop, what if not using index
            #for lst_wd in lst_wds:
            #    print(lst_wd)
            #    lst_wd = [wd for wd in lst_wd if wd != ""]  # lst_wd is a new list, it does NOT change lst_wds! WRONG!
            #    print(lst_wd)
            for i in range(len(lst_wds)):
                lst_wds[i] = [wd for wd in lst_wds[i] if wd != ""]  # now lst_wds[i] has been CHANGED!
                
            #print(lst_wds)
            # previously it's "if len(lst_wd) >= 2", you are getting rid of some "independent" char!
            lst_wds = [lst_wd for lst_wd in lst_wds if len(lst_wd) >= 1]  
            #print(lst_wds)
            
            # save to the global member var 
            for i in range(len(lst_wds)):
                self.lst_words.append(lst_wds[i])
            
            # print(self.lst_words)
            return True
        
        
        while self.lst_words:
            if getOrdered1stLtr(self.lst_words[0]):
                self.lst_words.pop(0)
            else: 
                return ""
        
        #print(self.lst_ordered1stLtr)
        
        
        # now you have self.lst_ordered1stLtr [[]], how to order the inner lists of words??! Topological Sort!
        for i in range(len(self.lst_ordered1stLtr)):
            if len(self.lst_ordered1stLtr[i]) == 1:
                ch = self.lst_ordered1stLtr[i][0]
                if ch not in self.dict_VNode:
                    self.dict_VNode[ch] = [0, set()]
                else:
                    pass
            else:
                for j in range(len(self.lst_ordered1stLtr[i])-1):
                    ch0, ch1 = self.lst_ordered1stLtr[i][j], self.lst_ordered1stLtr[i][j+1]
                    if ch1 not in self.dict_VNode:
                        self.dict_VNode[ch1] = [1, set()] 
                    
                        if ch0 not in self.dict_VNode:
                            self.dict_VNode[ch0] = [0, {ch1}]
                        else:
                            #self.dict_VNode[ch0][0] += 1
                            self.dict_VNode[ch0][1].add(ch1)
                    else:
                        if ch0 not in self.dict_VNode:
                            self.dict_VNode[ch0] = [0, {ch1}]
                            self.dict_VNode[ch1][0] += 1
                        else:
                            if ch1 not in self.dict_VNode[ch0][1]:
                                self.dict_VNode[ch0][1].add(ch1)
                                self.dict_VNode[ch1][0] += 1
                            else:  # the directed edge is already existed
                                pass
        #print(self.dict_VNode)
        
        # Topological Sort
        str_res   = ""
        lst_stack = []
        for ch in self.dict_VNode:
            if self.dict_VNode[ch][0] == 0: lst_stack.append(ch)
        while lst_stack:
            ch0 = lst_stack.pop()
            str_res += ch0
            for ch1 in self.dict_VNode[ch0][1]:
                self.dict_VNode[ch1][0] -= 1
                if self.dict_VNode[ch1][0] == 0:
                    lst_stack.append(ch1)
        
        return str_res
        
                
                # Originally I wanted to use List to store the adjacent list info. to represent the directed graph.
                # then switched to dictionay for a better choice.
                #idx0, idx1 = charIndexInVNode(ch0), charIndexInVNode(ch1)
                #if idx1 == -1:
                #    self.lst_VNode.append(ch1, 1)
                #else:
                #    pass
                    
                #if idx0 == -1:  # not exist
                #    self.lst_VNode.append(ch0, 0)
                #else:  # exist
                #    self.lst_VNode[idx0].lst_adjVertex.append()




# Algo. 1.1, same as Algo. 1.0, with some comments and degugging code removed.
class Solution:
    def __init__(self):
        self.lst_ordered1stLtr = [] 
        self.lst_words         = []
        self.dict_VNode        = {}
    
    
    def alienOrder(self, words: List[str]) -> str:
        """
        : type words: List[str]
        : rtype: str
        :
        : TC: 74.78%, O(n*m+n*m) = O(n*m), 
        : SC: 12.50%, O(n*m) = total number of letters from all words;
        :\Algo. 1 from Ligang, use Example 1 as illustration, the idea is obvious, the problem lies in implementation!
        : The solution consists of 3 steps: 
        :\The 1st step is to construct the sliced ordered letters, i.e. the self.lst_ordered1stLtr[[]], which is a list
        : of lists. If you check Example 1, the process is kind like "recursion", with running a same function 
        : (i.e. def getOrdered1stLtr(words: List[str]) -> bool:) over and over again. You implement it, and then use 
        : a queue of "words" to loop over, to get final self.lst_ordered1stLtr[[]].
        :\Then you know it's a directed graph and Topological Sort problem. The 2nd step is to create the Adjacent List
        : as the graph representation, so later you can implement the Topological Sort algo. My original thought is to
        : use array (i.e. List) to store the adjacent list (see ref. Chinese book <<Data Structure>>, p. 164), then for 
        : each single letter, most likely you'll need to search the whole list to get its index, and you'll also need 
        : to dynamically add a new letter to the list, which make the process more compliated. Here you can use a dictionary
        : as hash table (i.e. self.dict_VNode) to avoid all of those processes. For each dict element, the key is the 
        : letter x, and the value is a list of 2 elements, one is the letter's InDegree, and the other is a set of adjacent
        : letters. One point here is that, the order info. of the array (list) to store the adjacent list is of no use,
        : and the order of one letter's adjacent letters is also of no use, the only thing you need to know is whether 
        : the letter exists in the adjacent list or the adjacent elements, and if it exist, where it is. Then Dictionary 
        : is a perfect choice. 
        :\The 3rd step is to implement the Topological Sort algo., with a stack (or maybe queue) and the InDegree info.
        : see ref. Chinese book <<Data Structure>>, p. 182. 
        :\ Use class member (i.e. self.lst_ordered1stLtr, self.lst_words, self.dict_VNode) as global variables to store 
        : immediate and final info. Any other ways to implement? What about real global variables? 
        : here the comment "\ U" will make a problem of 
        : "SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2208-2209: truncated \ UXXXXXXXX escape",
        : use "\ U" will solve the problem. 
        :\How about define the function getOrdered1stLtr out of function alienOrder? and its interaction with local/global
        : variables.
        """
        n = len(words)
        if n == 0: return ""
        if n == 1: return words[0]
        
        self.lst_ordered1stLtr = []
        self.lst_words         = [words]
        
        
        def getOrdered1stLtr(words: List[str]) -> bool:
            n = len(words)
            
            lst_ltr = [words[0][0]]
            lst_wds = [[words[0][1:]]]  
            for i in range(1, n):   
                if words[i][0] == words[i-1][0]:
                    lst_wds[len(lst_wds)-1].append(words[i][1:])
                else:
                    if words[i][0] in lst_ltr: return False
                    lst_ltr.append(words[i][0])
                    lst_wds.append([words[i][1:]])
            self.lst_ordered1stLtr.append(lst_ltr)
            
            for i in range(len(lst_wds)):
                lst_wds[i] = [wd for wd in lst_wds[i] if wd != ""] 
            lst_wds = [lst_wd for lst_wd in lst_wds if len(lst_wd) >= 1]  
            
            for i in range(len(lst_wds)):
                self.lst_words.append(lst_wds[i])
            
            return True
        
        
        while self.lst_words:
            if getOrdered1stLtr(self.lst_words[0]):
                self.lst_words.pop(0)
            else: 
                return ""
            
        
        # now you have self.lst_ordered1stLtr [[]], how to order the inner lists of words??! Topological Sort!
        # 1st use dictionary to create the adjacent list representation of the directed graph.
        for i in range(len(self.lst_ordered1stLtr)):
            if len(self.lst_ordered1stLtr[i]) == 1:
                ch = self.lst_ordered1stLtr[i][0]
                if ch not in self.dict_VNode:
                    self.dict_VNode[ch] = [0, set()]
                else:
                    pass
            else:
                for j in range(len(self.lst_ordered1stLtr[i])-1):
                    ch0, ch1 = self.lst_ordered1stLtr[i][j], self.lst_ordered1stLtr[i][j+1]
                    if ch1 not in self.dict_VNode:
                        self.dict_VNode[ch1] = [1, set()] 
                    
                        if ch0 not in self.dict_VNode:
                            self.dict_VNode[ch0] = [0, {ch1}]
                        else:
                            #self.dict_VNode[ch0][0] += 1
                            self.dict_VNode[ch0][1].add(ch1)
                    else:
                        if ch0 not in self.dict_VNode:
                            self.dict_VNode[ch0] = [0, {ch1}]
                            self.dict_VNode[ch1][0] += 1
                        else:
                            if ch1 not in self.dict_VNode[ch0][1]:
                                self.dict_VNode[ch0][1].add(ch1)
                                self.dict_VNode[ch1][0] += 1
                            else:  # the directed edge is already existed
                                pass
        
        # Topological Sort
        str_res   = ""
        lst_stack = []
        for ch in self.dict_VNode:
            if self.dict_VNode[ch][0] == 0: lst_stack.append(ch)
        while lst_stack:
            ch0 = lst_stack.pop()
            str_res += ch0
            for ch1 in self.dict_VNode[ch0][1]:
                self.dict_VNode[ch1][0] -= 1
                if self.dict_VNode[ch1][0] == 0:
                    lst_stack.append(ch1)
        
        return str_res




# Algo. 1.2, Same as Algo. 1.0, Use global variables of lst_ordered1stLtr, lst_words, dict_VNode, instead of 
# class member, it works and passed all test cases. Below is part of the initial code.
lst_ordered1stLtr = []
lst_words         = []
dict_VNode        = {}

class Solution:
    #def __init__(self):
    #    self.lst_ordered1stLtr = [] 
    #    self.lst_words         = []
    #    self.dict_VNode        = {}
    
    def alienOrder(self, words: List[str]) -> str:
        """
        : type words: List[str]
        : rtype: str
        :
        : TC: 74.78%, O(n*m+n*m) = O(n*m), 
        : SC: 12.50%, O(n*m) = total number of letters from all words;
        """
        n = len(words)
        if n == 0: return ""
        if n == 1: return words[0]
        
        lst_ordered1stLtr = []
        lst_words         = [words]
        # have to have this, or it will NOT pass certain cases, because of some previous results.
        dict_VNode        = {}   




# Algo. 1.3, Same as Algo. 1.0, define function getOrdered1stLtr out of function alienOrder, 
# it works, below is some illustration code.
class Solution:
    def __init__(self):
        self.lst_ordered1stLtr = [] 
        self.lst_words         = []
        self.dict_VNode        = {}
    
    
    def getOrdered1stLtr(self, words: List[str]) -> bool:
        # ...
        return True
    

    def alienOrder(self, words: List[str]) -> str:
        # ...
        while self.lst_words:
            # use self to call member functions
            if self.getOrdered1stLtr(self.lst_words[0]):
                self.lst_words.pop(0)
            else: 
                return ""
        # ...




