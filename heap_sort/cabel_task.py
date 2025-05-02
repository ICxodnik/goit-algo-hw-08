import heapq

def heap_sort_desc(iterable):
    h = []
    # Вставляємо в купу від'ємні значення
    for value in iterable:
        heapq.heappush(h, -value)
    
    # Витягуємо елементи і міняємо знаки для відновлення оригінальних значень
    return [-heapq.heappop(h) for _ in range(len(h))]

if __name__ == "__main__":

    cables_lengths = [12, 4, 13, 5, 6, 7, 11]
    sorted_cables = heap_sort_desc(cables_lengths)
    print("Відсортований масив (за спаданням):", sorted_cables)

