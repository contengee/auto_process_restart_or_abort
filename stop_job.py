def stop_job(process_name):
    # 細部見に行く前に弾く処理出来る
    iframe = driver.find_element_by_name('content')
    driver.switch_to.frame(iframe)
    iframe2 = driver.find_element_by_name('detailsDisplay')
    driver.switch_to.frame(iframe2)
    iframe3 = driver.find_element_by_name('portalDisplay')
    driver.switch_to.frame(iframe3)
    iframe4 = driver.find_element_by_name('SMASimulation_NavTreeJobs')
    driver.switch_to.frame(iframe4)

    action_img = driver.find_element_by_xpath('//*[@id="0,0"]/td[1]/a/img')
    job_status = action_img.get_attribute('alt')
    message = 'test'
    if '失敗' in job_status:
        message ='failed: '
    elif '中止' in job_status:
        message = 'aborted: '
    elif '終了' in job_status:
        message = 'completed: '
    else:
        chk_bx = driver.find_element_by_id('rmbrow-0,0')
        chk_bx.click()
        sleep (1)
        abort_btn = driver.find_element_by_xpath('//*[@id="divToolbar"]/div[1]/table/tbody/tr/td[4]')
        abort_btn.click()
        sleep(3)
        Alert(driver).accept()
        sleep(3)
        message = 'abort successed: '
    print(message + process_name)
    driver.switch_to.default_content()
    # 可能なら履歴クリア
    clear_search = driver.find_element_by__xpath('//*[@id="global_ctn_search"]/div[2]/div[2]/div[1]')