from skeleton.__main__ import main

def test_default(capsys):
    ret = main()
    out, err = capsys.readouterr()

    assert ret == 0
    assert out == "Greetings Elvis !\n"
    assert err == ""


def test_one_name(capsys):
    ret = main(["--names", "Adrien"])
    out, err = capsys.readouterr()

    assert ret == 0
    assert out == "Greetings Adrien !\n"
    assert err == ""

def test_many_names(capsys):
    ret = main(["--names", "Adrien", "Ileyk"])
    out, err = capsys.readouterr()

    assert ret == 0
    assert out == "Greetings Adrien !\nGreetings Ileyk !\n"
    assert err == ""
