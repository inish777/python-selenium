# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class create_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_create_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_group(wd)
        self.logout(wd)
        self.assertTrue(success)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, wd):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("asdfsdf")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("asdfsadfg")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("asgafsgasdgsdag")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def login(self, wd):
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:4000/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
