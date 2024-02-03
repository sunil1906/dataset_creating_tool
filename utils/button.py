import pygame, sys

class Button:
    def __init__(self, id, window, gui_font, text, width, height, pos, elevation):
        #Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]
        self.gui_font = gui_font
        self.window = window
        self.id = id

		# top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

		# bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#354B5E'
		#text
        self.text_surf = self.gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
		# elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(self.window,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(self.window,self.top_color, self.top_rect,border_radius = 12)
        self.window.blit(self.text_surf, self.text_rect)

    def check_click(self):
        is_clicked = False
        # print("Waiting for mouse event")
        mouse_pos = pygame.mouse.get_pos()       
        # print('got mouse event') 
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    is_clicked = True
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'
        
        return is_clicked

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Gui Menu')
    clock = pygame.time.Clock()

    gui_font = pygame.font.Font(None,30)
    button1 = Button("TEMP_ID", window, gui_font,'Click me',200,40,(200,250),1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill('#DCDDD8')
        button1.draw()
        if(button1.check_click()):
            print('CLicked!!!')

        pygame.display.update()
        clock.tick(60)
	
