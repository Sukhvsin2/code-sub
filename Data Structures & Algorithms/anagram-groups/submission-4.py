class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        # divide that into chars, sort, build back a string
        for s in strs:
            sorted_string = ''.join(sorted(s))
            map.setdefault(sorted_string, []).append(s)

        result = []
        # loop over all values into a list.
        for k, v in map.items():
            result.append(v)
        
        return result