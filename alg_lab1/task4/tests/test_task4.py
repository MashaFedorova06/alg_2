import unittest
from time import perf_counter
import tracemalloc
from alg_lab1.task4.src.task4 import find_min_segments


class TestFindSegments(unittest.TestCase):
    def test_no_segments(self):
        # Given
        segments = []
        expected_result = []
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_min_segments(segments)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_single_segment(self):
        # Given
        segments = [(1, 3)]
        expected_result = [3]
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_min_segments(segments)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_multiple_segments(self):
        # Given
        segments = [(1, 3), (2, 5), (4, 7), (5, 6)]
        expected_result = [3, 6]
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_min_segments(segments)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_disjoint_segments(self):
        # Given
        segments = [(1, 2), (3, 4), (5, 6)]
        expected_result = [2, 4, 6]
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_min_segments(segments)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_overlapping_segments_given(self):
        # Given
        segments = [(4, 7), (1, 3), (2, 5), (5, 6)]
        expected_result = [3, 6]
        expected_time = 2
        expected_memory = 256

        # When
        tracemalloc.start()
        t_start = perf_counter()
        result = find_min_segments(segments)
        t_end = perf_counter() - t_start
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time, f"Значение {t_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
