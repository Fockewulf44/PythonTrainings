# Running Sum solution
class Solution:
    def runningSum(nums: list[int]) -> list[int]:
        Sumlist = []
        ind = 0
        for i in nums:
            ind += i
            Sumlist.append(ind)
        return Sumlist