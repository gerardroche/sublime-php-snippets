# WHAT PHP SNIPPETS IS

PHP snippets for Sublime Text.

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Version](https://img.shields.io/github/tag/gerardroche/sublime-php-snippets.svg?style=flat-square&label=version)](https://github.com/gerardroche/sublime-php-snippets/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-php-snippets.svg?style=flat-square)](https://github.com/gerardroche/sublime-php-snippets/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/PHPSnippets.svg?style=flat-square)](https://packagecontrol.io/packages/PHPSnippets) [![Author](https://img.shields.io/badge/twitter-gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche)

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
| `<?` | PHP: Script start tag |
| `<?=` | PHP: Script short echo tag |
| `/**` | PHP: Start Docblock |
| `?=` | PHP: Script short echo tag |
| `_C` | PHP: COOKIE['...'] |
| `_E` | PHP: ENV['...'] |
| `_F` | PHP: FILES['...'] |
| `_G` | PHP: GET['...'] |
| `_P` | PHP: POST['...'] |
| `_R` | PHP: REQUEST['...'] |
| `_S` | PHP: SERVER['...'] |
| `_SS` | PHP: SESSION['...'] |
| `am` | PHP: array map a closure |
| `array` | PHP: Initialise a variable with an array |
| `c` | PHP: class declaration |
| `case` | PHP: case statement |
| `class` | PHP: class declaration |
| `closure` | PHP: Closure declaration |
| `con` | PHP: class constructor definition |
| `def` | PHP: define(..., ...) |
| `def?` | PHP: defined(...) |
| `do` | PHP: do-while statement |
| `doc_c` | PHP: Documented class |
| `doc_d` | PHP: Documented constant definition |
| `doc_f` | PHP: Documented function |
| `doc_i` | PHP: Documented interface |
| `doc_s` | PHP: Documented function signature |
| `doc_v` | PHP: Documented class variable |
| `dst` | PHP: declare strict_types statement |
| `echo` | PHP: echo '...' |
| `echo` | PHTML: &lt;?php echo ... ?&gt; |
| `echoh` | PHTML: echo htmlentities(...) |
| `else` | PHP: else statement |
| `else` | PHTML: else statement |
| `elseif` | PHP: elseif statement |
| `elseif` | PHTML: elseif statement |
| `endfor` | PHTML: endfor statement |
| `endforeach` | PHTML: endforeach statement |
| `endif` | PHTML: endif statement |
| `endswitch` | PHTML: endswitch statement |
| `endwhile` | PHTML: endwhile statement |
| `ethis` | PHP: echo $this-&gt; |
| `ethis` | PHTML: &lt;?php echo $this-&gt;... ?&gt; |
| `ev` | PHP: echo '...' |
| `f` | PHP: function definition |
| `flatten` | PHP: Flatten an array |
| `for` | PHP: for statement |
| `foreach` | PHP: foreach {value} statement |
| `foreach` | PHTML: foreach {value} statement |
| `foreachk` | PHP: foreach {key} {value} statement |
| `foreachk` | PHTML: foreach {key} {value} statement |
| `fpri` | PHP: final private class method declaration |
| `fpris` | PHP: final private static class method declaration |
| `fpro` | PHP: final protected class method declaration |
| `fpub` | PHP: final public class method declaration |
| `fpubs` | PHP: final public static class method declaration |
| `fun` | PHP: function definition |
| `getter` | PHP: getter |
| `globals` | PHP: $GLOBALS['...'] |
| `gm` | PHP: getter |
| `i` | PHP: interface definition |
| `if` | PHP: if statement |
| `if` | PHTML: if statement |
| `if?` | PHP: $... = ( ... ) ? ... : ... |
| `ifelse` | PHP: if-else statement |
| `ifelse` | PHTML: if-else statement |
| `inc` | PHP: include expression |
| `inc1` | PHP: include_once expression |
| `is` | PHP: $... = ( ... ) ? ... : ... |
| `kv` | PHP: Array key value |
| `m` | PHP: class method declaration |
| `met` | PHP: function definition |
| `n` | PHP: namespace definition |
| `namespace` | PHP: namespace definition |
| `p` | PHP: class property declaration |
| `php` | PHTML: &lt;?php ... ?&gt; |
| `pr` | PHP: Print human readable information about a variable |
| `pre` | PHP: Print human readable information about a variable and exit |
| `pri` | PHP: private class method declaration |
| `pro` | PHP: protected class method declaration |
| `pub` | PHP: public class method declaration |
| `pubs` | PHP: public static class method declaration |
| `r` | PHP: return statement |
| `req` | PHP: require expression |
| `req1` | PHP: require_once expression |
| `reqd` | PHP: require dirname expression |
| `ret` | PHP: return |
| `ret0` | PHP: return false statement |
| `ret1` | PHP: return true statement |
| `retf` | PHP: return false statement |
| `rett` | PHP: return true statement |
| `rt` | PHP: return $this statement |
| `rv` | PHP: return variable statement |
| `self` | PHP: self:: |
| `setter` | PHP: setter |
| `sm` | PHP: setter |
| `switch` | PHP: switch statement |
| `t` | PHP: $this-&gt; |
| `this` | PHP: $this-&gt; |
| `this` | PHTML: &lt;?php $this-&gt;... ?&gt; |
| `throw` | PHP: throw exception statement |
| `trait` | PHP: trait definition |
| `try` | PHP: Wrap in try { ... } catch (...) { ... } |
| `use` | PHP: namespace use declaration |
| `vd` | PHP: Dump information about a variable |
| `vde` | PHP: Dump information about a variable and exit |
| `while` | PHP: while statement |

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

                If you prefer PHTML echo related statement snippets to complete
                in long form, example:

                    <?php echo $var ?>

                Then comment out the following setting.

                The default is is to complete in the short form, example:

                    <?= $var ?>

            -->

            <dict>
                <key>name</key>
                <string>TM_PHP_OPEN_TAG_WITH_ECHO</string>
                <key>value</key>
                <string>=</string>
            </dict>

            <!--

                If you prefer opening braces to be formatted on the same line,
                for example:

                    function name() {

                    }

                Then uncomment the following setting.

                The default is to format braces on the next line, for example:

                    function name()
                    {

                    }

                Note: This may not implemented by all snippets. Please open
                issues and pull requests for those that are missing.

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
