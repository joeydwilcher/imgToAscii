# Cloning / Running
`git clone git@github.com:joeydwilcher/imgToAscii.git`

`source imgToAscii-env/bin/activate`

`python3 image2ascii.py /path/to/image/file`

# Fonts

Monospace fonts are pretty much required to make ascii art look decent, so make sure you have one installed.
For making the images have better width/height ratio, please use Square(http://strlen.com/square/).

# TODOs:
- Implement multiple character sets for dithering algorithm
- Implement stucture based ascii art algorithm: http://www.cse.cuhk.edu.hk/~ttwong/papers/asciiart/asciiart.pdf
    - Vectorize image: imlement pypotrace: https://pypi.org/project/pypotrace/
    - Separate into grid
    - Select best fit character
        - (optional) deform vector slightly
        - (optional) get more better best fit character
        - (optional) repeat
    - Substitute characters