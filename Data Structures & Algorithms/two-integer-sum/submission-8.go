func twoSum(nums []int, target int) []int {
    hash := make(map[int]int)

	for index, n := range nums{

		// after saving num in a map search if target-n exists 
		// if yes then we found both values

		if val, ok := hash[target-n]; ok{
			return []int{val, index}
		}

		// save the value of target-n at index
		hash[n] = index
	}

	return []int{}
}
