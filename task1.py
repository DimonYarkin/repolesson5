with open("test.txt", "w", encoding='utf-8') as out_f:
    list_srt = []
    while True:
        user_str = input("Введите строку для добавления (пустая строка выход): ")
        if not user_str:
            break
        else:
            list_srt.append(f"{user_str}\n")
    out_f.writelines(list_srt)
