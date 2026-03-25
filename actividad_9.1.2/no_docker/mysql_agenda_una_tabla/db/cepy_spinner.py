import sys
import threading
import time


class CepySpinner:
    GREEN = "\033[32m"  # verde
    RESET = "\033[0m"  # resetear color

    def __init__(self, message="", type=0, delay=0.3, end_symbol="✔"):
        self.message = message
        self.type = type
        self.delay = delay
        self._spinner_activo = False
        self.end_symbol = end_symbol

    def start(self):
        if not self._spinner_activo:
            self._spinner_activo = True
            match self.type:
                case 0:
                    self.simbolos = "."
                    self.numero_iteraciones = 3
                    self._hilo_spinner = threading.Thread(target=self._spinner_v1)
                case 1:
                    self.simbolos = "■"
                    self.numero_iteraciones = 10
                    self._hilo_spinner = threading.Thread(target=self._spinner_v1)
                case 2:
                    self.simbolos = "|/-\\"
                    self._hilo_spinner = threading.Thread(target=self._spinner_v2)
                case 3:
                    self.simbolos = "⠋⠙⠹⠸⠼⠴⠦⠧⠇"
                    self._hilo_spinner = threading.Thread(target=self._spinner_v2)
                case 4:
                    self.simbolos = "▁▂▃▄▅▆▇█▇▆▅▄▃▂"
                    self._hilo_spinner = threading.Thread(target=self._spinner_v2)
                case 5:
                    self.simbolos = "🌑🌒🌓🌔🌕🌖🌗🌘"
                    self._hilo_spinner = threading.Thread(target=self._spinner_v2)
                case _:
                    self.simbolos = "⠋⠙⠹⠸⠼⠴⠦⠧⠇"
                    self._hilo_spinner = threading.Thread(target=self._spinner_v2)
            self._hilo_spinner.start()

    def _spinner_v1(self):
        i = 0
        while self._spinner_activo:
            simbolos = self.simbolos * (i % self.numero_iteraciones + 1)
            sys.stdout.write(f"\r{self.message} {simbolos}")
            sys.stdout.flush()
            time.sleep(self.delay)
            i += 1
        print(f"\r{self.message} {self.GREEN}{self.end_symbol}{self.RESET}")


    def _spinner_v2(self):
        i = 0
        while self._spinner_activo:
            sys.stdout.write(f"\r{self.message} {self.simbolos[i % len(self.simbolos)]}")
            sys.stdout.flush()
            time.sleep(self.delay)
            i += 1
        print(f"\r{self.message} {self.GREEN}{self.end_symbol}{self.RESET}")

    def stop(self):
        self._spinner_activo = False
        self._hilo_spinner.join()

if __name__ == "__main__":
    hilo = CepySpinner()
    hilo.start()
    time.sleep(5)
    hilo.stop()

    hilo = CepySpinner("Conectando")
    hilo.start()
    time.sleep(5)
    hilo.stop()

    hilo = CepySpinner(message="Conectando", type=1)
    hilo.start()
    time.sleep(5)
    hilo.stop()

    hilo = CepySpinner(message="Conectando", type=2)
    hilo.start()
    time.sleep(5)
    hilo.stop()

    hilo = CepySpinner(message="Conectando", type=3)
    hilo.start()
    time.sleep(5)
    hilo.stop()

    hilo = CepySpinner(message="Conectando", type=4)
    hilo.start()
    time.sleep(5)
    hilo.stop()

    hilo = CepySpinner(message="Conectando", type=5)
    hilo.start()
    time.sleep(5)
    hilo.stop()







