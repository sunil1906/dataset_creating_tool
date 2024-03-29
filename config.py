import os, json

SCALE_DETAILS = None
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'scale_adjustment.json'), 'r') as openfile:
    SCALE_DETAILS = json.load(openfile)

SCALE = float(SCALE_DETAILS["SCALE"])

BEFORE_AFTER_FRAMES = 5

SCREEN_WIDTH = 1280 * SCALE
SCREEN_HEIGHT = 720 * SCALE
TITLE_OF_WINDOW = 'Dataset Creating Tool'
PATH_TO_WINDOW_ICON_IMAGE = './static/icon.png'
FPS = 30
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
VIDEO_CUT_LEFT = 550
VIDEO_CUT_RIGHT = 20

FORWARD_BACKWARD_FAST_FORWARD = 20

# Text box to display id
TOP_LEFT_COORDINATES_OF_ID_DISPLAY_TEXT_BOX = (300 * SCALE, 230 * SCALE)

# Button settings for ID
ID_SUBMIT_BUTTON_WIDTH = 200 * SCALE
TOP_LEFT_COORDINATES_OF_ID_DISPLAY = (SCREEN_WIDTH//2 - ID_SUBMIT_BUTTON_WIDTH//2, 430 * SCALE)
ID_SUBMIT_BUTTON_HEIGHT = 40 * SCALE
ID_SUBMIT_BUTTON_ELEVATION = 2

# Profile creation yes/no prompt
TOP_LEFT_COORDINATES_OF_PROFILE_CREATE_YES_NO_PROMPT_TEXT = (250 * SCALE, 250 * SCALE)

# Back Button settings for yes no profile creation display
TOP_LEFT_COORDINATES_OF_PROFILE_CREATE_YES_NO_BACK_BUTTON = (50 * SCALE, 75 * SCALE)
PROFILE_CREATE_YES_NO_DISPLAY_BACK_BUTTON_WIDTH = 150 * SCALE
PROFILE_CREATE_YES_NO_DISPLAY_BACK_BUTTON_HEIGHT = 35 * SCALE
PROFILE_CREATE_YES_NO_BACK_BUTTON_ELEVATION = 2

# Profile create yes button
TOP_LEFT_COORDINATES_OF_PROFILE_CREATE_YES_BUTTON = (400 * SCALE, 400 * SCALE)
PROFILE_CREATE_YES_DISPLAY_BUTTON_WIDTH = 200 * SCALE
PROFILE_CREATE_YES_DISPLAY_BUTTON_HEIGHT = 40 * SCALE
PROFILE_CREATE_YES_DISPLAY_BUTTON_ELEVATION = 2

# Profile create no button
TOP_LEFT_COORDINATES_OF_PROFILE_CREATE_NO_BUTTON = (650 * SCALE, 400 * SCALE)
PROFILE_CREATE_NO_DISPLAY_BUTTON_WIDTH = 200 * SCALE
PROFILE_CREATE_NO_DISPLAY_BUTTON_HEIGHT = 40 * SCALE
PROFILE_CREATE_NO_DISPLAY_BUTTON_ELEVATION = 2

# Slider details adjust landmarks page
ADJUST_LANDMARKS_PAGE_SLIDER_HEIGHT = 40 * SCALE
ADJUST_LANDMARKS_PAGE_SLIDER_WIDTH = 800 * SCALE    # Approx. (video_frame_width - pause_button_width - 10)
ADJUST_LANDMARKS_PAGE_SLIDER_POS = (110 * SCALE, 650 * SCALE)

# Video player details adjust landmarks page
ADJUST_LANDMARKS_PAGE_VIDEO_PLAYER_HEIGHT = int(480 * SCALE)
ADJUST_LANDMARKS_PAGE_VIDEO_PLAYER_WIDTH = int(854 * SCALE)
ADJUST_LANDMARKS_PAGE_VIDEO_PLAYER_POS = (50 * SCALE, 100 * SCALE)

# Pause button adjust landmarks page
TOP_LEFT_COORDINATES_OF_ADJUST_LADMARKS_PAGE_PAUSE_BUTTON = (50 * SCALE, 650 * SCALE)
ADJUST_LANDMARKS_PAGE_PAUSE_BUTTON_WIDTH = 50 * SCALE
ADJUST_LANDMARKS_PAGE_PAUSE_BUTTON_HEIGHT = 50 * SCALE
ADJUST_LANDMARKS_PAGE_PAUSE_BUTTON_ELEVATION = 2

# Play button details adjust landmarks page
TOP_LEFT_COORDINATES_OF_ADJUST_LADMARKS_PAGE_PLAY_BUTTON = (50 * SCALE, 650 * SCALE)
ADJUST_LANDMARKS_PAGE_PLAY_BUTTON_WIDTH = 50 * SCALE
ADJUST_LANDMARKS_PAGE_PLAY_BUTTON_HEIGHT = 50 * SCALE
ADJUST_LANDMARKS_PAGE_PLAY_BUTTON_ELEVATION = 2

# Proceed button details adjust landmarks page
TOP_LEFT_COORDINATES_OF_ADJUST_LADMARKS_PAGE_PROCEED_BUTTON = (1050 * SCALE, 10 * SCALE)
ADJUST_LANDMARKS_PAGE_PROCEED_BUTTON_WIDTH = 200 * SCALE
ADJUST_LANDMARKS_PAGE_PROCEED_BUTTON_HEIGHT = 40 * SCALE
ADJUST_LANDMARKS_PAGE_PROCEED_BUTTON_ELEVATION = 2

# Detected Landmarks display coordinates
NUMBER_OF_LANDMARKS_DISPLAY_PER_PAGE = 3
DETECTED_LANDMARKS_DISPLAY_COORDINATES_LIST = [(1000 * SCALE, 130 * SCALE), (1000 * SCALE, 330 * SCALE), (1000 * SCALE, 530 * SCALE)]
DETECTED_LANDMARKS_DISPLAY_IMAGE_SIZE = ((1350 * SCALE) // 8, (1080 * SCALE) // 8) 

# Adjust Landmarks button display coordinates
ADJUST_LANDMARKS_BUTTON_DISPLAY_COORDINATES_LIST = [(1200 * SCALE, 150 * SCALE), (1200 * SCALE, 350 * SCALE), (1200 * SCALE, 550 * SCALE)]
ADJUST_LANDMARKS_BUTTON_WIDTH = 40 * SCALE
ADJUST_LANDMARKS_BUTTON_HEIGHT = 40 * SCALE
ADJUST_LANDMARKS_BUTTON_ELEVATION = 2

# Adjust landmark yes/no prompt
TOP_LEFT_COORDINATES_OF_ADJUST_LANDMARK_YES_NO_PROMPT_TEXT = (250 * SCALE, 250 * SCALE)

# Detected landmarks display previous page buttons
TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_PREVIOUS_PAGE_BUTTON = (1180 * SCALE, 80 * SCALE)
DETECTED_LANDMARKS_PREVIOUS_PAGE_BUTTON_WIDTH = 40 * SCALE
DETECTED_LANDMARKS_PREVIOUS_PAGE_BUTTON_HEIGHT = 40 * SCALE
DETECTED_LANDMARKS_PREVIOUS_PAGE_BUTTON_ELEVATION = 2

# Detected landmarks display next page buttons
TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_NEXT_PAGE_BUTTON = (1230 * SCALE, 80 * SCALE)
DETECTED_LANDMARKS_NEXT_PAGE_BUTTON_WIDTH = 40 * SCALE
DETECTED_LANDMARKS_NEXT_PAGE_BUTTON_HEIGHT = 40 * SCALE
DETECTED_LANDMARKS_NEXT_PAGE_BUTTON_ELEVATION = 2

# Landmarks display border
TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_BORDER = (950 * SCALE, 60 * SCALE)
DETECTED_LANDMARKS_BORDER_WIDTH = 325 * SCALE
DETECTED_LANDMARKS_BORDER_HEIGHT = 650 * SCALE

# Detected landmarks title
TOP_LEFT_COORDINATES_OF_DETECTED_LANDMARKS_TITLE = (955 * SCALE, 65 * SCALE)
