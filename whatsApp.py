from helpers import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def sendMessage(driver, message):
    input_box = driver.find_element(By.CSS_SELECTOR, "[aria-label='Type a message']")
    time.sleep(2)
    input_box.clear()  
    time.sleep(1)
    input_box.send_keys(message) 
    time.sleep(1)
    input_box.send_keys(Keys.ENTER)  
    time.sleep(1)


def getLastMessage(driver, user):
    time.sleep(2)
    myMessages = driver.find_elements(By.CLASS_NAME, "message-out")
    senderMessages = driver.find_elements(By.CLASS_NAME, "message-in")
    
    
    print(F"-------------------CHAT WITH {user}----------------------------\n\n")

    print("SENDER MESSAGES")
    [print(i.find_element(By.CLASS_NAME, "_akbu").text) for i in senderMessages]

    print("\n\nMY MESSAGES")
    [print(i.find_element(By.CLASS_NAME, "_akbu").text) for i in myMessages]


def open_whatsapp_web():
    driver = configure_undetected_chrome_driver(open_browser=True)
    driver.get("https://web.whatsapp.com")

    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
        )
        print("Logged in successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
        return

    chats = driver.find_elements(By.CLASS_NAME, "_ak8q")

    [print(i.text) for i in chats]

    
    for i in chats:
        if i.text == "Archived":
            pass
        else:
            i.click()
            sendMessage(driver, "Hello there I am whatsApp chat bot created by Ali Hassan let me know how may I help you")
            # getLastMessage(driver, i.text)
            time.sleep(2)

    driver.quit()


if __name__ == "__main__":
    open_whatsapp_web()
