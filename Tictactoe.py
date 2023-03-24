import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the size of the screen
WIDTH = 600
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

# Set the number of rows and columns on the board
ROWS = 3
COLS = 3

# Set the size of each cell on the board
CELL_SIZE = 200

# Set the margin between each cell on the board
CELL_MARGIN = 10

# Set the size of the mark on the board
MARK_SIZE = 100

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the font
FONT = pygame.font.SysFont(None, 48)

# Create the screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# Set the title of the screen
pygame.display.set_caption("Tic Tac Toe")

# Create the board
board = [[None for col in range(COLS)] for row in range(ROWS)]

# Set the current player
current_player = "X"

# Set the game state
game_over = False
winner = None
# Display the menu
def display_menu():
    # Create the menu text
    menu_font = pygame.font.SysFont(None, 60)
    menu_text = menu_font.render("Tic Tac Toe", True, BLACK)
    menu_text_rect = menu_text.get_rect(center=(WIDTH//2, HEIGHT//4))

    # Create the play button
    play_button_font = pygame.font.SysFont(None, 48)
    play_button_text = play_button_font.render("Play", True, BLACK)
    play_button_text_rect = play_button_text.get_rect(center=(WIDTH//2, HEIGHT//2))

    # Create the quit button
    quit_button_font = pygame.font.SysFont(None, 48)
    quit_button_text = quit_button_font.render("Quit", True, BLACK)
    quit_button_text_rect = quit_button_text.get_rect(center=(WIDTH//2, HEIGHT*3//4))

    # Draw the menu on the screen
    screen.fill(WHITE)
    screen.blit(menu_text, menu_text_rect)
    pygame.draw.rect(screen, WHITE, play_button_text_rect, 2)
    pygame.draw.rect(screen, WHITE, quit_button_text_rect, 2)
    screen.blit(play_button_text, play_button_text_rect)
    screen.blit(quit_button_text, quit_button_text_rect)
    pygame.display.update()

    # Handle events for the menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if play_button_text_rect.collidepoint(x, y):
                    return
                elif quit_button_text_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

# Draw the board
def draw_board():
    screen.fill(BLACK)

    # Draw the cells
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE + (col + 1) * CELL_MARGIN
            y = row * CELL_SIZE + (row + 1) * CELL_MARGIN
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))

            # Draw the marks
            mark = board[row][col]
            if mark == "X":
                x_mark = x + CELL_SIZE // 2
                y_mark = y + CELL_SIZE // 2
                pygame.draw.line(screen, RED, (x_mark - MARK_SIZE // 2, y_mark - MARK_SIZE // 2), (x_mark + MARK_SIZE // 2, y_mark + MARK_SIZE // 2), 5)
                pygame.draw.line(screen, RED, (x_mark - MARK_SIZE // 2, y_mark + MARK_SIZE // 2), (x_mark + MARK_SIZE // 2, y_mark - MARK_SIZE // 2), 5)
            elif mark == "O":
                x_mark = x + CELL_SIZE // 2
                y_mark = y + CELL_SIZE // 2
                pygame.draw.circle(screen, RED, (x_mark, y_mark), MARK_SIZE // 2, 5)

    pygame.display.update()

# Handle events
def handle_events():
    global current_player
    global game_over

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            col = x // (CELL_SIZE + CELL_MARGIN)
            row = y // (CELL_SIZE + CELL_MARGIN)
            if board[row][col] is None:
                board[row][col] = current_player
                current_player = "O" if current_player == "X" else "X"

# Check for a win or tie
def check_win():
    global game_over, winner

    # Check for a win on the rows
    for row in board:
        if row.count("X") == COLS:
            game_over = True
            winner = "X"
            return
        elif row.count("O") == COLS:
            game_over = True
            winner = "O"
            return

    # Check for a win on the columns
    for col in range(COLS):
        column = [board[row][col] for row in range(ROWS)]
        if column.count("X") == ROWS:
            game_over = True
            winner = "X"
            return
        elif column.count("O") == ROWS:
            game_over = True
            winner = "O"
            return

    # Check for a win on the diagonals
    diagonal1 = [board[i][i] for i in range(ROWS)]
    diagonal2 = [board[i][COLS - i - 1] for i in range(ROWS)]
    if diagonal1.count("X") == ROWS or diagonal2.count("X") == ROWS:
        game_over = True
        winner = "X"
        return
    elif diagonal1.count("O") == ROWS or diagonal2.count("O") == ROWS:
        game_over = True
        winner = "O"
        return

    # Check for a tie
    if all(mark is not None for row in board for mark in row):
        game_over = True
        winner = None


# Display the winner
def display_winner():
    global winner
    if(game_over):
        
        if winner is not None:
            text = FONT.render(f"{winner} wins!", True, RED)
        else:
            text = FONT.render("It's a tie!", True, RED)

        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        # Clear the screen
        screen.fill(WHITE)
        
        screen.blit(text, text_rect)
        pygame.display.update()

# Main function
def main():
    global game_over, winner, current_player

    while True:
        display_menu()  # Display the menu
        game_over = False
        winner = None
        current_player = "X"

        while not game_over:
            handle_events()
            draw_board()
            check_win()
            display_winner()

        pygame.time.delay(3000)
        board.clear()
        for i in range(ROWS):
            board.append([None] * COLS)


if __name__ == "__main__":
    main()

       
