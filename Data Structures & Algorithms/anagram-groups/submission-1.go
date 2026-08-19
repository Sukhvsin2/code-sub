import "slices"

func groupAnagrams(strs []string) [][]string {
	hashMap := make(map[string][]string)
	for _, str := range strs{
		char := []rune(str)
		slices.Sort(char)
		hashMap[string(char)] = append(hashMap[string(char)], str)
	}
	result := [][]string{}
	for _, v := range hashMap{
		result = append(result, v)
	}
	return result
}
