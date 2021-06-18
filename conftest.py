# пытался решить проблему с выводом кириллицы в консоль при генерации репорта
def pytest_make_parametrize_id(config, val): return repr(val)