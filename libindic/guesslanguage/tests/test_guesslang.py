#!/usr/bin/env python
# -*- coding:utf-8 -*-

from testtools import TestCase
from .. import LangGuess


class GuessLangTest(TestCase):

    def setUp(self):
        super(GuessLangTest, self).setUp()
        self.instance = LangGuess()

    def test_guesslanguage(self):
        self.assertEqual(self.instance.guessLanguage(u"മലയാളം"), "Malayalam")
