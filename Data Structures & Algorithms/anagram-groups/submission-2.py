class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for string in strs:
            form=''.join(sorted(string))
            if form in anagram:
                anagram[form].append(string)
            else:
                anagram[form]=[string]
        return list(anagram.values())          

        