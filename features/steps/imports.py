from behave import *
from tests.browser_setup import start_browser, stop_browser
from features.locators.locators import HomePageLocators
from faker import Faker
from playwright.sync_api import expect
fake = Faker('pt_BR')
import json