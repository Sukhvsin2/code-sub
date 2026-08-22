type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	var encoded_str string
	for _, s := range strs{
		encoded_str += strconv.Itoa(len(s)) + "#" + s
	}

	return encoded_str
}

func (s *Solution) Decode(encoded string) []string {
	fmt.Println(encoded)
	words := []string{}
	i:=0
	for i < len(encoded){
		j := i
		for string(encoded[j]) != "#"{
			j += 1
		}
		// now b/w i and j we have the word's length number
		length, err := strconv.Atoi(encoded[i:j])
		if err != nil{
			panic(err)
		}
		words = append(words, encoded[j+1 : j+1+length])
		i = j+1+length
	}

	return words
}
