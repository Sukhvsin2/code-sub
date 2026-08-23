func topKFrequent(nums []int, k int) []int {
	array := make([][]int, len(nums)+1)
	hashMap := make(map[int]int)
	for _, num := range nums{
		hashMap[num] += 1
	}

	for k, v := range hashMap{
		array[v] = append(array[v], k) 
	}
	result := []int{}

	for i:=len(array)-1; i>0; i--{
		if len(result) < k{
			result = append(result, array[i]...)
		}
	}

	return result
}
