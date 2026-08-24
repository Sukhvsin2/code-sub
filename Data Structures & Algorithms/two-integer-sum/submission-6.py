class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        result = []

        for i, n in enumerate(nums):
            if target-n in hashMap:
                return [hashMap.get(target-n, 0), i]
            hashMap[n] = i

        return result
        