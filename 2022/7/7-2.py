#!/usr/bin/env python

import sys

class File(object):
    def __init__(self, location=None, name=None, size=0):
        self._location = location
        self._name = name
        self._size = size

    @property
    def location(self):
        return self._location

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size


class FileObserver(object):
    def __init__(self):
        self._cwd = '/'
        self._files = []

    def process_cmd(self, cmd):
        if cmd.startswith('$ cd'):
            new_cwd = cmd.split()[2]

            if new_cwd.startswith('/'):
                pass
            elif new_cwd == '..':
                cwd_fragments = self._cwd.split('/')
                if len(cwd_fragments[1:-2]) == 0:
                    new_cwd = '/'
                else:
                    new_cwd = '/' + '/'.join(cwd_fragments[1:-2]) + '/'
            else:
                if self._cwd == '/':
                    new_cwd = '/' + new_cwd + '/'
                else:
                    new_cwd = self._cwd + new_cwd + '/'
            self._cwd = new_cwd
        elif cmd.startswith('$ ls') or cmd.startswith('dir'):
            pass
        else:
            (size, name) = cmd.split()
            try:
                size = int(size)
            except ValueError:
                raise ValueError('Unknown command or input: %s' % (cmd, ))
            new_f = File(location=self._cwd, name=name, size=size)
            self.add_file(new_f)

    def add_file(self, f):
        existing = [x for x in self._files if x.location == f.location and x.name == f.name]
        if len(existing) == 0:
            self._files.append(f)

    def __str__(self):
        ret = ''
        for f in self._files:
            ret += '%d %s%s\n' % (f.size, f.location, f.name)
        return ret

    def all_dirs(self):
        dirs_with_files = set([x.location for x in self._files])
        all_dirs = set()
        for d in dirs_with_files:
            all_dirs.add(d)
            if d != '/':
                fragments = d.split('/')[1:-1]
                for i in range(len(fragments)):
                    all_dirs.add('/' + '/'.join(fragments[:i+1]) + '/')
        return all_dirs

    def dir_total_size(self, dirname):
        all_files = [x for x in self._files if x.location == dirname or x.location.startswith(dirname)]
        return sum([x.size for x in all_files])

    def dir_files_size(self, dirname):
        return sum([x.size for x in self._files if x.location == dirname])

    def dir_sizes(self):
        ret = {}
        all_dirs = self.all_dirs()
        for d in self.all_dirs():
            ret[d] = self.dir_total_size(d)
        return ret

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    fo = FileObserver()

    for l in lines:
        fo.process_cmd(l)

    ds = fo.dir_sizes()

    unused = 70000000 - ds['/']
    required_delete = 30000000 - unused

    # I mean, technically...
    smallest = ds['/']

    for d in ds:
        if ds[d] > required_delete and ds[d] - required_delete < smallest - required_delete:
            smallest = ds[d]

    print('%d' % (smallest, ))


if __name__ == '__main__':
    main()
