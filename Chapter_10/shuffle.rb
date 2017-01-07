def shuffle some_array
	recursive_shuffle some_array, []
end

def recursive_shuffle unshuffled_array, shuffled_array
	if unshuffled_array.length == 0
		puts shuffled_array.to_s
	else
		random = unshuffled_array[rand(unshuffled_array.length)]
		recursive_shuffle (unshuffled_array - [random]), (shuffled_array.push random)
	end
end

shuffle [1,2,4,6,9,14,18]
shuffle [2,3,4,7,8,13,17]