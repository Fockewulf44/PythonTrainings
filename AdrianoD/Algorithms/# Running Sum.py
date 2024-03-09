# Running Sum solution
import typing


def runningSum(nums: list[int]) -> list[int]:
    Sumlist = []
    ind = 0
    for i in nums:
        ind += i
        Sumlist.append(ind)
    return Sumlist

list1 = [1,2,3,4,5]

print(runningSum(list1))
