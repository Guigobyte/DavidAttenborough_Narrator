# David Attenborough narrates your Rocket League gameplay, or your life. 

## Credit: 
Charlie Holtz \
Source: https://github.com/cbh123/narrator \
Twitter: https://twitter.com/charliebholtz/status/1724815159590293764

## AI Account Setup

For this project to work, you need some $$$ in your [OpenAI account](https://platform.openai.com/account/billing/overview) (minimum deposit of $5) so that you can use API calls. This also requires an ElevenLabs [Starter Subscription](https://elevenlabs.io/subscription) ($5/month, but it's $1 for the first month).


Create an account for [OpenAI](https://beta.openai.com/) and [ElevenLabs](https://elevenlabs.io).

Create and paste your [OpenAI API Key](https://platform.openai.com/api-keys) and ElevenLabs API Key in ***API_KEYS.txt***. To find your ElevenLabs API Key, click on your profile icon in the top right of the page, then click on **Profile**.
``` 
OPENAI_API_KEY={OpenAI API Key Here}
ELEVENLABS_API_KEY={ElevenLabs API Key Here}
```

### -- Voice Setup --

- Navigate to [ElevenLabs VoiceLab](https://elevenlabs.io/voice-lab) and select **Add Generative or Cloned Voice --> Instant Voice Cloning**
- Upload ***David_Attenborough.mp3***.
- Add a Name and Description and click **Add Voice**.

You should now have a new box with the created voice on your VoiceLab page. 
- Hover over **ID** in the top right of the new voice box to see the Voice ID. You can click on **ID** to copy the voice ID to your clipboard (save this ID for the next section).



## Code Setup

Clone this repo, and setup and activate a virtualenv through a terminal with the following commands:

```
pip install virtualenv
virtualenv venv
venv/bin/activate
```


Install the dependencies:
`pip install -r requirements.txt` 

Download [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). This is needed to properly install the 'simpleaudio' dependency.

**Open *narrator.py***
- *Line 65*: Replace **`{Insert Voice ID}`** (Line 65) with your newly created Voice ID.
- *Line 21*: Select one of two options:
  - `mode = "webcam"` or `mode = "RocketLeague"`
    - `"webcam"` mode will use your webcam to narrate what you look like / what you are doing.\
    - `"RocketLeague"` mode will narrate your Rocket League window **only if you have Rocket League as the active window**.


Lastly, download [ffmpeg](https://www.ffmpeg.org/download.html).
- For Windows users, download **ffmpeg-git-full.7z** from https://www.gyan.dev/ffmpeg/builds/.
- Extract the .zip (.7z) file to some location on your PC {yourpath}.
- Add *{yourpath}\ffmpeg\bin* to your [System PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/). 



## Run it!

Open a **new terminal**[^1] and navigate to the folder with ***narrator.py*** and execute the following:
```
py narrator.py
```

[^1]: A new terminal is required to update the system PATH variable. Running ***narrator.py*** in an already active terminal may not work.
