def dic_mission():
    mission_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970",
                    "hobbies": ["Sing", "Compose", "Act"]}
    user_choice = int(input("Please enter your choice: "))
    if user_choice == 1:
        print(mission_dict["last_name"])
    elif user_choice == 2:
        print(mission_dict["birth_date"])
    elif user_choice == 3:
        print(len(mission_dict["hobbies"]))
    elif user_choice == 4:
        print(mission_dict["hobbies"])
        print(mission_dict["hobbies"][len(mission_dict["hobbies"]) - 1])
    elif user_choice == 5:
        print(mission_dict["hobbies"])
        mission_dict["hobbies"].append("Cooking")
        print(mission_dict["hobbies"])
    elif user_choice == 6:
        split_txt = mission_dict["birth_date"].split(".")
        for i in range(0, 3):
            birth_tuple = (split_txt[i])
        print(birth_tuple)
    elif user_choice == 7:
        mission_dict["age"] = "51"
        print(mission_dict["age"])
