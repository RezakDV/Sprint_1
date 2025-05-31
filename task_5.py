class TestCase:

# Инициализируем поля steps и result
    def __init__(self):
        self.steps = {}  
        self.result = None 

# Метод set_step для добавления шагов тест-кейса
    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text
        
# Метод delete_step для удаления шага из steps по ключу step_number
    def delete_step(self, step_number):
        self.step_number = step_number
        if step_number in self.steps:
            del self.steps[step_number]

# Метод set_result для установления результата тест-кейса
    def set_result(self, result):
        self.result = result

# Метод get_test_case для вывода информации о составе тест-кейса
    def get_test_case(self):
        print({
            'Шаги': dict(self.steps.items()),
            'Ожидаемый результат': self.result
        })

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()