times = 0
while true
	puts "WHAT DO YOU WANT TO ASK GRANDMA???"
	input = gets.chomp
	if input != input.upcase
		puts "HUH?!?! SPEAK UP SON!!!"
		puts ""
	else
		if input != "BYE"
			puts "NO, NOT SINCE " + (1930 + rand(20)).to_s + "!!!"
			puts ""
		else
			times += 1
			if times < 3
				puts "NO, NOT SINCE " + (1930 + rand(20)).to_s + "!!!"
				puts ""
			else
				puts "BYE SON"
				puts ""
				break
			end
		end
	end
end