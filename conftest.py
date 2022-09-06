import pytest


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")


@pytest.fixture(scope="module")   #module действует на весь модуль, Class на весь класс и  function на всю функцию
def set_group():            #предусловие для функций в которые мы вставим эти функции
    print("Enter system")
    yield #команды которые буду выполняться после выполнения теста
    print("Exit system")

# @pytest.mark.run(order=1) задаем очередность