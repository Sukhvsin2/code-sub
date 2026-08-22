func productExceptSelf(nums []int) []int {
    prefix := make([]int, len(nums))
    suffix := make([]int, len(nums))

    prefix[0], suffix[len(suffix)-1] = 1, 1


    for i:=0; i<len(nums)-1; i++{
        prefix[i+1] = prefix[i] * nums[i]
    }

    for i:=len(nums)-1; i>0; i--{
        suffix[i-1] = suffix[i] * nums[i]
    }

    result := make([]int, len(nums))
    result[0] = suffix[0]
    result[len(result)-1] = prefix[len(prefix)-1]
    for i:=1;i<len(nums)-1;i++{
        result[i] = prefix[i] * suffix[i]
    }

    return result
}

