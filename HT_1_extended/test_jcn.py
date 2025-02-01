#импортируем данные
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')

#бесконечный цикл прохода по всем словам (чтобы завершить цикл и, соотв-но, программу, следует нажать Ctrl + C)
while 1:
    word1, word2 = input("").split()                #вводим пару слов, разделяя их через пробел
    synsets1_full = wn.synsets(word1)               #здесь храним synset-ы для 1-го слова
    synsets2_full = wn.synsets(word2)               #здесь храним synset-ы для 2-го слова
    similarity = 0                                  #инициализация переменной подсчета близости слов
    for part_of_speech in ('n', 'v'):               #цикл прохода по всем частям речи (noun, verb)
        synsets1, synsets2 = [], []                 #иниц-ия списков для хранения synset-ов с соотв-й частью речи для обоих слов
        for x in synsets1_full:                     #циклически "достаем" из synsets1_full слова нужной части речи
            if x.pos() == part_of_speech:
                synsets1.append(x)
        for x in synsets2_full:                     #циклически "достаем" из synsets2_full слова нужной части речи
            if x.pos() == part_of_speech:
                synsets2.append(x)
        #ниже - непосредственное применение метода для подсчета близости слов и запись результатов в список my_list
        my_list = [synset1.jcn_similarity(synset2, brown_ic) for synset1 in synsets1 for synset2 in synsets2]
        if len(my_list) != 0:                       #проверка на пустоту списка my_list (т.е. на возможность применения метода)
            similarity_buf = max(my_list)           #вычисляем близость двух слов для соответствующей части речи
        else:
            similarity_buf = 0
        similarity = max(similarity, similarity_buf) #подсчет близости двух слов
    print(similarity)                                #печать результата для каждой пары

