import importlib.util
import unittest
from dataclasses import dataclass
from pathlib import Path

path = Path(__file__).parents[1] / 'custom_components/maestro_rtinfo/fields.py'
spec = importlib.util.spec_from_file_location('fields', path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class FieldTests(unittest.TestCase):
    def test_values_and_private(self):
        @dataclass
        class State:
            temp_fumi: int = 22
            pwd_wifi: str = 'secret'
            unknown_fields: object = None
        data = State(unknown_fields={'new_sensor': 17, 'auth_token': 'secret', 'empty': None})
        self.assertEqual(mod.values(data), {'temp_fumi': 22, 'new_sensor': 17})

    def test_state_has_priority_and_false_is_kept(self):
        class Stove:
            Status = {'value': 3, 'flag': True}
            State = {'value': 0, 'flag': False}
        self.assertEqual(mod.snapshot(Stove()), {'value': 0, 'flag': False})

    def test_unavailable_values_not_exposed(self):
        self.assertEqual(mod.values({'no': None, 'nested': [1], 'long': 'x' * 256}), {})


if __name__ == '__main__':
    unittest.main()
