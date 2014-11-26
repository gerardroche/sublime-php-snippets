CHANGELOG
=========

0.5.0-dev (next version)
------------------------

- New snippet: pri - Private class method declaration
- New snippet: pub - Public class method declaration

0.4.0
-----

- Change snippet: c - Add optional "final" modifier
- New snippet: am - Array map a closure
- New snippet: flatten - Flatten an array
- New snippet: rv - Return a variable statement
- New snippet: pre - Print human readable information about a variable and exit
- New snippet: pr - Print human readable information about a variable
- New snippet: vde - Dump information about a variable and exit
- New snippet: vd - Dump information about a variable
- Change snippet: array - Simplified initialising an array
- Change snippet: foreach - Now iterates over value rather than key-value. Use foreachk to iterate over key-value.
- New snippet: foreachk - Foreach key-value statement

0.3.0
-----

- New snippet: m - Class method declaration
- New snippet: i - Interface declaration
- New snippet: f - Function declaration
- New snippet: c - Class declaration
- New snippet: t - trait declaration
- New snippet: use - Namespace use declaration
- New snippet: ns - Namespace declaration
- New snippet: &lt;? - script start tag
- :bugfix: doc_* snippets cursor exit point should be indented on line between braces
- Refactor: Rename snippets using the tab trigger as the filename & organise into scope specific folders
  source.php scope snippets are now in the scope/ folder and html scope, i.e.
  phtml, are now in a phtml/ folder.
- Change snippet switch/case field names to "expression"
- Change snippet echo string snippet to single quotes
- Change snippet field names from expressions to "condition"

0.2.0
-----

- :bugfix: Snippets should be based on PHP ~5 ([Semantic Version](http://semver.org))
- Use descriptive field names; try to avoid names like foo, bar, baz, etc.
- Change snippet: Add visibility field to class constructor
- :bugfix: Limit scope of "this" to valid contexts
- Change field comment style `# code...` to `// code...`
- :bugfix: Class PHPDoc missing space prefix
- :bugfix: PSR coding standard; No trailing spaces
- Remove `// END ...` comments from PHPDoc
- Add rthis > return $this;
- Add trait
- Add versions of this > $this->| and ethis > echo $this->| that trigger inside php tags
  "this" expands to $this->|
  "ethis" expands to echo $this->|
- :bugfix: Snippets should be PSR compliant; brace should be on next line
- :bugfix: PHPDoc should end with */ not **/
- :bugfix: end of field cycle should be after the semi-colon

0.1.0
-----

* Initial import of PHP snippets from Sublime Text 3 build 3065






