def dict_sort some_array
	recursive_dict_sort some_array, []
end

def recursive_dict_sort unsorted_array, sorted_array
	if unsorted_array.length == 0
		puts sorted_array.to_s
	else
		min = unsorted_array[0].downcase
		remove = unsorted_array[0]
		unsorted_array.each do |number|
			if number.downcase < min
				min = number.downcase
				remove = number
			end
		end
		recursive_dict_sort (unsorted_array - [remove]), (sorted_array.push remove)
	end
end

dict_sort ["b","s","h","w","d","q","s","f"]
dict_sort ["D", "a", "c", "B", "f'", "E"]