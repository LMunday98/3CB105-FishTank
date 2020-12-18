import sys
import threading

class ThreadController():

    def __init__(self, _controller_array, _repeat):
        print("Thread Controller: create")
        self.controller_array = _controller_array
        self.repeat = _repeat
        self.threads = []

    def finish_threads(self):

        for controller in self.controller_array:
            controller.finish()

    def create_thread(self, targetProcess):
        self.threads.append(threading.Thread(target=self.start_process, args=(targetProcess,)))

    def start_process(self, process):
        process.start()

    def start(self):
        print("Thread Controller: start")
        try:
            # create threads
            print("Threading: create")
            for controller in self.controller_array:
                self.create_thread(controller)

            # set daemon if repeat
            print("Threading: daemon")
            if (self.repeat == True):
                for t in self.threads:
                    t.setDaemon(True)

            # start threads
            print("Threading: start")
            for t in self.threads:
                t.start()

        except Exception as e:
            print("Threading: error")
