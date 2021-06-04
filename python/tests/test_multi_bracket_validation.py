from code_challenges.multi_bracket_validation.multi_bracket_validation import multiBracketValidation


def test_import():
    assert multiBracketValidation

def test_bracket_check():
    actual = multiBracketValidation("{}")
    expected = True
    assert actual == expected

def test_bracket_paren():
    actual = multiBracketValidation("{}(){}")
    expected = True
    assert actual == expected

def test_extra_characters():
    actual = multiBracketValidation("()[[Extra Characters]]")
    expected = True
    assert actual == expected

def test_no_ending():
    actual = multiBracketValidation("[({}]")
    expected = False
    assert actual == expected

def test_no_match():
    actual = multiBracketValidation("(](")
    expected = False
    assert actual == expected