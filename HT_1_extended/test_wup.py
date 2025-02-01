from nltk.corpus import wordnet as wn               #импортируем данные

#бесконечный цикл прохода по всем словам (чтобы завершить цикл и, соотв-но, программу, следует нажать Ctrl + C)
while 1:
    word1, word2 = input("").split()                #вводим пару слов, разделяя их через пробел
    #ниже получаем synset-ы для каждого слова в паре двух слов - здесь можно рассматривать все части речи сразу
    synsets1 = wn.synsets(word1)
    synsets2 = wn.synsets(word2)
    #ниже - непосредственное применение метода для подсчета близости слов и запись результатов в список my_list
    my_list = [synset1.wup_similarity(synset2) for synset1 in synsets1 for synset2 in synsets2]
    #вычисляем максимальное число близости этих двух слов
    if len(my_list) != 0:
        similarity = max(my_list)
    else:
        similarity = 0
    #печать результата для каждой пары слов
    print(similarity)

