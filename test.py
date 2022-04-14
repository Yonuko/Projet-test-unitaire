from Module import *

def test_person():
    person = Person("Michel")

    assert person.name == "Michel"
    assert person.life_points == 100
    pass


def test_hit():
    person = Person("Michel")
    person.hit(person)
    assert person.life_points == 100 - 10
    pass

def test_is_dead():
    person = Person("Patrick")
    assert person.is_dead() == False
    for _ in range(10):
        person.hit(person)
    assert person.is_dead() == True
    pass

def test_gained_life_points():
    person = Person("Jean")
    person.hit(person)
    person.gained_life_points(10)
    assert person.get_life_points() == 100
    pass

def test_wizzard_hit():
    wizzard = Wizard("Merlin")
    wizzard.hit(wizzard)
    assert wizzard.get_life_points() == 65
    pass

def test_health_potion():
    potion = HealthPotion()
    person = Person("Hugo")
    potion.was_used_by(person)
    assert person.get_life_points() == 110
    pass