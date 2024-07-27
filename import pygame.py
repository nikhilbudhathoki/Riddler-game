import tkinter as tk
import pygame
import time
from PIL import Image, ImageTk

# Define image and music paths (replace with your actual paths)
image_paths = ["ridd_sit.jpg", "riddler_car1.jpg"]
music_paths = ["bat-brain-riddle.mp3","bat-brain-riddle.mp3"]


class ImageSoundTransition:
    def __init__(self, root, canvas, image_paths, music_paths, delay, fade_duration=0.5):  # Optional fade duration
        self.root = root
        self.canvas = canvas
        self.images = [ImageTk.PhotoImage(Image.open(path).resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.BICUBIC)) for path in image_paths]
        self.musics = [pygame.mixer.Sound(path) for path in music_paths]
        self.delay = delay
        self.current_index = 0
        self.fade_duration = fade_duration  # Duration (in seconds) for fading effects

        # Initialize Pygame mixer (within the class for proper cleanup)
        pygame.mixer.init()

    def start(self):
        self.display_image_with_sound()

    def display_image_with_sound(self):
        # Display image with fading effect
        self.fade_image(self.images[self.current_index], self.fade_duration)
        self.canvas.create_image(0, 0, image=self.images[self.current_index], anchor=tk.NW)

        # Play music with fading effect
        self.fade_music(self.musics[self.current_index], self.fade_duration)
        self.musics[self.current_index].play(-1, 0.0)  # Play music in a loop with fade-in

        # Wait for music or delay
        self.root.after(int(self.delay * 1000), self.next_transition)  # Schedule next transition after delay in milliseconds

    def next_transition(self):
        # Stop music
        self.musics[self.current_index].fadeout(int(self.fade_duration * 1000))  # Fade out music before stopping

        # Update index and loop
        self.current_index = (self.current_index + 1) % len(self.images)
        self.display_image_with_sound()

    def fade_image(self, image, duration):
        # Implement your preferred image fading logic here (using PIL or other libraries)
        # This code snippet demonstrates a basic approach using alpha manipulation:
        step =
