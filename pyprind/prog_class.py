import time
import sys
import os

class Prog():
    def __init__(self, iterations, track_time, stream):
        self.cnt = 0
        self.max_iter = float(iterations) # accommodation for Python 2.x users
        self.track = track_time
        self.time = [time.clock(), 0]
        self.stream = stream
        self.__check_stream()
        
    def __check_stream(self):
        if self.stream == 1 and os.isatty(sys.stdout.fileno()):
            self._stream_out = sys.stdout.write
            self._stream_flush = sys.stdout.flush
        elif self.stream == 2 and os.isatty(sys.stderr.fileno()):
            self._stream_out = sys.stderr.write
            self._stream_flush = sys.stderr.flush
        else:
            print('Warning: No valid output stream.')
            self._stream_out = self._no_stream
            self._stream_flush = self._no_stream       
 
    def _no_stream(self, text=None):
        pass