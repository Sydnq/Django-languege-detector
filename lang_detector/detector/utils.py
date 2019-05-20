import re

_url_pattern = re.compile(r'https?://[-_.?&~;+=/#0-9A-Za-z]{1,2000}')
_mail_pattern = re.compile(r'[-_.0-9A-Za-z]{1,64}@[\w]+\.[a-z]{2,3}$')


def is_mail(text):
    """Check if provided text is email."""
    return re.match(_mail_pattern, text)


def is_url(text):
    """Check if provided text is url."""
    return re.match(_url_pattern, text)


# Translate is ISO-639-1 language code to language name
# see: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# for more info
ISO_TO_LANGUAGE = {
    "ab": "Abkhazian",
    "aa": "Afar",
    "af": "Afrikaans",
    "ak": "Akan",
    "sq": "Albanian",
    "am": "Amharic",
    "ar": "Arabic",
    "an": "Aragonese",
    "hy": "Armenian",
    "as": "Assamese",
    "av": "Avaric",
    "ae": "Avestan",
    "ay": "Aymara",
    "az": "Azerbaijani",
    "bm": "Bambara",
    "ba": "Bashkir",
    "eu": "Basque",
    "be": "Belarusian",
    "bn": "Bengali",
    "bh": "Bihari languages",
    "bi": "Bislama",
    "bs": "Bosnian",
    "br": "Breton",
    "bg": "Bulgarian",
    "my": "Burmese",
    "ca": "Catalan, Valencian",
    "ch": "Chamorro",
    "ce": "Chechen",
    "ny": "Chichewa, Chewa, Nyanja",
    "zh": "Chinese",
    "cv": "Chuvash",
    "kw": "Cornish",
    "co": "Corsican",
    "cr": "Cree",
    "hr": "Croatian",
    "cs": "Czech",
    "da": "Danish",
    "dv": "Divehi, Dhivehi, Maldivian",
    "nl": "Dutch, Flemish",
    "dz": "Dzongkha",
    "en": "English",
    "eo": "Esperanto",
    "et": "Estonian",
    "ee": "Ewe",
    "fo": "Faroese",
    "fj": "Fijian",
    "fi": "Finnish",
    "fr": "French",
    "ff": "Fulah",
    "gl": "Galician",
    "ka": "Georgian",
    "de": "German",
    "el": "Greek, Modern (1453-)",
    "gn": "Guarani",
    "gu": "Gujarati",
    "ht": "Haitian, Haitian Creole",
    "ha": "Hausa",
    "he": "Hebrew",
    "hz": "Herero",
    "hi": "Hindi",
    "ho": "Hiri Motu",
    "hu": "Hungarian",
    "ia": "Interlingua (International Auxiliary Language Association)",
    "id": "Indonesian",
    "ie": "Interlingue, Occidental",
    "ga": "Irish",
    "ig": "Igbo",
    "ik": "Inupiaq",
    "io": "Ido",
    "is": "Icelandic",
    "it": "Italian",
    "iu": "Inuktitut",
    "ja": "Japanese",
    "jv": "Javanese",
    "kl": "Kalaallisut, Greenlandic",
    "kn": "Kannada",
    "kr": "Kanuri",
    "ks": "Kashmiri",
    "kk": "Kazakh",
    "km": "Central Khmer",
    "ki": "Kikuyu, Gikuyu",
    "rw": "Kinyarwanda",
    "ky": "Kirghiz, Kyrgyz",
    "kv": "Komi",
    "kg": "Kongo",
    "ko": "Korean",
    "ku": "Kurdish",
    "kj": "Kuanyama, Kwanyama",
    "la": "Latin",
    "lb": "Luxembourgish, Letzeburgesch",
    "lg": "Ganda",
    "li": "Limburgan, Limburger, Limburgish",
    "ln": "Lingala",
    "lo": "Lao",
    "lt": "Lithuanian",
    "lu": "Luba-Katanga",
    "lv": "Latvian",
    "gv": "Manx",
    "mk": "Macedonian",
    "mg": "Malagasy",
    "ms": "Malay",
    "ml": "Malayalam",
    "mt": "Maltese",
    "mi": "Maori",
    "mr": "Marathi",
    "mh": "Marshallese",
    "mn": "Mongolian",
    "na": "Nauru",
    "nv": "Navajo, Navaho",
    "nd": "North Ndebele",
    "ne": "Nepali",
    "ng": "Ndonga",
    "nb": "Norwegian Bokmål",
    "nn": "Norwegian Nynorsk",
    "no": "Norwegian",
    "ii": "Sichuan Yi, Nuosu",
    "nr": "South Ndebele",
    "oc": "Occitan",
    "oj": "Ojibwa",
    "cu": "Church Slavic, Old Slavonic, Church Slavonic, Old Bulgarian, Old Church Slavonic",
    "om": "Oromo",
    "or": "Oriya",
    "os": "Ossetian, Ossetic",
    "pa": "Panjabi, Punjabi",
    "pi": "Pali",
    "fa": "Persian",
    "pl": "Polish",
    "ps": "Pashto, Pushto",
    "pt": "Portuguese",
    "qu": "Quechua",
    "rm": "Romansh",
    "rn": "Rundi",
    "ro": "Romanian, Moldavian, Moldovan",
    "ru": "Russian",
    "sa": "Sanskrit",
    "sc": "Sardinian",
    "sd": "Sindhi",
    "se": "Northern Sami",
    "sm": "Samoan",
    "sg": "Sango",
    "sr": "Serbian",
    "gd": "Gaelic, Scottish Gaelic",
    "sn": "Shona",
    "si": "Sinhala, Sinhalese",
    "sk": "Slovak",
    "sl": "Slovenian",
    "so": "Somali",
    "st": "Southern Sotho",
    "es": "Spanish, Castilian",
    "su": "Sundanese",
    "sw": "Swahili",
    "ss": "Swati",
    "sv": "Swedish",
    "ta": "Tamil",
    "te": "Telugu",
    "tg": "Tajik",
    "th": "Thai",
    "ti": "Tigrinya",
    "bo": "Tibetan",
    "tk": "Turkmen",
    "tl": "Tagalog",
    "tn": "Tswana",
    "to": "Tonga (Tonga Islands)",
    "tr": "Turkish",
    "ts": "Tsonga",
    "tt": "Tatar",
    "tw": "Twi",
    "ty": "Tahitian",
    "ug": "Uighur, Uyghur",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "ve": "Venda",
    "vi": "Vietnamese",
    "vo": "Volapük",
    "wa": "Walloon",
    "cy": "Welsh",
    "wo": "Wolof",
    "fy": "Western Frisian",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "za": "Zhuang, Chuang",
    "zu": "Zulu"
}