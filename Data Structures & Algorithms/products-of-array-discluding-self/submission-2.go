func productExceptSelf(nums []int) []int {
	result := make([]int, len(nums))
	result[0] = 1
	for i:=0; i<len(nums)-1; i++ {
		result[i+1] = result[i] * nums[i]
	}
	suffix := 1
	for i:=len(nums)-1; i>0; i-- {
		result[i] = result[i] * suffix
		suffix *= nums[i]
	}
	result[0] = suffix

	return result
}
