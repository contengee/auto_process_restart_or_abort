def goto_performance():
    # 実行中かどうかをチェックして、 実行中なら以下の処理を飛ばして次に進む
    iframe = driver.find_element_by_name('content')
    driver.switch_to.frame(iframe)
    iframe2 = driver.find_element_by_name('detailsDisplay')
    driver.switch_to.frame(iframe2)
    sma_home = driver.find_element_by_xpath('//*[@id="SMAHome_Discover"]')
    sma_home.click()
    sleep(10)