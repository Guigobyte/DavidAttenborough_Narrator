# David Attenborough narrates your Rocket League gameplay, or your life. 

## Credit: 
Charlie Holtz
Source: https://github.com/cbh123/narrator
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

```
Create and paste your OpenAI and ElevenLabs API keys in API_KEYS.txt, 
OPENAI_API_KEY={OpenAI API Key Here}
ELEVENLABS_API_KEY={ElevenLabs API Key Here}
```


Make a new voice in Eleven and get the voice id of that voice using their [get voices](https://elevenlabs.io/docs/api-reference/voices) API, or by clicking the flask icon next to the voice in the VoiceLab tab.

```
export ELEVENLABS_VOICE_ID=<voice-id>
```

## Run it!

In on terminal, run the webcam capture:
```bash
python capture.py
```
In another terminal, run the narrator:

```bash
python narrator.py
```

