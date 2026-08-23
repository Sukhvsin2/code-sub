func groupAnagrams(strs []string) [][]string {
	hashMap := make(map[string][]string)

	for _, word := range strs{
		sorted_chars := strings.Split(word, "")
		sort.Strings(sorted_chars)
		w:=strings.Join(sorted_chars, "")

		hashMap[w] = append(hashMap[w], word)
	}

	result := [][]string{}

	for _, v := range hashMap{
		result = append(result, v)
	}

	return result
}
