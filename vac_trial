#pip install sounddevice numpy

import sounddevice as sd
import numpy as np
import wavio

# Parameters
RATE = 44100    # samples per second
CHANNELS = 2
DTYPE = np.int16
SECONDS = 5      # length of recording
FILENAME = "output.wav"  # name of output file

# Initialize array to hold audio
audio_data = np.zeros((RATE * SECONDS, CHANNELS), dtype=DTYPE)

# Record audio
print("Recording...")
sd.rec(audio_data, samplerate=RATE, channels=CHANNELS)
sd.wait()  # Wait for the recording to finish

# Save the audio to a WAV file
print("Saving to file...")
wavio.write(FILENAME, audio_data, RATE, sampwidth=2)

print(f"Audio saved as {FILENAME}")
