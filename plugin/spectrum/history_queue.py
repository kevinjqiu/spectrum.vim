
class HistoryQueue(object):

    def __init__(self, max_size=None):
        self._max_size = max_size
        self._q = []
        self._cur_idx = 0

    def current(self):
        return self._q[self._cur_idx]

    def set_current(self, colorscheme):
        """
        >>> q=HistoryQueue(1)
        >>> q.set_current('cs1')
        >>> q.current()
        'cs1'
        >>> q._q
        ['cs1']
        >>> q._cur_idx
        0
        >>> q.set_current('cs2')
        >>> q.current()
        'cs2'
        >>> q._q
        ['cs2']
        >>> q._cur_idx
        0
        >>> q=HistoryQueue()
        >>> q.set_current('cs1')
        >>> q.set_current('cs2')
        >>> q.set_current('cs3')
        >>> q.current()
        'cs3'
        >>> q._q
        ['cs1', 'cs2', 'cs3']
        >>> q._cur_idx
        2
        """
        del self._q[self._cur_idx+1:]
        self._q.append(colorscheme)
        self._cur_idx = len(self._q)-1
        self._trim()

    def previous(self):
        """
        >>> q=HistoryQueue(3)
        >>> q.set_current('cs1')
        >>> q.set_current('cs2')
        >>> q.set_current('cs3')
        >>> q.current()
        'cs3'
        >>> q.previous()
        'cs2'
        >>> q.previous()
        'cs1'
        >>> q.previous()
        Traceback (most recent call last):
        ...
        StandardError: Already at the first colorscheme
        """
        if self._cur_idx == 0:
            raise StandardError('Already at the first colorscheme')
        self._cur_idx -= 1
        return self._q[self._cur_idx]

    def next(self):
        """
        >>> q=HistoryQueue(3)
        >>> q.set_current('cs1')
        >>> q.set_current('cs2')
        >>> q.set_current('cs3')
        >>> q.previous()
        'cs2'
        >>> q.previous()
        'cs1'
        >>> q.next()
        'cs2'
        >>> q.next()
        'cs3'
        >>> q.next()
        Traceback (most recent call last):
        ...
        StandardError: Already at the latest colorscheme
        """
        if self._cur_idx == len(self._q)-1:
            raise StandardError('Already at the latest colorscheme')
        self._cur_idx += 1
        return self._q[self._cur_idx]

    def _is_full(self):
        return self._cur_idx == self._max_size-1

    def _trim(self):
        if self._max_size is not None:
            extra_items = len(self._q) - self._max_size
            if extra_items > 0:
                del self._q[:extra_items]
                self._cur_idx -= extra_items

    def __str__(self):
        output = []
        for idx in xrange(0, len(self._q)):
            if idx == self._cur_idx:
                output.append("*%s*"%self._q[idx])
            else:
                output.append(self._q[idx])
        return "[%s]"%(",".join(output))
