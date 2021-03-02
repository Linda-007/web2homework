from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver = driver
    def add_member(self):
        # 1.不可交互
        # 2.元素遮挡，元素后面存在其他不可见元素
        # 3.元素有多个，需要人工挑选合适的元素
        def wait_name(driver):
            eles = driver.find_element(By.XPATH, "//*[@id='username']")
            if len(eles):
                return True
            else:
                return False
            return len(eles)

        WebDriverWait(self.driver, 10).until(wait_name)
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[1].click()
        # 输入姓名
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("lili")
        # 输入账号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("lili01")
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("12678988978")
        # 点击保存
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()
