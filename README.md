# gerardroche/sublime-php-snippets

A plugin for Sublime Text.

Provides decent PHP snippets.

Works best with [PHP Grammar], [PHP Completions], and [PHPUnit].

## Overview

* [Features](#features)
* [Key Bindings](#key-bindings)
* [Installation](#installation)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [License](#license)

# Features

* PHP [~5.6](http://semver.org)
* [PSR](http://www.php-fig.org) compliant
* Scoped to minimise auto-complete noise

See the [documentation](DOCUMENTATION.md) for a list of the snippets.

## Key Bindings

| OS X | Windows | Linux | Description |
|------|---------|-------|-------------|
| <kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Alt</kbd>+<kbd>/</kbd> | Activate completions |

To enable [tab-completions](http://docs.sublimetext.info/en/latest/extensibility/completions.html#tab-completed-completions) set `"tab_completion": true` in `Preferences > Settings - User`.

## Installation

### Package Control installation

The preferred method of installation is via Package Control.

1. Install [Package Control](https://packagecontrol.io).
2. From inside Sublime Text, open Package Control's Command Pallet: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Windows, Linux) or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `php-snippets` and hit Return. The package will be downloaded to the appropriate directory.
5. Restart Sublime Text to complete installation. The features listed above should now be available.

### Manual installation

1. Close Sublime Text.
2. Download or clone this repository to a directory named `php-snippets` in the Sublime Text Packages directory for your platform:
    * Sublime Text 3
        - Linux: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/.config/sublime-text-3/Packages/php-snippets`
        - OS X: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/php-snippets`
        - Windows: `git clone https://github.com/gerardroche/sublime-php-snippets.git %APPDATA%\Sublime/ Text/ 3/Packages/php-snippets`
    * Sublime Text 2
        - Linux: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/.config/sublime-text-2/Packages/php-snippets`
        - OS X: `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/php-snippets`
        - Windows: `git clone https://github.com/gerardroche/sublime-php-snippets.git %APPDATA%\Sublime/ Text/ 2/Packages/php-snippets`
3. Restart Sublime Text to complete installation. The features listed above should now be available.

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

Your issue reports and pull requests are always welcome.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [BSD 3-Clause License](LICENSE).

[PHP Grammar]: https://packagecontrol.io/packages/php-grammar
[PHP Completions]: https://packagecontrol.io/packages/PHP%20Completions%20Kit
[PHP Snippets]: https://packagecontrol.io/packages/php-snippets
[PHPUnit]: https://github.com/gerardroche/sublime-phpunit
[PHPUnit Completions]: https://github.com/gerardroche/sublime-phpunit
[PHPUnit Snippets]: https://github.com/gerardroche/sublime-phpunit
