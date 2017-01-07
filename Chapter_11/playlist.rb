Dir.chdir '/Users/EricLui/Downloads'

song_names = Dir['**/*.mp3']

Dir.chdir '/Users/EricLui/Desktop'

puts "What do you want the name of the playlist to be?"
playlist_name = gets.chomp

require 'yaml'

songs_string = song_names.to_yaml

File.open (playlist_name + '.m3u'), 'w' do |f|
	f.write songs_string
end