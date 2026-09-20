"""Testes automatizados das regras de negócio. Execute: python -m unittest -v"""

import unittest

from app import (
    classificar_consumo,
    MSG_COMERCIAL,
    MSG_ECONOMICO,
    MSG_MODERADO,
    MSG_EXCESSIVO,
)


class TestClassificarConsumo(unittest.TestCase):
    def test_comercial_qualquer_consumo(self):
        for consumo in (0, 5, 25, 300):
            self.assertEqual(classificar_consumo("comercial", consumo), MSG_COMERCIAL)

    def test_apartamento_economico(self):
        self.assertEqual(classificar_consumo("apartamento", 0), MSG_ECONOMICO)
        self.assertEqual(classificar_consumo("apartamento", 9.99), MSG_ECONOMICO)

    def test_apartamento_limite_10_ja_e_moderado(self):
        self.assertEqual(classificar_consumo("apartamento", 10), MSG_MODERADO)

    def test_apartamento_moderado_ate_25(self):
        self.assertEqual(classificar_consumo("apartamento", 25), MSG_MODERADO)

    def test_apartamento_excessivo_acima_de_25(self):
        self.assertEqual(classificar_consumo("apartamento", 25.01), MSG_EXCESSIVO)

    def test_casa_moderada_ate_25(self):
        # Casa nunca é "econômica": a regra do consumo baixo vale só para apartamento
        self.assertEqual(classificar_consumo("casa", 5), MSG_MODERADO)
        self.assertEqual(classificar_consumo("casa", 25), MSG_MODERADO)

    def test_casa_excessiva_acima_de_25(self):
        self.assertEqual(classificar_consumo("casa", 25.1), MSG_EXCESSIVO)


if __name__ == "__main__":
    unittest.main()
