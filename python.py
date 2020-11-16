PASSAGE_THRESHOLD = 2.5
with open('file.txt', encoding='UTF-8') as file:
    ten = []
    eleven = []
    norm = []
    notnorm = []
    for line in file:
        second_name, clas, marks = line.split()
        marks = marks.replace('н','')
        marks=[int(i) for i in marks]
        avrg = []
        avrg.append(second_name)
        avrg.append(sum(marks)/len(marks))
        if clas=='10':
            ten.append(avrg)
        else:
            eleven.append(avrg)
        if avrg[1]<PASSAGE_THRESHOLD:
            notnorm.append(avrg)
        else:
            norm.append(avrg)
with open('data.txt', 'w') as file:
    file.write('Перешедшие порог\n')
    for item in norm:
        if item in ten:
            file.write('10 ' + item[0] + ' ' + str(item[1]) + '\n')
    for item in norm:        
        if item in eleven:
            file.write('11 ' + item[0] + ' ' + str(item[1]) + '\n')
    file.write('Неперешедшие порог\n')
    for item in notnorm:
        if item in ten:
            file.write('10 ' + item[0] + ' ' + str(item[1]) + '\n')
    for item in notnorm:
        if item in eleven:
            file.write('11 ' + item[0] + ' ' + str(item[1]) + '\n')
