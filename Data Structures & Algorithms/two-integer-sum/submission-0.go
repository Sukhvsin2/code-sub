func twoSum(nums []int, target int) []int {
	var result = make([]int, 2)
	if len(nums) > 1{
		for i := range nums{
			for j:=1; j < len(nums); j++{
				if i == j{
					continue
				}
				if nums[i] + nums[j] == target {
					result[0], result[1] = i, j
					return result
				}
			}
		}
	}

	return result
}
