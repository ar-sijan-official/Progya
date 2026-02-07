import os
import time
import wave
import pyaudio
import numpy as np
import noisereduce as nr
from pydub import AudioSegment
from datetime import datetime
import sys
try:
    import audioop
except ImportError:
    import audioop_lts as audioop
    sys.modules["audioop"] = audioop

# Now your other imports will work
import os
import time
# ... rest of your code

# --- CONFIGURATION ---
DURATION_SEC = 0.5 * 60  # 5 Minutes
BREAK_SEC = 5          # 5 Seconds
OUTPUT_FOLDER = "mp3_recordings"
CHANNELS = 1
RATE = 44100
CHUNK = 1024

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def record_chunk(duration, filename):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=CHANNELS, 
                    rate=RATE, input=True, frames_per_buffer=CHUNK)

    print(f"[*] Recording: {filename}...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("[+] Done.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Convert buffer to numpy array for noise reduction
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
    
    # Noise Reduction (Spectral Gating)
    # This automatically estimates the noise floor from the signal
    reduced_noise = nr.reduce_noise(y=audio_data, sr=RATE, prop_decrease=0.8)

    # Save as temporary WAV (pydub needs a file or specific format to export to MP3)
    temp_wav = "temp_voice.wav"
    with wave.open(temp_wav, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(RATE)
        wf.writeframes(reduced_noise.tobytes())

    # Convert WAV to MP3
    audio_seg = AudioSegment.from_wav(temp_wav)
    audio_seg.export(os.path.join(OUTPUT_FOLDER, filename), format="mp3")
    
    # Cleanup temp file
    os.remove(temp_wav)

def main():
    print("AI Classroom Recorder Started. Press Ctrl+C to stop.")
    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"lecture_{timestamp}.mp3"
            
            record_chunk(DURATION_SEC, filename)
            
            print(f"--- Resting for {BREAK_SEC} seconds ---")
            time.sleep(BREAK_SEC)
    except KeyboardInterrupt:
        print("\n[!] Recorder stopped by user.")

if __name__ == "__main__":
    main()