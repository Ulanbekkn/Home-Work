import re

data = open("MOCK_DATA.txt", "r")
content = data.read()
data.close()

while True:
    print(f'Что из этого хотите выбрать?\n'
          f'1 - Считать имена и фамилии\n'
          f'2 - Считать все емайлы\n'
          f'3 - Считать название файлов\n'
          f'4 - Считать цвета\n'
          f'5 - Выход')
    user_input = input("Ваш выбор? - ")
    if user_input in "12345":
        if user_input == "1":
            with open("names.txt", "w") as file:
                names_list = re.findall(r"[A-Z][a-z-]+\s[A-Za-z' ]+\b", content)
                for name in names_list:
                    file.write(name + "\n")
        elif user_input == "2":
            with open("emails.txt", "w") as file:
                emails_list = re.findall(r"(?:\b[\w]+@[\w\-]+(\.[\w]+)+)", content)
                for email in emails_list:
                    file.write(email[0] + "\n")
        elif user_input == "3":
            with open("files.txt", "w") as file:
                files_list = re.findall(r"\t[\w]+\.[\w]+", content)
                for filee in files_list:
                    file.write(filee + "\n")
        elif user_input == "4":
            with open("colors.txt", "w") as file:
                colors_list = re.findall(r"#[\w]{6}", content)
                for color in colors_list:
                    file.write(color + "\n")
        elif user_input == "5":
            break
    else:
        print("Только числа от 1 до 5")
