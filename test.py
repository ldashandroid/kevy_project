# Assumptions and Notes
# I assumed here that secret is a python function and not a string that would eval to a python function
#

import unittest
from prime_check import is_prime, check_if_secret_is_additive, MyException
class TestIsPrime(unittest.TestCase):
    def setUp(self):
	pass
    
    def test_is_prime(self):
	self.assertTrue(is_prime(5))
	self.assertFalse(is_prime(8))


class TestSecret(unittest.TestCase):
    def setUp(self):
	pass

    def test_additive_secret(self):
	self.assertEqual(mock_additive_secret(2+3),
                        (mock_additive_secret(2) + mock_additive_secret(3)))
        self.assertIsInstance(mock_additive_secret(2), int)

    def test_non_additive_secret(self):
	self.assertNotEqual(mock_nonadditive_secret(2+3),
                           (mock_nonadditive_secret(2) + mock_nonadditive_secret(3)))
        
	self.assertIsInstance(mock_nonadditive_secret(2), int)

class TestPrimesAndSecret(unittest.TestCase):
    def setUp(self):
	pass

    def test_check_if_secret_is_additive(self):
	self.assertTrue(check_if_secret_is_additive(mock_additive_secret, 5000))
	self.assertFalse(check_if_secret_is_additive(mock_nonadditive_secret, 5000))
	with self.assertRaises(MyException):
	    check_if_secret_is_additive(mock_additive_secret, 10000000000)

	with self.assertRaises(MyException):
	    check_if_secret_is_additive(mock_additive_secret, 1)


def mock_additive_secret(x):
    return x

def mock_nonadditive_secret(x):
    return 1

if __name__ == "__main__":
    unittest.main()

