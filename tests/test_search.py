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
from oeis import search, Sequence

class TestSearchIntegration(unittest.TestCase):
    def test_search_returns_sequence_objects(self):
        results = search("Fibonacci")
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        for seq in results[:5]:
            self.assertIsInstance(seq, Sequence)
            self.assertRegex(seq.a_number, r"A\d{6}")
            self.assertIsInstance(seq.name, str)

    def test_search_with_no_results(self):
        results = search("thisisnotarealsearchterm123456")
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 0)

    def test_search_case_insensitivity(self):
        lower = search("lucas")
        upper = search("LUCAS")
        self.assertEqual(
            [s.a_number for s in lower],
            [s.a_number for s in upper]
        )

    def test_search_partial_match(self):
        results = search("Lucas")
        self.assertIsInstance(results, list)
        self.assertTrue(
            any("Lucas" in getattr(seq, "name", "") for seq in results)
        )

    def test_search_returns_expected_fields(self):
        results = search("Fibonacci")
        for seq in results[:5]:
            self.assertTrue(
                "Fibonacci" in getattr(seq, "name", "") or "A000045" == seq.a_number,
                f"Entry does not contain expected keywords: {repr(seq)}"
            )

    def test_search_too_many_results(self):
        # Should raise ValueError for too many results
        with self.assertRaises(ValueError) as cm:
            search("prime")
        self.assertIn("too many results", str(cm.exception).lower())

    def test_search_empty_string(self):
        # Should raise ValueError for empty query
        with self.assertRaises(ValueError) as cm:
            search("")
        self.assertIn("empty string", str(cm.exception).lower())

    def test_search_numeric_query(self):
        results = search("123")
        self.assertIsInstance(results, list)
        # Should not crash and should return a list

    def test_search_special_characters(self):
        results = search("Fibonacci!")
        self.assertIsInstance(results, list)

    def test_search_exact_a_number(self):
        results = search("A000045")
        self.assertIsInstance(results, list)
        self.assertTrue(any(seq.a_number == "A000045" for seq in results))

if __name__ == "__main__":
    unittest.main()