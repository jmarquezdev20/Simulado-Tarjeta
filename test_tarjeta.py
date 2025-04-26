import unittest
from tarjeta import Tarjeta

class TestTarjeta(unittest.TestCase):
    """Clase que contiene las pruebas unitarias para la clase Tarjeta."""

    def setUp(self):
        """Configuración inicial para cada prueba.
        Crea una instancia de la clase Tarjeta con datos de ejemplo.
        """
        self.tarjeta = Tarjeta("Juan", "1234567890123456", 1000)

    def test_consultar_saldo_activa(self):
        """Prueba la funcionalidad de consultar el saldo cuando la tarjeta está activa.
        Verifica que el saldo retornado sea el saldo actual de la tarjeta.
        """
        self.tarjeta.estado = True
        self.tarjeta.consultar_saldo()
        self.assertEqual(self.tarjeta.saldo, 1000)

    def test_recargar_valido(self):
        """Prueba la funcionalidad de recargar saldo con un monto válido.
        Verifica que el saldo de la tarjeta se incremente correctamente.
        """
        self.tarjeta.recargar(500)
        self.assertEqual(self.tarjeta.saldo, 1500)

    def test_recargar_invalido(self):
        """Prueba la funcionalidad de recargar saldo con un monto inválido (negativo).
        Verifica que el saldo de la tarjeta no se modifique.
        """
        self.tarjeta.recargar(-200)
        self.assertEqual(self.tarjeta.saldo, 1000)

    def test_pagar_exitoso(self):
        """Prueba la funcionalidad de pagar con saldo suficiente.
        Verifica que el saldo de la tarjeta disminuya correctamente.
        """
        self.tarjeta.pagar(200)
        self.assertEqual(self.tarjeta.saldo, 800)

    def test_pagar_sin_saldo(self):
        """Prueba la funcionalidad de intentar pagar con saldo insuficiente.
        Verifica que el saldo de la tarjeta no se modifique.
        """
        self.tarjeta.pagar(2000)
        self.assertEqual(self.tarjeta.saldo, 1000)

    def test_activar_desactivar(self):
        """Prueba la funcionalidad de activar y desactivar la tarjeta.
        Verifica que el estado de la tarjeta cambie correctamente.
        """
        self.tarjeta.desactivar()
        self.assertFalse(self.tarjeta.estado)
        self.tarjeta.activar()
        self.assertTrue(self.tarjeta.estado)

if __name__ == '__main__':
    """Punto de entrada para ejecutar las pruebas directamente desde este archivo."""
    unittest.main()