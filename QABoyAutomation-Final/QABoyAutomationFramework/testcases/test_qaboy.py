import unittest

from pageobjects.aboutscreen import AboutScreen
from pageobjects.homescreen import HomeScreen
from pageobjects.postscreen import PostScreen
from pageobjects.searchscreen import SearchScreen
from pageobjects.sidebar import SideBar
from values import strings
from webdriver import Driver


class TestQABoy(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_title_is_present()
        home_screen.validate_icon_is_present()
        home_screen.validate_menu_options_are_present()
        home_screen.validate_posts_are_visible()
        home_screen.validate_social_media_links()

    def test_about_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.click_about_me_link()

        about_screen = AboutScreen(self.driver)
        about_screen.validate_title_is_present()
        about_screen.validate_icon_is_present()
        about_screen.validate_menu_options_are_present()
        about_screen.validate_social_media_links()
        about_screen.validate_about_me_header()
        about_screen.validate_about_me_post()

    def test_post_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.click_first_post()

        post_screen = PostScreen(self.driver)
        post_screen.validate_title_is_present()
        post_screen.validate_icon_is_present()
        post_screen.validate_menu_options_are_present()
        post_screen.validate_social_media_links()
        post_screen.validate_featured_image()
        post_screen.validate_published_date()
        post_screen.validate_share_buttons()
        post_screen.validate_categories_and_tags()
        post_screen.validate_comment_section()

    def test_search_for_article(self):
        sidebar = SideBar(self.driver)
        sidebar.search_for_article(strings.article_title)

        search_screen = SearchScreen(self.driver)
        search_screen.click_article(strings.article_title)

        post_screen = PostScreen(self.driver)
        post_screen.validate_article_title(strings.article_title)

    def test_check_user_comment(self):
        sidebar = SideBar(self.driver)
        sidebar.click_user_comment()

        post_screen = PostScreen(self.driver)
        post_screen.validate_comment_section()

    def test_archived_articles(self):
        sidebar = SideBar(self.driver)
        sidebar.click_archive()

    def test_article_categories(self):
        sidebar = SideBar(self.driver)
        sidebar.click_category()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
