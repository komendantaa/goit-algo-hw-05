import timeit
import random
from algorithms.boyer_moore_search import boyer_moore_search
from algorithms.kmp_search import kmp_search
from algorithms.rabin_karp_search import rabin_karp_search

# Завантаження текстів із файлів:
def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

text_1 = load_text("./assets/text_1.txt")
text_2 = load_text("./assets/text_2.txt")


#  Вибір підрядків:
existing_substring = "алгоритм"
non_existing_substring = "qwertyxyz"

# Вимірювання часу виконання:
def measure_time(search_func, text, pattern):
    return timeit.timeit(lambda: search_func(text, pattern), number=10)

results = []

for text, text_name in [(text_1, "text_1"), (text_2, "text_2")]:
    print(f"\nResults for {text_name.upper()}:")
    print(f"{'Algorithm':<20} {'Type':<15} {'Time (s)':<10}")
    print("-" * 45)
    
    results = [
        ("Boyer-Moore", "existing", measure_time(boyer_moore_search, text, existing_substring)),
        ("Boyer-Moore", "non-existing", measure_time(boyer_moore_search, text, non_existing_substring)),
        ("KMP", "existing", measure_time(kmp_search, text, existing_substring)),
        ("KMP", "non-existing", measure_time(kmp_search, text, non_existing_substring)),
        ("Rabin-Karp", "existing", measure_time(rabin_karp_search, text, existing_substring)),
        ("Rabin-Karp", "non-existing", measure_time(rabin_karp_search, text, non_existing_substring)),
    ]
    
    for algorithm, result_type, time_taken in results:
        print(f"{algorithm:<20} {result_type:<15} {time_taken:<10.6f}")

