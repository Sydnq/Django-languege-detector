from django.conf import settings

from django import forms
from detector.model.model import detect_language


class TextForm(forms.Form):
    """Input form for text to detect language for."""

    language_text = forms.CharField(label="Language Text", widget=forms.Textarea)

    def detect_language(self):
        """Detect the language of provided text and return it."""
        # process and check the language
        language_text = self.cleaned_data['language_text']
        try:
            detected_language = detect_language(language_text)
            if detected_language:
                detected_language = settings.ISO_TO_LANGUAGE.get(detected_language)
        except Exception as e:
            # simplified error handling in essens
            # error should be logged somewhere and
            # we return unknown.
            return 'unknown'
        else:
            return detected_language
