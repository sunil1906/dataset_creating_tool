import pygame, sys
from utils import colors
from utils.button import Button
import config

def terminate():
    pygame.quit()
    sys.exit()

def GetId(MAIN_WINDOW, prev_entered_id):
    
    FPS = config.FPS
    fpsClock = pygame.time.Clock()
    font = pygame.font.SysFont(None, int(50 * config.SCALE))

    submit_id_button = Button(id="SUBMIT_ID_BUTTON", window=MAIN_WINDOW, gui_font=font, text="Submit", width=config.ID_SUBMIT_BUTTON_WIDTH, height=config.ID_SUBMIT_BUTTON_HEIGHT, pos=config.TOP_LEFT_COORDINATES_OF_ID_DISPLAY, elevation=config.ID_SUBMIT_BUTTON_ELEVATION)

    text = prev_entered_id
    input_active = True

    while input_active:
        fpsClock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if len(text):
                        input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        MAIN_WINDOW.fill(colors.WHITE)
        text_surf = font.render('Video Name: ' + text, True, colors.BLACK)
        MAIN_WINDOW.blit(text_surf, config.TOP_LEFT_COORDINATES_OF_ID_DISPLAY_TEXT_BOX)
        submit_id_button.draw()
        if len(text) and submit_id_button.check_click():
            input_active = False
        pygame.display.update()
    
    return text