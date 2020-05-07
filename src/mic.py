import speech_recognition as sr
from src.reader import Reader


class MicrophoneReader(Reader):
    """A class based on the speech recognition package to listen to audio continuously via microphone inputs."""

    RECORD = {
        "en-US": "Say something!",
        "fa-IR": "چیزی بگو!"
    }

    def __init__(self, *args, **kwargs):
        super(MicrophoneReader, self).__init__(*args, **kwargs)

    def read(self):
        self.adjust_amb_noise(self.language)
        audio = self.record(self.language)
        return self.recognize_google(audio, self.language)

    def adjust_amb_noise(self, language):
        self._print(self.ADJUST_AMB_NOISE.get(language, ''), self.verbose, self.safe_rtl)

        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)

        self._print(self.ENERGY_THRESHOLD.get(language, '').format(
            self.r.energy_threshold), self.verbose, self.safe_rtl)
        return self

    def record(self, language):
        with sr.Microphone() as source:
            self._print(self.RECORD.get(language, ''),
                        self.verbose, self.safe_rtl)
            return self.r.listen(source)
