def goto_job_details(process_name):
    driver.switch_to.default_content()
    sp_process_name ='sp:' + process_name

    search_tab = driver.find_element_by_xpath('//*[@id="input_search_div"]/form/div[1]/input')
    search_tab.send_keys(sp_process_name)
    sleep(3)

    search_btn = driver.find_element_by_xpath('//*[@id="global_ctn_search"]/div[2]/div[2]/div[2]/div')
    search_btn.click()
    sleep(5)

    first_tile = driver.find_element_by_xpath("//div[@is-visible='true'][@row-id='0'][@column-id='0']/div/div[5]")
    first_tile.click()
    sleep(1)

    detail = driver.find_element_by_id('action_DisplayDetails')
    detail.click()
    sleep(5)

    job_detail = driver.find_element_by_xpath('//*[@id="catMenu"]/ul/li[12]')
    job_detail.click()
    sleep(5)