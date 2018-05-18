import win32gui
import time
import pygame

pygame.init()

game_x = 800
game_y = 600

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
game_display = pygame.display.set_mode((game_x, game_y))
clock = pygame.time.Clock()
game_display.fill(white)


font = pygame.font.SysFont("comicsansms", 36)

class stream_bot:
    def __init__(self):
        # gather foreground window.
        self.window = None
        self.current_song = None
        self.initailize_spotify()
        pygame.display.update()
        # main loop
        self.visualize()

    def initailize_spotify(self):
        #
        print("please open Spotify")
        text = font.render("Please Open Spotify For Bot Initialization", True, (0, 128, 0))

        game_display.blit(text, (0, 0))
        time.sleep(5)
        self.window = win32gui.GetForegroundWindow()
        self.current_song = win32gui.GetWindowText(self.window)

        text = font.render("Currently Playing: " + self.current_song, True, (0, 128, 0))
        game_display.blit(text, (320 - text.get_width() // 2, 12 - text.get_height() // 2))

    def get_song(self):
        self.current_song = win32gui.GetWindowText(self.window)

    def visualize(self):
        exit_game = False

        while not exit_game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
            if self.get_song().lower() != self.current_song.lower():  # if there is a new song

                game_display.blit(self.current_song,(300,300))

            pygame.display.update()
            clock.tick(30)

    # print("Finding Spotify Window. Please click open Spotify.")
    #
    # time.sleep(10)
    # window = win32gui.GetForegroundWindow()
    # current_song = win32gui.GetWindowText(window)
    # print("Currently Playing:", current_song)
    # while True:
    #     # ugly but works for now.
    #     maybe_new_song = win32gui.GetWindowText(window)
    #     if maybe_new_song.lower() == current_song.lower():  # ignore
    #         pass
    #     else:
    #         current_song = maybe_new_song
    #         # clear stdout
    #         print("\nCurrently Playing:", current_song)


if __name__ == '__main__':
    stream_bot()
