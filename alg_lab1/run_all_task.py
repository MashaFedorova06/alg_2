from alg_lab1.task7.src.task7 import main as task7
from alg_lab1.task11.src.task11 import main as task11
from alg_lab1.task8.src.task8 import main as task8
from alg_lab1.task11.src.task11 import main as task2
from alg_lab1.task4.src.task4 import main as task4
from alg_lab1.task12.src.task12 import main as task12



def main(path):
    tasks = [(task7, [path + "/task7/txtf/input.txt", path + "/task7/txtf/output.txt"]),
             (task11, [path + "/task11/txtf/input.txt", path + "/task11/txtf/output.txt"]),
             (task2, [path + "/task2/txtf/input.txt", path + "/task2/txtf/output.txt"]),
             (task8, [path + "/task8/txtf/input.txt", path + "/task8/txtf/output.txt"]),
             (task4, [path + "/task4/txtf/input.txt", path + "/task4/txtf/output.txt"]),
             (task12, [path + "/task12/txtf/input.txt", path + "/task12/txtf/output.txt"]),
             ]
    for task, paths in tasks:
        task(paths[0], paths[1])


if __name__ == '__main__':
    main('.')
