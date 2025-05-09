import sounddevice as sd
from scipy.io.wavfile import write

SAMPLING_RATE = 44100  # Hz
DURATION = 5  # Record for 5 seconds

print("Recording...")
audio = sd.rec(int(SAMPLING_RATE * DURATION), samplerate=SAMPLING_RATE, channels=1, dtype='float32')
sd.wait()  # Wait until the recording is finished
print("Recording complete.")

# Save the recorded audio to a file for analysis
write("test_recording.wav", SAMPLING_RATE, audio)
print("Audio saved to 'test_recording.wav'.")
