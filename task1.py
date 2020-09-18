out_f = open("test.txt", "w")
list_srt = []
while True:
    user_str = input("Введите строку для добавления (пустая строка выход): ")
    if user_str == "":
        break
    else:
        list_srt.append(f"{user_str}\n")
out_f.writelines(list_srt)
out_f.close()
