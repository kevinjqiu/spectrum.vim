" directory to store inspiration color schemes
" This dir must be writable to the current user
let spectrum#inspiration_storage_dir = "$HOME/.spectrum"
let spectrum#inspiration_endpoint = "http://inspiration.sweyla.com/code/vim/inspiration%(seed)s.vim"
" the maximum number of colorscheme changes to remember
let spectrum#max_history = 10

python << EOP

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

nmap <silent><Leader>q :python spectrum.shuffle()<CR>
nmap <silent><Leader>+ :python spectrum.next()<CR>
nmap <silent><Leader>- :python spectrum.previous()<CR>
nmap <silent><Leader>csd :python spectrum.inspiration()<CR>
nmap <silent><Leader>csb :python spectrum.inspiration('bright')<CR>
nmap <silent><Leader>csi :python spectrum.inspect()<CR>
nmap <silent><Leader>csl :python spectrum.like()<CR>
