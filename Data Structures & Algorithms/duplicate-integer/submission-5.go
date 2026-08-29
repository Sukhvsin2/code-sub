func hasDuplicate(nums []int) bool {
    hash := make(map[int]int)
    for _, n:=range nums{
        if _, ok := hash[n]; ok {
            fmt.Println(n, hash[n])
            return true
        }

        hash[n] += 1
    }

    return false
    
}
