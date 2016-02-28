import unittest

import fetch


class TestController(unittest.TestCase):
    def setUp(self):
        self.valid_measurements = [
            ('M 1234 ', 1234),
        ]
        self.valid_buttons = [
            ('BTN A \n', 'A'),
            ('BTN B \n', 'B'),
        ]
        self.invalid = ['', 'XX']
        self.controller = fetch.Controller(None)

    def test_matches_valid_measurements(self):
        for stream in self.invalid:
            self.assertIsNone(self.controller.is_measurement(stream))

    def test_matches_valid_measurements(self):
        for stream, value in self.valid_measurements:
            measurement = self.controller.is_measurement(stream)
            self.assertIsNotNone(measurement)
            self.assertEqual(value, measurement)

    def test_matches_valid_button(self):
        for stream, value in self.valid_buttons:
            button = self.controller.is_button(stream)
            self.assertIsNotNone(button)
            self.assertEqual(value, button)
