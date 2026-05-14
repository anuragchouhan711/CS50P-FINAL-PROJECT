import pytest
import project
import math

planets = [
        {"no": 1, "name": "mercury", "radius": 3,  "speed": 0.625,   "symbol": "m", "angle": 0.0, "px": 0, "py": 0, "revolutions": 0},
        {"no": 2, "name": "venus",   "radius": 5,  "speed": 0.241,  "symbol": "V", "angle": 1.0, "px": 0, "py": 0, "revolutions": 0},
        {"no": 3, "name": "earth",   "radius": 7,  "speed": 0.15,  "symbol": "E", "angle": 2.0, "px": 0, "py": 0, "revolutions": 0},
        {"no": 4, "name": "mars",    "radius": 9,  "speed": 0.079,  "symbol": "M", "angle": 0.5, "px": 0, "py": 0, "revolutions": 0},
        {"no": 5, "name": "jupiter", "radius": 13, "speed": 0.012,  "symbol": "J", "angle": 1.5, "px": 0, "py": 0, "revolutions": 0},
        {"no": 6, "name": "saturn",  "radius": 16, "speed": 0.005,  "symbol": "S", "angle": 3.0, "px": 0, "py": 0, "revolutions": 0},
        {"no": 7, "name": "uranus",  "radius": 18, "speed": 0.0017,  "symbol": "U", "angle": 0.8, "px": 0, "py": 0, "revolutions": 0},
        {"no": 8, "name": "neptune", "radius": 20, "speed": 0.0009, "symbol": "N", "angle": 2.5, "px": 0, "py": 0, "revolutions": 0},
    ]
def test_update_planet():
    p = ["all"]
    cx = 40
    cy = 20
    Two_PI = 2 * math.pi
    project.update_planet(p, cx, cy, planets, Two_PI)
    assert planets[0]['px'] != 0

def test_revolution():
    Two_PI = 2 * math.pi
    planet_old_angle = planets[4]['angle']

    planets[4]['angle'] += 2 * Two_PI
    planet = planets[4]
    project.revolution(planet, Two_PI , planet_old_angle)
    assert planet['revolutions'] == 1

    planets[4]['angle'] += 6 * Two_PI
    planet = planets[4]
    project.revolution(planet, Two_PI , planet_old_angle)
    assert planet['revolutions'] > 0

def test_orbit_planet():
    Two_PI = 2 * math.pi
    result = project.orbit_planet(40 , 20 , planets , Two_PI)
    assert (0,0) not in result

    assert type(result) == set

    assert len(result) > 0










