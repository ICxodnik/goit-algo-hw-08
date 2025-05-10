import heapq

def merge_k_lists(lists):
    heap = []
    result = []

    # Додаємо перший елемент кожного списку у купу разом з індексами
    for i, l in enumerate(lists):
        if l:  # перевірка, що список не порожній
            heapq.heappush(heap, (l[0], i, 0))  # (значення, індекс списку, індекс елемента)

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Якщо є наступний елемент у цьому ж списку, додаємо його
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result

if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

