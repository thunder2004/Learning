while True:
    try:
        time_s = int(input("\nВведите количество секунд: "))

        if time_s < 1:
            break
        days = time_s // 86400
        hours = (time_s % 86400) // 3600
        mins = ((time_s % 86400) % 3600) // 60
        sec_s = (((time_s % 86400) % 3600) % 60)

        if days > 0:
            if days == 1:
                print("Day:", days, end=" ")
            else:
                print("Days:", days, end=" ")
        if hours > 0:
            if hours == 1:
                print("Hour:", hours, end=" ")
            else:
                print("Hours:", hours, end=" ")
        if mins > 0:
            if mins == 1:
                print("Minute:", mins, end=" ")
            else:
                print("Minutes:", mins, end=" ")
        if sec_s > 0:
            if sec_s == 1:
                print("Second:", sec_s, end=" ")
            else:
                print("Seconds:", sec_s, end=" ")

    except ValueError:
        print("Братан ты че несеш!?")

