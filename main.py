import pygame
import sys

# Initialize an empty dictionary
# Store data in key-value pairs
# key(name), value(number)
phonebook = {}

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("PyContact v1.0")


# import pygame's font module
font = pygame.font.SysFont(None, 32)

# Colours
White = (255, 255, 255)
Black = (0 ,0 , 0)
Gray = (200, 200, 200)

current_input = "name"
name_input = ""
phone_input = ""

def handle_text_input(event):
    global name_input, phone_input, current_input

    if event.key == pygame.K_BACKSPACE:
        if current_input == "name":
            name_input = name_input[0:-1:1] # remove letter
        elif current_input == "phone":
            phone_input = phone_input[0:-1:1] # remove number

    elif event.unicode:
        char = event.unicode
        if current_input == "name" and len(name_input) < 15:
            name_input += char
        elif current_input == "phone" and len(phone_input) < 10 and char.isdigit():
            phone_input += char




# Define a function that renders a textlabel
def build_textLabel(text, pos, color):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, pos)

#pygame.Rect(x, y, width, height)
def build_button(text, text_color, button_color, rect):
    pygame.draw.rect(screen, button_color, rect)
    build_textLabel(text, (rect[0], rect[1]), text_color)

def display_phonebook():
    x = 50
    y = 100
    for name, phone in phonebook.items():
        build_textLabel(name + " : " + phone, (x, y), White)
        y += 50

        #prevent content overflow on the screen
        if y > 550:
            break

# Main loop
running = True
mode = "menu"

while running:

    screen.fill((0, 0, 50))


    # Menu screen
    if mode == "menu":
        build_textLabel("Menu", (0, 0), (255, 0, 0))

        #pygame.Rect(x, y, width, height)
        add_button = pygame.Rect(0, 50, 180, 25)
        remove_button = pygame.Rect(0, 100, 180, 25)
        display_button = pygame.Rect(0, 150, 180, 25)
        exit_button = pygame.Rect(0, 200, 180, 25)

        build_button("Add Contact", (0, 0, 0), (255, 255, 255), add_button)
        build_button("Remove Contact", (0, 0, 0), (255, 255, 255), remove_button)
        build_button("View Contacts", (0, 0, 0), (255, 255, 255), display_button)
        build_button("Exit", (0, 0, 0), (255, 255, 255), exit_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if add_button.collidepoint(event.pos):
                    mode = "add"
                elif remove_button.collidepoint(event.pos):
                    mode = "remove"
                elif display_button.collidepoint(event.pos):
                    mode = "display"
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


    # Add contact screen
    elif mode == "add":
        build_textLabel("Add Contact", (0, 0), (0, 255, 0))

        # Build 2 sets of text labels and inputs
        build_textLabel("Name:", (50, 100), (255, 255, 255))
        pygame.draw.rect(screen, Gray if current_input == "name" else White, (130, 100, 150, 25))
        build_textLabel(name_input, (130, 100), (0, 0, 0))

        build_textLabel("HP No.:", (50, 150), (255, 255, 255))
        pygame.draw.rect(screen, Gray if current_input == "phone" else White, (130, 150, 150, 25))
        build_textLabel(phone_input, (130, 150), (0, 0, 0))

        addScreen_add_button = pygame.Rect(160, 300, 50, 25)
        build_button("Add", (0, 0, 0), (224, 236, 255), addScreen_add_button)


        addScreen_back_button = pygame.Rect(100, 500, 100, 25)
        build_button("Back", (0, 0, 0), (224, 236, 255), addScreen_back_button)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if addScreen_back_button.collidepoint(event.pos):
                    mode = "menu"
                elif addScreen_add_button.collidepoint(event.pos):
                    if name_input and phone_input:
                        phonebook[name_input] = phone_input
                        name_input = ""
                        phone_input = ""
                        mode = "menu"
                        print(phonebook)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    current_input = "phone" if current_input == "name" else "name"
                else:
                    handle_text_input(event)




    # Remove contact screen
    elif mode == "remove":
        build_textLabel("Remove Contact", (0, 0), (255, 255, 0))

        build_textLabel("Name: ", (50, 100), White)
        pygame.draw.rect(screen, Gray, (50, 120, 200, 30))
        build_textLabel(name_input, (50, 120), Black)

        removeScreen_back_button = pygame.Rect(100, 500, 100, 25)
        build_button("Back", (0, 0, 0), (224, 236, 255), removeScreen_back_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                handle_text_input(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if removeScreen_back_button.collidepoint(event.pos):
                    mode = "menu"


    # Display contact screen
    elif mode == "display":
        build_textLabel("Display Contact", (0, 0), (0, 255, 255))

        display_phonebook()

        displayScreen_back_button = pygame.Rect(100, 500, 100, 25)
        build_button("Back", (0, 0, 0), (224, 236, 255), displayScreen_back_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if  displayScreen_back_button.collidepoint(event.pos):
                    mode = "menu"




    # To refresh screen on every frame
    pygame.display.update()













