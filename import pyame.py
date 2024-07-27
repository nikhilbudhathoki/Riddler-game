import pygame
import time
from PIL import Image

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

def load_gif_frames(gif_path):
    gif = Image.open(gif_path)
    frames = []
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = gif.copy()
        frame_image = frame_image.convert('RGBA')
        frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
        frames.append(pygame.transform.scale(frame_surface, (screen_width, screen_height)))
    return frames

def display_gif_with_sound(gif_frames, music_path):
    # Load and play the music
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()

    start_time = time.time()
    frame_index = 0
    while frame_index < len(gif_frames):
        screen.blit(gif_frames[frame_index], (0, 0))
        pygame.display.flip()
        frame_index += 1
        if frame_index == 1:  # Play sound only once for the first frame
            pygame.mixer.music.play()
        pygame.time.delay(100)  # Adjust this delay to control the frame rate of the GIF

    # Wait for the music to finish
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

def run_slideshow(images, music):
    for image_path, music_path in zip(images, music):
        # Load the image or GIF frames
        if image_path.lower().endswith('.gif'):
            frames = load_gif_frames(image_path)
            display_gif_with_sound(frames, music_path)
        else:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (screen_width, screen_height))
            screen.blit(image, (0, 0))
            pygame.display.flip()

            # Load and play the music
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()

            # Wait for the music to finish
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)

# List of images and music tracks
images = ["ridd_sit.jpg", "riddler_car1.jpg", 'i3.jpg', 'i4.jpg', 'i5.jpg', 'i6.jpg', 'i7.jpg', 'i8.gif', 'i9.gif', 'i10.gif', 'i11.gif','i12.jpg','i13.jpg', 'i14.jpg', 'i15.png','i16.jpg']
music = ["bat-brain-riddle.mp3", "m2.mp3", 'm3.wav', 'm4.mp3', 'm5.mp3', 'm6.mp3', 'M7.mp3', 'm8.mp3', 'm9.wav', 'm10.wav', 'm11.mp3','m12.wav','m13.mp3', 'm14.wav', 'm15.wav', 'm16.wav']

# Run the slideshow
run_slideshow(images, music)

# Quit Pygame
pygame.quit()
