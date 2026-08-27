import "slices"

func isValidSudoku(board [][]byte) bool {
    rows := make(map[int][]int, 9)
    cols := make(map[int][]int, 9)
    square := make(map[[2]int][]int, 9)

    for r := range(9){
        for c := range(9){
            val := string(board[r][c])
            if val == "."{
                continue
            }
            intVal, _ := strconv.Atoi(val)
            if slices.Contains(rows[r], intVal) || slices.Contains(cols[c], intVal) || slices.Contains(square[[2]int{r/3, c/3}], intVal) {
                return false
            }
            rows[r] = append(rows[r], intVal)
            cols[c] = append(cols[c], intVal)
            square[[2]int{r/3, c/3}] = append(square[[2]int{r/3, c/3}], intVal)
        }
    }
    return true
}
