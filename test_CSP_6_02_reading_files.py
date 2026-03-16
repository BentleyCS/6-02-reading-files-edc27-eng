import CSP_6_02_reading_files as HW

def test_toString():
    assert HW.toString('62_Text.txt') == ("This is a test\nThis is also a test")

def test_longestLine():
    assert HW.longestLine('62_Text.txt') == ("This is also a test")

def test_toBinary():
    assert HW.toBinary('62_Binary.txt') == (['11001100', '00110011', '10101010'])