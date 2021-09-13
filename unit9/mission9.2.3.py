def who_is_missing(file_name):
    file_to_open = open(file_name, 'r')
    found_file = open("found.txt", 'w')
    num_in_file = file_to_open.read()
    sum_of_num = 0
    count = 0
    for num in num_in_file:
        sum_of_num += num
        count += 1
    count += 1
    sum_with_miss = ((1 + count) * (count - 1)) // 2
    miss = str(sum_with_miss - sum_of_num)
    found_file.write(miss)
    file_to_open.close()
    found_file.close()
