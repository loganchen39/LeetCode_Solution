# Algo. 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        : Input x (int):
        : Output (bool):
        :
        : TC: 99.10%, O(1),
        : SC: 6.5%(should be wrong), O(1)
        :\Algo. 1 BF from Ligang, Convert int to string, and then compare with reverse.
        """
        if x < 0: return False
        
        str_x = str(x)
        if str_x == str_x[-1::-1]: return True
        else: return False




# Algo. 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        : Input x (int):
        : Output (bool):
        :
        : TC: 27.10%, O(1),
        : SC: 6.5%(should be wrong), O(1)
        :\Algo. 2 BF from Solu. 1, Revert the last half of the number; 
        """
        if x < 0: return False
        if x%10 == 0 and x != 0: return False
        if 0 <= x and x <= 9: return True
        
        reverse_2nd_part = 0  # x%10
        first_part       = x  # int(x/10)
        while reverse_2nd_part <= first_part:
            reverse_2nd_part = reverse_2nd_part*10 + first_part%10
            first_part       = int(first_part/10)
            if reverse_2nd_part == first_part        : return True
            if reverse_2nd_part == int(first_part/10): return True
        else:
            return False

