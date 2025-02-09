import unittest
from time import perf_counter
import tracemalloc
from alg_lab1.task7.src.task7 import problema_sapozhnika


class TestProblemaSapozhnika(unittest.TestCase):

    def test_optimal_selection_1(self):
        """Проверяет оптимальный выбор сапогов 1"""

        # Given
        k = 10
        n = 5
        minutes = [3, 4, 7, 2, 9]
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = problema_sapozhnika(k, minutes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 3)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_optimal_selection_2(self):
        """Проверяет оптимальный выбор сапогов 2"""

        # Given
        k = 20
        n = 7
        minutes = [8, 6, 5, 7, 9, 1, 2]
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = problema_sapozhnika(k, minutes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 4)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_optimal_selection_3(self):
        """Проверяет оптимальный выбор сапогов (большие времена, мало места)"""

        # Given
        k = 5
        n = 4
        minutes = [4, 3, 2, 1]
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = problema_sapozhnika(k, minutes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 2)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_empty_list(self):
        """Тест с пустым списком времен."""
        # Given
        k = 100
        n = 0
        minutes = []
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = problema_sapozhnika(k, minutes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 0)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_multiple_items_all_fit(self):
        """Тест со списком элементов, которые все помещаются в ограничение по времени."""

        # Given
        k = 100
        n = 4
        minutes = [20, 30, 10, 40]
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = problema_sapozhnika(k, minutes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 4)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_zero_time_limit(self):
        """Тест с нулевым ограничением по времени."""

        # Given
        k = 0
        n = 3
        minutes = [1, 2, 3]
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = problema_sapozhnika(k, minutes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 0)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
