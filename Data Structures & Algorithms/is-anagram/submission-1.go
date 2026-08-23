import (
	"reflect"
	"slices"
)

func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}

	listS, listT := []string{}, []string{}
	for i, _ := range t{
		listS, listT = append(listS, string(s[i])), append(listT, string(t[i]))
	}

	slices.Sort(listS)
	slices.Sort(listT)

	if reflect.DeepEqual(listS, listT){
		return true
	}

	return false
}
