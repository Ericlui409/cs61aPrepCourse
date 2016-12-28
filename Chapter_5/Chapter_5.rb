puts "Hello! What is your first name?"
first_name = gets.chomp
puts "What is your middle name?"
middle_name = gets.chomp
puts "What is your last name?"
last_name = gets.chomp
puts "Greetings, " + first_name + " " + middle_name + " " + last_name + "."

puts "What is your favourite number?"
number = gets.chomp.to_i + 1
puts "Your number is too small, use " + number.to_s + " instead."