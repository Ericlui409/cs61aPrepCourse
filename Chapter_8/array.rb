puts "Type as many words as you want!"
list = []
while true
	input = gets.chomp
	if input.length > 0
		list.push input
	else
		puts list.sort
		break
	end
end

