func twoSum(nums []int, target int) []int {
    seen:=make (map[int]int)
    complement:=0
    for index := range nums {
        complement = target - nums[index]
        if _,exists :=seen[complement];exists {
            return []int {seen[complement],index}
        }else {seen[nums[index]]=index}
    }
    return []int{0,0}
}
