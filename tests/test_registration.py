from selene import browser, have, be
from selene import command
import os.path

import tests


def test_success_registration():
    browser.open('/automation-practice-form')
    # browser.execute_script("document.body.style.zoom='50%'")
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')
    # WHEN
    # Ввод имени
    browser.element('#firstName').should(be.blank).type('Ira')
    # Проверка, что имя введено
    browser.element('#firstName').should(have.attribute('value').value_containing('Ira'))
    # Ввод фамилии
    browser.element('#lastName').should(be.blank).type('Uchuvatova')
    # Проверка, что фамилия введена
    browser.element('#lastName').should(have.attribute('value').value_containing('Uchuvatova'))
    # Ввод email
    browser.element('#userEmail').should(be.blank).type('example@mail.ru')
    # Проверка, что email введен
    browser.element('#userEmail').should(have.attribute('value').value_containing('example@mail.ru'))
    # Скролл до чек-боксов с хобби и выбор хобби
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Reading')).perform(command.js.scroll_into_view).click()
    # Выбор пола
    browser.element('[name=gender][value=Female]+label').click()
    # Ввод телефона
    browser.element('#userNumber').should(be.blank).type('1234567890')
    # Вызов календаря в поле День рождения
    browser.element('#dateOfBirthInput').should(be.not_.blank).click()
    # Выбор года
    browser.element('.react-datepicker__year-select').click().element('[value="1986"]').click()
    # Выбор месяца
    browser.element('.react-datepicker__month-select').send_keys('April').click()
    # Проверка, что выбран нужный месяц и год
    browser.element('.react-datepicker__header').should(have.text('April 1986'))
    # Выбор дня
    browser.element(f'.react-datepicker__day--0{26}').click()
    # Ввод и выбор Subjects
    browser.element('#subjectsInput').should(be.blank).type('Mat')
    browser.all('.subjects-auto-complete__option').element_by(
        have.exact_text('Maths')
    ).click()
    # Проверка, что Subjects введены
    browser.element('#subjectsContainer').should(have.text('Maths'))
    # Выбор картинки
    browser.element('input[type="file"]').send_keys(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resourses/1.png')
        )
    )
    # Ввод адреса
    browser.element('#currentAddress').should(be.blank).set_value('NN')
    # Проверка, что адрес введен
    browser.element('#currentAddress').should(have.attribute('value').value_containing('NN'))
    # Вызов выпадающего меню Штат
    browser.element('#state').click()
    # Выбор штата
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()
    # Вызов выпадающего меню Город
    browser.element('#city').click()
    # Выбор города
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Delhi')
    ).click()
    # Нажать кнопку Submit
    browser.element('#submit').click()

    # THEN
    # Проверка появления модального окна с подтверждением регистрации
    browser.element('.modal-content').element('.modal-header').should(have.text('Thanks for submitting the form'))
    # Проверка соответствия таблицы введенным данным
    browser.element('.table').all('td').even.should(
        have.exact_texts('Ira Uchuvatova', 'example@mail.ru', 'Female', '1234567890', '26 April,1986', 'Maths',
                         'Reading',
                         '1.png', 'NN', 'NCR Delhi'))
