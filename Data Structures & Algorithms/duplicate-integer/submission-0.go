func hasDuplicate(nums []int) bool {

    set := make(map[int]struct{})

    for _, num := range nums {
        set[num] = struct{}{}
    }

    if len(set) != len(nums){
        return true
    }

    return false
}
