from pages.base_page import BasePage
from playwright.sync_api import Page


class SalePage(BasePage):
    def __init__(self, page: Page) -> None:
        from config.config import Config
        super().__init__(page, Config.SALE_URL)
        self.page_title = page.locator('title')
        self.sale_page_header = page.get_by_label("Sale").get_by_text("Sale")
        self.women_deals_title = page.get_by_text("Women's Deals")
        self.men_deals_title = page.get_by_text("Mens's Deals")

    def get_title_text(self) -> str:
        return self.page_title.inner_text()
