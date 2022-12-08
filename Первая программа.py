
HELP='''
help - напечатать справку о программе.
add - добавить задачу в список.
show - напечатать все добавленные задачи.
exit - Выход из программы
show data - просмотреть все задачи по датам'''

tasks = []
today=[]
tomorrow=[]
other=[]

run = True
while run:
    command=input('введите команду: ')
    if command=='help':
        print(HELP)
    elif command=='show':
        print(tasks)
    elif command == 'show data':
        print ("сегодня",today,"завтра",tomorrow,'другое',other)
    elif command=='add':
        task=input('введите название задачи: ')
        tasks.append(task)
        print("задача добавлена")
        data = input('введите дату: ')
        if data == "сегодня":
            today.append(task)
            print("задача добавлена в today")
        elif data == "завтра":
            tomorrow.append(task)
            print("задача добавлена в tomorrow")
        else:
            other.append(task)
            print("задача добавлена в other")
    elif command=='exit':
        print('Спасибо за использование! ')
        break
    else:
        print('неизвестная команда')
        break

print('до свидания!')

