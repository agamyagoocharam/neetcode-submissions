class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # Using Hashtable (using array) - optimal
    #     time complexity O(n+m), Space complexity = O(1)
        if len(s) != len(t):
            return False
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')]+=1
            count[ord(t[i]) - ord('a')]-=1
        for val in count:
            if val!=0:
                return False
        return True
    #Using Hashmap
    #time complexity O(n+m), Space Complexity o(1) as we have just 26 chars
    
        # if len(s)!=len(t):
        #     return False
        # dct_s,dct_t = {},{}
        # for i in range(len(s)):
        #     dct_s[s[i]] = dct_s.get(s[i],0) + 1
        #     dct_t[t[i]] = dct_t.get(t[i],0) + 1
        # return dct_s==dct_t
        

        