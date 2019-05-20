from django import forms

from events.models import Event
from detector.model.model import detect_language
from .utils import is_mail, is_url, ISO_TO_LANGUAGE


class TextForm(forms.Form):
    """Input form for text to detect language for."""

    language_text = forms.CharField(
        label="Language Text",
        widget=forms.Textarea)

    def clean_language_text(self):
        """Check to make sure provided text is not an email and url."""
        lang_text = self.cleaned_data['language_text']
        if is_mail(lang_text) or is_url(lang_text):
            raise forms.ValidationError(
                "The provided text is url or email. Please provide proper text.")
        return lang_text

    def detect_language(self):
        """Detect the language of provided text and return it."""
        # process and check the language
        language_text = self.cleaned_data['language_text']
        try:
            detected_language = detect_language(language_text)
            if detected_language:
                detected_language = ISO_TO_LANGUAGE.get(detected_language)

            # Create new event and save it
            event = Event(
                detected_languege=detected_language,
                query_text=language_text)
            event.save()

        except Exception as e:
            # simplified error handling in essens
            # error should be logged somewhere and
            # we return unknown.
            return 'unknown'
        else:
            return detected_language
