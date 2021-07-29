while True:
    time_s = int(input("Введите количество секунд: "))
    if time_s < 1:
        break
    days = time_s // 86400
    hours = (time_s % 86400) // 3600
    mins = ((time_s % 86400) % 3600) // 60
    sec_s =  (((time_s % 86400) % 3600) % 60)

    if days == 1:
        print("Day:", days)
    else:
        print("Days:", days)
    if hours == 1:
        print("Hour:", hours)
    else:
        print("Hours:", hours)
    if mins == 1:
        print("Minute:", mins)
    else:
        print("Minutes:", mins)
    if sec_s == 1:
        print("Second:",sec_s)
    else:
        print("Seconds:", sec_s)