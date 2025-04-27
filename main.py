from typing import Tuple, List, Optional


def input_pairs_range(prompt: str) -> Optional[Tuple[int, int]]:
    """
    Запрашивает диапазон пар или 'нет'.
    """
    while True:
        try:
            raw_input = input(prompt).strip().lower()
            if raw_input == "нет":
                return (0, 0)
            
            start, end = map(int, raw_input.split("-"))
            if start == 0 and end == 0:
                return (0, 0)
            
            if 1 <= start <= end <= 6:
                return (start, end)
            
            print("Ошибка: номера пар от 1 до 6, начало <= конец.")
        except ValueError:
            print("Ошибка: введите 'начало-конец' или 'нет'.")


def get_common_pairs(group: Tuple[int, int], curator: Tuple[int, int]) -> List[int]:
    """
    Возвращает общие пары. Если кто-то не работает, возвращает пустой список.
    """
    if group == (0, 0) or curator == (0, 0):
        return []
    
    g_start, g_end = group
    c_start, c_end = curator
    
    common_start = max(g_start, c_start)
    common_end = min(g_end, c_end)
    
    return list(range(common_start, common_end + 1)) if common_start <= common_end else []


def has_early_visit_possible(group: Tuple[int, int], curator: Tuple[int, int]) -> bool:
    """
    Проверяет, может ли куратор прийти раньше своих пар к группе.
    Условие: пары куратора начинаются сразу после окончания группы.
    Пример: группа 1-2, куратор 3-5 → может прийти на 2-ю пару.
    """
    if group == (0, 0) or curator == (0, 0):
        return False
    
    g_end = group[1]
    c_start = curator[0]
    
    return g_end < c_start


def calculate_probability(
    common_pairs: List[int],
    curator_total: int,
    early_visit: bool
) -> float:
    """
    Рассчитывает итоговую вероятность:
    - Основная вероятность: общие пары.
    - Ранний визит: 5%, если нет общих пар, но куратор может прийти.
    """
    if common_pairs:
        return (len(common_pairs) / curator_total) * 100
    elif early_visit:
        return 5.0  # Фиксированная вероятность 5%
    else:
        return 0.0


def main():
    print("Добро пожаловать! Рассчитаем вероятность прихода куратора.")
    
    group = input_pairs_range("Введите диапазон пар группы (например, 1-3) или 'нет': ")
    curator = input_pairs_range("Введите диапазон пар куратора (например, 2-4) или 'нет': ")
    
    if group == (0, 0):
        print("У группы нет пар. Вероятность: 0%")
        return
    
    if curator == (0, 0):
        print("Куратор не работает. Вероятность: 0%")
        return
    
    common_pairs = get_common_pairs(group, curator)
    curator_total = curator[1] - curator[0] + 1
    early_visit = has_early_visit_possible(group, curator)
    probability = calculate_probability(common_pairs, curator_total, early_visit)
    
    print(f"Общие пары: {common_pairs if common_pairs else 'нет'}")
    
    if probability == 5.0:
        print("Внимание: Куратор может прийти раньше своих пар!")
    
    print(f"Вероятность проверки: {probability:.1f}%")

if __name__ == "__main__":
    main()