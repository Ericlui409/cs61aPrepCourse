Dir.chdir '/Users/EricLui/Desktop/Pictures'

pic_names = Dir['**/*.{JPG,jpg}']

puts "What would you like to call this batch?"
batch_name = gets.chomp

puts
print "Downloading #{pic_names.length} files: "

pic_number = 1

pic_names.each do |name|
	print '.'
	puts
	new_name = if pic_number < 10
		"#{batch_name} 0#{pic_number}.jpg"
	else
		"#{batch_name} #{pic_number}.jpg"
	end
	if File.exist? new_name
		print "Error, file #{new_name} already exist."
		puts
		exit
	else
		File.rename name, new_name
		pic_number += 1
	end
end
puts "Done"