def my_mp3_playlist(file_path):
    file_to_open = open(file_path, 'r')
    lines_in_file = file_to_open.read()
    longest_line = max(lines_in_file, key=len)
    num_of_songs = len(lines_in_file)
    counter = 0
    num = lines_in_file[0]
    for i in lines_in_file:
        curr_frequency = lines_in_file.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    tuple_mp3 = (longest_line, num_of_songs, num)
    return tuple_mp3
