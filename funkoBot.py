from config import keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def order(k):

    driver = webdriver.Chrome('chromedriver')

    # URL du produit
    driver.get(k['product_url'])

    time.sleep(1)


    # Ajouter au panier
    add_to_cart = driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div[1]/div[2]/div[1]/div[2]/button')
    add_to_cart.click()

    time.sleep(2)

    # Aller au checkout
    driver.get(k['cart_url'])

    # Procèder a l'achat
    checkout_button = driver.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div/div[2]/div[1]/div[2]/button')
    checkout_button.click()

    # Formulaire d'envoi
    add_email = driver.find_element_by_xpath('//*[@id="checkout_email"]')
    add_email.send_keys(k["email"])

    keepmeup_off = driver.find_element_by_xpath('//*[@id="checkout_buyer_accepts_marketing"]')
    keepmeup_off.click()

    add_firstname = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]')
    add_firstname.send_keys(k["first_name"])

    add_lastname = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]')
    add_lastname.send_keys(k["last_name"])

    add_address = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]')
    add_address.send_keys(k["address"])

    add_city = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]')
    add_city.send_keys(k["city"])

    # Selectioner l'état
    select_state = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]/option[35]')
    select_state.click()

    add_zip = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]')
    add_zip.send_keys(k["zip"])

    continue_to_shipping = driver.find_element_by_xpath('//*[@id="continue_button"]')
    continue_to_shipping.click()

    #Comfirmer la méthode d'expédition
    continue_to_payment = driver.find_element_by_xpath('//*[@id="continue_button"]')
    continue_to_payment.click()

    # Formulaire de paiement

    time.sleep(5)

    card_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'number')))
    #card_number = driver.find_element_by_xpath('//*[@id="number"]')
    card_number.send_keys(k["card_number"])

    name_card = driver.find_element_by_xpath('//*[@id="name"]')
    name_card.send_keys(k["name_card"])

    exp_card = driver.find_element_by_xpath('//*[@id="expiry"]')
    exp_card.send_keys(k["expiration_card"])

    ccv = driver.find_element_by_xpath('//*[@id="verification_value"]')
    ccv.send_keys(k["ccv"])

    #PayNow

    pay_now = driver.find_element_by_xpath('//*[@id="continue_button"]')
    pay_now.click()

    time.sleep(5)

if __name__ == '__main__':
    order(keys)
