import yaml
import math

def calculate_growth_rate(x1, y1, x2, y2):
    # Calculates the exponential growth rate given two points
    return (y2/y1)**(1/(x2-x1))

def calculate_cost(a, b, rank):
    # Special case for rank 0
    if rank == 0:
        return 0
    return int(round(a * (b ** (rank - 1))))

def generate_ranks_data(initial_cost, final_cost, initial_rank, final_rank):
    # Calculate growth rate 'b' using the initial and final known costs
    b = calculate_growth_rate(initial_rank, initial_cost, final_rank, final_cost)
    
    ranks_data = {}
    for rank in range(0, 131):  # Including rank 0
        if rank == 0:
            ranks_data[str(rank)] = {'Prefix': '&a&l0'}   # Only Prefix for rank 0
        else:
            # For other ranks, include command with rank number as well
            command = f"lp user %player% perm set cmi.command.warp.a{rank}"
            ranks_data[str(rank)] = {
                'Prefix': f"&a&l{rank}",
                'Cost': calculate_cost(initial_cost, b, rank),
                'CMD': [command]
            }
    
    return ranks_data

def create_ranks_file(filename, ranks_data):
    with open(filename, 'w') as file:
        yaml.dump({'Ranks': ranks_data}, file, default_flow_style=False)

# Main execution
initial_cost = 20
final_cost = 700000
initial_rank = 1
final_rank = 61

ranks_data = generate_ranks_data(initial_cost, final_cost, initial_rank, final_rank)
create_ranks_file('ranks.yml', ranks_data)