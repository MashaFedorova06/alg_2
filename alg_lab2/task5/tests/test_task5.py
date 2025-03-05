import unittest
from time import perf_counter
import tracemalloc
from alg_lab2.task5.src.task5 import BinarySearchTree


class TestIsValidBST(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def test_empty_tree(self):
        # Given
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(self.tree.root, None)
        self.assertEqual(self.tree.exists(5), 'false')
        self.assertEqual(self.tree.next(5), 'none')
        self.assertEqual(self.tree.prev(5), 'none')
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_insert(self):
        # Given
        expected_time = 2
        expected_memory = 256
        self.tree.insert(2)
        self.tree.insert(3)
        self.tree.insert(11)
        self.tree.insert(1)
        self.tree.insert(64)
        self.tree.insert(124)
        self.tree.insert(4)

        # When
        tracemalloc.start()
        t_start = perf_counter()
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(self.tree.exists(3), 'true')
        self.assertEqual(self.tree.exists(22), 'false')
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_delete_leaf(self):
        # Given
        expected_time = 2
        expected_memory = 256
        self.tree.insert(8)
        self.tree.insert(3)
        self.tree.insert(10)
        self.tree.delete(3)

        # When
        tracemalloc.start()
        t_start = perf_counter()
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(self.tree.exists(3), 'false')
        self.assertEqual(self.tree.exists(8), 'true')
        self.assertEqual(self.tree.exists(10), 'true')
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_delete_one_child(self):
        # Given
        expected_time = 2
        expected_memory = 256
        self.tree.insert(8)
        self.tree.insert(3)
        self.tree.insert(10)
        self.tree.delete(10)

        # When
        tracemalloc.start()
        t_start = perf_counter()
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(self.tree.exists(10), 'false')
        self.assertEqual(self.tree.next(8), 'none')
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_delete_two_children(self):
        # Given
        expected_time = 2
        expected_memory = 256
        self.tree.insert(8)
        self.tree.insert(3)
        self.tree.insert(10)
        self.tree.insert(1)
        self.tree.insert(6)
        self.tree.insert(14)
        self.tree.insert(4)
        self.tree.insert(7)
        self.tree.insert(13)
        self.tree.delete(8)

        # When
        tracemalloc.start()
        t_start = perf_counter()
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(self.tree.exists(8), 'false')
        self.assertEqual(self.tree.root.key, 10)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_next(self):
        # Given
        expected_time = 2
        expected_memory = 256
        self.tree.insert(8)
        self.tree.insert(3)
        self.tree.insert(10)
        self.tree.insert(1)
        self.tree.insert(6)
        self.tree.insert(14)

        # When
        tracemalloc.start()
        t_start = perf_counter()
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(self.tree.next(7), 8)
        self.assertEqual(self.tree.next(10), 14)
        self.assertEqual(self.tree.next(15), 'none')
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_prev(self):
        # Given
        expected_time = 2
        expected_memory = 256
        self.tree.insert(8)
        self.tree.insert(3)
        self.tree.insert(10)
        self.tree.insert(1)
        self.tree.insert(6)
        self.tree.insert(14)

        # When
        tracemalloc.start()
        t_start = perf_counter()
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(self.tree.prev(7), 6)
        self.assertEqual(self.tree.prev(1), 'none')
        self.assertEqual(self.tree.prev(15), 14)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
