from tensor_test import YandexSearch

yandex = YandexSearch()


def test_search_in_yandex():
    assert yandex.search_in_yandex() is True


def test_search_suggest():
    assert yandex.search_suggest() is True


def test_search_links_in_result():
    links = yandex.search_links_in_result()
    assert 'tensor.ru' in links


def test_check_link_yandex_image():
    link = yandex.check_link_yandex_image()
    assert 'https://yandex.ru/images/' in link


def test_check_first_category():
    assert yandex.check_first_category() is True


def test_check_open_first_img():
    assert yandex.open_first_image() is True


def test_check_btn_next():
    assert yandex.check_button_next() is True


def test_check_btn_prev():
    assert yandex.check_button_prev() is True
