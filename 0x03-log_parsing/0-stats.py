#!/usr/bin/python3
import sys
import re
""" """
pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "(.*?)" (\d{3})? (\d+)$')
with open('stdin', 'r') as file:
    for line_number, line in enumerate(file, start=0):
        line = line.split()
        match = pattern.match(line)
        if match:
            print(f"Line {line_number} matches: {line}")
