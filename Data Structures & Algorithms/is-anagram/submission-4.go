func isAnagram(s string, t string) bool {
	seen1:=make(map[byte]int)
	seen2:=make(map[byte]int)
	for index := range len(s){
		if _,exists := seen1[s[index]]; exists{
			seen1[s[index]] +=1
		}else{
			seen1[s[index]]=1
		}
	}
	for index := range len(t){
		if _,exists := seen2[t[index]]; exists{
			seen2[t[index]] +=1
		}else{
			seen2[t[index]]=1
		}
	}
	if len(seen1) != len(seen2) {
    return false
}

	for char, count := range seen1 {
		if seen2[char] != count {
			return false
		}
	}

	return true
}
