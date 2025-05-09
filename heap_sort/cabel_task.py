import heapq

def heap_sort_desc(iterable):
    # Зберігаємо елементи як від’ємні числа, щоб отримати max-купу
    h = [-value for value in iterable]
    heapq.heapify(h)
    return [-heapq.heappop(h) for _ in range(len(h))]

def took_cables(cables_lengths, length):
    total = 0
    # Перетворюємо список в max-купу за допомогою від’ємних значень
    max_heap = [-val for val in cables_lengths]
    heapq.heapify(max_heap)

    used_cables = []
    
    while max_heap and total < length:
        max_val = -heapq.heappop(max_heap)  # інвертуємо назад у додатне число
        total += max_val
        used_cables.append(max_val)

    # Залишки в купі — це кабелі, які не були використані
    remaining_cables = [-val for val in max_heap]
    return total, heap_sort_desc(remaining_cables)

if __name__ == "__main__":

    cables_lengths = [12, 4, 13, 5, 6, 7, 11]
    sorted_cables = heap_sort_desc(cables_lengths)
    print("Відсортований масив (за спаданням):", sorted_cables)

    length_to_take = 40
    cost, cables_left = took_cables(cables_lengths, length_to_take)
    print("Сумарна довжина кабелів, що використані:", cost)
    print("Кабелі, що лишились:", cables_left)
