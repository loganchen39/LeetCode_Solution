# Algo. 1
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        : Input data (List[int]): Description;
        : Output (bool): Description;
        :
        : TC: 41.80%, O(n), with for- and while-loop;
        : SC: 50%, O(n) for str_bin_data;
        :\Algo. 1 BF from Ligang, convert int to 8-bit string, and process (maybe return) in a while-loop.
        """
        n = len(data)
        if n == 0: return True
        
        str_bin_data = []
        for v in data:
            str_bin_data.append(format(v, '08b'))  # one key to convert integer to 8-bit string.
            
        i = 0
        # since i will jump like i+=3, so use while instead of for-loop.
        while i < n:  
            if str_bin_data[i][0] == '0':
                i += 1
                # continue
            elif str_bin_data[i][0:3] == '110':
                if i+1 >= n: return False
                if str_bin_data[i+1][0:2] != '10': return False
                i += 2
            elif str_bin_data[i][0:4] == '1110':
                if i+2 >= n: return False
                if str_bin_data[i+1][0:2] != '10' or str_bin_data[i+2][0:2] != '10': return False
                i += 3
            elif str_bin_data[i][0:5] == '11110':
                if i+3 >= n: return False
                if str_bin_data[i+1][0:2] != '10' or str_bin_data[i+2][0:2] != '10' or str_bin_data[i+3][0:2] != '10': 
                    return False  # here you need to return, not to just set to var like: b_res = False, and not return!
                i += 4
            else:
                return False
            
        return True


