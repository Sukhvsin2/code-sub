func topKFrequent(nums []int, k int) []int {
	if(len(nums) > 1){
		countMap := make(map[int]int)
		freq := make([][]int, len(nums)+1)

		for _, n := range nums{
			countMap[n] = countMap[n] + 1
		}

		for key, val := range countMap{
			freq[val-1] = append(freq[val-1],key)
		}

		result := []int{}
		for i:=len(nums); i>=0; i-- {
			if len(freq[i]) != 0 {
				if len(result) >= k {
					break
					return result[:k]
				}
				result = append(result, freq[i]...)
			}
		}
		return result
	}

	return nums
}
