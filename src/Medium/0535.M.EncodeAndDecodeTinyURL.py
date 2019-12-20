# Algo. 1
class Codec:
    """
    : TC: 90.39%, O(1)
    : SC: 35.71%, O(n) for self.dic.
    : 
    :\1st idea, some kind of mapping, hash table. 
    :\Algo. 1 from A. 1 implement by Ligang, using simple counter, if needed, you can also add time info.
    : like "201910222238" to make sure the uniqueness of the id, like what we did in the Kola project
    : at Box company in Hangzhou.
    """
    def __init__(self):
        self.cnt = 0
        self.dic = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.cnt += 1
        self.dic[self.cnt] = longUrl
        return "http://tinyurl.com/" + str(self.cnt)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        s0, s1, s2 = shortUrl.rpartition("/")
        return self.dic[int(s2)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))




