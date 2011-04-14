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

    def spin(self):
        colorscheme = random.choice(list(self.colorschemes))
        vim.command("colorscheme %s" % colorscheme)
              

spectrum = Spectrum()

def spectrum_spin():
    spectrum.spin()
EOP

nmap <silent><Leader>q :python spectrum_spin()<CR>
