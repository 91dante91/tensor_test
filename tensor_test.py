import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"


class YandexSearch:
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def search_in_yandex(self):
        self.driver.get('https://yandex.ru/')
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="text"]')
        except NoSuchElementException:
            return False
        else:
            element.send_keys('тензор')
            return True

    def search_suggest(self):
        if self.search_in_yandex():
            time.sleep(2)
            try:
                element = self.driver.find_element(By.XPATH, '/html/body/div[2]/ul/li[1]')
            except NoSuchElementException:
                return False
            else:
                element.click()
                return True

    def search_links_in_result(self):
        if self.search_suggest():
            time.sleep(2)
            try:
                element = self.driver.find_elements(By.CSS_SELECTOR,
                                                    '#search-result > li> div > '
                                                    'div.Organic-Subtitle.Organic-Subtitle_noWrap.Typo.Typo_type_greenurl'
                                                    '.organic__subtitle > div.Path.Organic-Path.path.organic__path > a > '
                                                    'b')
            except NoSuchElementException:
                print('The item you were looking for was not found.')
            else:
                links = []
                for i in range(5):
                    links.append(element[i].text)
                return links

    def search_yandex_pictures(self):
        self.driver.get('https://yandex.ru/')
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, 'body > div.body__wrapper > div.container.rows > '
                                                                'div.row.rows__row.rows__row_main > div > '
                                                                'div.container.container__services.container__line > '
                                                                'nav > div > ul > li:nth-child(3) > a')
        except NoSuchElementException:
            return False
        else:
            element.click()
            return True

    def check_link_yandex_image(self):
        if self.search_yandex_pictures():
            window_after = self.driver.window_handles[1]
            self.driver.switch_to.window(window_after)
            self.driver.current_url
            return self.driver.current_url

    def check_first_category(self):
        self.driver.get('https://yandex.ru/images/')
        try:
            first_category = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div[1]')
            name_first_category = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[3]/div[2]/div[1]/div/div/div[1]').text
        except NoSuchElementException:
            return False
        else:
            first_category.click()
            search_line = self.driver.find_element(By.CLASS_NAME, 'input__control').get_attribute('value')
            if name_first_category == search_line:
                return True

    def open_first_image(self):
        if self.check_first_category():
            time.sleep(2)
            try:
                img_select = self.driver.find_element(By.XPATH,
                                                      '/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a')
            except NoSuchElementException:
                return False
            else:

                time.sleep(2)
                img_select.click()
                return True

    def check_button_next(self):
        if self.open_first_image():
            time.sleep(3)
            try:
                btn_next = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[4]')
            except NoSuchElementException:
                return False
            else:
                link_first_img = self.driver.find_element(By.XPATH,
                                                          '/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div['
                                                          '1]/div[3]/div/img').get_attribute('src')
                time.sleep(3)
                btn_next.click()
                time.sleep(3)
                link_second_img = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div['
                                                           '1]/div[3]/div/img').get_attribute('src')
                if link_first_img != link_second_img:
                    return True

    def check_button_prev(self):
        if self.open_first_image():
            time.sleep(3)
            try:
                btn_next = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[4]')

            except NoSuchElementException:
                return False
            else:
                link_first_img = self.driver.find_element(By.XPATH,
                                                          '/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div['
                                                          '1]/div[3]/div/img').get_attribute('src')
                btn_next.click()
                time.sleep(3)
                btn_prev = self.driver.find_element(By.XPATH, '/html/body/div[11]/div[1]/div/div/div[3]/div/div['
                                                              '2]/div[1]/div[1]')
                btn_prev.click()
                new_link_first_img = self.driver.find_element(By.XPATH,
                                                              '/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div['
                                                              '1]/div[3]/div/img').get_attribute('src')

                if link_first_img == new_link_first_img:
                    return True


if __name__ == '__main__':
    yandex = YandexSearch()
    # yandex.search_in_yandex()
    # yandex.search_suggest()
    # yandex.search_links_in_result()
    # yandex.search_yandex_pictures()
    # yandex.check_first_category()
    # print(yandex.open_first_image())
    print(yandex.check_button_next())
    # yandex.check_button_prev()
# service = Service("C:\Development\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# wait = ui.WebDriverWait(driver, 10)
# driver.maximize_window()
# driver.get('https://yandex.ru/')
#
# search = driver.find_element(By.XPATH, '//*[@id="text"]')
# search.send_keys('тензор')
# sleep(1)
#
#
# # suggets_all = driver.find_elements(By.CLASS_NAME, 'mini-suggest__popup-content')
# def check_sugget(class_name):
#     try:
#         elements = driver.find_elements(By.CLASS_NAME, class_name)
#         return True
#     except NoSuchElementException:
#         return False
#
# # print(len(suggets_all))
# #
# #     return len(driver.find_elements(By.CLASS_NAME, class_name)) > 0
#
# suggets = check_sugget('mini-suggest__popup-content')
# print(suggets)
# search.send_keys(Keys.ENTER)
# sleep(1)
# search_links = driver.find_elements(By.XPATH, '//*[@id="search-result"]/li/div/div/div/a')
# all = driver.find_elements(By.CSS_SELECTOR,
#                            '#search-result > li> div > div.Organic-Subtitle.Organic-Subtitle_noWrap.Typo.Typo_type_greenurl.organic__subtitle > div.Path.Organic-Path.path.organic__path > a > b')
#
# links = []
# # for link in search_links:
# #
# #     l = link.get_attribute('href')
# #     links.append(l)
# # print(links)
# for i in all:
#     l = i.text
#     links.append(l)
# # driver.quit()
# print(links)
# driver.get('https://yandex.ru/')
# window_before = driver.window_handles[0]
# images = driver.find_element(By.CSS_SELECTOR, 'body > div.body__wrapper > div.container.rows > div.row.rows__row.rows__row_main > div > div.container.container__services.container__line > nav > div > ul > li:nth-child(3) > a')
# images.click()
# window_after = driver.window_handles[1]
# driver.switch_to.window(window_after)
# first_category = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div[1]')
# name_first_category = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div[1]').text
# # print(type(name_first_category.text))
# first_category.click()
# inp = driver.find_element(By.CLASS_NAME, 'input__control')
# text_input = inp.get_attribute('value')
# print(text_input)
# assert name_first_category == text_input
# time.sleep(2)
# img_select = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a')
# time.sleep(2)
# img_select.click()
# time.sleep(2)
# img_dr = driver.find_element(By.XPATH, '/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[3]/div/img')
# print(img_dr.get_attribute('src'))
# btn_next = driver.find_element(By.XPATH, '/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[4]').click()
# img_r = driver.find_element(By.CLASS_NAME, 'MMImage-Origin')
# print(img_r.get_attribute('src'))
# time.sleep(1)
# btn_prev = driver.find_element(By.XPATH, '/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[1]').click()


# driver.quit()
