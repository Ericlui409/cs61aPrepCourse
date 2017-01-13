def shuffle some_array
	recursive_shuffle some_array, []
end

def recursive_shuffle unshuffled_array, shuffled_array
	if unshuffled_array.length == 0
		return shuffled_array
	else
		random = unshuffled_array[rand(unshuffled_array.length)]
		recursive_shuffle (unshuffled_array - [random]), (shuffled_array.push random)
	end
end

Dir.chdir '/Users/EricLui/Downloads'

song_names = shuffle Dir['**/*.mp3']

Dir.chdir '/Users/EricLui/Desktop'

puts "What do you want the name of the playlist to be?"
playlist_name = gets.chomp

require 'yaml'

songs_string = song_names.to_yaml

File.open (playlist_name + '.m3u'), 'w' do |f|
	f.write songs_string
end