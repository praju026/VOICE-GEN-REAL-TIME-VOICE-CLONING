# 🎙️ Real-Time Voice Cloning

This is an implementation of the paper [Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis](https://arxiv.org/pdf/1806.04558.pdf), allowing for real-time voice cloning using three models: speaker encoder, synthesizer, and vocoder.

Originally created as a [Master’s thesis](https://matheo.uliege.be/handle/2268.2/6801).

[![Demo](https://i.imgur.com/8lFUlgz.png)](https://www.youtube.com/watch?v=-O_hYhToKoA)

---

## 🧠 Pipeline Overview

1. **Speaker Encoder**: Converts a short voice clip into a fixed-size embedding.
2. **Synthesizer (Tacotron)**: Uses the embedding and text to generate a mel spectrogram.
3. **Vocoder (WaveRNN)**: Converts the mel spectrogram into raw audio.

-

## 📄 Papers Implemented

| Paper | Model | Title | Source |
|-------|-------|-------|--------|
| [1806.04558](https://arxiv.org/pdf/1806.04558.pdf) | SV2TTS | Transfer Learning from Speaker Verification... | This repo |
| [1802.08435](https://arxiv.org/pdf/1802.08435.pdf) | WaveRNN | Efficient Neural Audio Synthesis | [fatchord/WaveRNN](https://github.com/fatchord/WaveRNN) |
| [1703.10135](https://arxiv.org/pdf/1703.10135.pdf) | Tacotron | End-to-End Speech Synthesis | Same as above |
| [1710.10467](https://arxiv.org/pdf/1710.10467.pdf) | GE2E | Speaker Verification | This repo |

---

## ⚠️ Important Notes

- This repo is educational and experimental.
- It works well, but the audio quality is behind modern models.
- For higher quality: check [Coqui TTS](https://github.com/coqui-ai/TTS) or [MetaVoice-1B](https://github.com/metavoiceio/metavoice-src).

---

## 🛠️ Setup Instructions

### ✅ Requirements

- OS: Windows or Linux
- Python: 3.7 recommended
- Tools: `ffmpeg`, `git`
- GPU: Recommended for training/inference speed

### 📦 Install Dependencies

```bash
git clone https://github.com/CorentinJ/Real-Time-Voice-Cloning.git
cd Real-Time-Voice-Cloning

# Optional: create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv/Scripts/activate

# Install PyTorch from https://pytorch.org
# Then install other dependencies
pip install -r requirements.txt


### 5. Launch the Toolbox
You can then try the toolbox:

`python demo_toolbox.py -d <datasets_root>`  
or  
`python demo_toolbox.py`  

depending on whether you downloaded any datasets. If you are running an X-server or if you have the error `Aborted (core dumped)`, see [this issue](https://github.com/CorentinJ/Real-Time-Voice-Cloning/issues/11#issuecomment-504733590).

###password
   check users.json file


   📥 Pretrained Models
Pretrained models download automatically. If they don’t:

Manually download from(also check this repo for original model):
https://github.com/CorentinJ/Real-Time-Voice-Cloning/wiki/Pretrained-models

Place files in: encoder/, synthesizer/, and vocoder/ folders respectively.



🙏 Credits
Original repo by Corentin Jemine

Research from Google AI, DeepMind, Baidu, and others
