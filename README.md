# WHAT PHP SNIPPETS IS

PHP snippets for Sublime Text.

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Version](https://img.shields.io/github/tag/gerardroche/sublime-php-snippets.svg?style=flat-square&label=version)](https://github.com/gerardroche/sublime-php-snippets/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-php-snippets.svg?style=flat-square)](https://github.com/gerardroche/sublime-php-snippets/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/PHPSnippets.svg?style=flat-square)](https://packagecontrol.io/packages/PHPSnippets)

* PSR compliant
* Scoped to minimise auto-complete noise

## INSTALLATION

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/browse/authors/gerardroche).

### Manual installation

Close Sublime Text, then download or clone this repository to a directory named **PHPSnippets** in the Sublime Text Packages directory for your platform:

OS | Command
-- | -----
Linux | `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/.config/sublime-text-3/Packages/PHPSnippets`
OSX | `git clone https://github.com/gerardroche/sublime-php-snippets.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/PHPSnippets`
Windows | `git clone https://github.com/gerardroche/sublime-php-snippets.git %APPDATA%\Sublime/ Text/ 3/Packages/PHPSnippets`

## USAGE

| OS X | Windows | Linux | Description |
|------|---------|-------|-------------|
| `Command+Space` | `Ctrl+Space` | `Alt+/` | Activate completions |

Enable [tab-completions](http://docs.sublimetext.info/en/latest/extensibility/completions.html#tab-completed-completions).

**Menu → Preferences → Settings**

```js
"tab_completion": true
```

| Trigger | Description |
| ------- | ----------- |
| `<?` | PHP: start tag |
| `<?` | PHTML: &lt;?php ... ?&gt; |
| `<?=` | PHP: short echo tag |
| `/**` | PHP: phpdoc |
| `?=` | PHP: short echo tag |
| `_C` | PHP: COOKIE['|'] |
| `_E` | PHP: ENV['|'] |
| `_F` | PHP: FILES['|'] |
| `_G` | PHP: GET['|'] |
| `_P` | PHP: POST['|'] |
| `_R` | PHP: REQUEST['|'] |
| `_S` | PHP: SERVER['|'] |
| `_SS` | PHP: SESSION['|'] |
| `am` | PHP: array map |
| `arr` | PHP: variable = array |
| `c` | PHP: class |
| `c` | PHP: class declaration |
| `case` | PHP: case |
| `class` | PHP: class |
| `closure` | PHP: closure |
| `con` | PHP: constructor |
| `def` | PHP: define |
| `def?` | PHP: defined |
| `do` | PHP: do while |
| `doc_c` | PHP: phpdoc class |
| `doc_d` | PHP: phpdoc constant |
| `doc_f` | PHP: phpdoc function |
| `doc_i` | PHP: phpdoc interface |
| `doc_s` | PHP: phpdoc function |
| `doc_v` | PHP: phpdoc property |
| `dst` | PHP: declare strict_types |
| `echo` | PHP: echo string |
| `echo` | PHTML: echo variable |
| `echoh` | PHTML: echo htmlentities |
| `else` | PHP: else |
| `else` | PHTML: else |
| `elseif` | PHP: elseif |
| `elseif` | PHTML: elseif |
| `endfor` | PHTML: endfor |
| `endforeach` | PHTML: endforeach |
| `endif` | PHTML: endif |
| `endswitch` | PHTML: endswitch |
| `endwhile` | PHTML: endwhile |
| `ethis` | PHP: echo $this-&gt; |
| `ethis` | PHTML: echo $this-&gt; |
| `ev` | PHP: echo variable |
| `f` | PHP: function |
| `flatten` | PHP: flatten array |
| `for` | PHP: for |
| `foreach` | PHP: foreach value |
| `foreach` | PHTML: foreach value |
| `foreachk` | PHP: foreach key => value |
| `foreachk` | PHTML: foreach key => value |
| `foreachv` | PHP: foreach value |
| `fpri` | PHP: final private method |
| `fpris` | PHP: final private static method |
| `fpro` | PHP: final protected method |
| `fpub` | PHP: final public method |
| `fpubs` | PHP: final public static method |
| `fun` | PHP: function |
| `getter` | PHP: getter |
| `globals` | PHP: $GLOBALS['|'] |
| `gm` | PHP: getter |
| `i` | PHP: interface |
| `if` | PHP: if |
| `if` | PHTML: if |
| `if?` | PHP: var = cond ? a:b |
| `ifelse` | PHP: if-else |
| `ifelse` | PHTML: if-else |
| `inc` | PHP: include 'file' |
| `inc1` | PHP: include_once 'file' |
| `is` | PHP: isset var |
| `kv` | PHP: 'key' => 'value' |
| `m` | PHP: method |
| `met` | PHP: method |
| `n` | PHP: namespace |
| `namespace` | PHP: namespace |
| `p` | PHP: property |
| `php` | PHTML: &lt;?php ... ?&gt; |
| `pr` | PHP: print_r |
| `pre` | PHP: print_r and exit |
| `pri` | PHP: private method |
| `pro` | PHP: protected method |
| `psm` | PHP: public static method |
| `pub` | PHP: public method |
| `pubs` | PHP: public static method |
| `r` | PHP: return |
| `req` | PHP: require file |
| `req1` | PHP: require_once file |
| `reqd` | PHP: require dirname file |
| `ret` | PHP: return |
| `ret0` | PHP: return false |
| `ret1` | PHP: return true |
| `retf` | PHP: return false |
| `rett` | PHP: return true |
| `rt` | PHP: return $this |
| `rv` | PHP: return var |
| `self` | PHP: self:: |
| `setter` | PHP: setter |
| `sm` | PHP: setter |
| `switch` | PHP: switch |
| `t` | PHP: $this-&gt; |
| `this` | PHP: $this-&gt; |
| `this` | PHTML: &lt;?php $this-&gt;| ?&gt; |
| `throw` | PHP: throw exception |
| `trait` | PHP: trait |
| `try` | PHP: try catch |
| `use` | PHP: use |
| `vd` | PHP: dump var |
| `vde` | PHP: dump var and exit |
| `while` | PHP: while |

## CONFIGURATION

Create a file named `php-snippets-phtml-settings.tmPreferences` in your User packages directory (`Menu → Preferences → Browse Packages...`) with the following (modified to meet your needs):

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


            <!--
                If you prefer HTML echo statement snippets to use long-form echo
                statements: <?php echo | ?>. Comment out the following section:
            -->

            <dict>
                <key>name</key>
                <string>TM_PHP_OPEN_TAG_WITH_ECHO</string>
                <key>value</key>
                <string>=</string>
            </dict>


            <!--
                If you prefer opening braces to be formatted on the same line,
                uncomment the following section:
            -->

            <!--
            <dict>
                <key>name</key>
                <string>TM_PHP_SNIPPET_OPENING_BRACE</string>
                <key>value</key>
                <string> {</string>
            </dict>
            -->

        </array>
    </dict>
</dict>
</plist>

```

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
