# sublime-php-snippets changelog

## 0.9.0

* `phtml` snippets now use php short tags by default i.e. `<?= $var ?>` vs `<?php echo $var ?>`. See the readme [configuration section](https://github.com/gerardroche/sublime-php-snippets#configuration) for more details on how to configure the old behaviour. 

## 0.8.0

* PHPDoc field names "description" changed to "summary" as per [PHPDoc specification](http://phpdoc.org/docs/latest/guides/docblocks.html)
* Method snippets like `pub` and `pri` now prefill `$` in argument fields
* All snippets now target more specific scopes to minimise auto-complete noise
* `class` snippet PHPDoc is now deletable
* `class` snippet constructor has a new deletable PHPDoc
* Deleting the `class` snippet extends field deletes the extend keyword
* Changed snippet: `class` - Simplified constructor field
* Added new snippet `getter`: basic class method getter
* Added new snippet `setter`: basic class method setter

## 0.7.0

* Renamed some snippet file names to avoid issues on some systems
* Last field in a snippets field cycle is longer `// code...`, it's now blank
* Added visibility modifier field to `trait` snippet
* Added new snippet `self`: Expands to `self::`
* Added new snippet `this`: A variation of `this` snippet that works in a variable scope i.e. both `this` and `$this` now expand to `$this->`
* Fixed `for` snippet PSR coding standard

## 0.6.0

* Changed Return `$this` statement trigger renamed from `rthis` to `rt`
* Changed Namespace declaration trigger renamed from `ns` to `n`
* Added new snippet `r`: Return statement
* Added new snippet `p`: Class property declaration
* Added new snippet `fpro`: Final protected class method declaration
* Added: Visibility field to `class`
* Fixed `class` snippet field cycle didn't work

## 0.5.0
* Added new snippet `closure`: Closure declaration
* Added new snippet `fpri`: Final private class method declaration
* Added new snippet `fpris`: Final private static class method declaration
* Added new snippet `fpub`: Final public class method declaration
* Added new snippet `fpubs`: Final public static class method declaration
* Added new snippet `pri`: Private class method declaration
* Added new snippet `pro`: Protected class method declaration
* Added new snippet `pub`: Public class method declaration
* Added new snippet `pubs`: Public static class method declaration

## 0.4.0

* Changed Simplified initialising an `array`
* Changed `c` Added "final" modifier to class
* Changed `foreach` now iterates over value rather than key-value. Use `foreachk` to iterate over a key and value
* Added new snippet `am`: Array map a closure
* Added new snippet `flatten`: Flatten an array
* Added new snippet `foreachk`: Foreach key-value statement
* Added new snippet `pr`: Print human readable information about a variable
* Added new snippet `pre`: Print human readable information about a variable and exit
* Added new snippet `rv`: Return a variable statement
* Added new snippet `vd`: Dump information about a variable
* Added new snippet `vde`: Dump information about a variable and exit

## 0.3.0

* Changed echo string snippet to single quotes
* Changed field names from expressions to "condition"
* Changed switch/case field names to "expression"
* Changed Renamed snippets using the tab trigger as the filename & organise into scope specific folders
* Added new snippet `&lt;?`: Script start tag
* Added new snippet `c`: Class declaration
* Added new snippet `f`: Function declaration
* Added new snippet `i`: Interface declaration
* Added new snippet `m`: Class method declaration
* Added new snippet `ns`: Namespace declaration
* Added new snippet `t`: Trait declaration
* Added new snippet `use`: Namespace use declaration
* Fixed `doc_*` snippets cursor exit point should be indented on line between braces

## 0.2.0

* Changed Field comment style changed from `# code...` to `// code...`
* Changed Add visibility field to class constructor
* Fixed Class PHPDoc missing space prefix
* Fixed End of field cycle should be after the semi-colon
* Fixed Limit scope of `this` snippet to valid contexts
* Fixed PHPDoc should end with `*/` not `**/`
* Fixed PSR coding standard; No trailing spaces
* Fixed Removed `// END ...` comments from PHPDoc
* Fixed Snippets should be based on PHP ~5 ([Semantic Version](http://semver.org))
* Fixed Snippets should be PSR compliant; brace should be on next line
* Added new snippet `rthis`: Return $this; statement
* Added new snippet `trait`: Trait declaration
* Added new snippet `this`: `$this->|` (phtml)
* Added new snippet `ethis`: `echo $this->|` (phtml)

## 0.1.0

* Initial import of PHP snippets from Sublime Text 3 build 3065






