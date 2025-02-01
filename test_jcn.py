#импортируем данные
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')

#цикл прохода по всем словам
for i in range(1,204):
    word1, word2 = input("").split()            #вводим пары слов, разделяя их через пробел
    #получаем синсеты для каждого слова в паре двух слов - здесь рассматриваем часть речи NOUN
    synsets1 = wn.synsets(word1, pos=wn.NOUN)
    synsets2 = wn.synsets(word2, pos=wn.NOUN)
    #создаем список из чисел-близости пар слов для этих двух синсетов
    my_list = [synset1.jcn_similarity(synset2, brown_ic) for synset1 in synsets1 for synset2 in synsets2]
    #вычисляем максимальное число близости этих двух слов (для части речи NOUN)
    if len(my_list) != 0:
        max_similarity1 = max(my_list)
    else:
        max_similarity1 = 0
    #аналогичные действия для части речи VERB
    synsets1 = wn.synsets(word1, pos=wn.VERB)
    synsets2 = wn.synsets(word2, pos=wn.VERB)
    my_list = [synset1.jcn_similarity(synset2, brown_ic) for synset1 in synsets1 for synset2 in synsets2]
    if len(my_list) != 0:
        max_similarity2 = max(my_list)
    else:
        max_similarity2 = 0
    #аналогичные действия для части речи ADJECTIVE
    synsets1 = wn.synsets(word1, pos=wn.ADJ)
    synsets2 = wn.synsets(word2, pos=wn.ADJ)
    my_list = [synset1.jcn_similarity(synset2, brown_ic) for synset1 in synsets1 for synset2 in synsets2]
    if len(my_list) != 0:
        max_similarity3 = max(my_list)
    else:
        max_similarity3 = 0
    #вычисляем максимальное число близости этих двух для всех частей речи в целом
    max_similarity = max(max_similarity1, max_similarity2, max_similarity3)
    #печать результата для каждой пары
    print(max_similarity)