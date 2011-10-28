" directory to store inspiration color schemes
" This dir must be writable to the current user
let spectrum#inspiration_storage_dir = "$HOME/.spectrum"
let spectrum#inspiration_endpoint = "http://inspiration.sweyla.com/code/vim/inspiration%(seed)s.vim"
" the maximum number of colorscheme changes to remember
let spectrum#max_history = 10

python << EOP
import vim
import sys
from os import path

def fix_syspath():
    current_file = vim.eval('expand("<sfile>")')
    current_path = path.join(path.split(current_file)[:-1])[0]
    if current_path not in sys.path:
        sys.path.insert(0, current_path)

fix_syspath()

from spectrum.spectrum import spectrum

EOP

function! SpectrumShuffle()
    python spectrum.shuffle()
endfunction

function! SpectrumNext()
    python spectrum.next()
endfunction

function! SpectrumPrevious()
    python spectrum.previous()
endfunction

function! SpectrumInspirationDark()
    python spectrum.inspiration('dark')
endfunction

function! SpectrumInspirationBright()
    python spectrum.inspiration('bright')
endfunction

function! SpectrumLike()
    python spectrum.like()
endfunction

function! SpectrumExclude()
    python spectrum.exclude()
endfunction

function! SpectrumInspect()
    python spectrum.inspect()
endfunction

function! SpectrumInspirationPurge()
    python spectrum.purge_inspiration()
endfunction

function! SpectrumShowExcluded()
    python spectrum.show_excluded_colorschemes()
endfunction

function! SpectrumShowFavorite()
    python spectrum.show_favorite_colorschemes()
endfunction
