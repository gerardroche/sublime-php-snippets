CHANGELOG
=========

0.6.0
-----

- 9bd8ee7 Fixed class snippet: field cycle was broken
- 88702fd Changed return $this statement trigger from rthis to rt
- 3c5eb86 Changed namespace declaration snippet ns to n
- 146c31b Changed class snippet: Added visibility
- f20daf5 New snippet: r - Return statement [Gerard Roche]
- f82e9e2 New snippet: p - Class property declaration
- c6a4806 New snippet: fpro - Final protected class method declaration

0.5.0
-----

- Added: closure - Closure declaration
- Added: fpri - Final private class method declaration
- Added: fpris - Final private static class method declaration
- Added: fpub - Final public class method declaration
- Added: fpubs - Final public static class method declaration
- Added: pri - Private class method declaration
- Added: pro - Protected class method declaration
- Added: pub - Public class method declaration
- Added: pubs - Public static class method declaration

0.4.0
-----

- Changed: array - Simplified initialising an array
- Changed: c - Add optional "final" modifier
- Changed: foreach - Now iterates over value rather than key-value. Use foreachk to iterate over key-value
- Added: am - Array map a closure
- Added: flatten - Flatten an array
- Added: foreachk - Foreach key-value statement
- Added: pr - Print human readable information about a variable
- Added: pre - Print human readable information about a variable and exit
- Added: rv - Return a variable statement
- Added: vd - Dump information about a variable
- Added: vde - Dump information about a variable and exit

0.3.0
-----

- Fixed: doc_* snippets cursor exit point should be indented on line between braces
- Changed: echo string snippet to single quotes
- Changed: field names from expressions to "condition"
- Changed: switch/case field names to "expression"
- Refactored: Rename snippets using the tab trigger as the filename & organise into scope specific folders
- Added: &lt;? - script start tag
- Added: c - Class declaration
- Added: f - Function declaration
- Added: i - Interface declaration
- Added: m - Class method declaration
- Added: ns - Namespace declaration
- Added: t - trait declaration
- Added: use - Namespace use declaration

0.2.0
-----

- Fixed: Class PHPDoc missing space prefix
- Fixed: End of field cycle should be after the semi-colon
- Fixed: Limit scope of `this` snippet to valid contexts
- Fixed: PHPDoc should end with `*/` not `**/`
- Fixed: PSR coding standard; No trailing spaces
- Fixed: Removed `// END ...` comments from PHPDoc
- Fixed: Snippets should be based on PHP ~5 ([Semantic Version](http://semver.org))
- Fixed: Snippets should be PSR compliant; brace should be on next line
- Changed: Field comment style changed from `# code...` to `// code...`
- Changed: Add visibility field to class constructor
- Added: rthis - return $this;
- Added: trait - Trait declaration
- Added: (phtml) this - `$this->|`
- Added: (phtml) ethis - `echo $this->|`

0.1.0
-----

* Initial import of PHP snippets from Sublime Text 3 build 3065






