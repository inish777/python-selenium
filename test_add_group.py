# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from group import Group


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
        self.open_home_page("http://localhost:4000/")
        self.login("admin", "secret")
        self.create_new_group(Group(name="asdfsdf", header="fsgurghur", footer="fiwrwgin"))
        self.logout()
        self.assertTrue(success)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, group):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def login(self, login, password):
        wd = self.wd
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, baseurl):
        wd = self.wd
        wd.get(baseurl)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
