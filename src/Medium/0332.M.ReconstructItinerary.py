# Algo. 1, WRONG!
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        : Input tickets (List[List[str]]): Description;
        : Output (List[str]): Description;
        :
        : TC: Failed, wrong algo., with 18/80 test cases passed;
        : SC: Failed, wrong algo.
        : 
        :\Algo. 1 from Ligang, Wrong algo., for input: 
        : [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]], my output
        : ["JFK","KUL"], and expected output:
        : ["JFK","NRT","JFK","KUL"]
        : The problem lies in "You may assume ALL tickets form at least one valid itinerary.", i.e. you need to
        : include ALL tickets, which has higher priority than Lexical order! While my solution make the Lexical order
        : higher priority than including ALL tickets.
        : Since my understanding of the problem is wrong in the first place, so all the solutions thereafter are 
        : wrong! Need to avoid these kind of mistakes. It is actually a directed Graph and DFS problem! You need to get
        : it right in the first place. This "From-To" has direction, so most likely it's a directed Graph problem!
        """
        n = len(tickets)
        if n == 0: return []
        if n == 1: return tickets[0]
        
        ##No need for this, you can use >, <, >=, <=, ==, != to compare two strings, lexicographically, i.e.
        ##using ASCII value of the characters.
        ##https://thepythonguru.com/python-strings/
        #def isLessThanOrEqualTo(t1: str, t2: str) -> bool:
        #    for i in range(3):
        #        if t1[i] < t2[i]: return True
        #       elif t1[i] > t2[i]: return False
        #        else: pass
        #    else:
        #        return True  # equal
            
        
        dict_1From2Tos = dict()
        for t in tickets:
            if t[0] in dict_1From2Tos:
                m = len(dict_1From2Tos[t[0]])
                ##Better use while-loop, here if t[1] is larger than any dict_1From2Tos[t[0]][i], then when run into
                ##the "else:" section, the "i" is still m-1 (in C++ it would be m), so you need to set extra bool
                ##var to differentiate where to insert: at m-1 or m?
                #for i in range(m):
                #    if t[1] <= dict_1From2Tos[t[0]][i]:
                #        dict_1From2Tos[t[0]].insert(i, t[1])
                #        break
                #else:
                #    if i >= m-1:  # wrong, 
                #        dict_1From2Tos[t[0]].insert(i, t[1])
                i = 0
                while i < m:
                    if t[1] <= dict_1From2Tos[t[0]][i]:
                        dict_1From2Tos[t[0]].insert(i, t[1])
                        break
                    else: 
                        i += 1
                else:
                    if i >= m:  # it's ok, diff from for-loop
                        dict_1From2Tos[t[0]].insert(i, t[1])
            else:
                dict_1From2Tos[t[0]] = [t[1]]
        
        lst_res = []
        if "JFK" not in dict_1From2Tos: return []
        curr_airport = "JFK"
        while True:
            lst_res.append(curr_airport)
            if curr_airport in dict_1From2Tos and dict_1From2Tos[curr_airport]:
                next_airport = dict_1From2Tos[curr_airport].pop(0)
                curr_airport = next_airport
            else:
                break
        
        return lst_res




# Algo. 2, Failed again!
class Solution:
    def __init__(self):
        self.lst_res = []
        # self.n_ticket = n_ticket
        
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        : Input tickets (List[List[str]]): Description;
        : Output (List[str]): Description;
        :
        : TC: 
        : SC: 
        :
        :\Before checking out the LC solutions, below are my problems and questions as I failed to complete it.
        :1. I looks like a recursive and backtracking problem (although you can also implement iterative algo.), 
        :   The lexical order may not be kept with the normal recurisve algo., because of dead-end, 
        :   for example: [["JFK", "kUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
        :   It visits ["JFK", "kUL"] first but it's a dead end, my solution is to use a flag "visited", some LC solution
        :   is first pop it, and if it reaches a dead-end, it append it to the dictionary value of list again.
        :2. This "visited" flag is also useful to exclude repeating visit in a recursive function within a for-loop like
        :   I originally implemented. Examples like: [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "SFO"], ["ATL", "SFO"], ["SFO", "ATL"]],
        :   It first visits ["JFK", "ATL"] and then ["ATL", "JFK"], without a "visited" flag, it'll visit ["JFK", "ATL"] again, 
        :   which is wrong!
        :3. How exactly does the "recursion" work (within a for-loop)? When and how does it return? How does the internal stack
        :   work?
        :4. Draw out a typical case: [["JFK", "AAA"], ["AAA", "JFK"], ["JFK", "BBB"], ["BBB", "GGG"], ["GGG", "BBB"], ["BBB", "DDD"]
        :   , ["DDD", "EEE"], ["DDD", "FFFF"], ["FFF", "DDD"]], with the normal recursive algo., the branch of "JFK"->"BBB" 
        :   (and thereafter ->"DDD"->"EEE") is a dead end, it needs to visit "CCC" first, and then go back to visit "BBB" to get
        :   the final valid itinerary. I previously had a wrong thought that, if there is no "BBB"->"JFK", then it is a dead end. 
        :   That thought is WRONG! You can have something like one-way loop of: "JFK"->"BBB"->"DDD"->"JFK", it goes back to "JFK".
        :   For this kind of problem, I originally thought the use of some flag of "Traversed_Failed", which seems to make it
        :   more complicated.
        :
        :\Algo. 2,
        """
        n = len(tickets)
        if n == 0: return []
        if n == 1: return tickets[0]
        
        dict_1From2Tos = dict()
        for t in tickets:
            if t[0] in dict_1From2Tos:
                m = len(dict_1From2Tos[t[0]])
                i = 0
                while i < m:
                    if t[1] <= dict_1From2Tos[t[0]][i][0]:
                        # Traversed = False, Previously it was just t[1]; Failed = False, failed on this route currently;
                        dict_1From2Tos[t[0]].insert(i, [t[1], False, False])  
                        break
                    else: 
                        i += 1
                else:
                    if i >= m:  # it's ok, diff from for-loop
                        dict_1From2Tos[t[0]].insert(i, [t[1], False, False])
            else:
                # Previously it was just [t[1]]
                dict_1From2Tos[t[0]] = [[t[1], False, False]]  
        
        # self.lst_res = []
        lst_tmp = []
        n_ticket = 0
        if "JFK" not in dict_1From2Tos: return []
        curr_airport = "JFK"
        lst_stack = []
        
        
        def dfs(curr_airport, dict_adjLst, nt, lst_tmp, n_ticket):
            #print("n_ticket = " + str(n_ticket) + ", nt = " + str(nt) + ", curr_airport = " + curr_airport)
            #print(lst_tmp)
            #print("\n")
            
            if n_ticket == nt:
                #print("\n returning: n_ticket == nt: ")
                lst_tmp.append(curr_airport)
                n_ticket += 1
                #print(lst_tmp)
                #print("curr_airport = " + curr_airport + "\n")
                
                #self.lst_res = lst_tmp
                #exit()  # not working
                return True  # how to BREAK the recursion within a for-loop?!
            
            # Failed, go back
            if curr_airport not in dict_adjLst:
                #pass
                return False
            
                # if n_ticket < nt:  # Dead end
                # Reset all the "traversed" flag to False
                
                # del lst_tmp[1:]
                #print("if curr_airport not in dict_adjLst:, Resetting all the traversed flag to False!\n")
                #print(lst_tmp)
                #print("\n")
                
                # lst_tmp = []  # Wrong! Can NOT reset to [], 
                # n_ticket = 0
                # curr_airport = "JFK"
                #for str_ap in dict_1From2Tos:
                #    for j in range(len(dict_1From2Tos[str_ap])):
                #        #print("str_ap = " + str_ap + ", j = " + str(j) + ", d[str_ap][j][1] = " + str(dict_1From2Tos[str_ap][j][1]))
                #        if dict_1From2Tos[str_ap][j][1] == True: 
                #            dict_1From2Tos[str_ap][j][1] = False
                #            #print("if dict_1From2Tos[str_ap][j][1] == True:, Setting to False")
                #            #print("str_ap = " + str_ap + ", j = " + str(j) + ", d[str_ap][j][1] = " + str(dict_1From2Tos[str_ap][j][1]))
                
                
            else:
                lst_tmp.append(curr_airport)
                # n_ticket += 1
                for i in range(len(dict_adjLst[curr_airport])):
                    if curr_airport == "JFK":
                        #print("i = " + str(i) + ", if curr_airport == 'JFK':, Traversed = ")
                        #print(dict_adjLst[curr_airport][i][1])
                        pass
                    
                    if dict_adjLst[curr_airport][i][1] == False:
                        next_airport = dict_adjLst[curr_airport][i][0]
                        dict_adjLst[curr_airport][i][1] = True
                        lst_stack.append((curr_airport, next_airport))
                        if dfs(next_airport, dict_adjLst, nt, lst_tmp, n_ticket+1):
                            break
                        else:  # dfs returns False?
                            #pass
                            dict_adjLst[curr_airport][i][1] = False
                else:
                    lst_tmp.pop()
                    for i in range(len(dict_adjLst[curr_airport])):
                        # if dict_adjLst[curr_airport][i][1] == True:
                        dict_adjLst[curr_airport][i][1] == False
                    
            
        
        dfs(curr_airport, dict_1From2Tos, n, lst_tmp, n_ticket)
        print("\nOut of dfs, lst_tmp = ")
        print(lst_tmp)
        if len(lst_tmp) != n+1:
            print("ERROR: len(lst_tmp) != n+1")
            return []
        else:
            return lst_tmp




# Algo. 3
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        : Input tickets (List[List[str]]): Description;
        : Output (List[str]): Description;
        :
        : TC: 70.15%, ?
        : SC: 7.69%, ?
        :
        :\Algo. 3, From discussion "Short Python solution DFS + Backtracking", easy to understand and implement, the
        : idea is actually the same as mine, except I failed to pass the test cases, due to some details of the implementation.
        : The general idea is, to try every possible "path" in lexical order recursively, may succeed; but if failed (i.e. dead 
        : end), here the tricky thing is, it uses "ap = G[s].pop()", and if dfs failed, it "G[s].insert(0, ap)", similar
        : to my idea of using visited flag. And if the dfs does not succeed, it uses "trip.pop()", need to print out 
        : the varialbes inside the recursion to see how exactly it works.
        """
        def build_graph(tickets):
            G = {}
            for t in tickets:
                s, e = t
                G[s] = G.get(s, []) + [e]
            for s in G:
                G[s].sort(reverse=True)
            return G
        
        def dfs(G, s):
            # You can use trip and length vars like this!? Mainly because it's defined inside the function.
            trip.append(s)  
            if len(trip) == length:  # base case for recursion; 
                return True
            
            if s in G:
                i, n = 0, len(G[s])
                # Try every adjacent edge, may succeed; may fail (dead end), then pop out; 
                while i < n:
                    ap = G[s].pop()  # smallest one
                    if dfs(G, ap): 
                        return True
                    else:
                        # G[s].appendleft(ap)  # for deque
                        G[s].insert(0, ap)
                        i += 1
            # would be wrong if you use "else: " here. For some s in G, it may also reach dead end, then you need to pop it.
            #else:  
            trip.pop()
            return False
                
        
        G = build_graph(tickets)
        trip, length = [], len(tickets)+1
        dfs(G, "JFK")
        return trip

# For case: [["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["BBB", "DDD"], ["DDD", "EEE"], ["DDD", "FFF"], ["FFF", "DDD"], ["JFK","CCC"],["CCC","JFK"]]
# The output of trip from recursion is: 
# []
# ['JFK']
# ['JFK', 'AAA']
# ['JFK', 'AAA', 'JFK']
# ['JFK', 'AAA', 'JFK', 'BBB']
# ['JFK', 'AAA', 'JFK', 'BBB', 'DDD']
# ['JFK', 'AAA', 'JFK', 'BBB', 'DDD']
# ['JFK', 'AAA', 'JFK', 'BBB', 'DDD', 'FFF']
# ['JFK', 'AAA', 'JFK', 'BBB', 'DDD', 'FFF', 'DDD']
# ['JFK', 'AAA', 'JFK']
# ['JFK', 'AAA', 'JFK', 'CCC']
# ['JFK', 'AAA', 'JFK', 'CCC', 'JFK']
# ['JFK', 'AAA', 'JFK', 'CCC', 'JFK', 'BBB']
# ['JFK', 'AAA', 'JFK', 'CCC', 'JFK', 'BBB', 'DDD']
# ['JFK', 'AAA', 'JFK', 'CCC', 'JFK', 'BBB', 'DDD']
# ['JFK', 'AAA', 'JFK', 'CCC', 'JFK', 'BBB', 'DDD', 'FFF']
# ['JFK', 'AAA', 'JFK', 'CCC', 'JFK', 'BBB', 'DDD', 'FFF', 'DDD']

