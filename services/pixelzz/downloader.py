from selenium import webdriver
import requests
from time import sleep

class ImageDownloader:
    filename = ''
    def __init__(self):
        pass

    def write_in_file(self, data, url):
        
        print(url)
        path = 'Images/' + url.split('/')[-1]
        print(path)
        with open(path, 'wb') as f:
            for chunk in data:
                f.write(chunk)

    def download_image(self, url):
        
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            self.write_in_file(r, url)
        else:
          print("error")

class Scraper:
    main_url = 'https://pixelz.cc/images/category/video-games/page/'
    total_pages = 25
    chromedriver_path = '../chromedriver/chromedriver'
    image_link_arr = []

    def __init__(self, page_no):
      self.main_url += str(page_no)
      pass
    
    def __get_default_chrome_options(self):
  
      chrome_options = webdriver.ChromeOptions()

      # chrome_options.add_argument('--headless')
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')
      chrome_options.add_argument('--ignore-certificate-errors')
      
      return chrome_options

    def run_script(self):

      options = self.__get_default_chrome_options()

      driver = webdriver.Chrome(self.chromedriver_path,options=options)
      driver.get(self.main_url)
      el = driver.find_elements_by_class_name('dcs_view_details')

      for i in el:
        self.image_link_arr.append(i.get_attribute('href'))

      driver.close()

    def get_downloadable_image_link(self):

      options = self.__get_default_chrome_options()

      driver = webdriver.Chrome(self.chromedriver_path,options=options)
      for url in self.image_link_arr:
        driver.get(url)
        el = driver.find_element_by_id('main_product_image')
        uri = el.get_attribute('href')
        id = ImageDownloader()
        id.download_image(uri)
      
if __name__ == '__main__':

  for page_no in range(1, 25):
    scr = Scraper(page_no)

    scr.run_script()
    scr.get_downloadable_image_link()