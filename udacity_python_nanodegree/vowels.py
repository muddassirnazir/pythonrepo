prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"

vowel_count = 0
prophecy_lower = prophecy.lower()
# TODO: set the value of vowel_count to be the number of vowels in prophecy
vowel_count = prophecy_lower.count('a')
vowel_count += prophecy_lower.count('e')
vowel_count +=prophecy.count('i')
vowel_count +=prophecy.count('o')
vowel_count += prophecy.count('u')


# Print the final count
print(vowel_count)
