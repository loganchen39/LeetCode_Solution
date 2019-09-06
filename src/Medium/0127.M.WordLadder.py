# Algo. 1
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        :
        :
        : TC1: NA, FAILED on case 28, with 27/40 test cases passed; 
        : TC2: NA, FAILED because of Time Limit Exceeded, with 30/40 test cases passed; 
        : SC:
        :\Algo. 1, Firsr thought, graph algo. of shortest path, which nurmally uses BFS; It's quite similar to 
        : solu. 1. The problems lie as follows:
        :1. How to build a correct graph? if you use recursion to build the graph as my first algo., the graph itself
        : is more like Depth-First-Search (because of recursion), the it's DIFFERENT from an appropriate one; 
        : consider the case: 
        : "qa"
        : "sq"
        : ["ca", "ba", "ra","fa", "ya", "ma", "ga", "ha", "qa", "na","la", "ta", "pa", 
        :  "cm", "ci", "cr", "co", 
        :  "br", "bi", "be",
        :  "re", "rn", "rh", "rb", 
        :  "fe", "fr", "fm", "si","go","se","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ti","to","yo",
        :  "ow","sn","po","ho","or","au","ur","sr","tc","lt","lo","as","nb","yb","if","pb","ge","th","pm","sh","li","hz",
        :  "no","di","hi","pi","os","uh","wm","an","me","mo","st","er","sc","ne","mn","mi","am","ex","pt","io","tb","ni","mr",
        :  "he","lr","sq","ye"]
        : The graph with recursion and DFS-like is like as follows
        :{'qa': [('ca', 2), ('ba', 2), ('ra', 2), ('fa', 2), ('ya', 2), ('ma', 2), ('ga', 2), ('ha', 2), ('na', 2), ('la', 2), ('ta', 2), ('pa', 2)], 
        : 'ca': [('cm', 3), ('ci', 3), ('cr', 3), ('co', 3)], 
        : 'cm': [('tm', 4), ('sm', 4), ('pm', 4), ('wm', 4), ('am', 4), ('fm', 4)], 
        : 'tm': [('ti', 5), ('to', 5), ('tc', 5), ('th', 5), ('tb', 5)], 
        : 'ti': [('si', 6), ('li', 6), ('bi', 6), ('di', 6), ('hi', 6), ('pi', 6), ('mi', 6), ('ni', 6)], 
        : 'si': [('se', 7), ('so', 7), ('sb', 7), ('sn', 7), ('sr', 7), ('sh', 7), ('st', 7), ('sc', 7), ('sq', 7)], 
        : Here the n_path for 'sq' is 7, while the correct answer is 5; 
        : 'se': [('le', 8), ('fe', 8), ('re', 8), ('ge', 8), ('me', 8), ('ne', 8), ('be', 8), ('he', 8), ('ye', 8)], 
        : 'le': [('ln', 9), ('lt', 9), ('lo', 9), ('lr', 9)], 
        : 'ln': [('rn', 10), ('an', 10), ('mn', 10)], 
        : 'rn': [('rh', 11), ('rb', 11)], 
        : 'rh': [('ph', 12), ('uh', 12)], 
        : 'ph': [('po', 13), ('pb', 13), ('pt', 13)],
        : 'po': [('go', 14), ('yo', 14), ('ho', 14), ('no', 14), ('mo', 14), ('io', 14)], 
        : 'yo': [('yb', 15)], 
        : 'yb': [('db', 16), ('mb', 16), ('nb', 16)], 
        : 'mb': [('mt'...
        : When I use BFS with a queue and while-loop to build the graph, it passed this test case. However it's "Time Limit Exceeded"! 
        : Need better algo.
        :2. Use normal BFS to find the endWord; 
        :3. Use a (word, n_path) to record the path or level of the word; Use dict as Graph DS and use another dict to
        :   store if visited; 
        """
        if beginWord in wordList: wordList.remove(beginWord)
        if endWord not in wordList: return 0
        
        n = len(wordList)
        m = len(beginWord)
    
        
        def isDiffByOne(s0, s1):
            if len(s0) != len(s1): return False
            
            n_diff = 0
            for i in range(len(s0)):
                if s0[i] != s1[i]: n_diff += 1
            if n_diff == 1: return True
            else: return False
            
        
        G = {}
        dict_visited = {}
        def build_graph(G, word, n_path): 
            queue = deque([(word, n_path)])
            while queue:
                curr_word, np = queue.popleft()
                for i in range(n):
                    if wordList[i] not in dict_visited and isDiffByOne(curr_word, wordList[i]):
                        # S.add(wordList[i])
                        dict_visited[wordList[i]] = False
                        G[curr_word] = G.get(curr_word, []) + [(wordList[i], np+1)]
                        queue.append((wordList[i], np+1))
                # if curr_word not in G: return
            
            #for i in range(len(G[word])):
            #    wd, np = G[word][i]
            #    build_graph(G, wd, np)
            
            
        def bfs():            
            # int_shrtPath = 0
            lst_queue = deque([])
            lst_queue.append(beginWord)
            while lst_queue:
                vtx = lst_queue.popleft()
                #print(vtx)
                if vtx in G: 
                    lst_adjVtx = G[vtx]
                    for v, np in lst_adjVtx:
                        if v == endWord: 
                            return np
                        if not dict_visited[v]:
                            lst_queue.append(v)
                            dict_visited[v] = True
                        
        
        build_graph(G, beginWord, 1)
        #print(G)
        if not G: return 0
        return bfs()


