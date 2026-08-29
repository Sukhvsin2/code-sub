func productExceptSelf(nums []int) []int {
	prefix := make([]int, len(nums))

	prefix[0] = 1

	for i:=1; i<len(nums);i++{
		prefix[i] = nums[i-1] * prefix[i-1]
	}

	suffix := 1

	for i := len(nums)-1; i>0; i--{
		prefix[i] = prefix[i] * suffix
		suffix = suffix * nums[i]

	}

	prefix[0] = suffix

	return prefix

}
