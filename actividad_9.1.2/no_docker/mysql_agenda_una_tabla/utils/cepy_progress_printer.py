import sys


class CepyProgressPrinter:
    """Clase para imprimir progreso en consola con colores y porcentaje."""

    ANSI_AZUL = "\033[34m"
    ANSI_VERDE = "\033[32m"
    ANSI_ROJO = "\033[31m"
    ANSI_RESET = "\033[0m"

    def __init__(self, msg: str, total: int, color = ANSI_AZUL):
        self.total = total
        self.msg = msg
        self.color = color

    def update(self, paso: int):
        porcentaje = (paso / self.total) * 100
        sys.stdout.write(f"\r{self.color}{self.msg}: {paso}/{self.total} ({porcentaje:.1f}%){self.ANSI_RESET}")
        sys.stdout.flush()

    def finish(self, mensaje="Generación completada."):
        print(f"\n{self.ANSI_VERDE}{mensaje}{self.ANSI_RESET}")

    def check_finish(self, ):
        print(f" {self.ANSI_VERDE}\u2714{self.ANSI_RESET}")
        # ✔️  \u2714