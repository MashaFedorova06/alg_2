import unittest
from time import perf_counter
import tracemalloc
from alg_lab1.task8.src.task8 import max_lectures


class TestMaxLectures(unittest.TestCase):

    def test_max_lectures_1(self):
        """Проверяет максимальное количество лекций (первый тест)"""

        # Given
        requests = [(1, 5), (5, 10), (3, 6), (7, 9), (9, 12)]
        expected_result = 3
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = max_lectures(requests)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_max_lectures_2(self):
        """Проверяет максимальное количество лекций (с пересекающимися временем)"""

        # Given
        requests = [(1, 5), (4, 7), (7, 10), (2, 5), (8, 12)]
        expected_result = 2
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = max_lectures(requests)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_max_lectures_empty(self):
        """Тест с пустым списком запросов"""

        # Given
        requests = []
        expected_result = 0
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = max_lectures(requests)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_single_request(self):
        """Тест с одним запросом"""

        # Given
        requests = [(1, 5)]
        expected_result = 1
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = max_lectures(requests)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_non_overlapping_lectures(self):
        """Тест с лекциями, не пересекающимися по времени"""

        # Given
        requests = [(1, 3), (4, 6), (7, 9), (10, 12)]
        expected_result = 4
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = max_lectures(requests)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
