import os.path
import json

from src.utils import *
from config import ROOT_DIR

OPERATIONS_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')

def main():
    five_operations = get_formated_operations(five_first_operations)
    for i in five_operations:
        print(i)

if __name__ == '__main__':
    main()