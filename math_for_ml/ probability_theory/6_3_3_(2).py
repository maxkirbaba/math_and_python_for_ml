import numpy as np

# 1. Считываем размеры данных
M, N, K = map(int, input().split())

# 2. Считываем тренировочные данные и преобразуем в матрицу NumPy
train_data = np.array([list(map(int, input().split())) for _ in range(M)])

# Разделяем на вектор ответов (y) и матрицу признаков-слов (X)
y_train = train_data[:, 0]  # Первый столбец (0 - не спам, 1 - спам)
X_train = train_data[:, 1:]  # Остальные K столбцов с ключевыми словами

# 3. Считываем тестовые данные в матрицу
X_test = np.array([list(map(int, input().split())) for _ in range(N)])

# 4. Считаем априорные вероятности классов
spam_count = np.sum(y_train == 1)
not_spam_count = M - spam_count

p_spam = spam_count / M
p_not_spam = not_spam_count / M

# 5. Считаем условные вероятности слов для каждого класса (векторы длины K)
# Суммируем строки по вертикали (axis=0) для нужного класса и делим на его объем
p_words_given_spam = np.sum(X_train[y_train == 1], axis=0) / spam_count
p_words_given_not_spam = np.sum(X_train[y_train == 0], axis=0) / not_spam_count

# 6. Формируем матрицы вероятностей для тестовой выборки
# np.where заменяет 1 на вероятность слова, а 0 на (1 - вероятность слова)
test_spam_probs = np.where(X_test == 1, p_words_given_spam, 1 - p_words_given_spam)
test_not_spam_probs = np.where(X_test == 1, p_words_given_not_spam, 1 - p_words_given_not_spam)

# 7. Перемножаем вероятности слов в строках (axis=1) и умножаем на априорную вероятность
score_spam = np.prod(test_spam_probs, axis=1) * p_spam
score_not_spam = np.prod(test_not_spam_probs, axis=1) * p_not_spam

# 8. Применяем условия классификации ко всем тестам одновременно
# По умолчанию ставим 0 (не спам). Если спам больше -> ставим 1.
ans = np.where(score_spam > score_not_spam, 1, 0)
# Если разница меньше погрешности -> перезаписываем на -1
ans = np.where(np.abs(score_spam - score_not_spam) <= 1e-5, -1, ans)

# Выводим результат через пробел
print(*ans)
