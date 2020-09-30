def login():
    #options = webdriver.chrome.options.Options()
    #profile_path = 'path_to_chrome_profile'
    #options.add_argument ('--user-data-dir=' + profile_path)
    #driver = webdriver.Chrome(executable_path='path to chromedriver', options=options)

    driver.get ("URL1")

    # window size change to max
    driver.maximize_window()

    # before login
    chk_box = driver.find_element_by_xpath('//*[@id="Accept"]')
    chk_box.click()
    go_btn = driver.find_element_by_xpath('//*[@id="test_btn"]')
    go_btn.click()
    sleep(1)

    # login
    usrname = driver.find_element_by_xpath('//*[@id="inner]/div[2]/form/fieldset/div[3]/label/input')
    usrname.send_keys('your_ID')
    passwd = driver.find_element_by_xpath('//*[@id="inner"]/div[2]/form/fieldset/div[4]/label/input')
    passwd.send_keys('your_passwd')
    login_btn = driver.find_element_by_xpath('//*[@id="inner"]/div[2]/form/div/input')
    login_btn.click()
    sleep(20)

    # switch to URL2 page
    driver.execute.script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get ('URL2')
    sleep (15)

    # role change
    role = driver.find_element_by_xpath('//*[@id="topbar"]/div[5]/div[2]/div[1]/div[2]/span')
    if role.text == 'not role':
        role.click()
        sleep(1)

        role_a = driver.find_element_by_xpath('//*[@id="items-cnt"]/li[1]')
        role_a.click()
        sleep(1)

        ok_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/ul/li[4]/button[1]')
        ok_btn.click()
        sleep(5)