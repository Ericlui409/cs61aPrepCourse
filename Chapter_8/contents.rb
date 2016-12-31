contents = [["Chapter 1: ", "Getting Started", "page 1"], ["Chapter 2: ", "Numbers", "page 9"], ["Chapter 3: ", "Letters", "page 13"]]

puts("Table of Contents".center(50))

contents.each do |this|
	puts(this[0].ljust(10) + this[1].ljust(30) + this[2].ljust(10))
end