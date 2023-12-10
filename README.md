# David Attenborough narrates your Rocket League gameplay, or your life. 

## Credit: 
Charlie Holtz \
Source: https://github.com/cbh123/narrator \
Twitter: https://twitter.com/charliebholtz/status/1724815159590293764

## Setup

For this project to work, you need some $$$ in your [OpenAI account](https://platform.openai.com/account/billing/overview) (minimum deposit of $5) so that you can use API calls. This also requires an ElevenLabs "Starter" [subscription](https://elevenlabs.io/subscription) ($5/month, but it's $1 for the first month).


Clone this repo, and setup and activate a virtualenv:

```bash
pip install virtualenv
virtualenv venv
venv/bin/activate
```

Then, install the dependencies:
`pip install -r requirements.txt`

Create an account for [OpenAI](https://beta.openai.com/) and [ElevenLabs](https://elevenlabs.io).

Create and paste your [OpenAI API Key](https://platform.openai.com/api-keys) and ElevenLabs API Key in ***API_KEYS.txt***. To find your ElevenLabs API Key, click on your profile icon in the top right of the page, then click on **Profile**.
``` 
OPENAI_API_KEY={OpenAI API Key Here}
ELEVENLABS_API_KEY={ElevenLabs API Key Here}
```

Navigate to the [ElevenLabs VoiceLab](https://elevenlabs.io/voice-lab) and select **Add Generative or Cloned Voice-->Instant Voice Cloning** and upload ***David_Attenborough.mp3***. Add a Name and Description and finally click **Add Voice**. \
You should now have a new box with the created voice on your VoiceLab page. Hover over **ID** in the top right of the new voice box to see the Voice ID. You can click on **ID** to copy the voice ID to your clipboard.




## Run it!

In on terminal, run the webcam capture:
```bash
python capture.py
```
In another terminal, run the narrator:

```bash
python narrator.py
```

