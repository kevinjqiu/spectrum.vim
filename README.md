Spectrum.vim
============
Tired of your current vim colorscheme? Have hundreds of vim colorschemes but don't know which ones you like because it takes too many key strokes to explore? Spectrum is here to help.

Spectrum allows you to shuffle through your installed colorschemes, keeping a history of your exploration for your reference.

Requirements
============
* Vim 7+ and compiled with Python
* Python 2.6+

Installation
============
* `git clone https://github.com/gmarik/vundle.git`, and then copy everything in `plugin/` into your `$HOME/.vim/plugin/`. If you're using Pathogen, add `spectrum.vim/` to your runtime path.
* If you use [vundle](https://github.com/gmarik/vundle.git) add `Bundle git@github.com:kevinjqiu/spectrum.vim.git` to your bundle config and then in vim, do `:BundleInstall`. Feel free to checkout [my vim setup](https://github.com/kevinjqiu/vimmy)

Default Key binding
===================
* `<Leader>q` - randomly pick a colorscheme
* `<Leader>-` - go back one colorscheme
* `<Leader>+` - go forward one colorscheme
* `<Leader>csi` - inspect the current colorscheme queue
* `<Leader>csl` - "like" the current colorscheme
* `<Leader>csu` - "unlike" (exclude) the current colorscheme
