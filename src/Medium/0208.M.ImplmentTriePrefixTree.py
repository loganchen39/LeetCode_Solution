# Algo. 1
class Trie:
    """
    : TC: 92.02%, O(n) (n being the word length), for all 3 functioins.
    : SC: 62.96%, O(N), N being the length of all characters of all words.
    :
    :\The key is to choose what data structure to use to store the Trie.
    :\Algo. 1 from Discuss "Simple Python solution (beats 99% runtime, 95% memory)", implemented by Ligang,
    : using dict, no need for extra TrieNode class. It's efficient and easy to understand and implement. 
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for c in word:
            if c not in t: t[c] = {}
            t = t[c]
            
        t["-"] = {}  # sign as end of the word
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for c in word:
            if c not in t: return False
            else: t = t[c]
        if "-" in t: return True
        else: return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for c in prefix:
            if c not in t: return False
            else: t = t[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)




