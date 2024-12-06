nums = [5, 6, 2, 1, 3, 4]

def bubble_sort(ls):
    # чтобы цикл сработал хотя бы раз,меняем значение переменной True
    swap = True
    while swap:
        swap = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                # меняем элементы местами
                ls[i], ls[i+1] = ls[i+1], ls[i]
                # меняем значение переменной swap для следующего повтора цикла
                swapped = True

bubble_sort(nums)
print(nums)

def selection_sort(ls):
    # i- количество отсортированных элементов
    for i in range(len(ls)):
        # изначально считаем минимальным первый элемент
        lowest = i
        # цикл для перебора неотсортированных элементов
        for j in range(i + 1, len(ls)):
            if ls[j]< ls[lowest]:
                lowest = j
        # самый минимальный элемент меняем с первым элементом

selection_sort(nums)
print(nums)

def insertion_sort(ls):
    #
    for i in range(1, len(ls)):
        item = ls[i]
        #
        j = i - 1
        #
        while j >= 0 and ls[j] > item:
            ls[j+1] = ls[j]
            j -= 1
            #
            ls[j+1] = item

insertion_sort(nums)
print(nums)