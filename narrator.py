import os
from openai import OpenAI
import base64
import json
import time
import random
import simpleaudio as sa
import errno
import cv2
import pygetwindow as gw
import threading
from elevenlabs import generate, play, voices, set_api_key
from scripts import Screenshot, Photo


###################################
##             Setup             ##
###################################

# Select from two modes: "webcam" and "RocketLeague"
mode = "webcam"

#-----------------------#

playback_thread = None

# Read in User's API Keys
with open("API_KEYS.txt", 'r') as f:
    OpenAI_Key, ElevenLabs_Key = [line.split('=')[1].strip() for line in f]

# Set ElevenLabs and OpenAI API Keys
set_api_key(ElevenLabs_Key)
os.environ["OPENAI_API_KEY"] = OpenAI_Key

client = OpenAI()

# Folder Names
soundFolder = "soundFiles"
frameFolder = "frames"

# Create the folders if they don't exist
for folder in [soundFolder, frameFolder]:
    os.makedirs(os.path.join(os.getcwd(), folder), exist_ok=True)



##################################
##     Function Definitions     ##
##################################

def encode_image(image_path):
    while True:
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except IOError as e:
            if e.errno != errno.EACCES:
                # Not a "file in use" error, re-raise
                raise
            # File is being written to, wait a bit and retry
            time.sleep(0.1)


def play_audio(text):
    audio = generate(text=text, voice="{Insert Voice ID}", model="eleven_turbo_v2")
    
    file_path = f"{soundFolder}/narration.wav"

    with open(file_path, "wb") as f:
        f.write(audio)
        
    global playback_thread  
      
    # Check if the previous thread is still running
    if playback_thread and playback_thread.is_alive():
        playback_thread.join()  # Wait for the previous thread to finish before starting a new one
        time.sleep(random.uniform(1, 4))
    
    playback_thread = threading.Thread(target=play, args=(audio,))
    playback_thread.start()
    
    time.sleep(12)


def generate_new_line(base64_image):
    return [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image"},
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        },
    ]


def analyze_Photo(base64_image, script):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": """
                You are Sir David Attenborough. Narrate the picture of the human as if it is a nature documentary.
                Make it snarky and funny. Don't repeat yourself. Limit to two sentences. If I do anything remotely interesting, make a big deal about it!
                """,
            },
        ]
        + script
        + generate_new_line(base64_image),
        max_tokens=600,
    )
    response_text = response.choices[0].message.content
    return response_text

def analyze_Screenshot(base64_image, script):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": """
                You are Sir David Attenborough. Narrate the picture of the rocket league game as if you were a sports commentator, only focusing on what the car is doing.
                Do not mention that it is an image or a screenshot. Limit description to two sentences. Don't repeat yourself. If I do anything remotely interesting, make a big deal about it!
                """,
            },
        ]
        + script
        + generate_new_line(base64_image),
        max_tokens=600,
    )
    response_text = response.choices[0].message.content
    return response_text


def main():
    script = []
    
    if mode.casefold() == "webcam":
        # Initialize the webcam
        cap = cv2.VideoCapture(0)
        
        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
        
    while True:
        
        if mode.casefold() == "webcam":
            Photo(cap, frameFolder)
        elif mode.casefold() == "rocketleague":
             # Get the active window
            active_window = gw.getActiveWindow()

            #Check if Rocket League is running
            if active_window and "Rocket League" in active_window.title:
                Screenshot(frameFolder, active_window)
            else:
                time.sleep(5)
                continue  
        else:
            print("Invalid mode! Please enter \"webcam\" or \"RocketLeague\"")
            exit()
        
        
        
        # path to your image
        image_path = os.path.join(os.getcwd(), f"./{frameFolder}/frame.jpg")

        # getting the base64 encoding
        base64_image = encode_image(image_path)

        if mode.casefold() == "webcam":
            analysis = analyze_Photo(base64_image, script=script)
        elif mode.casefold() == "rocketleague":
            analysis = analyze_Screenshot(base64_image, script=script)
        
        #analysis = "In the concrete savannah, our speedy protagonist, the cheetah, effortlessly overtakes the unsuspecting human lion, proving that in this peculiar ecosystem, the hunter becomes the hunted – a delightful twist in the urban food chain."

        play_audio(analysis)

        script = script + [{"role": "assistant", "content": analysis}]


if __name__ == "__main__":
    main()
