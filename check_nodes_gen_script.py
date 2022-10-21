
node_names = []
with open("node_names.txt", "r") as file:
    node_names = file.readlines()

for node in node_names:
    print(f"ssh {node.strip()} sudo reboot 0 &")
    #print(f"echo \"{node.strip()} slots=20 max_slots=20\" > check_nodes_2/hostfile_{node.strip()} &&")
    #print(f"ssh {node.strip()} \"cat /proc/meminfo && lscpu\" > check_nodes/{node.strip()}_cpu_mem_info.txt &&")
    #print(f"mpirun -np 20 --hostfile check_nodes_2/hostfile_{node.strip()} ./hpl-2.3/testing/xhpl > check_nodes_2/{node.strip()}_xhpl.txt &")
