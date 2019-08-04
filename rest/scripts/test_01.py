import allure
import pytest

class Test_001:

    @allure.step(title='进入首页')
    def test_01(self):
        print("-----111")
        allure.attach('网址', "www.baidu.com")
        print("-----222")
        allure.attach('详情', " 描述")
        assert True

    @allure.step(title='进入首页')
    def test_02(self):
        print("-----111")
        assert False

    def test_03(self):
        print("-----111")
        assert True