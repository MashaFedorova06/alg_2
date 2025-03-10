import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_tests_task():
    suite = unittest.TestSuite()
    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(base_dir)
    test_task_arr = [
        'alg_lab2.task5.tests.test_task5',
        'alg_lab2.task6.tests.test_task6',
        'alg_lab2.task8.tests.test_task8'
    ]
    for test_file in test_task_arr:
        task = [i for i in test_file.split(".")][1]
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_file))
        print(f"============ Test {task} completed ============")
    runner_unittest = unittest.TextTestRunner()
    runner_unittest.run(suite)


if __name__ == "__main__":
    run_all_tests_task()
