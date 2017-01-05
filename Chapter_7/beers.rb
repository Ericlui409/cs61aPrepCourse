i = 99
while true
	if i > 2
		puts i.to_s + " bottles of beer on the wall, " + i.to_s + " bottles of beer."
		puts "Take one down and pass it around, " + (i - 1).to_s + " bottles of beer on the wall."
		puts ""
		i += -1
	elsif i == 2
		puts "2 bottles of beer on the wall, 2 bottles of beer."
		puts "Take one down and pass it around, 1 bottle of beer on the wall."
		puts ""
		i += - 1
	elsif i == 1
		puts "1 bottle of beer on the wall, 1 bottle of beer."
		puts "Take one down and pass it around, no more bottles of beer on the wall."
		puts ""
		i += - 1
	else
		puts "No more bottles of beer on the wall, no more bottles of beer."
		puts "Go to the store and buy some more, 99 bottles of beer on the wall."
		puts ""
		break
	end
end