with open('file.txt', 'r', encoding='UTF-8') as file:
    ten = []
    eleven = []
    norm = []
    notnorm = []
    stringlist = file.readlines()
    for i in range (len(stringlist)-1):
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
        if avrg[1]<2.5:
            notnorm.append(avrg)
        else:
            norm.append(avrg)
with open('data.txt', 'w') as file:
    file.write('Перешедшие порог\n')
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
