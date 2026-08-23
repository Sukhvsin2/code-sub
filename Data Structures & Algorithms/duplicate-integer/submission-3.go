func hasDuplicate(nums []int) bool {
    dict := make(map[int]int)

    for _, n := range(nums){
        if _, ok := dict[n]; ok {
            return true
        }
        dict[n] += 1
    }

    return false
}
