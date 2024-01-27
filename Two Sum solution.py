def twoSum(nums: list[int], target: int):
    dict = {}
    i = 0
    
    while i < len(nums):
        if dict.get(target - nums[i]) != None:
            print(dict)
            return [dict.get(target - nums[i]),i]
        dict.update({nums[i]: i})
        i += 1
        
print(twoSum([4, 7, 2, 5, 12, 7, 4, 10], 19))

