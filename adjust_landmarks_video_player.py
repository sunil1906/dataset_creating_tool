import pygame, sys, os, json, cv2
import config
from utils.slider import Slider
from utils.video_player import VideoPlayer
from utils.button import Button
from utils import colors
import adjust_landmark_prompt_yes_no

def adjust(MAIN_WINDOW, ROOT_DIR, DATA_DIR, id):
    clock = pygame.time.Clock()

    # Slider
    slider = Slider(window=MAIN_WINDOW,width=config.ADJUST_LANDMARKS_PAGE_SLIDER_WIDTH,height=config.ADJUST_LANDMARKS_PAGE_SLIDER_HEIGHT,pos=config.ADJUST_LANDMARKS_PAGE_SLIDER_POS)

    # Video Player
    path_to_meta_data = os.path.join(DATA_DIR, id, 'meta_data.json')
    meta_data = None
    with open(path_to_meta_data, 'r') as openfile:
        meta_data = json.load(openfile)
    path_to_video = os.path.join(ROOT_DIR, 'videos', id + '.avi')
    videoPlayer = VideoPlayer(window=MAIN_WINDOW, path_to_video=path_to_video,width=config.ADJUST_LANDMARKS_PAGE_VIDEO_PLAYER_WIDTH,height=config.ADJUST_LANDMARKS_PAGE_VIDEO_PLAYER_HEIGHT,pos=config.ADJUST_LANDMARKS_PAGE_VIDEO_PLAYER_POS)

    # Fonts used
    pause_play_button_font = pygame.font.SysFont(None, int(40 * config.SCALE))
    proceed_button_font = pygame.font.SysFont(None, int(40 * config.SCALE))
    landmarks_prev_next_button_font = pygame.font.SysFont(None, int(40 * config.SCALE))
    landmarks_title_font = pygame.font.SysFont('tahoma', int(20 * config.SCALE))
    landmarks_name_font = pygame.font.SysFont('tahoma', int(25 * config.SCALE))
    adjust_landmarks_button_font = pygame.font.SysFont('tahoma', int(25 * config.SCALE))

    # Button in page
    pause_button = Button(id="pause_button", window=MAIN_WINDOW, gui_font=pause_play_button_font, text=">", width=config.ADJUST_LANDMARKS_PAGE_PAUSE_BUTTON_WIDTH, height=config.ADJUST_LANDMARKS_PAGE_PAUSE_BUTTON_HEIGHT, pos=config.TOP_LEFT_COORDINATES_OF_ADJUST_LADMARKS_PAGE_PAUSE_BUTTON, elevation=config.ADJUST_LANDMARKS_PAGE_PAUSE_BUTTON_ELEVATION)
    play_button = Button(id="play_button", window=MAIN_WINDOW, gui_font=pause_play_button_font, text="||", width=config.ADJUST_LANDMARKS_PAGE_PLAY_BUTTON_WIDTH, height=config.ADJUST_LANDMARKS_PAGE_PLAY_BUTTON_HEIGHT, pos=config.TOP_LEFT_COORDINATES_OF_ADJUST_LADMARKS_PAGE_PLAY_BUTTON, elevation=config.ADJUST_LANDMARKS_PAGE_PLAY_BUTTON_ELEVATION)
    proceed_button = Button(id="proceed_button", window=MAIN_WINDOW, gui_font=proceed_button_font, text="Proceed", width=config.ADJUST_LANDMARKS_PAGE_PROCEED_BUTTON_WIDTH, height=config.ADJUST_LANDMARKS_PAGE_PROCEED_BUTTON_HEIGHT, pos=config.TOP_LEFT_COORDINATES_OF_ADJUST_LADMARKS_PAGE_PROCEED_BUTTON, elevation=config.ADJUST_LANDMARKS_PAGE_PROCEED_BUTTON_ELEVATION)
    landmarks_prev_page_button = Button(id="landmarks_prev_page_button", window=MAIN_WINDOW, gui_font=landmarks_prev_next_button_font, text="<", width=config.DETECTED_LANDMARKS_PREVIOUS_PAGE_BUTTON_WIDTH, height=config.DETECTED_LANDMARKS_PREVIOUS_PAGE_BUTTON_HEIGHT, pos=config.TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_PREVIOUS_PAGE_BUTTON, elevation=config.DETECTED_LANDMARKS_PREVIOUS_PAGE_BUTTON_ELEVATION)
    landmarks_next_page_button = Button(id="landmarks_next_page_button", window=MAIN_WINDOW, gui_font=landmarks_prev_next_button_font, text=">", width=config.DETECTED_LANDMARKS_NEXT_PAGE_BUTTON_WIDTH, height=config.DETECTED_LANDMARKS_NEXT_PAGE_BUTTON_HEIGHT, pos=config.TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_NEXT_PAGE_BUTTON, elevation=config.DETECTED_LANDMARKS_NEXT_PAGE_BUTTON_ELEVATION)


    landmarks = ['vocal_cord', 'og_junction', 'body', 'antrum', 'pylorus', 'd1', 'd2', 'incisura', 'fundus', 'no_mans_land']
    # Loading detected landmarks
    detected_landmark_images = []
    def generate_detected_landmark_images_data():
        detected_landmark_images.clear()
        idx = 0
        for landmark in landmarks:
            d = dict()
            d['name'] = landmark
            d['frame'] = meta_data[landmark]
            d['name_pos'] = (config.DETECTED_LANDMARKS_DISPLAY_COORDINATES_LIST[idx % config.NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE][0], config.DETECTED_LANDMARKS_DISPLAY_COORDINATES_LIST[idx % config.NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE][1] + config.DETECTED_LANDMARKS_DISPLAY_IMAGE_SIZE[1])
            try: 
                d['image'] = pygame.image.load(os.path.join(DATA_DIR, id, landmark, id + '_' + landmark + '_' + str(config.BEFORE_AFTER_FRAMES) + '.jpg'))
            except:
                d['image'] = pygame.image.load(os.path.join(ROOT_DIR, 'static', 'landmark_not_detected.jpg'))
            d['image'] = pygame.transform.scale(d['image'], config.DETECTED_LANDMARKS_DISPLAY_IMAGE_SIZE)
            d['image_pos'] = config.DETECTED_LANDMARKS_DISPLAY_COORDINATES_LIST[idx % config.NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE]
            d['landmark_button'] = Button(id="landmarks_" + landmark, window=MAIN_WINDOW, gui_font=landmarks_prev_next_button_font, text="", width=config.DETECTED_LANDMARKS_DISPLAY_IMAGE_SIZE[0], height=config.DETECTED_LANDMARKS_DISPLAY_IMAGE_SIZE[1], pos=config.DETECTED_LANDMARKS_DISPLAY_COORDINATES_LIST[idx % config.NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE], elevation=0)
            d['adjust_landmark_button'] = Button(id="adjust_landmarks_" + landmark, window=MAIN_WINDOW, gui_font=adjust_landmarks_button_font, text="/", width=config.ADJUST_LANDMARKS_BUTTON_WIDTH, height=config.ADJUST_LANDMARKS_BUTTON_HEIGHT, pos=config.ADJUST_LANDMARKS_BUTTON_DISPLAY_COORDINATES_LIST[idx % config.NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE], elevation=config.ADJUST_LANDMARKS_BUTTON_ELEVATION)
            detected_landmark_images.append(d)
            idx += 1
    generate_detected_landmark_images_data()

    video_paused = True
    current_landmark_display_page = 0
    total_number_of_landmark_pages = ( len(landmarks) // config.NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE )
    if len(landmarks) % config.NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE:
        total_number_of_landmark_pages += 1

    while True:
        MAIN_WINDOW.fill(colors.WHITE)
        total_frames = videoPlayer.total_frame_count
        curr_frame = 0
        videoPlayer.update_current_frame(frame=curr_frame)
        videoPlayer.play()
        while curr_frame < total_frames:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        video_paused = not video_paused
                
                    elif event.key == pygame.K_LEFT:
                        curr_frame = max(0, curr_frame - config.FORWARD_BACKWARD_FAST_FORWARD)
                        videoPlayer.update_current_frame(frame=curr_frame)
                        videoPlayer.play()

                    elif event.key == pygame.K_RIGHT:
                        curr_frame = min(total_frames, curr_frame + config.FORWARD_BACKWARD_FAST_FORWARD)
                        videoPlayer.update_current_frame(frame=curr_frame)
                        videoPlayer.play()
            
            if slider.get_is_slider_dragged():
                slider.set_is_slider_dragged(value=False)
                control_point_progress_percentage = slider.get_control_point_progress_percentage()
                curr_frame = min(total_frames, 1 + (total_frames * control_point_progress_percentage))
                videoPlayer.update_current_frame(frame=curr_frame)
                videoPlayer.play()

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

            # Landmarks display border
            pygame.draw.rect(MAIN_WINDOW, colors.BLACK, pygame.Rect(config.TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_BORDER[0], config.TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_BORDER[1], config.DETECTED_LANDMARKS_BORDER_WIDTH, config.DETECTED_LANDMARKS_BORDER_HEIGHT), 2)

            # Detected landmarks title
            text_surf = landmarks_title_font.render('Detected Landmarks:', True, colors.BLACK)
            MAIN_WINDOW.blit(text_surf, config.TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_TITLE)

            # Landmarks display
            for i in range(config.NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE):
                idx = current_landmark_display_page * config.NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE + i
                if idx >= len(landmarks):
                    continue
                MAIN_WINDOW.blit(detected_landmark_images[idx]['image'], detected_landmark_images[idx]['image_pos'])
                text_surf = landmarks_name_font.render(detected_landmark_images[idx]['name'], True, colors.BLACK)
                MAIN_WINDOW.blit(text_surf,detected_landmark_images[idx]['name_pos'] )
                detected_landmark_images[idx]['adjust_landmark_button'].draw()
                if detected_landmark_images[idx]['landmark_button'].check_click():
                    if detected_landmark_images[idx]['frame'] != -1:
                        curr_frame = detected_landmark_images[idx]['frame']
                        videoPlayer.update_current_frame(frame=curr_frame)
                        videoPlayer.play()
                if detected_landmark_images[idx]['adjust_landmark_button'].check_click():
                    # Ask Yes / No Prompt before adjusting landmark
                    response = adjust_landmark_prompt_yes_no.ask(MAIN_WINDOW=MAIN_WINDOW, landmark=detected_landmark_images[idx]['name'])
                    if response == 'Yes':
                        # 3 places modification required

                        # Place 1: meta data
                        meta_data[ detected_landmark_images[idx]['name'] ] = int(curr_frame)
                        with open((path_to_meta_data), "w") as outfile:
                            outfile.write(json.dumps(meta_data, indent=4))
                        # Place 2: landmark_images folder
                        cap = cv2.VideoCapture(path_to_video)
                        cnt = 0
                        for i in range(int(curr_frame) - config.BEFORE_AFTER_FRAMES, int(curr_frame) + config.BEFORE_AFTER_FRAMES):
                            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
                            ret, frame = cap.read()
                            if ret == True:
                                cropped = frame[:, config.VIDEO_CUT_LEFT : config.VIDEO_WIDTH - config.VIDEO_CUT_RIGHT]
                                cv2.imwrite(os.path.join(DATA_DIR, id, detected_landmark_images[idx]['name']) + '/' + id + '_' + detected_landmark_images[idx]['name'] + '_' + str(cnt) + '.jpg', cropped)
                            else:
                                print('Error! Not able to modify the landmark images in landmark images folder')
                            cnt += 1
                        cap.release()
                        
                        # Place 3: update landmark images shown in current page
                        generate_detected_landmark_images_data()
                        
                    # Update page UI
                    MAIN_WINDOW.fill(colors.WHITE)
                    videoPlayer.play()
                    videoPlayer.update_current_frame(frame=curr_frame)


            # Landmarks page previous and next buttons
            landmarks_prev_page_button.draw()
            if landmarks_prev_page_button.check_click():
                current_landmark_display_page = max(0, current_landmark_display_page - 1)
                MAIN_WINDOW.fill(colors.WHITE, rect = (config.TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_BORDER[0], config.TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_BORDER[1], config.DETECTED_LANDMARKS_BORDER_WIDTH, config.DETECTED_LANDMARKS_BORDER_HEIGHT))
            
            landmarks_next_page_button.draw()
            if landmarks_next_page_button.check_click():
                current_landmark_display_page = min(total_number_of_landmark_pages - 1, current_landmark_display_page + 1)
                MAIN_WINDOW.fill(colors.WHITE, rect = (config.TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_BORDER[0], config.TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_BORDER[1], config.DETECTED_LANDMARKS_BORDER_WIDTH, config.DETECTED_LANDMARKS_BORDER_HEIGHT))

            # Proceed button
            proceed_button.draw()
            if proceed_button.check_click():
                return "Proceed"

            pygame.display.update()
            clock.tick(25)
