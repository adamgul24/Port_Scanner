import unittest
from port_scanner import scan_port

class TestPortScanner(unittest.TestCase):

    def test_scan_port_open(self):
        # Assuming port 80 is open (common for HTTP)
        self.assertTrue(scan_port("www.example.com", 80))

    def test_scan_port_closed(self):
        # Assuming a high port number is closed
        self.assertFalse(scan_port("www.example.com", 65000))

if __name__ == '__main__':
    unittest.main()
