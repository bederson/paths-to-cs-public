class System():
    def __init__(self):
        self.callbacks = []

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def main_loop(self):
        while True:
            print "Input:",
            input = raw_input()
            if input == "quit":
                break
            else:
                for callback in self.callbacks:
                    callback(input)