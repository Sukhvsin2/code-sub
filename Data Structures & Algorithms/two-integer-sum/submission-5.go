func twoSum(nums []int, target int) []int {
    dict := make(map[int]int)
	result := []int{}
	for i, n := range nums{
		if val, ok := dict[target-n]; ok {
			return []int{val, i}
		}
		dict[n] = i
	}

	return result
}
