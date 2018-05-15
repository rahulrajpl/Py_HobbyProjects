import random
import curses


s = curses.initscr()  # initialise the screen
curses.curs_set(0)  # Cursor does not show up on the screen
sh, sw = s.getmaxyx()  # Get Height and Width of the screen
w = curses.newwin(sh, sw, 0, 0)  # Create a new Window with this H and W
w.keypad(1)  # Accepts the keypad input
w.timeout(100)  # Refresh the screen every 100 ms

# Snakes initial position
snk_x = sw/4
snk_y = sh/2

# Create initial Snake Body parts
snake =[
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Create the Food for the snake
food = [int(sh/2), int(sw/2)]  # Position the food at the center of the screen
w.addch(food[0], food[1], curses.ACS_PI)  # Add that food to screen.

# Tell snake where to go initially
key = curses.KEY_RIGHT

# Start an infinite loop for the snake for the rest of the game
while True:
    next_key = w.getch() # Get what is the next key user is entering
    key = key if next_key == -1 else next_key  # Set key as nothing or next_key

    # Check whether user lost the game
    # User loses if Y position is at Top or at Height of the screen Or If x Position in at the Width of the screen
    # or if the snake is its itself.
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    # Determine where is the new head of the snake is going to be
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert the new head of the snake
    snake.insert(0, new_head)

    # Determine if snake has ran into the food

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1) # New Food location
            ]
            food = nf if nf not in snake else None  # If its None its going to re do the loop
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # Add Food to window

    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')  # Add space where tail piece was

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
