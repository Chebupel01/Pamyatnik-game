import pygame
import sys

pygame.init()

# Устанавливаем размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создаем окно игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Устанавливаем заголовок окна
pygame.display.set_caption("Памятник")

# Создаем шрифт для текста
font = pygame.font.SysFont("Arial", 32)

# Создаем кнопку "Далее"
button_width = 200
button_height = 50
button_x = SCREEN_WIDTH // 2 - button_width // 2
button_y = SCREEN_HEIGHT // 2 - button_height // 2
button_color = (0, 255, 0)
button_text = "Играть"

# Основной цикл игры
while True:
    # Обрабатываем события
    for event in pygame.event.get():
        # Если пользователь закрыл окно, выходим из игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Если пользователь нажал кнопку мыши, проверяем, попал ли он в кнопку "Далее"
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                # Если пользователь попал в кнопку, переходим на следующий уровень
                print("Переход на следующий уровень")
                pygame.quit()
                sys.exit()

    # Заполняем экран белым цветом
    screen.fill((255, 255, 255))

    # Отрисовываем приветствие
    welcome_text = font.render("Добро пожаловать в игру Памятник!", True, (0, 0, 0))
    screen.blit(welcome_text, (SCREEN_WIDTH // 2 - welcome_text.get_width() // 2, 100))

    # Отрисовываем кнопку "Далее"
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    button_text_surface = font.render(button_text, True, (0, 0, 0))
    screen.blit(button_text_surface, (button_x + button_width // 2 - button_text_surface.get_width() // 2, button_y + button_height // 2 - button_text_surface.get_height() // 2))

    # Обновляем экран
    pygame.display.update()