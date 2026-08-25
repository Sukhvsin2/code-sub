func topKFrequent(nums []int, k int) []int {
    hashMap := make(map[int]int)
    for _, n := range nums{
        hashMap[n] += 1
    }

    freqArray := make([][]int, len(nums)+1)
    for k, v := range hashMap {
        freqArray[v] = append(freqArray[v], k)
    }

    result := []int{}
    for i:=len(nums); i>0; i--{
        if len(result) < k{
            result = append(result, freqArray[i]...)
        }
    }

    return result
}
