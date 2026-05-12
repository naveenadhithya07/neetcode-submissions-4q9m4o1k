class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new=sorted(set(nums))
        nums[:len(new)]=new
        return len(new)
        