import io                                       #импорт данных

#ФУНКЦИЯ:   загрузка необходимых векторов из спец.файла fname и их запись в словарь dictinary_vectors для соотв-х слов
def load_vectors(fname, dictinary_vectors):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    for line in fin:
        tokens = line.rstrip().split(' ')
        if dictinary_vectors.get(tokens[0], None):
            dictinary_vectors[tokens[0]] = list(map(float, tokens[1:]))

#ФУНКЦИЯ:   чтение файла fname: попарная запись слов в список list_words и по отдельности в словарь dictionary_vectors,
#           то есть создание ключей
def reading(fname, list_words, dictionary_vectors):
    f = open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    for each in f:
        word_1, word_2, human_value = each.split()
        list_words.append([word_1, word_2])
        dictionary_vectors[word_1], dictionary_vectors[word_2] = 1, 1
    f.close()

#ФУНКЦИЯ:   последовательное вычисление косинусов углов между векторами, хранящихся в словаре dictinary_vectors, 
#           для каждой пары слов из списка list_words и выдача их значений на экран
def calculating(list_words, dictinary_vectors):
    for each in list_words:
        numerator, sum_1, sum_2 = 0, 0, 0
        for i in range(len(dictinary_vectors[each[0]])):
            numerator += (dictinary_vectors[each[0]])[i] * (dictinary_vectors[each[1]])[i]
            sum_1 += (dictinary_vectors[each[0]])[i] ** 2
            sum_2 += (dictinary_vectors[each[1]])[i] ** 2
        denominator = (sum_1 ** 0.5) * (sum_2 ** 0.5)
        print(numerator / denominator)



#ОСНОВНАЯ ФУНКЦИЯ
words = []                                      #создаем список для хранения пар слов
vectors = {}                                    #создаем словарь для хранения слов и соответствующих им векторов

#ниже выбираем группу слов для анализа (Similarity/Relatedness), записываем их попарно в words и по отдельности в vectors
symbol = input("Введите символ 'S' для анализа группы Similarity; 'R' для анализа группы Relatedness: ")
if (symbol == 'S'):
    reading('wordsim_similarity_goldstandard.txt', words, vectors)      #Similarity
elif (symbol == 'R'):
    reading('wordsim_relatedness_goldstandard.txt', words, vectors)     #Relatedness
else:
    print("Error: incorrect symbol!")                                   #Error
    exit()

load_vectors('wiki-news-300d-1M.vec', vectors)  #загрузка необходимых векторов из спец.файла

calculating(words, vectors)                     #выдача результатов (числовое значение для каждой пары слов)