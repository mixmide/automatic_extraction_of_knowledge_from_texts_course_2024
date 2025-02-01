from nltk.corpus import wordnet as wn               #импортируем данные

#цикл прохода по всем словам
for i in range(1,204):
    word1, word2 = input("").split()                #вводим пары слов, разделяя их через пробел

    #получаем синсеты для каждого слова в паре двух слов - здесь можно рассматривать все части речи сразу
    synsets1 = wn.synsets(word1)
    synsets2 = wn.synsets(word2)

    #создаем список из чисел-близости пар слов для этих двух синсетов
    my_list = [synset1.wup_similarity(synset2) for synset1 in synsets1 for synset2 in synsets2]

    #вычисляем максимальное число близости этих двух слов
    if len(my_list) != 0:
        max_similarity = max(my_list)
    else:
        max_similarity = 0

    #печать результата для каждой пары
    print(max_similarity)

