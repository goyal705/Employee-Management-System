# Dimensions of the plot
plot_length = 25  # in feet
plot_width = 15   # in feet

# Number of storeys
num_storeys = 2

# Standard wall thickness
wall_thickness = 0.75  # in feet

# Standard floor height for each storey
floor_height = 10  # in feet

# Calculate the total surface area of the walls for both storeys
total_wall_area = 2 * num_storeys * ((plot_length + plot_width) * floor_height - plot_length * plot_width)

# Standard brick size
standard_brick_size = (7.5 / 12, 3.5 / 12, 2.5 / 12)  # in feet (length, width, height)

# Calculate the number of bricks needed
brick_volume = standard_brick_size[0] * standard_brick_size[1] * standard_brick_size[2]
num_bricks = total_wall_area / brick_volume

print(f"Approximate number of bricks required: {round(num_bricks)}")
