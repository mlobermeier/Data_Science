def test_libraries_installed():
    import numpy
    import pandas
    import matplotlib
    import seaborn

    assert numpy.__version__ is not None
    assert pandas.__version__ is not None
    assert matplotlib.__version__ is not None
    assert seaborn.__version__ is not None
