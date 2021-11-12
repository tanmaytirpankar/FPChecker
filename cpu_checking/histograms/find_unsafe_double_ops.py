#!/usr/bin/env python3

import argparse
import collections
import glob
import json
import os
import sys
import matplotlib.pyplot as plt

def load_report(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    f.close()
    return data

def find_unsafe_lines(histogram_data):
    unsafe_lines = []
    possibly_unsafe_lines = []



    for line_data in histogram_data:
        for exponent in line_data['fp32'].keys():
            if int(exponent) == -127 or int(exponent) == 128:
                possibly_unsafe_lines.append(line_data['line'])
                break
        for exponent in line_data['fp64'].keys():
            if int(exponent) < -127 or int(exponent) > 128:
                unsafe_lines.append(line_data['line'])
                break

    return [unsafe_lines, possibly_unsafe_lines]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotting histogram of exponents')
    parser.add_argument('-f', '--json_file',
                        help='JSON format histogram file output by FPChecker containing exponent data',
                        required=True)
    parser.add_argument('-o', '--output_dir',
                        help='Path to directory to create plots in',
                        default='plots')
    arguments = parser.parse_args()

    json_data = load_report(arguments.json_file)

    # json_formatted_obj = json.dumps(json_data, indent=2)
    # print(json_formatted_obj)

    result = find_unsafe_lines(json_data)
    print("\nUnsafe lines: ")
    print(result[0])
    print("\nPossibly unsafe lines: ")
    print(result[1])
    print("\n")