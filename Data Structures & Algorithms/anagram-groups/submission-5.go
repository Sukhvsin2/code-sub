import "slices"
func groupAnagrams(strs []string) [][]string {
	hashMap := make(map[string][]string)
	for _, str := range strs{
		splitStr := strings.Split(str, "")
		slices.Sort(splitStr)
		sortedStr := strings.Join(splitStr,"")
		hashMap[sortedStr] = append(hashMap[sortedStr], str)
	}
	result := [][]string{}
	for _, v := range hashMap{
		result = append(result, v)
	}

	return result
}
