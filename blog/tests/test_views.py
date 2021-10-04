from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver

class TestTopPage(LiveServerTestCase):
    def setUp(self):
        self.selenium = WebDriver(executable_path="/Users/nonakamotoya/chromedriver/chromedriver")

    def tearDown(self):
        self.selenium.quit()


    def test_toppage(self):
        self.selenium.get('http://localhost:8000')
        print(self.selenium.find_element_by_class_name('article'))