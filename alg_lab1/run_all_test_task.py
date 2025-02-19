import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_tests_task():
    suite = unittest.TestSuite()
    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(base_dir)
    test_task_arr = [
        'alg_lab1.task7.tests.test_task7',
        'alg_lab1.task11.tests.test_task11',
        'alg_lab1.task2.tests.test_task2',
        'alg_lab1.task8.tests.test_task8',
        'alg_lab1.task4.tests.test_task4',
        'alg_lab1.task12.tests.test_task12'
    ]
    for test_file in test_task_arr:
        task = [i for i in test_file.split(".")][1]
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_file))
        print(f"============ Test {task} completed ============")
    runner_unittest = unittest.TextTestRunner()
    runner_unittest.run(suite)


if __name__ == "__main__":
    run_all_tests_task()
