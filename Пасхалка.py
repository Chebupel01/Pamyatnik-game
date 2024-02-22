import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        screen_width, screen_height = self.screen.get_size()
        photo_width, photo_height = screen_width // 2, screen_height // 2
        button_width, button_height = screen_width // 6, screen_height // 20

        self.photo_rect = pygame.Rect((screen_width - photo_width) // 2, (screen_height - photo_height) // 2,
                                      photo_width, photo_height)
        self.text_rect = pygame.Rect((screen_width - photo_width) // 2, self.photo_rect.bottom + screen_height // 30,
                                     photo_width, screen_height // 20)
        self.correct_button = pygame.Rect((screen_width - photo_width) // 2,
                                          self.text_rect.bottom + screen_height // 30, button_width, button_height)
        self.incorrect_button = pygame.Rect((screen_width - button_width) // 2 + screen_width // 10 + 125,
                                            self.text_rect.bottom + screen_height // 30, button_width, button_height)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.correct_button.collidepoint(event.pos):
                        print("Нажата кнопка 'Верно'")
                    elif self.incorrect_button.collidepoint(event.pos):
                        print("Нажата кнопка 'Неверно'")

            self.screen.fill((255, 255, 255))

            pygame.draw.rect(self.screen, (200, 200, 200), self.photo_rect)
            pygame.draw.rect(self.screen, (200, 200, 200), self.text_rect)
            pygame.draw.rect(self.screen, (0, 255, 0), self.correct_button)
            pygame.draw.rect(self.screen, (255, 0, 0), self.incorrect_button)

            text = self.font.render('Текст под фото', True, (0, 0, 0))
            text_rect = text.get_rect(center=self.text_rect.center)
            self.screen.blit(text, text_rect)

            text = self.font.render('Верно', True, (0, 0, 0))
            button1_rect = text.get_rect(center=self.correct_button.center)
            self.screen.blit(text, button1_rect)

            text = self.font.render('Неверно', True, (0, 0, 0))
            button1_rect = text.get_rect(center=self.incorrect_button.center)
            self.screen.blit(text, button1_rect)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
