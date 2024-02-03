import pygame, sys, os
from utils import colors, os_folder_files_tools
from utils.button import Button
import config

def terminate():
    pygame.quit()
    sys.exit()

def ask(MAIN_WINDOW, landmark):
    selected_icon = "No"
    FPS = config.FPS
    fpsClock = pygame.time.Clock()
    prompt_font = pygame.font.SysFont(None, int(40 * config.SCALE))
    yes_no_button_font = pygame.font.SysFont(None, int(50 * config.SCALE))

    yes_button = Button(id="adjust_landmark_yes_button", window=MAIN_WINDOW, gui_font=yes_no_button_font, text="Yes", width=config.PROFILE_CREATE_YES_DISPLAY_BUTTON_WIDTH, height=config.PROFILE_CREATE_YES_DISPLAY_BUTTON_HEIGHT, pos=config.TOP_LEFT_COORDINATES_OF_PROFILE_CREATE_YES_BUTTON, elevation=config.PROFILE_CREATE_YES_DISPLAY_BUTTON_ELEVATION)
    no_button = Button(id="adjust_landmark_no_button", window=MAIN_WINDOW, gui_font=yes_no_button_font, text="No", width=config.PROFILE_CREATE_NO_DISPLAY_BUTTON_WIDTH, height=config.PROFILE_CREATE_NO_DISPLAY_BUTTON_HEIGHT, pos=config.TOP_LEFT_COORDINATES_OF_PROFILE_CREATE_NO_BUTTON, elevation=config.PROFILE_CREATE_NO_DISPLAY_BUTTON_ELEVATION)

    run = True
    while run:
        fpsClock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    selected_icon = "Yes"
                    return selected_icon

        MAIN_WINDOW.fill(colors.WHITE)

        # showing prompt for new profile creation
        text_surf = prompt_font.render('Are you sure you want to adjust the landmark of '  + landmark  + '?', True, colors.BLACK)
        MAIN_WINDOW.blit(text_surf, config.TOP_LEFT_COORDINATES_OF_ADJUST_LANDMARK_YES_NO_PROMPT_TEXT)

        # Video Button
        yes_button.draw()
        if yes_button.check_click():
            selected_icon = "Yes"
            run = False

        # Report button
        no_button.draw()
        if no_button.check_click():
            selected_icon = "No"
            run = False

        pygame.display.update()

    return selected_icon