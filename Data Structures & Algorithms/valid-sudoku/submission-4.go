import "slices"

func isValidSudoku(board [][]byte) bool {
	rows := make(map[int][]int, 9) 
	cols := make(map[int][]int, 9) 
	square := make(map[[2]int][]int, 9) 

	for r := range(9){
		for c := range(9){
			if string(board[r][c]) == "."{
				continue
			}
			val, _ := strconv.Atoi(string(board[r][c]))
			if slices.Contains(rows[r], val) || slices.Contains(cols[c], val) || slices.Contains(square[[2]int{r/3, c/3}], val) {
				return false
			}
			rows[r] = append(rows[r], val)
			cols[c] = append(cols[c], val)
			square[[2]int{r/3, c/3}] = append(square[[2]int{r/3, c/3}], val)
		}
	}

	return true
}
