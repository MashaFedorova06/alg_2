import unittest
from time import perf_counter
from alg_lab1.task11.src.task11 import knapsack_max_weight
import tracemalloc


class TestKnapsack(unittest.TestCase):

    def test_empty_weights(self):
        # Given
        W = 10
        n = 1
        weights = []
        expected_time = 5
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = knapsack_max_weight(W, n, weights)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 0)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_single_item_fits(self):
        # Given
        W = 10
        n = 1
        weights = [5]
        expected_time = 5
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = knapsack_max_weight(W, n, weights)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 5)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_single_item_too_heavy(self):
        # Given
        W = 10
        n = 1
        weights = [15]
        expected_time = 5
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = knapsack_max_weight(W, n, weights)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 0)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_multiple_items_fit(self):
        # Given
        W = 10
        n = 3
        weights = [1, 4, 8]
        expected_time = 5
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = knapsack_max_weight(W, n, weights)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 9)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_all_items_too_heavy(self):
        # Given
        W = 10
        n = 3
        weights = [15, 20, 25]
        expected_time = 5
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = knapsack_max_weight(W, n, weights)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 0)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_zero_capacity(self):
        self.assertEqual(knapsack_max_weight(0, 3, [1, 4, 8]), 0)
        # Given
        W = 0
        n = 3
        weights = [1, 4, 8]
        expected_time = 5
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = knapsack_max_weight(W, n, weights)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 0)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_larger_example(self):
        # Given
        W = 20
        n = 5
        weights = [7, 2, 5, 9, 3]
        expected_time = 5
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = knapsack_max_weight(W, n, weights)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 19)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
