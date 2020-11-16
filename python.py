# Можно режим чтения файла не указывать, почему, вы помните
with open('file.txt', encoding='UTF-8') as file:
    ten = []
    eleven = []
    norm = []
    notnorm = []
    # Здесь можно не использовать функцию readlines
    # Мы с вами проходили, что объект файла можно использовать в цикле for
    # Для построчного получения строк, то есть
    # for line in file, как вариант
    # Соответственно код станет короче и понятнее
    stringlist = file.readlines()
    for i in range (len(stringlist)-1):
        # Здесь непонятно использование функции map, у нас сплит строки возращает
        # список строк, то есть не нужно их преобразовывать с помощью функции str
        second_name, clas, marks = map(str,stringlist[i].split())
        marks = marks.replace('н','')
        marks=[int(i) for i in marks]
        avrg = []
        avrg.append(second_name)
        avrg.append(sum(marks)/len(marks))
        if clas=='10':
            ten.append(avrg)
        else:
            eleven.append(avrg)
        # 2.5 Так называемое магическое число, никто не знает почему именно 2.5 :)
        # Для таких случае лучше использовать переменные с константными именами,
        # например, PASSAGE_THRESHOLD = 2.5
        # И понятнее и если вдруг, данная константа будет использоваться где-то еще
        # проще будет менять в одном месте.
        # По наименованию смотрите pep8
        if avrg[1]<2.5:
            notnorm.append(avrg)
        else:
            norm.append(avrg)
with open('data.txt', 'w') as file:
    file.write('Перешедшие порог\n')
    # По аналогии с файлами, все последовательности обладают свойством перечисления,
    # то есть можно написать for item in norm:
    # Тогда каждую итерацию в переменную item будет записываться элемент списка
    for i in range(len(norm)):
        if norm[i] in ten:
            file.write('10 ' + norm[i][0] + ' ' + str(norm[i][1]) + '\n')
    for i in range(len(norm)):        
        if norm[i] in eleven:
            file.write('11 ' + norm[i][0] + ' ' + str(norm[i][1]) + '\n')
    file.write('Неперешедшие порог\n')
    for i in range(len(notnorm)):
        if notnorm[i] in ten:
            file.write('10 ' + notnorm[i][0] + ' ' + str(notnorm[i][1]) + '\n')
    for i in range(len(notnorm)):
        if notnorm[i] in eleven:
            file.write('11 ' + notnorm[i][0] + ' ' + str(notnorm[i][1]) + '\n')
