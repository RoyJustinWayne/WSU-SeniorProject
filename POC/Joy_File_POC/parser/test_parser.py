import unittest
import pi_parser

class TestParser(unittest.TestCase):

    def test_file_exists(self):
        result = pi_parser.check_exist("sensor_data.txt")
        self.assertTrue(result)

    def test_check_health(self):
        result1 = pi_parser.database_health_status()
        self.assertEqual(result1, "database OK")

if __name__ == '__main__':
    unittest.main()