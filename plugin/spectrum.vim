python << EOP
import vim
import random
from os import path, listdir

class Spectrum(object):
    
    def __init__(self):
        self.colorschemes = self._get_all_colorschemes()
        self.history = [self._current()]
        self.idx = 0

    def shuffle(self):
        colorscheme = random.choice(list(self.colorschemes))
        self.history.append(colorscheme)
        self.idx = len(self.history)-1
        self._set_scheme(self.history[self.idx])

    def previous(self):
        if self.idx == 0:
            print 'Already at the first colorscheme'
        else:
            self.idx -= 1
            self._set_scheme(self.history[self.idx])

    def next(self):
        if self.idx == len(self.history)-1:
            print 'Already at the latest colorscheme'
        else:
            self.idx += 1
            self._set_scheme(self.history[self.idx])

    def inspect(self):
        print self.history, "current:", self.idx
        
    def _set_scheme(self, colorscheme):
        vim.command("colorscheme %s" % colorscheme)

    def _get_all_colorschemes(self):
        retval = set()
        rtp = vim.eval('&rtp').split(',')

        for p in filter(path.exists, map(lambda p:path.join(p, 'colors'), rtp)):
            files = map(lambda file: '.'.join(file.split('.')[:-1]), filter(lambda file: file.endswith('.vim'), listdir(p)))
            retval |= set(files)
        return retval

    def _current(self):
        return vim.eval('g:colors_name')

spectrum = Spectrum()
EOP

nmap <silent><Leader>q :python spectrum.shuffle()<CR>
nmap <silent><Leader>+ :python spectrum.next()<CR>
nmap <silent><Leader>- :python spectrum.previous()<CR>
