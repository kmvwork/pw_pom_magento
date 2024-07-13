import time

import pytest
from pages.account_creation_page import AccountCreationPage
from utils.assertions import Assertions
from test_data import account_creation_data, expected_titles


@pytest.fixture
def account_creation_page(page):
    return AccountCreationPage(page)


def test_load_account_creation_page(account_creation_page: AccountCreationPage) -> None:
    account_creation_page.load()
    Assertions.assert_equal(account_creation_page.page.title(), expected_titles["account_creation"],
                            "Page title mismatch")


def test_fill_account_creation_form(account_creation_page: AccountCreationPage) -> None:
    account_creation_page.load()
    account_creation_page.fill_form(
        account_creation_data["first_name"],
        account_creation_data["last_name"],
        account_creation_data["email"],
        account_creation_data["password"],
        account_creation_data["confirm_password"]
    )
    Assertions.assert_equal(account_creation_page.first_name_input.input_value(), account_creation_data["first_name"],
                            "First name mismatch")
    Assertions.assert_equal(account_creation_page.last_name_input.input_value(), account_creation_data["last_name"],
                            "Last name mismatch")
    Assertions.assert_equal(account_creation_page.email_input.input_value(), account_creation_data["email"],
                            "Email mismatch")
    Assertions.assert_equal(account_creation_page.password_input.input_value(), account_creation_data["password"],
                            "Password mismatch")
    Assertions.assert_equal(account_creation_page.confirm_password_input.input_value(),
                            account_creation_data["confirm_password"], "Confirm password mismatch")


def test_submit_account_creation_form(account_creation_page: AccountCreationPage) -> None:
    account_creation_page.load()
    account_creation_page.fill_form(
        account_creation_data["first_name"],
        account_creation_data["last_name"],
        account_creation_data["email"],
        account_creation_data["password"],
        account_creation_data["confirm_password"]
    )
    account_creation_page.submit()
    Assertions.assert_url_equal(account_creation_page.page.url,
                                "https://magento.softwaretestingboard.com/customer/account/")
    Assertions.assert_equal(account_creation_page.header_created_account.text_content(), "My Account")
    Assertions.assert_equal(account_creation_page.text_success_created_account.text_content(),
                            "Thank you for registering with Main Website Store.")
