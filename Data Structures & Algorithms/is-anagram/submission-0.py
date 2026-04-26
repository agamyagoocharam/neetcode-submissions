class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_s, dct_t = {},{}
        for letter in s:
            if letter not in dct_s:
                dct_s[letter] = 1
            else: 
                dct_s[letter]+=1
        for letter in t:
            if letter not in dct_t:
                dct_t[letter] = 1
            else:
                dct_t[letter]+=1
        if dct_s == dct_t:
            return True
        else:
            return False

        