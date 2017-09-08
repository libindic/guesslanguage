''' Copyright (c) 2008, Kent S Johnson

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, 5th Floor, Boston, MA 02110-1301 USA
'''

from testtools import TestCase

from ..blocks import unicodeBlock
from itertools import chain


class BlocksTest(TestCase):

    def setUp(self):
        super(BlocksTest, self).setUp()

    def assertBlock(self, name, c):
        try:
            c = unichr(c)  # noqa: F821
        except:
            c = chr(c)
        block = unicodeBlock(c)
        self.assertEquals(name, unicodeBlock(c),
                          '%s != %s for %r' % (name, block, c))

    def test_unicodeBlock(self):
        for c in range(128):
            self.assertBlock('Basic Latin', c)
        try:
            for c in range(0x80, 0x180) + range(0x250, 0x2B0):
                self.assertBlock('Extended Latin', c)
        except:
            for c in chain(range(0x80, 0x180), range(0x250, 0x2B0)):
                self.assertBlock('Extended Latin', c)

        self.assertBlock('Thai', 0xE00)
        self.assertBlock('Thai', 0xE7F)
        self.assertBlock('Lao', 0xE80)
        self.assertBlock('Lao', 0x0EFF)
        self.assertBlock('Tibetan', 0xF00)
        self.assertBlock('Tibetan', 0xFFF)
        self.assertBlock('Cyrillic', 0x421)
