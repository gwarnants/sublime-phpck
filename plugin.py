import os
import sublime

def plugin_loaded():

    disable_native_php_package_completions()

def disable_native_php_package_completions():

    completions_file = os.path.join(
        sublime.packages_path(),
        'PHP',
        'PHP.sublime-completions'
    )

    if not os.path.isfile(completions_file):
        try:
            polyfill_makedirs(os.path.dirname(completions_file))
            polyfill_writefile(completions_file, '// created by php-completions (PHP Completions Kit) to disable the native PHP package completions')
        except:
            pass

def polyfill_writefile(path, content):

    with open(path, 'w+', encoding='utf8', newline='') as f:
        f.write(str(content))

    if 3000 <= int(sublime.version()) < 3088:
        # Fixes as best as possible a new file permissions issue
        # See https://github.com/titoBouzout/SideBarEnhancements/issues/203
        # See https://github.com/SublimeTextIssues/Core/issues/239
        oldmask = os.umask(0o000)
        if oldmask == 0:
            os.chmod(path, 0o644)
        os.umask(oldmask)


def polyfill_makedirs(path):

    if 3000 <= int(sublime.version()) < 3088:
        # Fixes as best as possible a new directory permissions issue
        # See https://github.com/titoBouzout/SideBarEnhancements/issues/203
        # See https://github.com/SublimeTextIssues/Core/issues/239
        oldmask = os.umask(0o000)
        if oldmask == 0:
            os.makedirs(path, 0o755);
        else:
            os.makedirs(path);
        os.umask(oldmask)
    else:
        os.makedirs(path)
