import re, os, glob

filenames = glob.glob(os.path.join("check_nodes", "compute-*_cpu*.txt"))
file_strings = []
for filename in filenames:
    with open(filename) as file:
        file_strings.append(file.read())

data_regex = r"MemTotal: *(\d*)|MemAvailable: *(\d*)|^CPU\(s\): *(\d*)|Thread\(s\) per core: *(\d)|Model name: *(.*)"


node_memory_total_values = []
node_memory_available_values = []\

hyperthreaded_count = 0

for file_index, string in enumerate(file_strings):
    matches = re.finditer(data_regex, string, re.MULTILINE)
    for match_index, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if match.group(groupNum) == None:
                continue

            #print(groupNum, match.group(groupNum))

            if groupNum == 1:
                if int(match.group(groupNum)) < 56000000:
                    print(f"Node number {filenames[file_index]} has a different memory amount {match.group(groupNum).strip()}")
                node_memory_total_values.append(int(match.group(groupNum)))
            elif groupNum == 2:
                node_memory_available_values.append(int(match.group(groupNum)))
            elif groupNum == 3:
                continue
                if int(match.group(groupNum)) != 20:
                    print(f"Node number {file_index} has a different cpu count {match.group(groupNum).strip()}")
            elif groupNum == 4:
                if int(match.group(groupNum)) != 1:
                    print(f"Node number {filenames[file_index]} has hyperthreading enabled")
                    hyperthreaded_count += 1
            elif groupNum == 5:
                if match.group(groupNum).strip() != "Intel(R) Xeon(R) CPU E5-2660 v3 @ 2.60GHz":
                    print(f"Node number {file_index} has a different cpu {match.group(groupNum).strip()}")

print(f"{hyperthreaded_count} nodes have hyperthreading enabled.")