func productExceptSelf(nums []int) []int {
	prefix_array := make([]int, len(nums))
	prefix_array[0] = 1
	for i:=0;i<len(nums)-1;i++{
		prefix_array[i+1] = prefix_array[i] * nums[i]
	}

	suffix := 1

	for i:=len(nums)-1;i>0;i--{
		prefix_array[i] = prefix_array[i] * suffix
		suffix *= nums[i]
	}
	prefix_array[0] = suffix

	return prefix_array

}
