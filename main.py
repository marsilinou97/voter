from selenium import webdriver
from selenium.webdriver.common.keys import Keys

first_name = "Marsilinou"
last_name = "Zaky"
email = ""
title = "Software Engineer Intern"

driver = webdriver.Chrome(executable_path="chromedriver.exe")
url = "https://www.nationalinternday.com/employer-vote?mkt_tok=eyJpIjoiTXpaaE5qUmtabVk1TW1ZNCIsInQ" \
      "iOiI2TW9CR1lVMzJZQ0JpSXFrOXJORmJIVFRVOFVraDRMVXFZM2FqWFFpQWhPN2FUVEZxejV5ZXR2R2NkbisrOUZDdlRSb2" \
      "tNUmRwU1hKTFVMTEJxNzMwdndyb1VrRnlvXC9jYjl0WGVGbTZXaE5PT0crQkdha2NZbkg5bERobTU5VDYifQ%3D%3D"
driver.get(url)
driver.implicitly_wait(30)
driver.switch_to.frame(driver.find_element_by_css_selector(".embed_frame"))
driver.find_element_by_id("entry_search3_input").send_keys("Qualcomm" + Keys.RETURN)
driver.find_element_by_css_selector(".vote_link.vote.ss_btn.ss_item_main_action").click()
driver.find_element_by_id("form_first_name").send_keys(first_name)
driver.find_element_by_id("form_last_name").send_keys(last_name)
driver.find_element_by_id("form_email").send_keys(email)
driver.find_element_by_id("form_custom_field_1").send_keys(title)
driver.execute_script("""document.getElementById("form_agree").click()""")
driver.find_element_by_css_selector(".form_submit.ss_btn").click()
