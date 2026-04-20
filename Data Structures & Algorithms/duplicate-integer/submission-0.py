class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for num in nums:
            if not num in dct:
                dct[num] = 1 
            else:
                dct[num]+=1
                if dct[num] > 1:
                    return True
        return False

        