import pygame
import sys

pygame.init()

# Устанавливаем размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создаем окно игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Устанавливаем заголовок окна
pygame.display.set_caption("Моя первая игра")

# Создаем шрифт для текста
font = pygame.font.SysFont("Arial", 32)

# Создаем кнопки уровней
button_width = 200
button_height = 50
button_x = SCREEN_WIDTH // 2 - button_width // 2
button_y = SCREEN_HEIGHT // 2 - button_height // 2
button_color = (0, 255, 0)
button_text = ["Уровень 1", "Уровень 2", "Уровень 3"]

# Текущий уровень
current_level = 0

# Основной цикл игры
while True:
    # Обрабатываем события
    for event in pygame.event.get():
        # Если пользователь закрыл окно, выходим из игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Если пользователь нажал кнопку мыши, проверяем, попал ли он в кнопку уровня
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    current_level += 1
                    print(f"Переход на уровень {current_level}")

    # Заполняем экран белым цветом
    screen.fill((255, 255, 255))

    # Отрисовываем кнопки уровней
    for i in range(3):
        if i <= current_level:
            button_color = (0, 255, 0)
        else:
            button_color = (128, 128, 128)
        pygame.draw.rect(screen, button_color, (button_x, button_y + i * (button_height + 20), button_width, button_height))
        button_text_surface = font.render(button_text[i], True, (0, 0, 0))
        screen.blit(button_text_surface, (button_x + button_width // 2 - button_text_surface.get_width() // 2, button_y + i * (button_height + 20) + button_height // 2 - button_text_surface.get_height() // 2))

    # Обновляем экран
    pygame.display.update()

# Выходим из игры
pygame.quit()
sys.exit()