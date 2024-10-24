
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import json

class Base_class:
    service = None
    driver = None

    def __init__(self) -> None:
        Base_class.driver = None

    def init(self):
        if Base_class.driver is None:
            Base_class.service = Service(ChromeDriverManager().install())
            Base_class.driver = webdriver.Chrome(service=self.service)
    
    def go_to_url(self):
        url = ""
        # Get the directory of the current script
        current_path = os.path.dirname(os.path.abspath(__file__))
        # Go 3 levels up from 'your_script.py' to reach 'your_project' directory
        project_root = os.path.dirname(os.path.dirname(current_path))
        resources_path = os.path.join(project_root, 'Resources')
        file_path = os.path.join(resources_path, 'config.json')

        with open(file_path, 'r') as file:
            data = json.load(file)
            # Extract the URL
            url = data['url']
        Base_class.driver.get(url)
        Base_class.driver.maximize_window()

    def teardown(self):
        Base_class.driver.quit()
