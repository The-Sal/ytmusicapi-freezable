# YTMusicAPI – Freezeable ❄️

A fork of [ytmusicapi](http://github.com/sigma67/ytmusicapi) that adds the ability for the module to be frozen with no extra arguments. 
Works with both PyInstaller and Nuitka.

## Installation
```bash
pip3 install git+https://github.com/The-Sal/ytmusicapi-freezable
```

## Usage
This modul serves as a drop-in replacement for the original ytmusicapi. 
See the official docs for ytmusicapi [here](https://ytmusicapi.readthedocs.io/en/latest/).

## Contributions
I've broken the test/ directory since it used pytest, which I don't really know how to use
so this is uses unittest instead therefore the tests GitHub runs will most likely fail. Also, the toml
file was edited to remove the pytest dependency. So... if anyone wants to fix that, feel free to make a PR.
