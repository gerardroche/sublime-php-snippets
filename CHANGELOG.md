# Changelog

## 0.6.0

### Bug Fixes

- Fixed: `class` snippet field cycle didn't work

### New Features

- Added: `r` - Return statement
- Added: `p` - Class property declaration
- Added: `fpro` - Final protected class method declaration
- Added: Visibility field to `class`

### Changes

- Changed: Return `$this` statement trigger renamed from `rthis` to `rt`
- Changed: Namespace declaration trigger renamed from `ns` to `n`

## 0.5.0

### New Features

- Added: `closure` - Closure declaration
- Added: `fpri` - Final private class method declaration
- Added: `fpris` - Final private static class method declaration
- Added: `fpub` - Final public class method declaration
- Added: `fpubs` - Final public static class method declaration
- Added: `pri` - Private class method declaration
- Added: `pro` - Protected class method declaration
- Added: `pub` - Public class method declaration
- Added: `pubs` - Public static class method declaration

## 0.4.0

### Changes

- Changed: Simplified initialising an `array`
- Changed: `c` Added "final" modifier to class
- Changed: `foreach` now iterates over value rather than key-value. Use `foreachk` to iterate over a key and value

### New Features

- Added: `am` - Array map a closure
- Added: `flatten` - Flatten an array
- Added: `foreachk` - Foreach key-value statement
- Added: `pr` - Print human readable information about a variable
- Added: `pre` - Print human readable information about a variable and exit
- Added: `rv` - Return a variable statement
- Added: `vd` - Dump information about a variable
- Added: `vde` - Dump information about a variable and exit

## 0.3.0

### Bug Fixes

- Fixed: doc_* snippets cursor exit point should be indented on line between braces

### New Features

- Added: `&lt;?` - Script start tag
- Added: `c` - Class declaration
- Added: `f` - Function declaration
- Added: `i` - Interface declaration
- Added: `m` - Class method declaration
- Added: `ns` - Namespace declaration
- Added: `t` - Trait declaration
- Added: `use` - Namespace use declaration

### Changes

- Changed: echo string snippet to single quotes
- Changed: field names from expressions to "condition"
- Changed: switch/case field names to "expression"
- Changed: Renamed snippets using the tab trigger as the filename & organise into scope specific folders

## 0.2.0

### Bug Fixes

- Fixed: Class PHPDoc missing space prefix
- Fixed: End of field cycle should be after the semi-colon
- Fixed: Limit scope of `this` snippet to valid contexts
- Fixed: PHPDoc should end with `*/` not `**/`
- Fixed: PSR coding standard; No trailing spaces
- Fixed: Removed `// END ...` comments from PHPDoc
- Fixed: Snippets should be based on PHP ~5 ([Semantic Version](http://semver.org))
- Fixed: Snippets should be PSR compliant; brace should be on next line

### New Features

- Added: `rthis` - Return $this; statement
- Added: `trait` - Trait declaration
- Added: `this` - `$this->|` (phtml)
- Added: `ethis` - `echo $this->|` (phtml)

### Changes

- Changed: Field comment style changed from `# code...` to `// code...`
- Changed: Add visibility field to class constructor

## 0.1.0

* Initial import of PHP snippets from Sublime Text 3 build 3065






