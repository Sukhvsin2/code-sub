import "slices"

func longestConsecutive(nums []int) int {
	if len(nums) < 1{
		return 0
	}
	// sort() and set()
	slices.Sort(nums)
	nums = slices.Compact(nums)

	count := 0
	length := 0
	fmt.Println(nums)
	for i:=0; i<len(nums)-1; i++{
		if nums[i]+1 != nums[i+1]{
			length = 0
			continue
		}
		length++
		count = max(count, length)
	}
	return count+1
}
