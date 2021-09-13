def copy_file_content(source, destination):
    source_file = open(source, 'r')
    dest_file = open(destination, 'w')
    for line in source_file:
        dest_file.write(line)
    source_file.close()
    dest_file.close()
