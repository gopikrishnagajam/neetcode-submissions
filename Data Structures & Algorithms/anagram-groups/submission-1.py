class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def check_ana(str1 ,str2):
            count = {}
            for char in str1:
                count[char] = 1 + count.get(char ,0)
            for char in str2:
                if char not in count:
                    return False
                else:
                    count[char]-=1
                    if count[char] == 0:
                        del count[char]
            return True if not count else False
        ana = {}

        i = 0
        while i<len(strs):
            c=i
            for key in ana:
                if check_ana(key, strs[i]):
                    ana[key].append(strs[i])
                    i+=1
                    break
            if c==i:
                ana[strs[i]]= [strs[i]]
                i+=1
            

        res = []
        for key in ana:
            res.append(ana[key])
        return res
            
            
                