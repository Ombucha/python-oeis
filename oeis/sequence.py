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

from __future__ import annotations

from functools import cached_property
from typing import List

from requests import get


BASE_URL = "https://oeis.org/"


class Sequence:
    """
    A class that represents a sequence.

    :param a_number: The A-number of the sequence.
    :type a_number: :class:`int`

    :ivar a_number: The A-number of the sequence.
    :ivar url: The URL of the sequence.
    :ivar graph: The graph of the sequence.
    :ivar greeting: The OEIS greeting.
    :ivar text: The textual data of the sequence.

    .. note::

        There are other custom attributes which depend on the sequence.
    """

    def __init__(self, a_number: str) -> None:
        self.a_number = a_number
        self.url = f"{BASE_URL}{self.a_number}"
        self.graph = f"{self.url}/graph?png=1"

        data = get(f"{BASE_URL}search?q=id:{self.a_number}&fmt=json").json()[0]

        special = {
            "xref": "cross_reference",
            "keyword": "keywords",
        }
        for key, value in data.items():
            attribute = special.get(key, key)
            if attribute in ("data", "offset"):
                self.__setattr__(
                    attribute, [int(element) for element in value.split(",")]
                )
            elif attribute == "keywords":
                self.__setattr__(attribute, list(value.split(",")))
            else:
                self.__setattr__(attribute, value)

    @cached_property
    def text(self) -> str:
        return get(f"{BASE_URL}search?q=id:{self.a_number}&fmt=text").text


def search(query: str) -> List[Sequence]:
    """
    Searches OEIS.

    :param query: The query to make.
    :type query: :class:`str`
    """
    data = get(f"{BASE_URL}search?q={query}&fmt=json").json()
    sequences = []
    for result in data:
        number = f"A{(6 - len(str(result['number']))) * '0' + str(result['number'])}"
        sequences.append(Sequence(number))
    return sequences
