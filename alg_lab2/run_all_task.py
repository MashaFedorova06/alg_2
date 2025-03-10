from alg_lab2.task6.src.task6 import main as task6
from alg_lab2.task8.src.task8 import main as task8
from alg_lab2.task5.src.task5 import main as task5



def main(path):
    tasks = [(task5, [path + "/task5/txtf/input.txt", path + "/task5/txtf/output.txt"]),
             (task6, [path + "/task6/txtf/input.txt", path + "/task6/txtf/output.txt"]),
             (task8, [path + "/task8/txtf/input.txt", path + "/task8/txtf/output.txt"]),
             ]
    for task, paths in tasks:
        task(paths[0], paths[1])


if __name__ == '__main__':
    main('.')
