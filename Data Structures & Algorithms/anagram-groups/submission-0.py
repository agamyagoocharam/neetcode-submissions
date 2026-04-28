class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            count = [0]*26
            for i in word:
                count[ord(i)-ord('a')]+=1
            result[tuple(count)].append(word)
        return list(result.values())

        #Using Sorting Technique (m*nlogn)
        # result = defaultdict(list)
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     result[sorted_word].append(word)
        # return list(result.values())
            