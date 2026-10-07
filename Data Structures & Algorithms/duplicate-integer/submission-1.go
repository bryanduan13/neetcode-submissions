func hasDuplicate(nums []int) bool {
    seen:=make(map[int]int)
    for index := range nums{
        if _,exists := seen[nums[index]]; exists{
            return true
        }
        seen[nums[index]]=1
    }
    return false 
}
