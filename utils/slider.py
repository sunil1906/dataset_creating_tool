import pygame, sys
from utils import colors

class Slider:
    def __init__(self, window, width, height, pos):
        self.window = window
        self.width = width
        self.height = height
        self.pos = pos
        self.is_slider_dragged = False

        self.BAR_MARGIN = 10
        self.BAR_HEIGHT = 10

        self.bar_top_left_x = self.pos[0] + self.BAR_MARGIN
        self.bar_top_left_y = self.pos[1] + self.height / 2 - self.BAR_HEIGHT / 2
        self.bar_width = width - 2 * self.BAR_MARGIN
        self.bar_height = self.BAR_HEIGHT

        self.rect_bar = pygame.Rect(self.bar_top_left_x, self.bar_top_left_y, self.bar_width, self.bar_height)
        self.outline_rect = pygame.Rect(pos[0], pos[1], width, height)

        self.control_point_progress = 0
        self.control_point_progress_percentage = 0
        self.control_point_radius = 10
        self.control_point_color = colors.RED
        self.control_point_center = (self.pos[0] + self.BAR_MARGIN + self.control_point_progress, self.pos[1] + self.height / 2)

    def update_progress(self, percentage):
        self.control_point_progress_percentage = percentage
        self.control_point_progress = (percentage * self.bar_width )

    def check_dragged(self):
        mouse_pos = pygame.mouse.get_pos()       
        if self.rect_bar.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.control_point_progress = mouse_pos[0] - self.pos[0] - self.BAR_MARGIN
                self.control_point_progress_percentage = self.control_point_progress / self.bar_width
                self.is_slider_dragged = True

    def update_center(self):
        self.control_point_center = (self.pos[0] + self.BAR_MARGIN + self.control_point_progress, self.pos[1] + self.height / 2)
    
    def draw(self):
        self.check_dragged()
        self.update_center()
        pygame.draw.rect(self.window,colors.LIGHT_GRAY, self.outline_rect,border_radius = 8)
        pygame.draw.rect(self.window,colors.BLACK, self.rect_bar,border_radius = 8)
        pygame.draw.circle(self.window, self.control_point_color, self.control_point_center, self.control_point_radius)

    def get_is_slider_dragged(self):
        return self.is_slider_dragged

    def set_is_slider_dragged(self, value):
        self.is_slider_dragged = value

    def get_control_point_progress_percentage(self):
        return self.control_point_progress_percentage

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((1280,720))
    pygame.display.set_caption('Slider')
    clock = pygame.time.Clock()

    slider = Slider(window=window,width=800,height=40,pos=(100,650))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(colors.WHITE)
        slider.draw()
        pygame.display.update()
        clock.tick(60)