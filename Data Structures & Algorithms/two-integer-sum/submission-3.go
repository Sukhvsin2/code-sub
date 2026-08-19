func twoSum(nums []int, target int) []int{
	dict := make(map[int]int)
	for i := range nums{
		_, ok := dict[target - nums[i]]
		if ok {
			return []int{dict[target-nums[i]], i}
		}
 		dict[nums[i]] = i
	}

	return []int{}
}
