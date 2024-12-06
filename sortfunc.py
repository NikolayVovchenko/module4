
nums = [5, 6, 2, 1, 3, 4]

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True

print(bubble_sort(nums))
print(nums)

def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j]< ls[lowest]:
                lowest = j

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