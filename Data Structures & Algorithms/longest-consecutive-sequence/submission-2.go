func longestConsecutive(nums []int) int {
	set := make(map[int]struct{})

	for _, n := range nums{
		set[n] = struct{}{}
	}

	longest := 0
	fmt.Println(set)
	for n, _ := range set{
		_, exists := set[n-1]
		if !exists {
			length := 0
			run := true
			for run{
				if _, increment_exists := set[n+length]; !increment_exists{
					run = false
					break
				}
				length++
			}
			longest = max(longest, length)
		}

	}

	return longest
}
