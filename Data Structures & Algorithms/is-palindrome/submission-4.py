class Solution:
	def isPalindrome(self, s: str) -> bool:
		i, j = 0, len(s)-1

		while i < j:

			while i < j and not s[i].isalnum():
				i += 1
				# print("i moved ",i , " = ", s[i])
			
			while j > i and not s[j].isalnum():
				j -= 1
				# print("j moved ",j , " = ", s[j])

			# print(s[i].lower() , "!=", s[j].lower())
			if s[i].lower() != s[j].lower():
				return False
			i+=1
			j-=1

		return True
