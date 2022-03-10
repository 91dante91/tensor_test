from YandexPages import SearchHelper


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    all_links = yandex_main_page.check_link_in_search_query()
    assert "tensor.ru" in all_links[0]


def test_yandex_pictures(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    elements = yandex_main_page.check_pictures_in_navigation_bar()
    assert "Картинки" in elements
    yandex_main_page.click_on_the_image_link()
    page_url = yandex_main_page.current_page_url()
    assert "https://yandex.ru/images/" in page_url
    yandex_main_page.click_first_category_in_pictures()
    yandex_main_page.click_first_image_in_category()
    yandex_main_page.click_next_image_btn()
    yandex_main_page.click_prev_image_btn()
