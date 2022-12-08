from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:\chromedriver.exe")

def test_show_all_my_pets():
    driver.get("https://petfriends.skillfactory.ru/login")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("911@mail.ru")
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys("911")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"/my_pets\"]"))).click()

    pets_number = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]"))).text.split('\n')[1].split(":")[1].strip()
    pet_cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))

    assert int(pets_number) == len(pet_cards)

def test_at_least_half_pets_has_photo():
    driver.get("https://petfriends.skillfactory.ru/login")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("911@mail.ru")
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys("911")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"/my_pets\"]"))).click()

    pets_number = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]"))).text.split('\n')[1].split(":")[1].strip()
    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table.table-hover img")))
    number_of_photoes = 0
    for i in range(len(images)):
        if images[i].get_attribute("src") != '':
            number_of_photoes += 1

    assert number_of_photoes >= int(pets_number) / 2

def test_all_pets_have_name_types_age():
    driver.get("https://petfriends.skillfactory.ru/login")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("911@mail.ru")
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys("911")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"/my_pets\"]"))).click()

    pet_data = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td")))

    for data in pet_data:
        assert data.text.strip() != ""


def test_all_pets_have_different_names():
    driver.get("https://petfriends.skillfactory.ru/login")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("911@mail.ru")
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys("911")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"/my_pets\"]"))).click()

    pet_cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))
    pet_names = []
    for i in range(len(pet_cards)):
        data_pet = pet_cards[i].text.replace("\n", '').replace("*", '').split(' ')
        pet_names.append(data_pet[0])
    count = 0
    for i in range(len(pet_names)):
        if pet_names.count(pet_names[i]) > 1:
            count += 1
        assert count == 0

def test_all_pets_are_unique():
    driver.get("https://petfriends.skillfactory.ru/login")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("911@mail.ru")
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys("911")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"/my_pets\"]"))).click()

    pet_cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))
    list_my_pets = []
    for i in range(len(pet_cards)):
        list_data = pet_cards[i].text.split("\n")
        list_my_pets.append(list_data[0])
    set_my_pets = set(list_my_pets )
    assert len(list_my_pets ) == len(set_my_pets)