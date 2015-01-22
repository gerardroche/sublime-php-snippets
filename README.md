# php-snippets

php-snippets plugin for Sublime Text. Provides decent PHP snippets.

## Overview

* [Features](#features)
* [Key Bindings](#key-bindings)
* [Installation](#installation)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [Complementary Plugins](#complementary-plugins)
* [License](#license)

# Features

* PHP [~5.6][semver]
* [PSR][php-fig] compliant
* Scoped to minimise auto-complete noise

See the [documentation] for a list of the snippets.

## Key Bindings

| OS X | Windows | Linux | Description |
|------|---------|-------|-------------|
| <kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Alt</kbd>+<kbd>/</kbd> | Activate completions |

To enable [tab-completions][tab-completed-completions] set `"tab_completion": true` in `Preferences > Settings - User`.

## Installation

### Manual installation

1. Download or clone this repository to a directory "php-snippets" in the Sublime Text Packages directory for your platform:
    * Sublime Text 3
        - Linux: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/.config/sublime-text-3/Packages/php-snippets`
        - OS X: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/php-snippets`
        - Windows: `git clone https://github.com/gerardroche/sublime-php-snippets.git %APPDATA%\Sublime/ Text/ 3/Packages/php-snippets`
    * Sublime Text 2
        - Linux: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/.config/sublime-text-2/Packages/php-snippets`
        - OS X: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/php-snippets`
        - Windows: `git clone https://github.com/gerardroche/sublime-php-snippets.git %APPDATA%\Sublime/ Text/ 2/Packages/php-snippets`
2. Restart Sublime Text to complete installation. The features listed above should now be available.

## Configuration

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

## Contributing

Issue reports and pull requests are always welcome.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Complementary Plugins

* [php-completions]
* [php-grammar]
* [php-snippets]
* [phpunit-completions]
* [phpunit-snippets]
* [phpunit]

## License

php-snippets is released under the [BSD 3-Clause License][license].

[documentation]: DOCUMENTATION.md
[license]: LICENSE
[Package Control]: https://packagecontrol.io
[php-completions]: https://github.com/gerardroche/sublime-phpck
[php-fig]: http://www.php-fig.org
[php-grammar]: https://github.com/gerardroche/sublime-php-grammar
[php-snippets]: https://github.com/gerardroche/sublime-php-snippets
[phpunit-completions]: https://github.com/gerardroche/sublime-phpunitck
[phpunit-snippets]: https://github.com/gerardroche/sublime-phpunit-snippets
[phpunit]: https://github.com/gerardroche/sublime-phpunit
[semver]: http://semver.org
[tab-completed-completions]: http://docs.sublimetext.info/en/latest/extensibility/completions.html#tab-completed-completions
