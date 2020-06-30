new = lambda: {}


def _append(name, value, fd):
    fd[name] = value


def _appendBlob(name, value, filename, fd):
    fd[name] = (value, filename)


def _delete(name, fd):
    del fd[name]


def _has(name, fd):
    return name in fd


def _set(name, value, fd):
    fd[name] = value


def _setBlob(name, value, filename, fd):
    fd[name] = (value, filename)
