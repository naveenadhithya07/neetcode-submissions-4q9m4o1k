class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        result=[]
        for _ in range(k):
            last_element=nums.pop()
            result=nums.insert(0,last_element)
        return result