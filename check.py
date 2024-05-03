import numpy as np
import logging

logger = logging.getLogger()
logger.setLevel("INFO")


def checking_result(path_to_matrix1, path_to_matrix2, path_to_result_matrix):
    first_matrix = np.loadtxt(path_to_matrix1, dtype=int, skiprows=1)
    second_matrix = np.loadtxt(path_to_matrix2, dtype=int, skiprows=1)

    loaded_result_matrix = np.loadtxt(path_to_result_matrix, int)

    multiply = np.dot(first_matrix, second_matrix)

    if np.array_equal(multiply, loaded_result_matrix):
        logging.info("\nMatrices are equal")
    else:
        logging.info("\nMatrices are not equal")

if __name__ == "__main__":
    checking_result("./Parprog_lab1/matrix1.txt", "./Parprog_lab1/matrix2.txt", "./Parprog_lab1/result.txt")
