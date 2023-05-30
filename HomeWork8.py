FILE_PATH = r"C:\Users\black\OneDrive\Рабочий стол\Home Work Python\Home-Work-Python\Contacts.txt"


def New_Contact():
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        lines = f.write("\n")
        lastname = f.write(str(input("Введите фамилию: ") + (" ")))
        name = f.write(str(input("Введите имя: ") + (" ")))
        fathername = f.write(str(input("Введите отчество: ") + (" ")))
        number = f.write(str(input("Введите номер телефона: ") + (" ")))
        notes = f.write(str(input("Заметка о контакте: ") + (" ")))
        print("Контакт сохранен")


def List_Contacts():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip(" "))


def Find_Contact():
    print("Введите имя, фамилию, номер телефона или заметку: ")
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        book = f.read().split("\n")
        serach = str(input("Введите параметр для поиска: "))
        for i in book:
            if serach in i:
                print(i)
            else:
                print("По вашему запросу нет совпадений")


def Delet_Contact(str):
    import re
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        book = f.read().split("\n")
        serach = str(
            input("Полностью введите данные контакта который хотите удалить"))
        for i in book:
            if serach in i:
                str = i
                pattern = re.compile(re.escape(str))
                with open(FILE_PATH, "r+", encoding="utf-8") as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        result = pattern.search(line)
                        if result is None:
                            f.write(line)
                            f.truncate()


def Edit():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        book = f.read().split("\n")
        serach = str(input("Введите параметр для поиска: "))
        for i in book:
            if serach in i:
                with open(FILE_PATH, "r+", encoding="utf-8") as f:
                    x = str(input("Что вы хотите изменить?: "))
                    y = str(input("На что вы хотите заменить?: "))
                    f.write(i.replace(x, y))
                    print("Изменения прошли успешно")


while True:
    work = input("Что вы хотите сделать?" + "\n"
                 + "0 - создать контакт, 1 - список контактов, 2 - поиск, 3 - удалить контакт, 4 - изменить контакт, 5 - выход: ")
    if work == "0":
        print(New_Contact())
    elif work == "1":
        List_Contacts()
    elif work == "2":
        Find_Contact()
    elif work == "3":
        Delet_Contact(str)
    elif work == "4":
        Edit()
    elif work == "5":
        break
