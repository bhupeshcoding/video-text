    # python3 -m venv path/to/venv
    # source path/to/venv/bin/activate
    # python3 -m pip install xyz


    # pip install vosk moviepy soundfile
# Download a Vosk model (e.g., small en): https://alphacephei.com/vosk/models
from vosk import Model, KaldiRecognizer
import json, wave

def transcribe_vosk(wav_path: str, vosk_model_dir: str):
    wf = wave.open(wav_path, "rb")
    model = Model(vosk_model_dir)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0: break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    results.append(json.loads(rec.FinalResult()))
    # Combine text + word timestamps
    text = " ".join(r.get("text","") for r in results).strip()
    return text, results
