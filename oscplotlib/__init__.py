"""
OSC 1337 wrapper for Matplotlib
"""

import base64
import io
import matplotlib.pyplot as plt

_IMG_STRING = "\n\033]1337;File=inline=1;preserveAspectRatio=1:{}\a\n"

class OSC1337:
    """
    Wrapper class for OSC 1337 images

    OSC1337 objects display (__repr__) as images, but are implemented as
    a thin wrapper around a base64 encoded png.
    """
    def __init__(self, b64str):
        self.b64str = b64str

    def __repr__(self):
        return _IMG_STRING.format(self.b64str)

    def savefig(self, fname):
        """Save the current OSC1337 object"""
        with open(fname, "wb") as f:
            f.write(base64.decodebytes(self.b64str.encode()))


def show():
    """
    Return an OSC1337 object wrapping the currently active figure.
    """
    figure = plt.gcf()

    buf = io.BytesIO()
    figure.savefig(buf, format='png')
    s = base64.b64encode(buf.getvalue()).decode()
    buf.close()

    return OSC1337(s)


def show_all():
    """
    Return a list of all active figures as OSC1337 objects
    """
    old_fignum = plt.gcf().number

    l = []
    for i in plt.get_fignums():
        plt.figure(i)
        l.append(show())

    plt.figure(old_fignum)

    return l


