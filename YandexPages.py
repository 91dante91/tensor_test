from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SUGGEST = (By.XPATH, "//ul[@class='mini-suggest__popup-content']")
    LOCATOR_YANDEX_RESULT_LINKS = (By.XPATH, "//li[@class= 'serp-item desktop-card']/div/div[1]/a")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CLASS_NAME, "services-new__list")
    LOCATOR_YANDEX_IMAGE_LINK = (By.LINK_TEXT, "Картинки")
    LOCATOR_YANDEX_FIRST_CATEGORY_IN_PICTURES = (By.XPATH, "//div[@class='PopularRequestList']/div[1]")
    LOCATOR_YANDEX_FIRST_IMAGE_IN_CATEGORY = (By.XPATH, "//div[@class='serp-controller__content']/div/div[1]")
    LOCATOR_YANDEX_NEXT_IMAGE_BUTTON = (By.XPATH, "//div[@class='MediaViewer-LayoutMain MediaViewer_theme_fiji-LayoutMain']/div/div[4]")
    LOCATOR_YANDEX_PREV_IMAGE_BUTTON = (By.XPATH, "//div[@class='MediaViewer-LayoutMain MediaViewer_theme_fiji-LayoutMain']/div/div[1]")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        self.check_suggest()
        search_field.send_keys(Keys.ENTER)

    def check_suggest(self):
        return self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST)

    def check_link_in_search_query(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_RESULT_LINKS)
        links = [link.get_attribute("href") for link in all_list][:5]
        return links

    def click_on_the_image_link(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGE_LINK).click()

    def check_pictures_in_navigation_bar(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR)
        nav_bar_menu = list(all_list[0].text.split("\n"))
        return nav_bar_menu

    def current_page_url(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url

    def get_name_first_category_in_pictures(self):
        first_category = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY_IN_PICTURES)
        return first_category.text

    def click_first_category_in_pictures(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY_IN_PICTURES).click()

    def click_first_image_in_category(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_IMAGE_IN_CATEGORY).click()

    def click_next_image_btn(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_NEXT_IMAGE_BUTTON).click()

    def click_prev_image_btn(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_PREV_IMAGE_BUTTON).click()
