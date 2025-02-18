from alg_lab1.utils import open_file, write_file, print_in_terminal


INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


def find_min_segments(segments):
    segments.sort(key=lambda x: x[1])

    coordinates = []
    current_coord = None

    for segment in segments:
        if current_coord is None or segment[0] > current_coord:
            current_coord = segment[1]
            coordinates.append(current_coord)

    return coordinates


def main(input_path, output_path):
    n, segments = open_file(input_path, 4)
    result = find_min_segments(segments)
    result_write = str(len(result)) + '\n' + " ".join(map(str, result))
    print_in_terminal([n, segments], str(len(result)) + "\n" + " ".join(map(str, result)), "---Task_4 Lab_1---")
    write_file(result_write, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
