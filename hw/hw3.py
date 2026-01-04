class User:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.__password = password

    def show_email(self):
        print(f"Email пользователя: {self._email}")

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            print("Пароль успешно изменен!")
        else:
            print("Ошибка: старый пароль введен неверно.")

user = User("1ceW1nd", "ice@gmail.com", "1234")
print(user.name)
user.show_email()

print(user.check_password("1234"))
print(user.check_password("0000"))

user.change_password("1234", "abcd")


#Абстракция

from abc import ABC, abstractmethod



class Transport(ABC):

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def move(self):
        print("Машина едет по дороге")


class Bicycle(Transport):
    def move(self):
        print("Велосипед едет по велодорожке")


car = Car()
bike = Bicycle()

car.move()
bike.move()