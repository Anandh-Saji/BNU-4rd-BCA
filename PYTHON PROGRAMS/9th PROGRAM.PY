def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

sorted_numbers = selection_sort(numbers)

print("Sorted list: ", sorted_numbers)
