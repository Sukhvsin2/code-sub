type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	encoded_str := ""
	for _, word := range strs{
		encoded_str += strconv.Itoa(len(word)) + "#" + word
	}
	return encoded_str
}

func (s *Solution) Decode(encoded string) []string {
	decoded_words := []string{}
	i := 0
	for i < len(encoded) {
		j := i
		for string(encoded[j]) != "#"{
			j++
		}

		word_length, _ := strconv.Atoi(encoded[i:j])
		word := encoded[j+1 : j+1+word_length]
		decoded_words = append(decoded_words, word)
		i = j+1+word_length
	}

	return decoded_words
}
