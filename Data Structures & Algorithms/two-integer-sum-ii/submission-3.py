class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]

        i, j = 0, len(numbers)-1

        while i < j:
            if target > (numbers[i] + numbers[j]):
                i += 1
            
            if target < (numbers[i] + numbers[j]):
                j -= 1
            
            if target == (numbers[i] + numbers[j]):
                return [i+1, j+1]
        
        return []