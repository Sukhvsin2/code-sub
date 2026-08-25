type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	result := ""

	for _, s := range strs{
		result += strconv.Itoa(len(s)) + "#" + s
	}

	return result

}

func (s *Solution) Decode(encoded string) []string {
	result := []string{}
	i := 0
	for i < len(encoded){
		j := i

		for string(encoded[j]) != "#"{
			j++
		}

		word_length, _ := strconv.Atoi(encoded[i:j])
		word := encoded[j+1 : j+1+word_length]
		result = append(result, word)

		i = j+1+word_length
	}

	return result
}
