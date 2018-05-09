import win32gui
import time


def main():
    print("Finding Spotify Window. Please click open Spotify.")
    time.sleep(10)
    window = win32gui.GetForegroundWindow()
    current_song = win32gui.GetWindowText(window)
    print("Currently Playing:", current_song)
    while True:
        # ugly but works for now.
        maybe_new_song = win32gui.GetWindowText(window)
        if maybe_new_song.lower() == current_song.lower():  # ignore
            pass
        else:
            current_song = maybe_new_song
            print("\nCurrently Playing:", current_song)


if __name__ == '__main__':
    main()
