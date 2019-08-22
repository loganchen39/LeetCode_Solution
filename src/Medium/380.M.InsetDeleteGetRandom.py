# Algo. 1
import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        
        TC: O(1), 28.88%, 
        SC: O(n), 12.50%, 

        Algo. 1 from Ligang, According the requirement, the HashTable (Set) would be the ideal choice of data structure. 
        """
        self.randSet = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.randSet: return False
        self.randSet.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.randSet: 
            self.randSet.remove(val)
            return True
        else: return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        
        Should get familiar with module random; 
        """
        #n = len(self.randSet)  # Set is not "indexable"
        # random on the indices, or on the element directly, Set can be converted to Tuple or List.
        return random.choice(tuple(self.randSet))

