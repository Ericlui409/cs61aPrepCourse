def sort some_array
	recursive_sort some_array, []
end

def recursive_sort unsorted_array, sorted_array
	if unsorted_array.length == 0
		puts sorted_array.to_s
	else
		min = unsorted_array[0]
		unsorted_array.each do |number|
			if number < min
				min = number
			end
		end
		recursive_sort (unsorted_array - [min]), (sorted_array.push min)
	end
end

sort [2,4,6,4,9,1,5]
sort [7,3,4,2,8,13,17]
sort ["b","s","h","w","d","q","s","f"]