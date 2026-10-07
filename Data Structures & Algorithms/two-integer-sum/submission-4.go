func twoSum(nums []int, target int) []int {
    seen:=make (map[int]int)
    complement:=0
    for index := range nums {
        complement = target - nums[index]
        if val,exists :=seen[complement];exists {
            return []int {val,index}
        }
        seen[nums[index]]=index
    }
    return []int{0,0}
}
