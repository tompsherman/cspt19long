"""
looking through an adventure game maze trying to find a way out
have a world class that loads different types of worlds
start with the line test world, then build up to cross, loop, etc. until main maze

world class technically builds map for me

my job is the traversal
create a path for player to walk through
where it takes minimum amount of moves to get through
under 1000 is MVP, under 900 stretch, over 2000 fail / self reflection needed
do kind of a degrees of separation where retry until you get the best score
start in a room then 

world class:
    standardized build in of world (building graph)

player class:
    travel in a direction and see if you want to go in a room

room class:
    nsew
    x / y
    get_exits is friend

go into room, get_exits in room, get NSEW, and you get an exits list (see ReadMe)\
    traversal builds map, will render 500 entries in the graph an no question marks left

read up the hints in it