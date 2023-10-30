import unittest

import email_check


class TestEmailCheck(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "john.doe@example.edu",
            "jane.doe@example.edu",
            "joe.smith@example.edu",
            "jane.smith@example.edu",
            "john.doe@example.ac.uk",
            "jane.doe@example.ac.uk",
            "joe.smith@example.ac.uk",
            "jane.smith@example.ac.uk",
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertEqual(email_check.check_email(email), "Valid")

    def test_invalid_emails(self):
        invalid_emails = [
            "john.doe@example.com",
            "jane.doe@example.com",
            "joe.smith@example.com",
            "jane.smith@example.com",
            "john.doe@example.org",
            "jane.doe@example.org",
            "joe.smith@example.org",
            "jane.smith@example.org",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertEqual(email_check.check_email(email), "Invalid")


if __name__ == "__main__":
    unittest.main()
