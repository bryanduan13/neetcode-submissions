func hasDuplicate(nums []int) bool {
    seen:=make(map[int]struct{})
    for index := range nums{
        if _,exists := seen[nums[index]]; exists{
            return true
        }
        seen[nums[index]]=struct{}{}
    }
    return false 
}
