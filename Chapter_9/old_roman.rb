def old_roman_numeral number
	m = number / 1000
	d = (number % 1000) / 500
	c = (number % 500) / 100
	l = (number % 100) / 50
	x = (number % 50) / 10
	v = (number % 10) / 5
	i = number % 5
	return "M" * m + "D" * d + "C" * c + "L" * l + "X" * x + "V" * v + "I" * i
end

puts old_roman_numeral 4
puts old_roman_numeral 67
puts old_roman_numeral 185
puts old_roman_numeral 1834
puts old_roman_numeral 2999
puts old_roman_numeral 3000
