type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	var encoded_string string
	for _, s := range strs{
		num := len(s)
		encoded_string += strconv.Itoa(num) + "#" + s
	}
	return encoded_string
}

func (s *Solution) Decode(encoded string) []string {
	words:= []string{}
	i := 0
	for i < len(encoded){
		j := i
		fmt.Println(string(encoded[j]))
		for string(encoded[j]) != "#"{
			j++
		}
		length, _ := strconv.Atoi(string(encoded[i:j]))


		word := encoded[j+1 : j+1+length]
		words = append(words, word)
		i = j+1+length

	}

	return words
}
