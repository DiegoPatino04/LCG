# This is the configuration file for the parameters of the project
# This file contains the parameters for the project, such as the alpha and beta values for the beta distribution,
#  the sample size, the seed for random number generation, and the parameters for the linear congruential generator (LCG).


ALPHA = 3          # Form
BETA = 2           # Scale
SAMPLE_SIZE = 10000
SEED = 12345
LCG_A = 1664525
LCG_C = 1013904223
LCG_M = 2**32
BINS = 50

PRINT_TRACE = True      # True = muestra tabla | False = no imprime tabla
MAX_PRINT_ROWS = SAMPLE_SIZE  # Cuántas filas mostrar si PRINT_TRACE = True