python << EOP
import vim
import random
from os import path, listdir

class Spectrum(object):
    
    def __init__(self):
        self.colorschemes = self._get_all_colorschemes()

    def _get_all_colorschemes(self):
        retval = set()
        rtp = vim.eval('&rtp').split(',')

        for p in filter(path.exists, map(lambda p:path.join(p, 'colors'), rtp)):
            files = map(lambda file: '.'.join(file.split('.')[:-1]), filter(lambda file: file.endswith('.vim'), listdir(p)))
            retval |= set(files)
        return retval

    def shuffle(self):
        colorscheme = random.choice(list(self.colorschemes))
        self._set_scheme(colorscheme)

    def previous(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def _set_scheme(self, colorscheme):
        vim.command("colorscheme %s" % colorscheme)

spectrum = Spectrum()

def shuffle():
    spectrum.shuffle()
EOP

nmap <silent><Leader>q :python shuffle()<CR>
