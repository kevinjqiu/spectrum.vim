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
* `git clone https://github.com/kevinjqiu/spectrum.git`, and then copy everything in `plugin/` into your `$HOME/.vim/plugin/`. and `doc/` to `$HOME/.vim/doc/`. If you're using Pathogen, add `spectrum.vim/` to your runtime path.
* If you use [vundle](https://github.com/gmarik/vundle.git) add `Bundle git@github.com:kevinjqiu/spectrum.vim.git` to your bundle config and then in vim, do `:BundleInstall`. Feel free to checkout [my vim setup](https://github.com/kevinjqiu/vimmy) and [my Vundle configure](https://github.com/kevinjqiu/vimmy/blob/master/.vim/conf/vundle.vim).

Commands available
==================
* SpectrumShuffle()
* SpectrumNext()
* SpectrumPrevious()
* SpectrumInspirationDark()
* SpectrumInspirationBright()
* SpectrumInspect()
* SpectrumLike()
* SpectrumExclude()
