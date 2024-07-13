from playwright.sync_api import Page
from typing import Optional


class BasePage:
    def __init__(self, page: Page, url: str) -> None:
        self.page = page
        self.url = url

    def load(self, wait_until: Optional[str] = "domcontentloaded") -> None:
        self.page.goto(self.url, wait_until=wait_until)
