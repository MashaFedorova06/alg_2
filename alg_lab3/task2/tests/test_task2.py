import unittest
from time import perf_counter
import tracemalloc
from alg_lab3.task2.src.task2 import find_components



class TestFindComponents(unittest.TestCase):

    def test_single_component(self):
        """Граф с одной связной компонентой"""

        # Given
        n = 4
        graph = {
            1: [2, 3],
            2: [1, 4],
            3: [1, 4],
            4: [2, 3]
        }
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_components(n, graph)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 1)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_two_components(self):
        """Граф с двумя компонентами связности"""

        # Given
        n = 4
        graph = {
            1: [2],
            2: [1],
            3: [4],
            4: [3]
        }
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_components(n, graph)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 2)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_disconnected_nodes(self):
        """Граф без ребер (n отдельных вершин)"""

        # Given
        n = 5
        graph = {i: [] for i in range(1, n + 1)}
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_components(n, graph)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 5)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


    def test_large_component(self):
        """Граф, где все вершины соединены цепочкой"""

        # Given
        n = 6
        graph = {
            1: [2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 5],
            5: [4, 6],
            6: [5]
        }
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_components(n, graph)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 1)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


    def test_single_node(self):
        """Граф из одной вершины"""

        # Given
        n = 1
        graph = {1: []}
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_components(n, graph)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, 1)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
