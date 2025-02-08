def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])  # Знайдено точний збіг
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]  # Можливий кандидат на верхню межу
            right = mid - 1

    # Якщо точний збіг не знайдено, повертаємо верхню межу
    return (iterations, upper_bound)

# Тестування функції
sorted_array = [0.1, 0.5, 1.3, 2.8, 3.4, 4.9, 5.6, 7.1, 8.8]
target = 3.0

result = binary_search_with_upper_bound(sorted_array, target)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")