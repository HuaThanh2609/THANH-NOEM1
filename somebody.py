from pydub import AudioSegment
from pydub.playback import play

# Load the audio file
audio = AudioSegment.from_file("")

# Define lyrics with approximate time in milliseconds
lyrics = [
    (0, "First line of the song"),
    (10000, "Second line of the song"),
    (20000, "Third line of the song")
]

# Play the audio and print lyrics at the right time
for time, line in lyrics:
    play(audio[time:time+1000])  # Adjust the timing accordingly
    print(line)
