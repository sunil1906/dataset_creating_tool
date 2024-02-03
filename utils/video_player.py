import pygame, sys, cv2
from utils.slider import Slider
from utils.button import Button
from utils import colors
import numpy as np

class VideoPlayer:
    def __init__(self, window, path_to_video, width, height, pos) -> None:
        self.path_to_video = path_to_video
        self.cap = cv2.VideoCapture(path_to_video)
        self.window = window
        self.width = width
        self.height = height
        self.pos = pos
        self.total_frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def update_current_frame(self, frame):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame)

    def play(self):
        ret, img = self.cap.read()
        if ret == True:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img = cv2.resize(img, (self.width, self.height))
            img=np.rot90(img)
            img=np.flip(img, 0)
            img=pygame.surfarray.make_surface(img)
            self.window.blit(img, self.pos)

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((1280,720))
    pygame.display.set_caption('Video Player')
    clock = pygame.time.Clock()


    slider = Slider(window=window,width=800,height=40,pos=(160,650))
    path_to_video = 'C:/Users/Sunil/Downloads/Patient-1.AVI'
    videoPlayer = VideoPlayer(window=window, path_to_video=path_to_video,width=854,height=480,pos=(100,100))

    pause_play_button_font = pygame.font.SysFont(None, 40)
    pause_button = Button(id="pause_button", window=window, gui_font=pause_play_button_font, text=">", width=50, height=50, pos=(100, 650), elevation=2)
    play_button = Button(id="play_button", window=window, gui_font=pause_play_button_font, text="||", width=50, height=50, pos=(100, 650), elevation=2)

    video_paused = True

    while True:
        window.fill(colors.WHITE)
        total_frames = videoPlayer.total_frame_count
        curr_frame = 1
        videoPlayer.play()
        curr_frame += 1
        videoPlayer.update_current_frame(frame=curr_frame)
        while curr_frame < total_frames+1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        video_paused = not video_paused
            
            if slider.get_is_slider_dragged():
                slider.set_is_slider_dragged(value=False)
                control_point_progress_percentage = slider.get_control_point_progress_percentage()
                curr_frame = min(total_frames, 1 + (total_frames * control_point_progress_percentage))
                videoPlayer.update_current_frame(frame=curr_frame)

            slider.update_progress(curr_frame/total_frames)
            slider.draw()

            if video_paused == False:
                videoPlayer.play()
                curr_frame += 1
                play_button.draw()
                if play_button.check_click():
                    video_paused = True
            else:
                pause_button.draw()
                if pause_button.check_click():
                    video_paused = False

            pygame.display.update()
            clock.tick(25)