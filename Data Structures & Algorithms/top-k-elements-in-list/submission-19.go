func topKFrequent(nums []int, k int) []int {
	result := make([][]int, len(nums)+1)

	hashMap := make(map[int]int)

	for _,n := range nums{
		hashMap[n] += 1
	}

	for key, v := range hashMap{
		result[v] = append(result[v], key)
	}

	res := []int{}
	for i:=len(result)-1; i>0; i--{
		if len(res) == k{
			return res
		}
		res = append(res, result[i]...)
	}
	return res
}
