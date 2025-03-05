import unittest
from time import perf_counter
import tracemalloc
from alg_lab3.task12.src.task12 import corridors_solve


class TestCorridors(unittest.TestCase):
    def test_example_1(self):
        # Given
        n = 3
        corridors = [
            (1, 2, 10),
            (2, 3, 5)
        ]
        path = [5, 10, 10, 10, 10]
        expected_result = "INCORRECT"
        expected_time = 1
        expected_memory = 16

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = corridors_solve(n, corridors, path)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_example_2(self):
        # Given
        n = 3
        corridors = [
            (1, 2, 10),
            (1, 3, 5)
        ]
        path = [10, 10, 10, 5]
        expected_result = "INCORRECT"
        expected_time = 1
        expected_memory = 16

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = corridors_solve(n, corridors, path)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_example_3(self):
        # Given
        n = 3
        corridors = [
            (1, 2, 10),
            (1, 3, 5)
        ]
        path = [10, 10, 10, 10, 5]
        expected_result = "3"
        expected_time = 1
        expected_memory = 16

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = corridors_solve(n, corridors, path)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
