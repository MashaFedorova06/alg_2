import unittest
from time import perf_counter
import tracemalloc
from alg_lab2.task6.src.task6 import is_valid_bst


class TestIsValidBST(unittest.TestCase):
    def test_correct_bst(self):
        """Корректное BST"""
        # Given
        expected_time = 2
        expected_memory = 256
        nodes = [
            (2, 1, 2),
            (1, -1, -1),
            (3, -1, -1)
        ]

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = is_valid_bst(nodes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, "CORRECT")
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_incorrect_bst(self):
        """Некорректное BST"""
        # Given
        expected_time = 2
        expected_memory = 256
        nodes = [
            (2, 1, 2),
            (3, -1, -1),  # Ошибка: левый ребенок больше родителя
            (1, -1, -1)
        ]

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = is_valid_bst(nodes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, "INCORRECT")
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_single_node(self):
        """BST из одного узла"""
        # Given
        expected_time = 2
        expected_memory = 256
        nodes = [
            (5, -1, -1)
        ]

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = is_valid_bst(nodes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, "CORRECT")
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


    def test_empty_tree(self):
        """Пустое дерево """
        # Given
        expected_time = 2
        expected_memory = 256
        nodes = []

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = is_valid_bst(nodes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, "CORRECT")
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_large_correct_bst(self):
        """Большое корректное BST"""
        # Given
        expected_time = 2
        expected_memory = 256
        nodes = [
            (10, 1, 2),
            (5, -1, -1),
            (15, -1, -1)
        ]

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = is_valid_bst(nodes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, "CORRECT")
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_large_incorrect_bst(self):
        """Большое некорректное BST"""
        # Given
        expected_time = 2
        expected_memory = 256
        nodes = [
            (10, 1, 2),
            (15, -1, -1),  # Ошибка: левый ребенок больше родителя
            (5, -1, -1)
        ]

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = is_valid_bst(nodes)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, "INCORRECT")
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
