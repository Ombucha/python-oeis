"""
MIT License

Copyright (c) 2025 Omkaar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


# pylint: skip-file

import unittest
from oeis import Sequence

class TestSequenceIntegration(unittest.TestCase):
    def test_valid_sequence_attributes(self):
        seq = Sequence("A000045")  # Fibonacci numbers
        self.assertEqual(seq.a_number, "A000045")
        self.assertTrue(seq.url.startswith("https://oeis.org/A000045"))
        self.assertTrue(seq.graph.endswith("/A000045/graph?png=1"))
        self.assertIsInstance(seq.data, list)
        self.assertTrue(all(isinstance(x, int) for x in seq.data))
        self.assertIsInstance(seq.offset, list)
        self.assertTrue(all(isinstance(x, int) for x in seq.offset))
        self.assertIsInstance(seq.name, str)
        self.assertGreater(len(seq.name), 0)
        self.assertIsInstance(seq.text, str)
        self.assertIn("Fibonacci", seq.text)
        self.assertIsInstance(seq.keywords, list)
        self.assertTrue(all(isinstance(k, str) for k in seq.keywords))
        self.assertIsInstance(seq.cross_references, list)
        self.assertIsInstance(seq.author, str)

    def test_repr_and_str(self):
        seq = Sequence("A000045")
        s = str(seq)
        r = repr(seq)
        self.assertIn("A000045", s)
        self.assertIn("A000045", r)

    def test_minimal_sequence(self):
        seq = Sequence("A000004")  # Known to have minimal fields
        self.assertIsInstance(seq.data, list)
        self.assertIsInstance(seq.offset, list)
        self.assertIsInstance(seq.name, str)
        self.assertIsInstance(seq.text, str)
        self.assertIsInstance(seq.keywords, list)
        self.assertIsInstance(seq.cross_references, list)
        self.assertIsInstance(seq.author, str)

    def test_invalid_sequence_raises(self):
        with self.assertRaises(Exception):
            Sequence("A999999")  # Unlikely to exist

    def test_sequence_data_and_offset_content(self):
        seq = Sequence("A000010")  # Euler's totient function
        self.assertTrue(all(isinstance(x, int) for x in seq.data))
        self.assertTrue(all(isinstance(x, int) for x in seq.offset))
        self.assertGreaterEqual(len(seq.data), 5)
        self.assertGreaterEqual(len(seq.offset), 1)

    def test_sequence_keywords_and_crossrefs(self):
        seq = Sequence("A000045")
        self.assertIsInstance(seq.keywords, list)
        self.assertTrue(all(isinstance(k, str) for k in seq.keywords))
        self.assertIsInstance(seq.cross_references, list)

    def test_sequence_author(self):
        seq = Sequence("A000045")
        self.assertIsInstance(seq.author, str)
        self.assertGreater(len(seq.author), 0)

    def test_sequence_text_property(self):
        seq = Sequence("A000045")
        text1 = seq.text
        text2 = seq.text  # Should be cached if implemented
        self.assertEqual(text1, text2)
        self.assertIsInstance(text1, str)
        self.assertIn("Fibonacci", text1)

if __name__ == "__main__":
    unittest.main()