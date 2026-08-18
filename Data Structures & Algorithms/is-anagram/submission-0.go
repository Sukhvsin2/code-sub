import "slices"
func isAnagram(s string, t string) bool {
    if len(s) != len(t){
        return false
    }

    itemS, itemT := divideString(s), divideString(t)

    for i := range len(itemS){
        if itemS[i] != itemT[i]{
            return false
        }
    }

    return true
}

func divideString(s string) []string{
    items := make([]string, len(s))
    for _, c := range s{
        fmt.Println(string(c))
        items = append(items, string(c))
    }

    slices.Sort(items)
    return items
}