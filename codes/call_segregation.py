#pip 3 install pydub
!pip install pydub
from pydub import AudioSegment

sound=AudioSegment.from_wav("/content/A1.wav")  # Name of audio file
AudioSegment.convertor="ffmpaeg.exe"
AudioSegment.ffmpeg="ffmpaeg.exe"
AudioSegment.ffprobe="ffprobe.exe"

EndMin=0
EndSec=0
EndMSec=10

StartTime=StartMin*60+StartSec*1000+StartMSec
EndTime=EndMin*60+EndSec*1000+EndMSec

extract=sound[StartTime:EndTime]
extract.export("A1_new2.wav",format="wav")
