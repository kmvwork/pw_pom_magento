from pages.base_page import BasePage
from playwright.sync_api import Page


class EcoFriendlyPage(BasePage):
    def __init__(self, page: Page) -> None:
        from config.config import Config
        super().__init__(page, Config.ECO_FRIENDLY_URL)
        self.page_title = page.locator('title')
        self.shopping_options_title = page.get_by_role("heading", name="Shopping Options")
        self.sort_by_title = page.get_by_text("Sort By").first

    def get_title_text(self) -> str:
        return self.page_title.inner_text()
