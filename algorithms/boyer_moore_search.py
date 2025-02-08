def bad_char_heuristic(pattern):
    # Використовуємо словник для зберігання індексів останнього входження кожного символу в шаблоні
    bad_char = {}
    for i in range(len(pattern)):
        # Зберігаємо індекс останнього входження символу
        bad_char[pattern[i]] = i
    return bad_char

def good_suffix_heuristic(pattern):
    m = len(pattern)
    # Створюємо масив для зберігання зсувів для добрих суфіксів
    good_suffix = [0] * (m + 1)
    # Створюємо масив для зберігання позицій границь
    border_pos = [-1] * (m + 1)
    i = m
    j = m + 1
    border_pos[i] = j

    while i > 0:
        # Перевіряємо символи шаблону з кінця на відповідність
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            # Якщо зсув ще не визначено, визначаємо його
            if good_suffix[j] == 0:
                good_suffix[j] = j - i
            # Переходимо до наступної границі
            j = border_pos[j]
        i -= 1
        j -= 1
        # Зберігаємо позицію границі
        border_pos[i] = j

    j = border_pos[0]
    for i in range(m + 1):
        # Якщо зсув ще не визначено, визначаємо його
        if good_suffix[i] == 0:
            good_suffix[i] = j
        # Якщо індекс збігається з позицією границі, переходимо до наступної границі
        if i == j:
            j = border_pos[j]

    return good_suffix

def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)

    # Викликаємо функцію для обчислення масиву поганих символів
    bad_char = bad_char_heuristic(pattern)
    # Викликаємо функцію для обчислення масиву добрих суфіксів
    good_suffix = good_suffix_heuristic(pattern)

    s = 0  # Індекс зсуву шаблону відносно тексту
    while s <= n - m:
        j = m - 1  # Індекс поточного символу в шаблоні

        # Перевіряємо символи шаблону з кінця на відповідність тексту
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # Якщо всі символи збігаються, знайдено підрядок
        if j < 0:
            # Зсуваємо шаблон на значення доброго суфікса
            s += good_suffix[0]
        else:
            # Обчислюємо зсуви за поганим символом і добрим суфіксом
            bad_char_shift = j - bad_char.get(text[s + j], -1)
            good_suffix_shift = good_suffix[j + 1]
            # Зсуваємо шаблон на максимальне значення зсувів
            s += max(1, bad_char_shift, good_suffix_shift)
