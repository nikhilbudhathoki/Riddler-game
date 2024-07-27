import pygame
import time
import random
from PIL import Image
import os

# Initialize Pygame
pygame.init()

# Initialize the mixer with error handling
def initialize_mixer():
    try:
        pygame.mixer.init()
        print("Pygame mixer initialized successfully.")
    except pygame.error as e:
        print(f"Error initializing mixer: {e}")

initialize_mixer()

# Set up the display for full-screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Riddle Slideshow")

# Load background images
def load_background_images():
    background_image_files = ["background1.png", "background2.jpg"]
    background_images = []

    for file in background_image_files:
        if not os.path.exists(file):
            print(f"Error: Background image file '{file}' not found.")
        else:
            image = pygame.image.load(file)
            image = pygame.transform.scale(image, (screen_width, screen_height))
            background_images.append(image)
            print(f"Background image '{file}' loaded successfully.")
    return background_images

background_images = load_background_images()

# Load and play background music
def load_and_play_music(music_file):
    if not os.path.exists(music_file):
        print(f"Error: Background music file '{music_file}' not found.")
        return False
    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("Background music loaded and playing.")
        return True
    except pygame.error as e:
        print(f"Error loading or playing music: {e}")
        return False

background_music_file = "bgg1.mp3"
music_loaded = load_and_play_music(background_music_file)

def load_gif_frames(gif_path):
    gif = Image.open(gif_path)
    frames = []
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = gif.copy()
        frame_image = frame_image.convert('RGBA')
        frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
        frames.append(pygame.transform.scale(frame_surface, (screen_width, screen_height)))
    return frames, gif.info['duration']

def display_gif_with_sound(gif_frames, frame_duration, music_path, background_image):
    try:
        effect_channel = pygame.mixer.Channel(1)
        effect_channel.set_volume(0.5)
        effect_channel.play(pygame.mixer.Sound(music_path))

        frame_index = 0
        while effect_channel.get_busy() and frame_index < len(gif_frames):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            screen.blit(background_image, (0, 0))
            screen.blit(gif_frames[frame_index], (0, 0))
            pygame.display.flip()
            pygame.time.delay(frame_duration)
            frame_index += 1

        while effect_channel.get_busy():
            pygame.time.wait(100)
    except pygame.error as e:
        print(f"Error playing music: {e}")

def fade_in(image, background_image):
    for alpha in range(0, 256, 5):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        image.set_alpha(alpha)
        screen.blit(background_image, (0, 0))
        screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)

def fade_out(background_image):
    for alpha in range(255, -1, -5):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        screen.fill((0, 0, 0))
        background_image.set_alpha(alpha)
        screen.blit(background_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)

def run_slideshow(images, music):
    background_image_index = 0
    for idx, (image_path, music_path) in enumerate(zip(images, music)):
        background_image = background_images[background_image_index]
        fade_out(background_image)

        screen.blit(background_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(random.randint(1000, 5000))

        if image_path.lower().endswith('.gif'):
            frames, duration = load_gif_frames(image_path)
            display_gif_with_sound(frames, duration, music_path, background_image)
        else:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (screen_width, screen_height))
            fade_in(image, background_image)

            try:
                effect_channel = pygame.mixer.Channel(1)
                effect_channel.set_volume(0.5)
                effect_channel.play(pygame.mixer.Sound(music_path))

                while effect_channel.get_busy():
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return False
                    pygame.time.wait(100)
            except pygame.error as e:
                print(f"Error playing music: {e}")

        if (idx + 1) % 4 == 0:
            background_image_index = (background_image_index + 1) % len(background_images)

def show_text(text, pos, font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def display_image_with_sound(image_path, music_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (screen_width, screen_height))
    background_image = background_images[0]
    fade_in(image, background_image)

    try:
        effect_channel = pygame.mixer.Channel(1)
        effect_channel.set_volume(0.5)
        effect_channel.play(pygame.mixer.Sound(music_path))

        while effect_channel.get_busy():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
            pygame.time.wait(100)
    except pygame.error as e:
        print(f"Error playing music: {e}")

def retry_button():
    font = pygame.font.Font(None, 36)
    button_color = (255, 0, 0)
    button_rect = pygame.Rect((screen_width // 2 - 50, screen_height // 2, 100, 50))
    pygame.draw.rect(screen, button_color, button_rect)
    show_text("Retry", (screen_width // 2 - 30, screen_height // 2 + 10), font)

    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False
                    return True
    return False

def collapsing_text(text, font, color, final_pos, speed=5):
    initial_pos = [final_pos[0], final_pos[1] - 50]
    while initial_pos[1] < final_pos[1]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        screen.fill((0, 0, 0))
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, initial_pos)
        pygame.display.flip()
        initial_pos[1] += speed
        pygame.time.delay(50)

def riddle_game():
    riddles = {
        "What has keys but can't open locks?": "piano",
        "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?": "echo",
        "The more you take, the more you leave behind. What am I?": "footsteps",
        "What has to be broken before you can use it?": "egg",
        "I’m tall when I’m young, and I’m short when I’m old. What am I?": "candle",
        "What month of the year has 28 days?": "all",
        "What is full of holes but still holds water?": "sponge",
        "What question can you never answer yes to?": "are you asleep",
        "What is always in front of you but can’t be seen?": "future",
        "There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?": "no stairs",
        "What can you break, even if you never pick it up or touch it?": "promise",
        "What goes up but never comes down?": "age",
        "A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?": "he was bald",
        "What gets wet while drying?": "towel",
        "What can you keep after giving to someone?": "your word",
        "I shave every day, but my beard stays the same. What am I?": "barber",
        "You see a boat filled with people, yet there isn’t a single person on board. How is that possible?": "all married",
        "You walk into a room that contains a match, a kerosene lamp, a candle, and a fireplace. What would you light first?": "match",
        "I have branches, but no fruit, trunk or leaves. What am I?": "bank",
        "What can’t talk but will reply when spoken to?": "echo"
    }
    font = pygame.font.Font(None, 36)
    riddle_keys = list(riddles.keys())
    random.shuffle(riddle_keys)
    correct_riddles = 0

    try:
        positive_sound = pygame.mixer.Sound("positive_sound.mp3")
        wrong_guess_sound = pygame.mixer.Sound("wrong_guess.mp3")
        game_over_sound = pygame.mixer.Sound("failed.mp3")
        victory_sound = pygame.mixer.Sound("you_won_music.mp3")
        new_victory_sound = pygame.mixer.Sound("new_victory_sound.wav")
    except pygame.error as e:
        print(f"Error loading sound effects: {e}")
        positive_sound = None
        wrong_guess_sound = None
        game_over_sound = None
        victory_sound = None
        new_victory_sound = None

    while correct_riddles < 3 and riddle_keys:
        choice = riddle_keys.pop()
        answer = riddles[choice]
        display = ['_' for _ in answer]
        lives = 6
        game_over = False
        start_time = time.time()

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            screen.fill((0, 0, 0))
            show_text("Riddle Time!", (screen_width // 2 - 100, 50), font)
            show_text(choice, (50, 150), font)
            show_text(" ".join(display), (50, 250), font)
            show_text(f"Lives: {lives}", (50, 350), font)
            elapsed_time = time.time() - start_time
            remaining_time = int(120 - elapsed_time)
            show_text(f"Time left: {remaining_time} sec", (50, 400), font)
            pygame.display.flip()

            if remaining_time <= 0:
                game_over = True
                show_text("Time's up!", (screen_width // 2 - 50, 450), font, (255, 0, 0))
                pygame.display.flip()
                time.sleep(3)
                display_image_with_sound("game_over.jpg", "game_over.wav")
                pygame.mixer.music.stop()
                return retry_button()

            guess = None
            input_active = True
            while input_active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            guess = ''
                        else:
                            guess = event.unicode.lower()
                            input_active = False

                elapsed_time = time.time() - start_time
                remaining_time = int(120 - elapsed_time)
                screen.fill((0, 0, 0))
                show_text("Riddle Time!", (screen_width // 2 - 100, 50), font)
                show_text(choice, (50, 150), font)
                show_text(" ".join(display), (50, 250), font)
                show_text(f"Lives: {lives}", (50, 350), font)
                show_text(f"Time left: {remaining_time} sec", (50, 400), font)
                pygame.display.flip()

                if remaining_time <= 0:
                    game_over = True
                    show_text("Time's up!", (screen_width // 2 - 50, 450), font, (255, 0, 0))
                    pygame.display.flip()
                    time.sleep(3)
                    display_image_with_sound("game_over.jpg", "game_over.wav")
                    pygame.mixer.music.stop()
                    return retry_button()

            if guess:
                if guess in answer:
                    if positive_sound:
                        positive_sound.play()
                    for position in range(len(answer)):
                        if guess == answer[position]:
                            display[position] = guess
                else:
                    lives -= 1
                    if wrong_guess_sound and lives > 0:
                        wrong_guess_sound.play()
                    if lives == 0:
                        game_over = True
                        if game_over_sound:
                            pygame.mixer.stop()
                            game_over_sound.play()
                        show_text("You lose! The answer was: " + answer, (50, 450), font, (255, 0, 0))
                        pygame.display.flip()
                        time.sleep(3)
                        display_image_with_sound("game_over.jpg", "game_over.wav")
                        pygame.mixer.music.stop()
                        return retry_button()

                if '_' not in display:
                    game_over = True
                    correct_riddles += 1
                    show_text("Correct!", (screen_width // 2 - 50, 450), font, (0, 255, 0))
                    pygame.display.flip()
                    if positive_sound:
                        positive_sound.play()
                    time.sleep(3)

    if correct_riddles == 3:
        show_text("You won!", (screen_width // 2 - 50, 200), font, (0, 100, 0))
        pygame.display.flip()
        if new_victory_sound:
            pygame.mixer.stop()
            new_victory_sound.play()
        time.sleep(3)
        display_image_with_sound("you_won.gif", "you_won_music.mp3")
        pygame.mixer.music.stop()
        collapsing_text("You Win!", font, (255, 255, 255), (screen_width // 2 - 50, 450))
        pygame.quit()
        return False

    return True

# List of images and music tracks
images = ["ridd_sit.jpg", "riddler_car1.jpg", 'i3.jpg', 'i4.jpg', 'i5.jpg', 'i6.jpg', 'i7.jpg', 'i8.gif', 'i9.gif', 'i10.gif', 'i11.gif', 'i12.jpg', 'i13.jpg', 'i14.jpg', 'i15.png', 'i16.jpg']
music = ["bat-brain-riddle.mp3", "m2.mp3", 'm3.wav', 'm4.wav', 'm5.mp3', 'm6.mp3', 'M7.mp3', 'm8.mp3', 'm9.wav', 'm10.wav', 'm11.mp3', 'm12.wav', 'm13.mp3', 'm14.wav', 'm15.wav', 'm16.wav']

# Run the slideshow
run_slideshow(images, music)

# Start the riddle game
while True:
    if not riddle_game():
        break

# Quit Pygame
pygame.quit()
