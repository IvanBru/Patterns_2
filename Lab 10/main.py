# Абстрактний клас або інтерфейс для всіх компонентів форми
class FormComponent:
    def render(self):
        pass


# Конкретний клас для простого поля вводу
class InputField(FormComponent):
    def __init__(self, name):
        self.name = name

    def render(self):
        return f'<input type="text" name="{self.name}">'


# Конкретний клас для групи полів вводу (fieldset)
class Fieldset(FormComponent):
    def __init__(self, legend):
        self.legend = legend
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def render(self):
        rendered_components = "".join(component.render() for component in self.components)
        return f'<fieldset><legend>{self.legend}</legend>{rendered_components}</fieldset>'


form = Fieldset("User Information")

# Додати просте поле вводу
username_field = InputField("username")
form.add_component(username_field)

# Створити групу полів вводу для адреси
address_fieldset = Fieldset("Address")
street_field = InputField("street")
city_field = InputField("city")
address_fieldset.add_component(street_field)
address_fieldset.add_component(city_field)
form.add_component(address_fieldset)

# Вивести HTML-код форми
print(form.render())
