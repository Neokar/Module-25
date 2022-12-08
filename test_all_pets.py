from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(("D:\chromedriver.exe"))
driver.get("https://petfriends.skillfactory.ru/login")

def test_show_all_pets():
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "email").send_keys("911@mail.ru")
    driver.find_element(By.ID, "pass").send_keys("911")
    driver.find_element(By.XPATH, "/html/body/div/div/form/div[3]/button").click()

    assert driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"

    pet_cards = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card')

    for i in range(len(pet_cards)):
        driver.implicitly_wait(10)
        image = pet_cards[i].find_element(By.XPATH, '//img[@class="card-img-top"]').get_attribute('src')
        driver.implicitly_wait(10)
        name = pet_cards[i].find_element(By.XPATH, '//h5[@class="card-title"]').text
        driver.implicitly_wait(10)
        description = pet_cards[i].find_element(By.XPATH, '//p[@class="card-text"]').text

        assert image != ''
        assert name != ''
        assert description != ''
        assert ', ' in description
        parts = description.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0




