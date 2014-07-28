# Sublime SASS Cleaner - A SASS Cleaner

[![Build Status](https://img.shields.io/travis/wbotelhos/sublime-sass-cleaner/master.svg)](https://travis-ci.org/wbotelhos/sublime-sass-cleaner "Travis CI")
[![Code Climate](https://codeclimate.com/github/wbotelhos/sublime-sass-cleaner.png)](https://codeclimate.com/github/wbotelhos/sublime-sass-cleaner "Code Climate")
[![Support Sublime SASS Cleaner](http://img.shields.io/gittip/wbotelhos.svg)](https://www.gittip.com/wbotelhos "Git Tip")

Sublime SASS Cleaner is a plugin that removes invalid characters from SASS file.

## Version

```
@version  0.1.0
@since    2014-07-28
@author   Washington Botelho
@doc      wbotelhos.com/sublime-sass-cleaner
```
## Dependencies

+ sass_cleaner.py

## Installation

### Mac OSX

```bash
cd /Users/$USER/Library/Application Support/Sublime Text 2/Packages
git clone https://github.com/wbotelhos/sublime-sass-cleaner SASSCleaner
```

### Linux

```bash
cd ~/.config/sublime-text-2/Packages
git clone https://github.com/wbotelhos/sublime-sass-cleaner SASSCleaner
```

### Windows

```bash
cd %APPDATA%/Sublime Text 2/Packages
git clone https://github.com/wbotelhos/sublime-sass-cleaner SASSCleaner
```

## Usage

While editing some files with `.sass` extension, just save it.

## Features

1) All `;` will be removed;
2) All `{` and `}` will be removed.

Before:

```css
body {
  height: 100%;
}
```

After:

```sass
body
  height: 100%

```

## Warning

It won't remove the left empty lines from your code.

## Licence

The MIT License

## Donate

You can do it via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=X8HEP2878NDEG&item_name=Sublime%20SASS%20Cleaner). Thanks! (:
