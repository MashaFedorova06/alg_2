import unittest
from time import perf_counter
import tracemalloc
from alg_lab2.task8.src.task import get_height


class TestBinaryTreeHeight(unittest.TestCase):

    def test_empty_tree(self):
        """Тест с пустым деревом"""

        # Given
        nodes = {}
        expected_result = 0
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        if 1 in nodes:
            result = get_height(1, nodes)
        else:
            result = 0

        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_single_node(self):
        """Тест с одним узлом"""

        # Given
        nodes = {1: [5, 0, 0]}  # Один узел без детей
        expected_result = 1
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = get_height(1, nodes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_simple_tree(self):
        """Тест с простым деревом"""

        # Given
        nodes = {1: [5, 2, 3], 2: [3, 0, 0], 3: [7, 0, 0]}
        expected_result = 2
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        if 1 in nodes:
            result = get_height(1, nodes)
        else:
            result = 0

        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_deep_tree(self):
        """Тест с глубоким деревом"""

        # Given
        nodes = {1: [10, 2, 3], 2: [5, 4, 5], 3: [15, 6, 7], 4: [3, 0, 0], 5: [7, 0, 0], 6: [13, 0, 0],
                 7: [20, 0, 0]}
        expected_result = 3
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()

        if 1 in nodes:
            result = get_height(1, nodes)
        else:
            result = 0

        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
