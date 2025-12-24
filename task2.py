"""
Дано k відсортованих списків цілих чисел.
Ваше завдання — об'єднати їх у один відсортований список.
Тепер при виконанні завдання ви повинні використати мінімальну купу
для ефективного злиття кількох відсортованих списків в один відсортований список.
Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків
та повертає відсортований список.
"""

import heapq


def merge_k_lists(lists):

    # Check if lists are not empty
    if not lists:
        return []

    heap = []
    merged_list = []

    # Add all values to a heap
    for lst in lists:
        for value in lst:
            heapq.heappush(heap, value)

    # Move min values from the heap to the merged_list
    while heap:
        merged_list.append(heapq.heappop(heap))

    return merged_list

    # return list(heapq.merge(*lists))


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Sorted list:", merged_list)

    assert merge_k_lists([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_lists([[], [], []]) == []
    assert merge_k_lists([[1, 4, 5], [], [2, 6]]) == [1, 2, 4, 5, 6]
