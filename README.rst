.. image:: https://raw.githubusercontent.com/Ombucha/python-oeis/main/banner.png

.. image:: https://img.shields.io/pypi/v/python-oeis
    :target: https://pypi.python.org/pypi/python-oeis
    :alt: PyPI version
.. image:: https://img.shields.io/pypi/dm/python-oeis
    :target: https://pypi.python.org/pypi/python-oeis
    :alt: PyPI downloads
.. image:: https://sloc.xyz/github/Ombucha/python-oeis
    :target: https://github.com/Ombucha/python-oeis/graphs/contributors
    :alt: Lines of code
.. image:: https://img.shields.io/github/repo-size/Ombucha/python-oeis
    :target: https://github.com/Ombucha/python-oeis
    :alt: Repository size

About
-----

**python-oeis** is a Python library for exploring and retrieving integer sequences from the [Online Encyclopedia of Integer Sequences (OEIS)](https://oeis.org/). Use it to search for sequences by keywords, fetch classic sequences like the Fibonacci numbers (A000045), primes (A000040), or your favorite obscure sequence, and access OEIS metadata programmatically.

Requirements
------------

- Python 3.8 or higher
- `requests <https://pypi.python.org/pypi/requests>`_

Installation
------------

Install the latest stable release from PyPI:

.. code-block:: sh

    # Unix / macOS
    python3 -m pip install "python-oeis"

    # Windows
    py -m pip install "python-oeis"

To install the development version from GitHub:

.. code-block:: sh

    git clone https://github.com/Ombucha/python-oeis
    cd python-oeis
    pip install .

Usage Example
-------------

Query the OEIS for sequences, just like searching for A-numbers or keywords on the OEIS website:

.. code-block:: python

    import oeis

    # Search for sequences related to 'prime numbers'
    results = oeis.search('prime numbers')
    for seq in results[:3]:
        print(seq.id, seq.name, seq.data[:10])

    # Fetch the Fibonacci sequence (A000045)
    fib = oeis.Sequence('A000045')
    print(fib.name)
    print(fib.data[:10])  # First 10 Fibonacci numbers

Links
-----

- `OEIS Main Site <https://oeis.org/>`_
- `Documentation <https://oeis.readthedocs.io/>`_
- `PyPI Project <https://pypi.org/project/python-oeis/>`_
