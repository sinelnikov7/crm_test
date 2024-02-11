# def test_tools(fox_driver_wont_close):
#     fox_driver_wont_close.get('https://strojregionfilomena.workhere.ru/')
#     fox_driver_wont_close.find_element(By.XPATH, '//a[starts-with(@href,"/tools")]').click()
#     assert fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.title__8XLeH').text == 'Инструменты'
#     time.sleep(2)
#     fox_driver_wont_close.find_element(By.XPATH, '//a[starts-with(@href, "/key-management")]').click()
#     assert fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.title__8XLeH').text == 'Управление ключами'
#     # table = fox_driver_wont_close.find_element(By.XPATH, '//tbody[@class="ant-table-tbody"]')
#     # count = table.get_attribute('childElementCount')
#     # count = table.get_attribute('outerHTML')
#     add_key = fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.plusBlock__AoWbv')
#     # add_key = fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.ant-notification-notice')
#     time.sleep(7)
#     # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='taLnk ulBlueLinks']"))).click()
#     # fox_driver_wont_close.execute_script('arguments[0].click;', add_key)
#     add_key.click()
#     fox_driver_wont_close.find_element(By.TAG_NAME, 'input').send_keys('2')
#     fox_driver_wont_close.find_element(By.XPATH, '//button[@class="ant-btn ant-btn-primary"]').click()
#     time.sleep(5)
#     assert fox_driver_wont_close.find_element(By.XPATH,
#                                               '//div[@class="dialog-header-default-title-name__yeBEd"]/div').text == 'Информация о ключе'
#     fox_driver_wont_close.find_element(By.XPATH,
#                                        '//div[@class="keyManagement__dialog__footer__OQ45J"]/button').click()
#     raw = fox_driver_wont_close.find_element(By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[2]')
#     # print(raw.get_attribute('outerHTML'))
#     key = raw.find_element(By.XPATH, '//span[@class="key-field__box__3fUIb"]').text
#     print(key)
#     raw.find_element(By.XPATH, '//button[@class="key-field__control__EDtFi"]').click()
#     time.sleep(10)
#     fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.plusBlock__AoWbv').click()
#     a = fox_driver_wont_close.find_element(By.TAG_NAME, 'input')
#     a.send_keys(Keys.CONTROL + "v")
#     time.sleep(5)
#     validate_key = a.get_attribute('value')
#     assert key == validate_key