import "slices"
func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}

	splitS, splitT := strings.Split(s, ""), strings.Split(t, "")
	fmt.Println(splitS, splitT)

	slices.Sort(splitS)
	slices.Sort(splitT)

	S, T := strings.Join(splitS, ""), strings.Join(splitT, "")

	if S == T{
		return true
	}
	return false
}
