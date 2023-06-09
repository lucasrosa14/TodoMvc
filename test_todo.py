import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_add_task(driver):
    driver.get('https://todomvc-app-for-testing.surge.sh/')

    input_element = driver.find_element(By.CLASS_NAME, 'new-todo')
    input_element.send_keys('Estudar BDD')
    input_element.send_keys(Keys.RETURN)
    time.sleep(1)

    task_element = driver.find_element(By.XPATH, '//label[text()="Estudar BDD"]')
    assert task_element.is_displayed()


def test_add_multiple_tasks(driver):
    driver.get('https://todomvc-app-for-testing.surge.sh/')

    input_element = driver.find_element(By.CLASS_NAME, 'new-todo')
    input_element.send_keys('Tarefa 1')
    input_element.send_keys(Keys.RETURN)
    time.sleep(1)

    task_element = driver.find_element(By.XPATH, '//label[text()="Tarefa 1"]')
    assert task_element.is_displayed()

    input_element.send_keys('Tarefa 2')
    input_element.send_keys(Keys.RETURN)
    time.sleep(1)

    task_element = driver.find_element(By.XPATH, '//label[text()="Tarefa 2"]')
    assert task_element.is_displayed()


def test_complete_task(driver):
    driver.get('https://todomvc-app-for-testing.surge.sh/')

    input_element = driver.find_element(By.CLASS_NAME, 'new-todo')
    input_element.send_keys('Tarefa para concluir')
    input_element.send_keys(Keys.RETURN)
    time.sleep(1)

    task_element = driver.find_element(By.XPATH, '//label[text()="Tarefa para concluir"]')
    assert task_element.is_displayed()

    checkbox_element = driver.find_element(By.XPATH, '//label[text()="Tarefa para concluir"]/preceding-sibling::input')
    checkbox_element.click()
    time.sleep(1)

    assert checkbox_element.is_selected()


def test_filter_active_tasks(driver):
    driver.get('https://todomvc-app-for-testing.surge.sh/')

    input_element = driver.find_element(By.CLASS_NAME, 'new-todo')
    input_element.send_keys('Tarefa ativa')
    input_element.send_keys(Keys.RETURN)
    time.sleep(1)

    task_element = driver.find_element(By.XPATH, '//label[text()="Tarefa ativa"]')
    assert task_element.is_displayed()

    checkbox_element = driver.find_element(By.XPATH, '//label[text()="Tarefa ativa"]/preceding-sibling::input')
    checkbox_element.click()
    time.sleep(1)

    active_filter_element = driver.find_element(By.LINK_TEXT, 'Active')
    active_filter_element.click()
    time.sleep(1)

    task_elements = driver.find_elements(By.XPATH, '//label[text()="Tarefa ativa"]')
    assert len(task_elements) == 0


def test_filter_completed_tasks(driver):
    driver.get('https://todomvc-app-for-testing.surge.sh/')

    input_element = driver.find_element(By.CLASS_NAME, 'new-todo')
    input_element.send_keys('Tarefa concluída')
    input_element.send_keys(Keys.RETURN)
    time.sleep(1)

    task_element = driver.find_element(By.XPATH, '//label[text()="Tarefa concluída"]')
    assert task_element.is_displayed()

    checkbox_element = driver.find_element(By.XPATH, '//label[text()="Tarefa concluída"]/preceding-sibling::input')
    checkbox_element.click()
    time.sleep(1)

    completed_filter_element = driver.find_element(By.LINK_TEXT, 'Completed')
    completed_filter_element.click()
    time.sleep(1)

    task_elements = driver.find_elements(By.XPATH, '//label[text()="Tarefa concluída"]')
    assert len(task_elements) == 1
