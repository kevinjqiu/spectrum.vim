import vim
from random import randint, choice 
from os import path, listdir, makedirs, walk, unlink
from urllib import urlretrieve as fetch
from history_queue import HistoryQueue

class Spectrum(object):
    
    def __init__(self):
        # configuration
        self.dot_folder = path.realpath(vim.eval('expand(spectrum#inspiration_storage_dir)'))
        self.dot_folder_colors = path.join(self.dot_folder, 'colors')
        self.inspiration_endpoint = vim.eval("spectrum#inspiration_endpoint")
        self.max_history_size = int(vim.eval("spectrum#max_history"))

        self._colorschemes = self._get_all_colorschemes()
        self._history = HistoryQueue(self.max_history_size)

        # create necessary folders
        if not path.exists(self.dot_folder):
            makedirs(self.dot_folder)
        if not path.exists(self.dot_folder_colors):
            makedirs(self.dot_folder_colors)
        rtp = vim.eval('&rtp').split(',')
        vim.command("set rtp+=%s" % self.dot_folder) 

    def shuffle(self):
        colorscheme = choice(list(self._colorschemes))
        self._history.set_current(colorscheme)
        self._set_scheme(self._history.current())

    def previous(self):
        try:
            self._set_scheme(self._history.previous())
        except StandardError as e:
            print e

    def next(self):
        try:
            self._set_scheme(self._history.next())
        except StandardError as e:
            print e

    def inspect(self):
        print self._history.__str__()
        
    def inspiration(self, style='dark'):
        """`style` is either 'dark' or 'bright'""",
        # TODO: generated colorschemes seem to be bright always...
        seed = {"seed":str(randint(1, 50000) if style != 'dark' else randint(50001,100001))}

        endpoint = self.inspiration_endpoint % seed
        try:
            colorscheme_name = 'inspiration%(seed)s' % seed
            fetch(endpoint, path.join(self.dot_folder_colors, colorscheme_name + '.vim'))
            self._history.set_current(colorscheme_name)
            self._set_scheme(self._history.current())
        except Exception as e:
            print e

    def purge_inspiration(self):
        """Clean all downloaded inspiration colorschemes"""
        for root, dirs, files in walk(self.dot_folder_colors):
            for file in filter(lambda f: path.isfile(f), [path.join(root, f) for f in files]):
                unlink(file)
                print "%s deleted." % file

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