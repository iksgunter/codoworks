# 4. SOLID (L)
# Реализуйте класс Bird и подклассы Sparrow и Penguin.
# Убедитесь, что замена Bird на любой его подкласс не ломает код.


class Bird:
    def i_am(self):
        pass


class Sparrow(Bird):
    def i_am(self):
        return "I'm Jack"


class Penguin(Bird):
    def i_am(self):
        return "I'm Covalsky"


def who_are_you(bird_: Bird):
    return bird_.i_am()


birds = [Sparrow(), Penguin()]
for bird in birds:
    print(who_are_you(bird))
