from unittest import TestCase
from printer import Printer, PrinterError

class TestPrinter(TestCase):
    # @classmethod # used when we reuse same printer for every test
    # def setUpClass(cls) -> None: # this method will run only once for entire test, same printer for every test
    #     cls.printer = Printer(pages_per_s = 2.0, capacity = 300)

    # setUp runs before each test    
    def setUp(self): # new printer for every test, create new object for each test
        self.printer = Printer(pages_per_s = 2.0, capacity = 300)
    
    # teardown runs after each test

    def test_print_within_capacity(self):
        message = self.printer.print(25)
        self.assertEqual(f"Printed 25 pages in 12.50 seconds", message)

    def test_print_within_capacity(self):
        self.printer.print(25)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 20
        expected = "Printed 20 pages in 10.00 seconds"
        result = self.printer.print(pages)
        self.assertEqual(result, expected)

    def test_speed_always_two_decimals(self):
        fast_printer = Printer(pages_per_s = 3.0, capacity = 300)
        result = fast_printer.print(11)
        expected = "Printed 11 pages in 3.67 seconds"
        self.assertEqual(result, expected)

    def test_multiple_runs_end_up_error(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

        with self.assertRaises(PrinterError):
            self.printer.print(1)
    