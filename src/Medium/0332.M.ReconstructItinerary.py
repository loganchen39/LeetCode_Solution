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




