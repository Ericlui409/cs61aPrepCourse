def roman_numeral number
	m  = number / 1000
	cm = (number % 1000) / 900
	d  = ((number % 1000) % 900) / 500
	cd = (((number % 1000) % 900) % 500) / 400
	c  = ((((number % 1000) % 900) % 500) % 400) / 100
	xc = (((((number % 1000) % 900) % 500) % 400) % 100) / 90
	l  = ((((((number % 1000) % 900) % 500) % 400) % 100) % 90) / 50
	xl = (((((((number % 1000) % 900) % 500) % 400) % 100) % 90) % 50) / 40
	x  = ((((((((number % 1000) % 900) % 500) % 400) % 100) % 90) % 50) % 40) / 10
	ix = (((((((((number % 1000) % 900) % 500) % 400) % 100) % 90) % 50) % 40) % 10) / 9
	v  = ((((((((((number % 1000) % 900) % 500) % 400) % 100) % 90) % 50) % 40) % 10) % 9 ) / 5
	iv = (((((((((((number % 1000) % 900) % 500) % 400) % 100) % 90) % 50) % 40) % 10) % 9 ) % 5) / 4
	i  = ((((((((((((number % 1000) % 900) % 500) % 400) % 100) % 90) % 50) % 40) % 10) % 9 ) % 5) % 4)
	return "M" * m + "CM" * cm + "D" * d + "CD" * cd + "C" * c + "XC" * xc + "L" * l + "XL" * xl + "X" * x + "IX" * ix + "V" * v + "IV" * iv + "I" * i
end

puts roman_numeral 4
puts roman_numeral 97
puts roman_numeral 185
puts roman_numeral 1834
puts roman_numeral 2999
puts roman_numeral 3000
