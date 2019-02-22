import sys
import string
import re

def tab(before):
    '''
    Replace tab character with HTML icon.
    '''
    return before + '\u21e5'

def backspace(before):
    '''
    Delete one character from the left.
    '''
    if len(before):
        return before[0:-1]
    else:
        return before

SCREEN_CODES = {
    '\x07': tab,
    '\x08': backspace,
}

ESCAPE_CODES = re.compile(r'\x1b(>|=|M|\[(J|K|C|m|H|1@|\d[a-zA-Z]|\?\w{2}|\d{1,2};\d{1,2}\w|\d{1,2}[a-zA-Z]))', re.UNICODE)

def fold(before, ch, after):
    while True:
        if ch in SCREEN_CODES:
            left = SCREEN_CODES[ch](before)
        else:
            left = before + ch
        if len(after) == 0:
            return left
        else:
            before, ch, after = left, after[0], after[1:]

def sanitize(line):
    '''
    Remove all non-printable characters
    '''
    preclean = ESCAPE_CODES.sub('', line)
    return fold('', '', preclean)

def is_prompt(line):
    '''
    Returns `True` if <line> begins with a bash prompt.
    '''
    prompt = 'bash-3.2$ '
    return line[0:len(prompt)] == prompt 

def filter_prompt(line):
    '''
    Returns a sanitized version of the prompt.
    '''
    return '$'.join(line.split('$')[1:])

class Parser(object):
    def __init__(self, iterator):
        '''
        Returns an iterator of parsed lines.
        '''
        # start in an input box
        self.state = 'bash'
        self._reader = iter(iterator)
        self._buffer = ''
        self.MAX_BUFFER_SIZE = 2000

    def flush_buffer(self):
        if not self.state == 'empty':
            buffer = self._buffer
            self._buffer = ''
            return '~~~' + buffer + '\n~~~\n{{: .{}}}\n'.format(self.state)
        else:
            self._buffer = ''
            return '~~~\n<Output omitted for brevity.>\n~~~\n'

    def push_buffer(self, line):
        if len(self._buffer) > self.MAX_BUFFER_SIZE:
            self.state = 'empty'
        if not self.state == 'empty':
            self._buffer += '\n' + line

    def iter(self):
        for line in self._reader:
            output = self.parse_line(line)
            if output:
                yield output

    def parse_line(self, line):
        if is_prompt(line):
            if not self.state == 'bash':
                # close output box, open an new input box and switch to bash state
                output = self.flush_buffer()
                self.state = 'bash'
                self.push_buffer(filter_prompt(line))
                return output
            else:
                # continue with input box 
                self.push_buffer(filter_prompt(line))
        else:
            if self.state == 'bash':
                # close input box, open a new output box and switch to output state
                output = self.flush_buffer()
                self.state = 'output'
                self.push_buffer(filter_prompt(line))
                return output
            else:
                # continue with output box
                self.push_buffer(line)

if __name__ == '__main__':
    sanitized_lines = [sanitize(line) for line in sys.stdin.read().splitlines()]
    for line in Parser(sanitized_lines).iter():
        print(line)
