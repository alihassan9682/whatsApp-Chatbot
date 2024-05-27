import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


# Configuration for undetected_chrome_driver with options
def configure_undetected_chrome_driver(open_browser=False):
    options = uc.ChromeOptions()
    my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

    if not open_browser:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--no-first-run")
    options.add_argument("--no-service-autorun")
    options.add_argument("--password-store=basic")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--user-agent={my_user_agent}")

    # Use a specific profile directory within the user's profile
    user_data_dir = os.path.join(
        os.environ["USERPROFILE"],
        "AppData",
        "Local",
        "Google",
        "Chrome",
        "User Data",
        "Default",
    )
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # Initialize the undetected Chrome driver
    driver = uc.Chrome(
        driver_executable_path=ChromeDriverManager().install(),
        options=options,
        use_subprocess=False,
    )
    return driver
