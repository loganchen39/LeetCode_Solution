# Algo. 1
class MedianFinder:
    def __init__(self):
        """
        :initialize your data structure here.
        
        :TC: addNum: O(n); findMedian: O(1); 17 / 18 test cases passed, with Time Limit Exceeded on a large case.
        :SC: O(n) for addNum; 
        :\Algo. 1 from Ligang using list and Straight Insertion Sort which failed as Time Limit Exceeded. 
        : The TC of O(n) for addNum seems not acceptable, or it's too easy to be "Hard". Need to use a more 
        : efficient data structure for this particular problem. 
        """
        self.lst_data = []
        
        
    def addNum(self, num: int) -> None:
        n = len(self.lst_data)
        if n == 0: self.lst_data.append(num)
        else: 
            for i in range(n):
                if num <= self.lst_data[i]:
                    self.lst_data.insert(i, num)
                    break  # don't forget this!
            else: 
                self.lst_data.append(num)

                
    def findMedian(self) -> float:
        # print(self.lst_data)
        n = len(self.lst_data)
        if n == 0: return None
        elif n%2 == 1: return self.lst_data[int(n/2)]
        else: return sum(self.lst_data[int(n/2)-1:int(n/2)+1])/2




# Algo. 2
class MedianFinder:
    def __init__(self):
        """
        :initialize your data structure here.
        
        :TC: 6.78%, addNum: O(n*logn) for both search/comparison and moving element; findMedian: O(1); 
        :SC: 6.67%, O(n) for addNum; 
        :\Algo. 2 from Ligang using list and Binary Insertion Sort, whose time complexity is better than
        : Straight Insertion Sort. The TC of insertion one element and moving elements afterward for list
        : is of O(n), right?! While the search and comparsion TC for 2 algos are O(n) and O(logn), respectively,
        : the latter is better.
        """
        self.lst_data = []
        
        
    def addNum(self, num: int) -> None:
        n = len(self.lst_data)
        if n == 0: self.lst_data.append(num); return
        if num <= self.lst_data[0]: self.lst_data.insert(0, num); return
        if num >= self.lst_data[n-1]: self.lst_data.append(num); return
            
        # use binary insertion Sort
        low, high = 0, n - 1
        while low <= high:
            mid = int((low+high)/2)
            if num == self.lst_data[mid]: self.lst_data.insert(mid, num); return
            elif num < self.lst_data[mid]: high = mid-1
            else: low = mid+1
        #self.lst_data.insert(high+1, num)  # This works ok!
        self.lst_data.insert(low, num)  # This also works ok! Finally high+1=low; 
        
                
    def findMedian(self) -> float:
        # print(self.lst_data)
        n = len(self.lst_data)
        if n == 0: return None
        elif n%2 == 1: return self.lst_data[int(n/2)]
        else: return sum(self.lst_data[int(n/2)-1:int(n/2)+1])/2

