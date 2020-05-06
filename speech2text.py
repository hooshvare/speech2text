from __future__ import print_function
import argparse
import os
import fleep
import arabic_reshaper
from bidi.algorithm import get_display

from src.mic import MicrophoneReader
from src.audio import AudioReader


def main():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-T",
        "--type",
        choices=['mic', 'audio'],
        help="Choose the type of source for speech recognition `mic or audio`"
    )
    parser.add_argument(
        "-S",
        "--source",
        help="Choose the source of audio file (.wav)"
    )

    parser.add_argument(
        "-L",
        "--language",
        default='fa-IR',
        choices=['fa-IR', 'en-US'],
        help="Choose your language"
    )

    parser.add_argument(
        "-RTL",
        "--safe_rtl",
        default=False,
        help="Safe RTL format."
    )

    args = parser.parse_args()

    if args.type == 'audio':
        if not args.source:
            parser.error(
                'The source file must be specified! (use --source=YOUR_AUDIO_PATH or -S YOUR_AUDIO_PATH)')
        elif not os.path.exists(args.source):
            parser.error('Your audio file does not exist!')
        else:
            with open(args.source, 'rb') as af:
                audio = fleep.get(af.read(128))

            if not audio.extension_matches('wav'):
                parser.error('Your audio file does not correct format (.wav)!')

    if args.type == 'mic':
        reader = MicrophoneReader(
            language=args.language, verbose=True, safe_rtl=args.safe_rtl)
    elif args.type == 'audio':
        reader = AudioReader(
            language=args.language, audio_file=args.source, verbose=True, safe_rtl=args.safe_rtl)
    else:
        reader = None

    if reader:
        status, text = reader.read()
        if status:

            if args.safe_rtl:
                text = get_display(arabic_reshaper.reshape(text))

            print(text)
