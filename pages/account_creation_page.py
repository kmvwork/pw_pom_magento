from pages.base_page import BasePage
from playwright.sync_api import Page


class AccountCreationPage(BasePage):
    def __init__(self, page: Page) -> None:
        from config.config import Config
        super().__init__(page, Config.ACCOUNT_CREATION_URL)
        self.first_name_input = page.locator('#firstname')
        self.last_name_input = page.locator('#lastname')
        self.email_input = page.locator('#email_address')
        self.password_input = page.locator('#password')
        self.confirm_password_input = page.locator('#password-confirmation')
        self.create_account_button = page.locator('button[title="Create an Account"]')
        self.text_success_created_account = page.get_by_text("Thank you for registering")
        self.header_created_account = page.get_by_role("heading", name="My Account").locator("span")

    def fill_form(self, first_name: str, last_name: str, email: str, password: str, confirm_password: str) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)

    def submit(self) -> None:
        self.create_account_button.click()
