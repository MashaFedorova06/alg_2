import unittest
from time import perf_counter
import tracemalloc
from alg_lab3.task1.src.task1 import dfs

class TestLabyrinthPath(unittest.TestCase):

    def test_no_path_empty_graph(self):
        """Тест с пустым графом"""
        graph = {}
        expected_result = 0
        expected_time = 5
        expected_memory = 512

        tracemalloc.start()
        t_start = perf_counter()
        visited = {}

        # Проверяем, есть ли стартовая вершина в графе, иначе сразу 0
        if 1 in graph and 2 in graph:
            result = 1 if dfs(graph, 1, 2, visited) else 0
        else:
            result = 0

        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_single_connection(self):
        """Тест с одним соединением"""
        graph = {1: [2], 2: [1]}
        expected_result = 1
        expected_time = 5
        expected_memory = 512

        tracemalloc.start()
        t_start = perf_counter()
        visited = {1: False, 2: False}
        result = 1 if dfs(graph, 1, 2, visited) else 0
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_multiple_paths(self):
        """Тест с несколькими путями"""
        graph = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}
        expected_result = 1
        expected_time = 5
        expected_memory = 512

        tracemalloc.start()
        t_start = perf_counter()
        visited = {i: False for i in range(1, 5)}
        result = 1 if dfs(graph, 1, 4, visited) else 0
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_disconnected_nodes(self):
        """Тест с несвязанными вершинами"""
        graph = {1: [2], 2: [1], 3: [4], 4: [3]}
        expected_result = 0
        expected_time = 5
        expected_memory = 512

        tracemalloc.start()
        t_start = perf_counter()
        visited = {i: False for i in range(1, 5)}
        result = 1 if dfs(graph, 1, 4, visited) else 0
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
