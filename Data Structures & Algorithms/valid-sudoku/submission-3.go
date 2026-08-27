func isValidSudoku(board [][]byte) bool {
    rows := make(map[int]map[byte]struct{})
    cols := make(map[int]map[byte]struct{})
    square := make(map[[2]int]map[byte]struct{})

    for r := range(9){
        for c := range(9){
            val := board[r][c]
            if string(val) == "."{
                continue
            }

            if contains(rows[r], val) || 
                contains(cols[c], val) || 
                contains(square[[2]int{r/3, c/3}], val){
                return false
            }
            if rows[r] == nil {
                rows[r] = make(map[byte]struct{})
            }

            if cols[c] == nil {
                cols[c] = make(map[byte]struct{})
            }

            key := [2]int{r / 3, c / 3}

            if square[key] == nil {
                square[key] = make(map[byte]struct{})
            }

            rows[r][val] = struct{}{}
            cols[c][val] = struct{}{}
            square[key][val] = struct{}{}
        }
    }
    return true
}

func contains(m map[byte]struct{}, val byte) bool{
    _, exists := m[val]
    return exists
}
