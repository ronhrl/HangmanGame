def shopping_func(shopping_str):
    user_choice_num = int(input("Please enter your choice: "))
    shopping_list = list()
    for item in shopping_str:
        shopping_list.append(item)
    while user_choice_num != 9:
        user_choice_num = int(input("Please enter your choice: "))
        if user_choice_num == 1:
            print(shopping_list)
        elif user_choice_num == 2:
            print(len(shopping_list))
        elif user_choice_num == 3:
            user_choice_item = input("Please enter the item you would like to check: ")
            if user_choice_item in shopping_list:
                return True
            else:
                return False
        elif user_choice_num == 4:
            user_choice_item = input("Please enter the item you would like to check: ")
            print(shopping_list.count(user_choice_item))
        elif user_choice_num == 5:
            user_choice_item = input("Please enter the item you would like to remove: ")
            shopping_list.remove(user_choice_item)
        elif user_choice_num == 6:
            user_choice_item = input("Please enter the item you would like to add: ")
            shopping_list.append(user_choice_item)
        elif user_choice_num == 7:
            for item in shopping_list:
                if len(item) < 3 or not item.isalpha():
                    print(item)
#        elif user_choice_num == 8:

        elif user_choice_num == 9:
            break
