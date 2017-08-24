import os

from sublime import packages_path


def plugin_loaded():
    # Disable default PHP package snippets

    _DEFAULT_SNIPPETS = [
        'Constructor.sublime-snippet',
        'PHPDoc-class-var.sublime-snippet',
        'PHPDoc-class.sublime-snippet',
        'PHPDoc-constant-definition.sublime-snippet',
        'PHPDoc-function-signature.sublime-snippet',
        'PHPDoc-function.sublime-snippet',
        'PHPDoc-interface.sublime-snippet',
        'Start-Docblock.sublime-snippet',
        'class-{-}.sublime-snippet',
        'defined(-).sublime-snippet',
        'define(-).sublime-snippet',
        'do-while(-).sublime-snippet',
        'echo-___.sublime-snippet',
        'elseif(-).sublime-snippet',
        'foreach(-).sublime-snippet',
        'for(-).sublime-snippet',
        'function-xx(-).sublime-snippet',
        'if(-)-else(-).sublime-snippet',
        'if(-).sublime-snippet',
        'if-a-b;.sublime-snippet',
        'include(-).sublime-snippet',
        'include_once(-).sublime-snippet',
        'new-array(-).sublime-snippet',
        'php-echo-htmlentities(___).sublime-snippet',
        'php-echo-$this.sublime-snippet',
        'php-echo-___.sublime-snippet',
        'php-else.sublime-snippet',
        'php-foreach-(___)-___-php-endforeach.sublime-snippet',
        'php-if-(___)-___-php-else-___-php-endif.sublime-snippet',
        'php-if-(___)-___-php-endif.sublime-snippet',
        'php-$this.sublime-snippet',
        'php.sublime-snippet',
        'require(-).sublime-snippet',
        'require_once(-).sublime-snippet',
        'return-FALSE;.sublime-snippet',
        'return-TRUE;.sublime-snippet',
        'return-$retVal;.sublime-snippet',
        'switch(-)-case.sublime-snippet',
        'switch(-).sublime-snippet',
        'throw.sublime-snippet',
        'try-{-___-}-catch-(___)-{-___-}.sublime-snippet',
        'while(-).sublime-snippet',
        '$GLOBALS[''].sublime-snippet',
        '$_COOKIE[''].sublime-snippet',
        '$_ENV[''].sublime-snippet',
        '$_FILES[''].sublime-snippet',
        '$_GET[''].sublime-snippet',
        '$_POST[''].sublime-snippet',
        '$_REQUEST[''].sublime-snippet',
        '$_SERVER[''].sublime-snippet',
        '$_SESSION[''].sublime-snippet',
    ]

    try:
        dst = os.path.join(packages_path(), 'PHP', 'Snippets')
        tcf = os.path.join(dst, '.disabled-native-php-snippets')

        if not os.path.isfile(tcf):
            print('php-snippets: disable native PHP snippets...')

            if not os.path.isdir(dst):
                os.makedirs(dst)

            for name in _DEFAULT_SNIPPETS:
                dstname = os.path.join(dst, name)
                if not os.path.isfile(dstname):
                    with open(dstname, 'w+', encoding='utf8') as f:
                        f.write('')

            with open(tcf, 'w+', encoding='utf8') as f:
                f.write('')

    except Exception as e:
        print('php-snippets: an error occured disabling native snippets ' + str(e))
