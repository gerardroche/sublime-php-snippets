# WHAT PHP SNIPPETS IS

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Stable Version](https://img.shields.io/github/tag/gerardroche/sublime-php-snippets.svg?style=flat-square&label=stable)](https://github.com/gerardroche/sublime-php-snippets/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-php-snippets.svg?style=flat-square)](https://github.com/gerardroche/sublime-php-snippets/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/php-snippets.svg?style=flat-square)](https://packagecontrol.io/packages/php-snippets) [![Author](https://img.shields.io/badge/twitter-gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche)

PHP snippets for Sublime Text.

## Overview

* [Features](#features)
* [Key Bindings](#key-bindings)
* [Installation](#installation)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [License](#license)

## FEATURES

* PHP ~5.6
* [PSR](http://www.php-fig.org) compliant
* Scoped to minimise auto-complete noise

## SNIPPETS

See [SNIPPETS.md](SNIPPETS.md).

## KEY BINDINGS

| OS X | Windows | Linux | Description |
|------|---------|-------|-------------|
| <kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Alt</kbd>+<kbd>/</kbd> | Activate completions |

To enable [tab-completions](http://docs.sublimetext.info/en/latest/extensibility/completions.html#tab-completed-completions) set `"tab_completion": true` in `Preferences > Settings - User`.

## INSTALLATION

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/browse/authors/gerardroche).

### Manual installation

1. Close Sublime Text.
2. Download or clone this repository to a directory named **`php-snippets`** in the Sublime Text Packages directory for your platform:
    * Linux: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/.config/sublime-text-3/Packages/php-snippets`
    * OS X: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/php-snippets`
    * Windows: `git clone https://github.com/gerardroche/sublime-php-snippets.git %APPDATA%\Sublime/ Text/ 3/Packages/php-snippets`
3. Done!

## CONFIGURATION

Set snippet variables using a `.tmPreferences` file. Put the file in the "User" packages directory. Locate it via `Menu > Preferences > Browse Packages...`

### Example

By default the `echo` snippet in a html scope expands with a short php tag:

```php
<?= $var ?>
```

To use the alternative:

```php
<?php echo $var ?>
```

Add **`php-snippets-phtml-settings.tmPreferences`** to the User packages directory:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
    <key>name</key>
    <string>php-snippets phtml settings</string>
    <key>scope</key>
    <string>text.html.basic</string>
    <key>settings</key>
    <dict>
        <key>shellVariables</key>
        <array>
            <dict>
                <key>name</key>
                <string>TM_PHP_OPEN_TAG_WITH_ECHO</string>
                <key>value</key>
                <string>php echo</string>
            </dict>
        </array>
    </dict>
</dict>
</plist>
```

## CONTRIBUTING

Your issue reports and pull requests are always welcome.

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
