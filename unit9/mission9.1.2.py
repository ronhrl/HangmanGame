def file_mission(file, task):
    list_of_words = open(file, 'r')
    if task == "sort":
        sorted(list_of_words)
    list_of_words.close()
