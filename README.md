# LibIndic GuessLanguage


[![Build Status](https://travis-ci.org/libindic/guesslanguage.svg?branch=master)](https://travis-ci.org/libindic/guesslanguage)
[![Coverage Status](https://coveralls.io/repos/github/libindic/guesslanguage/badge.svg?branch=master)](https://coveralls.io/github/libindic/guesslanguage?branch=master)


LibIndic's guesslanguage module may be used to detect the primary language of a
text. It works even with text containing mixed languages.

## Installation
1. Clone the repository `git clone https://github.com/libindic/guesslanguage.git`
2. Change to the cloned directory `cd guesslanguage`
3. Run setup.py to create installable source `python setup.py sdist`
4. Install using pip `pip install dist/libindic-guesslanguage*.tar.gz`

## Usage
```
>>> from libindic.guesslanguage import LangGuess
>>> instance = LangGuess()
>>> text = u"കേരളത്തിലെ എറണാകുളം ജില്ലയിൽ പെരിയാറിന്റെ തീരത്തുള്ള ഒരു ഗ്രാമമാണ് കാലടി காலடி"
>>> text = u"കേരളത്തിലെ എറണാകുളം ജില്ലയിൽ പെരിയാറിന്റെ തീരത്തുള്ള ഒരു ഗ്രാമമാണ് കാലടി காலடி"
>>> instance.guessLanguage(text)
'Malayalam'
>>> for key, value in instance.getScriptName(text).items():
...     print("%s : %s" % (key, value))
... 
ജില്ലയിൽ : ml_IN
എറണാകുളം : ml_IN
ഒരു : ml_IN
പെരിയാറിന്റെ : ml_IN
காலடி : ta_IN
കേരളത്തിലെ : ml_IN
ഗ്രാമമാണ് : ml_IN
കാലടി : ml_IN
തീരത്തുള്ള : ml_IN
```

For more details read the [docs](http://guesslanguage.rtfd.org/)
