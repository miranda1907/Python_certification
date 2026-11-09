def hanoi_solver(num):
    final_string = ""

    rod1 = [n for n in range(num, 0, -1)]
    rod2 = []  
    rod3 = []

    rods = [rod1, rod2, rod3]

    final_string += f"{rod1} {rod2} {rod3}\n"  

    final_string = move_disks(num, rod1, rod3, rod2, rods, final_string)       

    return final_string.rstrip("\n")

def move_disks(n, source, destination, auxiliary, rods, string):
    if n == 0:
        return string

    string = move_disks(n - 1, source, auxiliary, destination, rods, string)
    disk = source.pop()
    destination.append(disk)

    string += f"{rods[0]} {rods[1]} {rods[2]}\n"

    string = move_disks(n - 1, auxiliary, destination, source, rods, string)
     
    return string   


print(hanoi_solver(2))
print(hanoi_solver(3))
print(hanoi_solver(4))
print(hanoi_solver(5))
