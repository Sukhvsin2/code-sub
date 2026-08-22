func topKFrequent(nums []int, k int) []int {
	// hashmap with counts
	countMap := make(map[int]int)
	for _, n := range(nums){
		countMap[n] += 1
	}

	// sort that hashmap on count basis
	arr := make([][2]int, 0, len(countMap))
	for key, val := range countMap{
		arr = append(arr, [2]int{val, key})
	}

	sort.Slice(arr, func(i, j int) bool {
		return arr[i][0] > arr[j][0]
	})


	// return k values from sorted map/array
	result := make([]int, k)
	for i:=0; i<k;i++{
		result[i] = arr[i][1]
	}

	return result
}
