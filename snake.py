import numpy as np

# Params
class params:
    x_len = 10
    y_len = 10

# Tile classes
class tile_type:
    empty = 0
    head = 1
    body = 2
    tail = 3
    food = 4

# New function as class snake that automatically assigns head and tail to first and last element?

# Display function of game state
def display_gamestate(x_len, y_len, xy_coord_list, food_point):
    grid = np.zeros([x_len, y_len])
    for poi in xy_coord_list:
        grid[poi[0], poi[1]] = poi[2]
    grid[food_point[0]][food_point[1]] = tile_type.food
    print(grid)

# Checking target tiles
def check_target(coord_list, food_point):
    if coord_list[0][:2] == food_point:
        return 'Food'
    # has the snake bitten itself
    snake_body = [segment[:2] for segment in coord_list]
    if coord_list[0][:2] in snake_body[1:]:
        raise ValueError
    else:
        return 'Empty'

# Finding new food points that are not occupied by anything else
def finding_food_point(coordinates):
    food_inside_snake = True
    while food_inside_snake == True:
        food_coord = [np.random.randint(0, params.x_len), np.random.randint(0, params.y_len)]
        snake_body = [segment[:2] for segment in coordinates]
        food_inside_snake = food_coord[:2] in snake_body
    return food_coord

# function to simulate movement of snake body
def movement(coordinates,direction, food_point):
    # create new head at same place as old head
    coordinates.insert(0, coordinates[0].copy())
    coordinates[0][2] = tile_type.head
    coordinates[1][2] = tile_type.body
    # move new head to position of movement
    if direction == 'r':
        coordinates[0][1] += 1
    elif direction == 'l':
        coordinates[0][1] -= 1
    elif direction == 'u':
        coordinates[0][0] -= 1
    elif direction == 'd':
        coordinates[0][0] += 1
    else:
        raise ValueError
    # Creating new food point if food was found
    if check_target(coordinates, food_point) == 'Food':
        food_point = finding_food_point(coordinates)
    # delete last snake segment if no food was found
    else:
        coordinates.pop()
    return coordinates, food_point

# Main driver function
def hyphasma():
    # List to store all important points
    coord_list = []
    # Random starting point within grid range
    start_coords = [np.random.randint(0,params.x_len), np.random.randint(0,params.y_len), tile_type.head]
    # Adding starting point to grid
    coord_list.append(start_coords)
    # Adding food to grid
    food = finding_food_point(coord_list)
    # Display initial game state
    display_gamestate(params.x_len, params.y_len, coord_list, food)
    i=0
    while i < 100:
        coord_list, food = movement(coord_list, input('r/l/u/d: '), food)
        display_gamestate(params.x_len, params.y_len, coord_list, food)
        i += 1

hyphasma()