#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    number = int(input())
    binary = bin(number)[2:].split('0')
    print(max(len(num) for num in binary))