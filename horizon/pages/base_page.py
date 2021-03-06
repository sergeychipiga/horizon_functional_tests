from selenium.webdriver.common.by import By

from horizon.interfaces import IPage, IWeb
from horizon.utils import ContainerMixin


class D(object):

    def __init__(self, element):
        self._element = element
        self._cache = {}

    def __get__(self, page, objtype=None):
        page_id = id(page)
        if page_id not in self._cache:
            self._cache[page_id] = self._element.clone(page=page)
        return self._cache[page_id]


class BasePage(IPage, IWeb, ContainerMixin):

    def __init__(self, app):
        self.app = app
        self.locator = (By.TAG_NAME, 'html')
        self.web_driver = app.web_driver
        self.web_element = self.web_driver.find_element(*self.locator)
