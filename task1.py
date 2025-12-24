"""
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель,
використовуючи з'єднувачі, у порядку, який призведе до найменших витрат.
Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин,
а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
"""

import heapq


def join_cables_heap(cable_len):

    if not cable_len:
        return 0

    total_sum = 0
    heap = cable_len.copy()
    heapq.heapify(heap)

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        merged = first + second
        total_sum += merged
        heapq.heappush(heap, merged)

    return total_sum


def join_cables_list(cable_len):

    if not cable_len:
        return 0

    total_sum = 0
    cables = cable_len.copy()

    while len(cables) > 1:
        first = cables.pop(0)
        second = cables.pop(0)
        merged = first + second
        total_sum += merged
        cables.insert(0, merged)

    return total_sum


if __name__ == "__main__":
    cable_len = [12, 4, 25, 3, 1]

    heap_result = join_cables_heap(cable_len)
    list_result = join_cables_list(cable_len)

    print(f"Heap-підхід: {heap_result}")
    print(f"List-підхід: {list_result}")
