from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

@given('que eu estou na página inicial')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://todomvc-app-for-testing.surge.sh/')

@when('eu adiciono uma nova tarefa com o nome "{task_name}"')
def step_impl(context, task_name):
    input_element = context.driver.find_element(By.CLASS_NAME, 'new-todo')
    input_element.send_keys(task_name)
    input_element.send_keys(Keys.RETURN)
    time.sleep(1)

@then('a tarefa "{task_name}" deve ser exibida na lista de tarefas')
def step_impl(context, task_name):
    task_locator = (By.XPATH, f'//label[text()="{task_name}"]')
    WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located(task_locator))
    task_elements = context.driver.find_elements(*task_locator)
    assert len(task_elements) > 0, f'A tarefa "{task_name}" não foi encontrada na lista'

@when('eu clico na tarefa "{task_name}"')
def step_impl(context, task_name):
    task_locator = (By.XPATH, f'//label[text()="{task_name}"]/ancestor::li')
    task_element = context.driver.find_element(*task_locator)
    checkbox_element = task_element.find_element(By.CSS_SELECTOR, '.toggle')
    checkbox_element.click()
    time.sleep(1)

@then('a tarefa "{task_name}" deve ser marcada como concluída')
def step_impl(context, task_name):
    task_locator = (By.XPATH, f'//label[text()="{task_name}"]/ancestor::li')
    task_element = context.driver.find_element(*task_locator)
    assert task_element.get_attribute('class') == 'completed', f'A tarefa "{task_name}" não está marcada como concluída'

@when('eu filtro as tarefas ativas')
def step_impl(context):
    active_filter_element = context.driver.find_element(By.LINK_TEXT, 'Active')
    active_filter_element.click()
    time.sleep(1)

@then('a lista de tarefas deve exibir apenas tarefas ativas')
def step_impl(context):
    task_elements = context.driver.find_elements(By.CSS_SELECTOR, '.view:not(.completed)')
    assert len(task_elements) == 0, 'A lista de tarefas não exibe apenas tarefas ativas'

@when('eu filtro as tarefas concluídas')
def step_impl(context):
    completed_filter_element = context.driver.find_element(By.LINK_TEXT, 'Completed')
    completed_filter_element.click()
    time.sleep(1)

@then('a lista de tarefas deve exibir apenas tarefas concluídas')
def step_impl(context):
    task_elements = context.driver.find_elements(By.CSS_SELECTOR, '.view.completed')
    assert len(task_elements) == 0, 'A lista de tarefas não exibe apenas tarefas concluídas'
