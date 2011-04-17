import vim
import json
from random import randint, choice
from operator import itemgetter
from os import path, listdir, makedirs, walk, unlink
from urllib import urlretrieve as fetch
from history_queue import HistoryQueue
from weighted_choice import Choice

class Spectrum(object):

    def __init__(self):
        # configuration
        self.dot_folder = path.realpath(vim.eval('expand(spectrum#inspiration_storage_dir)'))
        self.dot_folder_colors = path.join(self.dot_folder, 'colors')
        self.inspiration_endpoint = vim.eval("spectrum#inspiration_endpoint")
        self.max_history_size = int(vim.eval("spectrum#max_history"))
        self.vote_filename = path.join(self.dot_folder, 'votes.json')
        self.excluded_filename = path.join(self.dot_folder, 'excluded.json')

        self._colorschemes = self._get_all_colorschemes()
        self._voted_colorschemes = self._get_voted_colorschemes()
        self._excluded = set(self._get_excluded_colorschemes())
        self._history = HistoryQueue(self.max_history_size)
        self._history.set_current(self._current())

        self._choice = Choice(self._colorschemes,
                              self._voted_colorschemes,
                              exclude=set(self._excluded))

        # create necessary folders
        if not path.exists(self.dot_folder):
            makedirs(self.dot_folder)
        if not path.exists(self.dot_folder_colors):
            makedirs(self.dot_folder_colors)
        rtp = vim.eval('&rtp').split(',')
        vim.command("set rtp+=%s" % self.dot_folder)

    def shuffle(self):
        colorscheme = self._choice.next()
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

    def like(self):
        """vote up the current colorscheme"""
        current = self._current()
        self._voted_colorschemes[current] = \
            self._voted_colorschemes.get(current, 0) + 1
        try:
            self._save(self.vote_filename, self._voted_colorschemes)
            print "Your vote for '%s' has been recorded." % current
            if current in self._excluded:
                self._excluded.remove(current)
                self._save(self.excluded_filename, self._excluded)
        except Exception as e:
            print e

    def exclude(self):
        """exclude the current colorscheme"""
        current = self._current()
        self._excluded.add(current)
        try:
            self._save(self.excluded_filename, self._excluded)
            print "'%s' has been excluded" % current
            if current in self._voted_colorschemes:
                del self._voted_colorschemes[current]
                self._save(self.vote_filename, self._voted_colorschemes)
        except Exception as e:
            print e

    def inspect(self):
        print str(self._history)

    def inspiration(self, style='dark'):
        """`style` is either 'dark' or 'bright'""",
        # FIXME: generated colorschemes seem to be bright always...
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

    def show_excluded_colorschemes(self):
        print self._excluded

    def show_favorite_colorschemes(self, count=5):
        """Show the top `count` colorschemes"""
        self._voted_colorschemes
        favs = sorted(self._voted_colorschemes.iteritems(),
                      key=itemgetter(1),
                      reverse=True)
        print "\n".join([cs for (cs,cnt) in favs[:count]])

    def _set_scheme(self, colorscheme):
        vim.command("colorscheme %s" % colorscheme)

    def _get_all_colorschemes(self):
        retval = set()
        rtp = vim.eval('&rtp').split(',')

        for p in filter(path.exists, (path.join(p, 'colors') for p in rtp)):
            colorscheme = [_get_colorscheme_name(file_name) for file_name in filter(_is_vim_file, listdir(p))]
            retval |= set(colorscheme)
        return retval

    def _get_voted_colorschemes(self):
        if path.exists(self.vote_filename):
            return self._load(self.vote_filename)
        else:
            return self._save(self.vote_filename, {})

    def _get_excluded_colorschemes(self):
        if path.exists(self.excluded_filename):
            return self._load(self.excluded_filename)
        else:
            return self._save(self.excluded_filename, [])

    def _current(self):
        return vim.eval('g:colors_name')

    def _save(self, filename, obj):
        with open(filename, 'w') as f:
            if isinstance(obj, set):
                obj = list(obj)
            json.dump(obj, f)
            return obj

    def _load(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

def _get_colorscheme_name(file_name):
    return '.'.join(file_name.split('.')[:-1])

def _is_vim_file(file_name):
    return file_name.endswith('.vim')

spectrum = Spectrum()
