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

`Menu > Preferences > Settings`

```json
{
    "tab_completion": true
}
```

| Trigger | Description |
| ------- | ----------- |
| `<?` | PHTML: &lt;?php ... ?&gt; |
| `<?` | start tag |
| `<?=` | short echo tag |
| `/**` | phpdoc |
| `?=` | short echo tag |
| `_C` | COOKIE['|'] |
| `_E` | ENV['|'] |
| `_F` | FILES['|'] |
| `_G` | GET['|'] |
| `_P` | POST['|'] |
| `_R` | REQUEST['|'] |
| `_S` | SERVER['|'] |
| `_SS` | SESSION['|'] |
| `am` | array map |
| `arr` | variable = array |
| `c` | class |
| `c` | PHP: class declaration |
| `case` | case |
| `class` | class |
| `closure` | closure |
| `con` | constructor |
| `def` | define |
| `def?` | defined |
| `do` | do while |
| `doc_c` | phpdoc class |
| `doc_d` | phpdoc constant |
| `doc_f` | phpdoc function |
| `doc_i` | phpdoc interface |
| `doc_s` | phpdoc function |
| `doc_v` | phpdoc property |
| `dst` | declare strict_types |
| `echo` | echo string |
| `echo` | PHTML: echo variable |
| `echoh` | PHTML: echo htmlentities |
| `else` | else |
| `else` | PHTML: else |
| `elseif` | elseif |
| `elseif` | PHTML: elseif |
| `endfor` | PHTML: endfor |
| `endforeach` | PHTML: endforeach |
| `endif` | PHTML: endif |
| `endswitch` | PHTML: endswitch |
| `endwhile` | PHTML: endwhile |
| `ethis` | echo $this-&gt; |
| `ethis` | PHTML: echo $this-&gt; |
| `ev` | echo variable |
| `f` | function |
| `flatten` | flatten array |
| `for` | for |
| `foreach` | foreach value |
| `foreach` | PHTML: foreach value |
| `foreachk` | foreach key => value |
| `foreachk` | PHTML: foreach key => value |
| `foreachv` | foreach value |
| `fpri` | final private method |
| `fpris` | final private static method |
| `fpro` | final protected method |
| `fpub` | final public method |
| `fpubs` | final public static method |
| `fun` | function |
| `getter` | getter |
| `globals` | $GLOBALS['|'] |
| `gm` | getter |
| `i` | interface |
| `if` | if |
| `if` | PHTML: if |
| `if?` | var = cond ? a:b |
| `ifelse` | if-else |
| `ifelse` | PHTML: if-else |
| `inc` | include 'file' |
| `inc1` | include_once 'file' |
| `is` | isset var |
| `kv` | 'key' => 'value' |
| `m` | method |
| `met` | method |
| `n` | namespace |
| `namespace` | namespace |
| `p` | property |
| `php` | PHTML: &lt;?php ... ?&gt; |
| `pr` | print_r |
| `pre` | print_r and exit |
| `pri` | private method |
| `pro` | protected method |
| `psm` | public static method |
| `pub` | public method |
| `pubs` | public static method |
| `r` | return |
| `req` | require file |
| `req1` | require_once file |
| `reqd` | require dirname file |
| `ret` | return |
| `ret0` | return false |
| `ret1` | return true |
| `retf` | return false |
| `rett` | return true |
| `rt` | return $this |
| `rv` | return var |
| `self` | self:: |
| `setter` | setter |
| `sm` | setter |
| `switch` | switch |
| `t` | $this-&gt; |
| `this` | $this-&gt; |
| `this` | PHTML: &lt;?php $this-&gt;| ?&gt; |
| `throw` | throw exception |
| `trait` | trait |
| `try` | try catch |
| `use` | use |
| `vd` | dump var |
| `vde` | dump var and exit |
| `while` | while |

## CONFIGURATION

Create a file named `php-snippets-phtml-settings.tmPreferences` in your User packages directory (`Menu > Preferences > Browse Packages...`) with the following (modified to meet your needs):

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
