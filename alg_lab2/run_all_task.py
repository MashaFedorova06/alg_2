from alg_lab2.task6.src.task6 import main as task6




def main(path):
    tasks = [(task6, [path + "/task6/txtf/input.txt", path + "/task6/txtf/output.txt"])
             ]
    for task, paths in tasks:
        task(paths[0], paths[1])


if __name__ == '__main__':
    main('.')
