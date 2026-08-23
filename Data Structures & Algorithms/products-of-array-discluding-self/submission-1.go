func productExceptSelf(nums []int) []int {
	// save product in prefix and suffix then multiply them.
	prefix := make([]int, len(nums))
	suffix := make([]int, len(nums))

	// save
	prefix[0], suffix[len(nums)-1] = 1,1


	// prefix loop
	for i:=0; i<len(nums)-1;i++{
		prefix[i+1] = prefix[i] * nums[i]
	}

	// suffix loop
	for i:=len(nums)-1; i>0; i--{
		suffix[i-1] = suffix[i] * nums[i]
	}

	result := make([]int, len(nums))
	// product of prefix and suffix
	for i:=0; i<len(nums); i++{
		result[i] = prefix[i] * suffix[i]
	}

	return result
}
