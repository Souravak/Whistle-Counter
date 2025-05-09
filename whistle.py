import sounddevice as sd
import numpy as np
from scipy.signal import find_peaks
from playsound import playsound


SAMPLING_RATE = 44100 
DURATION = 10 
THRESHOLD = 0.1
ALERT_FILE = "alert.mp3"

def detect_whistles(audio, samplerate):
    """Detects whistle-like peaks in the audio data."""
    energy = np.abs(audio)
    
    peaks, _ = find_peaks(energy, height=THRESHOLD, distance=samplerate // 2)
    return len(peaks)

def main():
    print("Pressure Cooker Whistle Counter")
    
    try:
        target_whistles = int(input("Enter the number of whistles to count: "))
        if target_whistles <= 0:
            print("Please enter a positive number!")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return
    
    whistle_count = 0
    
    try:
        while whistle_count < target_whistles:
            print("Listening for whistles...")
            audio = sd.rec(int(SAMPLING_RATE * DURATION), samplerate=SAMPLING_RATE, channels=1, dtype='float32')
            sd.wait()
            
            audio = audio.flatten()
            
            whistles = detect_whistles(audio, SAMPLING_RATE)
            whistle_count += whistles
            print(f"Whistles detected in this session: {whistles}")
            print(f"Total whistles so far: {whistle_count}/{target_whistles}")
        
        print(f"Target of {target_whistles} whistles reached! Playing alert...")
        playsound(ALERT_FILE)
    
    except KeyboardInterrupt:
        print("\nWhistle counter stopped by user.")
        print(f"Final whistle count: {whistle_count}")

if __name__ == "__main__":
    main()
