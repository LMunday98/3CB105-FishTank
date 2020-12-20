import sys
import threading

class ThreadController():

    def __init__(self, _controller_array, _process_paramaters):
        print("Thread Controller: create")
        self.controller_array = _controller_array
        self.repeat = _process_paramaters[1]
        self.gpioC = _process_paramaters[4]
        self.threads = []

    def finish_threads(self):
        if (self.repeat == True):
            try:
                input()
            except Exception as e:
                print("*Force Quit*")

        self.gpioC.finish()

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
            if (self.repeat == True):
                print("Threading: daemon")
                for t in self.threads:
                    t.setDaemon(True)

            # start threads
            print("Threading: start")
            for t in self.threads:
                t.start()

            # join threads if not repeating
            if (self.repeat == False):
                print("Threading: join")
                for t in self.threads:
                    t.join()

        except Exception as e:
            print("Threading: error")
