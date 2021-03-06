from augustus.cipher import SteppedAugustus


def test_SteppedAugustus_right_cipher():
    s0 = SteppedAugustus("Hello World")
    s1 = SteppedAugustus("Hello\tWorld")
    s2 = SteppedAugustus("Hello\nWorld")
    s3 = SteppedAugustus("á, à, â, é, è, ê, í, ì, î, ó, ò, ô, ú, ù, û")

    assert s0.right_cipher == "Igopt Xqupi"
    assert s1.right_cipher == "Igopt\tXqupi"
    assert s2.right_cipher == "Igopt\nXqupi"
    assert s3.right_cipher == "á, à, â, é, è, ê, í, ì, î, ó, ò, ô, ú, ù, û"


def test_SteppedAugustus_left_cipher():
    s0 = SteppedAugustus("Igopt Xqupi")
    s1 = SteppedAugustus("Igopt\tXqupi")
    s2 = SteppedAugustus("Igopt\nXqupi")
    s3 = SteppedAugustus("á, à, â, é, è, ê, í, ì, î, ó, ò, ô, ú, ù, û")

    assert s0.left_cipher == "Hello World"
    assert s1.left_cipher == "Hello\tWorld"
    assert s2.left_cipher == "Hello\nWorld"
    assert s3.left_cipher == "á, à, â, é, è, ê, í, ì, î, ó, ò, ô, ú, ù, û"


def test_SteppedAugustus_stop_chars():
    s0 = SteppedAugustus("Hello World", stop_chars="aeiou")
    s1 = SteppedAugustus("Hello World", stop_chars=set("aeiou"))

    assert s0.right_cipher == "Ifnop Xptoh"
    assert s0.left_cipher == "Gdjin Vnpiz"

    assert s1.right_cipher == "Ifnop Xptoh"
    assert s1.left_cipher == "Gdjin Vnpiz"


def test_SteppedAugustus_skip_chars():
    s0 = SteppedAugustus("Hello World", skip_chars="Hello World")
    s1 = SteppedAugustus("Hello World", skip_chars=set("Hello World"))

    assert s0.right_cipher == "Hello World"
    assert s0.left_cipher == "Hello World"

    assert s1.right_cipher == "Hello World"
    assert s1.left_cipher == "Hello World"
