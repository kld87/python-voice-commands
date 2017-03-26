## Info

PoC Python script that uses SpeechRecognition, CMU Sphinx, and https://wit.ai to listen for a trigger keyword, parse speech, and run a command based on the result.

## Usage

Create wit_key.txt containing your API key and run the script. The default trigger word is "computer". Probably only works in Linux.

## Commands

*"netflix": open google-chrome to Netflix
*"terminate": exits the script

## Sources

*https://pypi.python.org/pypi/SpeechRecognition/
*https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
*https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py 
*https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-sphinx-on-ubuntu-14-04