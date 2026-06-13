class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        n=len(nums)//2
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for num,freq in count.items():
            if freq>n:
                return num        