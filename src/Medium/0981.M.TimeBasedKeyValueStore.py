# Algo. 1
class TimeMap:
    """
    : TC (for get()): O(n)=O(len(lst_val)), "Time Limit Exceeded" with 44/45 test cases passed, TC not good; 
    : SC: O(n) for self.d_map; 
    :\Algo. 1 from Ligang using Dictionary as Hash Tabel, The question is how to deal with the TC issue as it pointed out
    : it will call a total of 120000 times (combined) per test case! 
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d_map[key] = self.d_map.get(key, []) + [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d_map: return ""
        
        lst_val = self.d_map[key]
        
        # This initialization is wrong, think about the case: 
        # ["TimeMap","set","set","get","get","get","get","get"]
        # [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
        #str_res = lst_val[0][1]  # wrong, think about the case: 
        #ts      = lst_val[0][0]
        
        str_res = ""
        ts      = 0
        for i in range(len(lst_val)):
            if lst_val[i][0] > ts and lst_val[i][0] <= timestamp:
                str_res = lst_val[i][1]
                ts      = lst_val[i][0]
        
        return str_res
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)




# Algo. 2
class TimeMap:
    """
    :\Algo. 2 from Ligang using Dictionary as Hash Tabel, The question is how to deal with the TC issue as it pointed out
    : it will call a total of 120000 times (combined) per test case! Since the timestamp is strictly increasing, 
    : we can use binary search to improve TC, but it still has "Time Limit Exceeded" error and only passed 44/45 test cases.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d_map[key] = self.d_map.get(key, []) + [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d_map: return ""    
        lst_val = self.d_map[key]
        n       = len(lst_val)
        
        # since the timestamp is strictly increasing, so we can use binary search algo. 
        low, high = 0, n-1
        if timestamp <  lst_val[low ][0]: return ""
        if timestamp >= lst_val[high][0]: return lst_val[high][1]
        while low <= high:
            mid = int((low+high)/2)
            if timestamp == lst_val[mid][0]:
                return lst_val[mid][1]
            elif timestamp < lst_val[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        return lst_val[low-1][1]
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)




# Algo. 3
class TimeMap:
    """
    : TC: 49.58%, set O(1), get O(logn) in worst case;
    : SC: 20%, O(N), 
    :\Algo. 3 from solu 1, which uses collections.defaultdict(list), and bisect.bisect. Not totally 
    : understand it yet.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #self.M[key] = self.d_map.get(key, []) + [[timestamp, value]]
        self.M[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        A = self.M.get(key, None)
        if A is None: return ""
        
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)




