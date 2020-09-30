def start_post_job(process_name):
    iframe = driver.find_element_by_name ('content')
    driver.switch_to.frame(iframe)
    sleep(1)

    param_open = driver.find_element_by_xpath("//div[@row-id='3']")
    param_open.click()

    d = driver.find_element_by_xpath("//div[@column-id='3'][@row-id='5']/ul/li/div/div/select")
    select = Select(d)
    select.select_by_index(1)
    sleep (1)

    d = driver.find_element_by_xpath("//div[@column-id='3'][@row-id='6']/ul/li/div/div/select")
    select = Select(d)
    select.select_by_index(1)
    sleep (1)

    d = driver.find_element_by_xpath("//div[@column-id='3'][@row-id='7']/ul/li/div/div/select")
    select = Select(d)
    select.select_by_index(1)
    sleep (1)

    d = driver.find_element_by_xpath("//div[@column-id='3'][@row-id='8']/ul/li/div/div/select")
    select = Select(d)
    select.select_by_index(1)
    sleep (1)

    d = driver.find_element_by_xpath("//div[@column-id='3'][@row-id='9']/ul/li/div/div/select")
    select = Select(d)
    select.select_by_index(1)
    sleep (1)

    d = driver.find_element_by_xpath("//div[@column-id='3'][@row-id='10']/ul/li/div/div/select")
    select = Select(d)
    select.select_by_index(1)
    sleep (1)

    run_btn = driver.find_element_by_xpath('//*[@id="runNew"]')
    run_btn.click()
    sleep(5)

    print('プロセス再実行成功 : '+ process_name)

    driver.switch_to.default_content()

    # 可能なら履歴クリア
    clear_search = driver.find_element_by_xpath('//*[@id="global_ctn_search"]/div[2]/div[2]/div[1]')