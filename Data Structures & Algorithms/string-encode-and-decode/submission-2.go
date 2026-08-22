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

	// loop until end of string
	for i < len(encoded){
		j := i
		// loop over number until we find #
		for string(encoded[j]) != "#"{
			j++
		}
		// convert length of number into int
		length, _ := strconv.Atoi(encoded[i:j])

		// read word by slice
		word := encoded[j+1 : j+1+length]
		// add word into the list
		words = append(words, word)

		// skip the counter to index after the above word.
		i = j+1+length

	}

	return words
}
