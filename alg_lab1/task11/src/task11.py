from alg_lab1.utils import open_file, write_file, print_in_terminal

INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


def knapsack_max_weight(W, n, weights):
        dp = [0] * (W + 1)
        for weight in weights:
            for w in range(W, weight - 1, -1):
                dp[w] = max(dp[w], dp[w - weight] + weight)
        return dp[W]


def main(input_path, output_path):
    W, n, weights= open_file(input_path,7)
    result = knapsack_max_weight(W, n, weights)
    print_in_terminal([W, n, weights], result, "---Task_11 Lab_1---")
    write_file(result, output_path, 11)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
