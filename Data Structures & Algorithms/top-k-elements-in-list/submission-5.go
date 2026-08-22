func topKFrequent(nums []int, k int) []int {
	countMap := make(map[int]int)
	for _, n := range nums{
		countMap[n] = countMap[n] + 1
	}

	freq := make([][]int, len(nums)+1)
	for key, val := range countMap{
		freq[val-1] = append(freq[val-1],key)
	}

	var result []int
	for i:=len(nums); i>=0; i-- {
		if len(freq[i]) > 0 {
			if len(result) == k {
				return result
			}
			result = append(result, freq[i]...)
		}
	}

	return result
}
