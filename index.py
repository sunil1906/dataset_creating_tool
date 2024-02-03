import pygame, sys, os
from utils import os_folder_files_tools
import config, get_video_name, adjust_landmarks_video_player

class EndoBuddy:
    def __init__(self) -> None:
        pygame.init()

        self.SCREEN_WIDTH = config.SCREEN_WIDTH
        self.SCREEN_HEIGHT = config.SCREEN_HEIGHT
        self.TITLE_OF_WINDOW = config.TITLE_OF_WINDOW
        self.FPS = config.FPS

        self.MAIN_WINDOW = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.TITLE_OF_WINDOW)
        pygame.display.set_icon(pygame.image.load(config.PATH_TO_WINDOW_ICON_IMAGE))
        self.fpsClock = pygame.time.Clock()
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.DATA_DIR = os.path.join(self.ROOT_DIR, 'dataset')

    def terminate(self):
        pygame.quit()
        sys.exit()

    def begin(self):
        if os_folder_files_tools.check_if_exists(folder_name='dataset', path=self.ROOT_DIR) == False:
            os_folder_files_tools.create_folder(folder_name='dataset', path=self.ROOT_DIR)
        
        prev_entered_id = ''
        while 1:
            ### Get ID
            id = get_video_name.GetId(self.MAIN_WINDOW, prev_entered_id)
            prev_entered_id = id
            if os_folder_files_tools.check_if_exists(folder_name=id+'.avi', path=os.path.join(self.ROOT_DIR, 'videos')) == False:
                print('Enter a video name which exists!!!!')
                continue
            print("Got:", id, 'as ID')

            does_id_exists = os_folder_files_tools.check_if_exists(folder_name=id, path=self.DATA_DIR)
            if does_id_exists == False:
                os_folder_files_tools.create_folder_for_new_dataset(ROOT_DIR=self.ROOT_DIR, folder_name=id, path=self.DATA_DIR)
                
            response = adjust_landmarks_video_player.adjust(MAIN_WINDOW=self.MAIN_WINDOW, ROOT_DIR=self.ROOT_DIR, DATA_DIR=self.DATA_DIR, id=id)

if __name__ == "__main__":
    endoBuddy = EndoBuddy()
    endoBuddy.begin()
