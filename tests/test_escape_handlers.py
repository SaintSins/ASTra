import unittest
from src.escape_handlers import escape_map, hide_escape_chars, restore_string

class TestEscapeHandlers(unittest.TestCase):
    
    def test_hide_single_asterisk(self) -> None:
        raw_text = "This is a literal \\* asterisk"
        result = hide_escape_chars(raw_text, escape_map)
        self.assertIn("@@@ESCAST@@@", result)
        self.assertNotIn("\\*", result)

    def test_restore_single_asterisk(self) -> None:
        hidden_text = "A literal @@@ESCAST@@@ character"
        # Now passing just the string and the map!
        result = restore_string(hidden_text, escape_map)
        self.assertEqual(result, "A literal * character")
    
    def test_multiple_escapes_in_one_string(self) -> None:
        raw_text = r"Click \*here\* or \_there\_"
        hidden_text = hide_escape_chars(raw_text, escape_map)
        
        # Directly restoring the string
        result = restore_string(hidden_text, escape_map)
        self.assertEqual(result, "Click *here* or _there_")

    def test_escaped_backslash(self) -> None:
        raw_text = r"\\"
        hidden_text = hide_escape_chars(raw_text, escape_map)
        
        result = restore_string(hidden_text, escape_map)
        self.assertEqual(result, "\\")

if __name__ == "__main__":
    unittest.main()