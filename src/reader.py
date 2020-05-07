import speech_recognition as sr
import arabic_reshaper
from bidi.algorithm import get_display


class Reader:
    """A main class based on the speech recognition package for speech to text."""

    UnknownValueError = {
        "en-US": "Google Speech Recognition could not understand audio",
        "fa-IR": "تشخیص گفتار گوگل نتوانست صدا را درک کند."
    }
    RequestError = {
        "en-US": "Could not request results from Google Speech Recognition service: {0}",
        "fa-IR": "درخواست نتایج از سرویس شناسایی گفتار گوگل امکان پذیر نیست: {0}"
    }
    ADJUST_AMB_NOISE = {
        'en-US': "Adjusting microphone.",
        'fa-IR': "تنظیم میکروفن."
    }
    ENERGY_THRESHOLD = {
        "en-US": "Set the minimum energy threshold to {0}.",
        "fa-IR": "حداقل آستانه انرژی را به {0} تنظیم کنید."
    }
    RECORD = {}

    def __init__(self, language='fa-IR', verbose=True, safe_rtl=False):
        self.sr = sr
        self.r = self.sr.Recognizer()
        self.language = language
        self.verbose = verbose
        self.safe_rtl = safe_rtl

    @staticmethod
    def _print(message, verbose=False, safe_rtl=False):
        if verbose:
            if safe_rtl:
                message = get_display(arabic_reshaper.reshape(message))
            print(message)

    def recognize_google(self, audio, language):

        try:
            text = self.r.recognize_google(audio, language=language)
        except self.sr.UnknownValueError:
            err = self.UnknownValueError.get(language, '')
            self._print(err, self.verbose)
            return False, err
        except self.sr.RequestError as e:
            err = self.RequestError.get(language, '').format(e)
            self._print(err, self.verbose, self.safe_rtl)
            return False, err

        return True, text
