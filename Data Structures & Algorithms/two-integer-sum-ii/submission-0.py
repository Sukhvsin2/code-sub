class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if len(numbers) == 2:
            return [1, 2]

        map = {}

        for i in range(len(numbers)):
            found_it = map.get(target - numbers[i], 0)
            if found_it:
                # print("found_it at index ", found_it, " and value ", target-numbers[i])
                return [found_it, i+1]
            map[numbers[i]] = i+1
            # print(i, " : ", map)

        return []
        