func hasDuplicate(nums []int) bool {
    m := make(map[int]int)

    for _, n := range nums{
        m[n] = m[n]+1
        if m[n] > 1{
            return true
        }
    }

    return false
}
