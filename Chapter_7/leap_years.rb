puts "Please enter a starting year."
s = gets.chomp.to_i

puts "Please enter an ending year."
e = gets.chomp.to_i

puts ""
while s <= e
	if s % 4 == 0 && s % 100 != 0 || s % 400 == 0
		puts s
	end
	s += 1
end