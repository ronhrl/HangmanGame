def fix_age(age):
    if (13 <= age < 15) or (16 < age <= 19):
        return 0
    else:
        return age


def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)
