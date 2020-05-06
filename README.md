# speech2text
A demo of speech to text by google

[![asciicast](https://asciinema.org/a/327399.svg)](https://asciinema.org/a/327399)

## Python Packages
- [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/)
- [SpeechRecognition](https://github.com/Uberi/speech_recognition#readme)
- [fleep](https://github.com/floyernick/fleep-py)
- [arabic-reshaper](https://github.com/mpcabd/python-arabic-reshaper)
- [python-bidi](https://github.com/MeirKriheli/python-bidi)

## Installation:
``` bash
pip install -r requirements.txt
```

## Usage
- Audio file:
``` bash
python speech2text.py --type=audio --source=harvard.wav --language=en-US
```

- Microphone:
``` bash
python speech2text.py --type=mic --language=fa-IR
```

## Supported versions/Pre-requisites.

| Python        |
| -------------:|
| 3.6           |
| 3.7           |
| 3.8           |

## License

Copyright (C) 2020, [Hooshvare Team](https://hooshvare.com/)
Licensed under the MIT license, see LICENSE file for details.
