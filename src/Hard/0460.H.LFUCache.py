# Algo. 1
from collections import OrderedDict
from heapq       import *

class LFUCache:
    """
    : TC: 75.36%, 
    : SC: 50%, 
    : 
    :\1st idea, key problem is SORTING according to the number of access, set an counter for each key-value item. 
    : Every time it needs to evict an item, it evicts the least frequently used item. Heap queue with dict?
    : dict_cache[key] = [count, value]? 
    :\idea, we can use several data structures! Not just one!
    :\Algo. 1 from Discuss "Python fast (220ms) using heap", partially implemented by Ligang.
    : Question: How will the heap_queue self.pq (freq, time, key) work? First according to freq, and then time? 
    : What about the last "key" element? The element should be tuple, not list, which means you can not assign
    : or change their values. So whenever freq becomes freq+1, you need to first pop it and then push it back.
    : But the heap_queue only pops out the first/smallest element, that's why here we have to use the set 
    : self.set_update, or it will not work out, because when freq becomes freq+1, it does not necessarily 
    : the 1st/smallest element! 
    : According to my test, heap_queue will be sorted according to all elements (here, freq/time/key), although
    : it will also sort by the 3rd element of "key" which we do not need, but it does not matter.  
    """

    def __init__(self, capacity: int):
        self.capacity       = capacity
        self.time           = 0
      # self.dict_cache     = collections.OrderedDict()
        self.dict_map       = {}  # key->value
        self.dict_freq_time = {}  # key->freq, time
        self.pq             = []  # [freq, time, key]
        self.set_update     = set()
        

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.dict_map:
            freq, _                  = self.dict_freq_time[key]
            self.dict_freq_time[key] = [freq+1, self.time]
            # update self.pq? 
            self.set_update.add(key)
            
            return self.dict_map[key]
        else:
            return -1

        
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0: return -1
        
        self.time += 1
        
        if key in self.dict_map:
            freq, _ = self.dict_freq_time[key]
            self.dict_freq_time[key] = [freq+1, self.time]
            # update self.pq?
            self.set_update.add(key)
            self.dict_map[key] = value
        else:
            if len(self.dict_map) < self.capacity:
                self.dict_map[key]       = value
                self.dict_freq_time[key] = [1, self.time]
                heappush(self.pq, (1, self.time, key))
            else:
                # First update previously visited keys, to re-order the heap_queue correctly.
                while self.pq and self.pq[0][2] in self.set_update:
                    key_update = self.pq[0][2]
                    heappop(self.pq)
                    freq, time = self.dict_freq_time[key_update]
                    heappush(self.pq, (freq, time, key_update))
                    self.set_update.remove(key_update)
                
                # Then we can remove the LFU item, and add the new item
                freq_lfu, time_lfu, key_lfu = self.pq[0]
                self.dict_map.pop(key_lfu)
                self.dict_freq_time.pop(key_lfu)
                heappop(self.pq)
                
                self.dict_map[key] = value
                self.dict_freq_time[key] = [1, self.time]
                heappush(self.pq, (1, self.time, key))
                

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




