import math

def calculate_growth_rate(x1, y1, x2, y2):
    # Calculate the growth rate b given two points (x1, y1) and (x2, y2) on the curve
    return ((y2/y1) ** (1/(x2-x1)))

def create_ranks_file(filename):
    initial_cost = 20  # Cost at rank 1
    final_cost = 700000  # Cost at rank 61
    initial_rank = 1  # Initial rank
    final_rank = 61  # Final rank where final_cost is known
    
    # Calculate the growth rate
    b = calculate_growth_rate(initial_rank, initial_cost, final_rank, final_cost)

    with open(filename, 'w') as file:
        file.write("Ranks:\n")
        
        # Iterate through the ranks and write their data
        for rank in range(1, 131):  # Ranks from 1 to 130
            file.write(f"  '{rank}':\n")          # Rank ID
            file.write(f"    Prefix: '&a&l{rank}'\n")  # Rank prefix
            if rank == 1:
                cost = initial_cost  # The cost for rank 1 is defined as the initial cost
            else:
                # Calculate the cost for every other rank
                cost = initial_cost * (b ** (rank - 1))
            file.write(f"    Cost: {int(round(cost))}\n")  # Write the cost rounded to an integer
            file.write("    CMD:\n")                       # Commands placeholder
            file.write(f"    - lp user %player% perm set cmi.command.warp.mine{rank}\n")  # Example command
            
# Replace 'ranks.yml' with the path to the file you want to generate
create_ranks_file('ranks.yml')