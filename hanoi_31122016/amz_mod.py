from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os, time

# Larging declares
driver = webdriver.PhantomJS()


# Define def
def amz_link_maker(word_search):
    return "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + word_search


def amz_page_count(driver):
    return int(driver.find_element_by_class_name('pagnDisabled').get_attribute('innerHTML'))


def amz_link_subpage(quantity, word_search):
    link_list = []
    i = 2
    while i <= quantity:
        link_list.append("https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&page=" + str(i) + \
                         "&field-keywords=" + word_search)
        i += 1
    return link_list


def amz_preprocessing_product(link):
    # Set performance measurement
    tm_start = time.time()

    # Getting elements
    driver.get(link)
    results_list = driver.find_element_by_id('s-results-list-atf')
    print results_list.get_attribute('class') # For testing
    print '[Getting elements] Process time: %.2f' % (time.time() - tm_start)

    # Getting sub-elements
    tm_start = time.time()
    results = results_list.find_elements_by_class_name('s-result-item')
    for result in results:
        print result.get_attribute('id')        # For testing
        print result.get_attribute('data-asin') # For testing
    print '[Getting sub-element] Process time: %.2f' % (time.time() - tm_start)

    # Extracting info
    tm_start = time.time()
    for result in results:
        # product_thumb = result.find_element_by_class_name('cfMarker')
        # Checking category
        try:
            result.find_element_by_class_name('acs-mn2-midWidgetHeader')
            continue
        except NoSuchElementException:
            print "---"

        print "[NAME] " + result.find_element_by_class_name('s-access-title').get_attribute('innerHTML')
        try:
            print "[BASE PRICE] " + result.find_element_by_class_name('a-size-base-plus').get_attribute('innerHTML')
        except NoSuchElementException:
            print "[BASE PRICE] 0.00"
        try:
            print "[SALE PRICE] " + result.find_element_by_class_name('sx-price-whole').get_attribute(
                'innerHTML') + "," + \
                  result.find_element_by_class_name('sx-price-fractional').get_attribute('innerHTML')
        except NoSuchElementException:
            print "[SALE PRICE] FREE"
        print "[SHOP NAME] " + result.find_elements_by_class_name('a-size-small')[1].get_attribute('innerHTML')
        print "---"
    print "[Extracting time] %.2f" % (time.time() - tm_start)
    return driver


if __name__ == '__main__':
    driver = amz_preprocessing_product(amz_link_maker('charger'))
    page_count = amz_page_count(driver)
    link_list = amz_link_subpage(page_count, 'charger')
    for link in link_list:
        amz_preprocessing_product(link)

   #  os.system('taskkill /im phantomjs.exe /F')
    os.system('pkill phantomjs')
