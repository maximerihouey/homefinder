# Homefinder

A simple Python module which aims at helping me finding my next apartment in
Nice, France the optimal way.

# Usage

## Google Maps API token

To use **Homefinder**, you need a
[Google Maps API token](https://developers.google.com/maps/). Then, you have to
export this token as an environment variable. For example, on UNIX-like
systems, you can simply add
```bash
export HOMEFINDER_GOOGLE_API_TOKEN={api_token}
```
to your ``~/.bashrc`` or ``~/.zshenv.usr`` init script, by replacing
``{api_token}`` by your own token. Do not forget to ``source`` it before using
**Homefinder**:
```bash
source ~/.bashrc
```

## Importing the data

Datasets examples are given in ``/data``. The description is self-explicit but
feel free to ask for some clarification and do not hesitate to contribute by
forking and making pull requests. :bowtie:

# MIT License

Copyright (c) 2016 Jaona Ramahaleo

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
