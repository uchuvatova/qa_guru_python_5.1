import random
from selene import browser, have, be
from selene import command


def test_success_registration_without_email():
    browser.open('/')
    # Ввод имени
    browser.element('#firstName').should(be.blank).type('Ira')
    # Проверка, что имя введено
    browser.element('#firstName').should(have.attribute('value').value_containing('Ira'))
    # Ввод фамилии
    browser.element('#lastName').should(be.blank).type('Uchuvatova')
    # Проверка, что фамилия введена
    browser.element('#lastName').should(have.attribute('value').value_containing('Uchuvatova'))
    # Скролл до чек-боксов с хобби
    browser.element('label[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
    # Выбор пола
    browser.element('label[for=gender-radio-2]').click()
    # Ввод телефона
    browser.element('#userNumber').should(be.blank).type(random.randint(1000000000, 9999999999))
    # Вызов календаря в поле День рождения
    browser.element('#dateOfBirthInput').should(be.not_.blank).click()
    # Выбор года
    browser.element('.react-datepicker__year-select').click().element('[value="1986"]').click()
    # Выбор месяца
    browser.element('.react-datepicker__month-select').click().element('[value="3"]').click()
    # Проверка, что выбран нужный месяц и год
    browser.element('.react-datepicker__header').should(have.text('April 1986'))
    # Выбор дня
    browser.element('.react-datepicker__day--026').click()
    # Проверка, что в поле День рождения отображается выбранная дата
    browser.element('#dateOfBirthInput').should(have.attribute('value').value_containing('26 Apr 1986'))
    # Ввод Subjects
    browser.element('#subjectsInput').should(be.blank).type('Testing')
    # Проверка, что Subjects введены
    browser.element('#subjectsInput').should(have.attribute('value').value_containing('Testing'))
    # Выбор хобби
    browser.element('label[for=hobbies-checkbox-2]').click()
    # Выбор картинки
    browser.element('input[type="file"]').send_keys('C:/Users/iauchuvat1/QA_Guru/qa_guru_python_5/tests/1.png')
    # Ввод адреса
    browser.element('#currentAddress').should(be.blank).type('NN')
    # Проверка, что адрес введен
    browser.element('#currentAddress').should(have.attribute('value').value_containing('NN'))
    # Скролл до кнопки Submit
    browser.element('#submit').perform(command.js.scroll_into_view)
    # Вызов выпадающего меню Штат
    browser.element('#state').click()
    # Выбор штата
    browser.element('#react-select-3-option-0').click()
    # Вызов выпадающего меню Город
    browser.element('#city').click()
    # Выбор города
    browser.element('#react-select-4-option-0').click()
    # Нажать кнопку Submit
    browser.element('#submit').click()
    # Проверка появления модального окна с подтверждением регистрации
    browser.element('.modal-content').element('.modal-header').should(have.text('Thanks for submitting the form'))


