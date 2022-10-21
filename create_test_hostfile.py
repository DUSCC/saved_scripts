#!/usr/bin/python3
import os

def get_input():
    print("input number of nodes to test:")
    n = int(input())
    return n

def write_hostfile(n):
    with open("hostfile_1corepernode", mode="w") as hfile:
        for i in range(1, n+1):
            hfile.write(f"compute-{i:03d} slots=1 max_slots=1" + os.linesep)

def main():
    n = get_input()
    write_hostfile(n)

main()
