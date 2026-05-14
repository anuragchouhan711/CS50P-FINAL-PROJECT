import time
import sys
import math
import argparse
import curses


def main():
    list = {"mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","all"}
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--speed", type=float, default=0.1, help="Speed of simulation (default: 0.1)",)
    parser.add_argument(
        "-p", "--planet", type=str, nargs="+", default=["all"], help="Planet names")
    parser.add_argument(
        "-t", "--timer", type=int, default=99999, help="years timer")
    args = parser.parse_args()

    if args.speed < 0.001:
        sys.exit("Too fast speed")
    if args.speed > 1:
        sys.exit("Too slow speed")

    args.planet = [p.lower() for p in args.planet]
    for things in args.planet:
        if things not in list:
            sys.exit("Please entre a valid planet.")


    def simulation(stdscr):
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1 , curses.COLOR_WHITE , -1)
        curses.init_pair(2 , curses.COLOR_MAGENTA, -1)
        curses.init_pair(3 , curses.COLOR_BLUE , -1)
        curses.init_pair(4 , curses.COLOR_RED, -1)
        curses.init_pair(5 , curses.COLOR_YELLOW, -1)
        curses.init_pair(6 , curses.COLOR_CYAN, -1)
        curses.init_pair(7 , curses.COLOR_BLUE,-1)
        curses.init_pair(8 , curses.COLOR_BLUE, -1)
        curses.init_pair(9, curses.COLOR_YELLOW,-1)
        curses.init_pair(10 ,curses.COLOR_WHITE,-1)
        try :
            starter(args.planet, args.speed, args.timer ,stdscr)
        except KeyboardInterrupt:
            sys.exit("Simulation stopped .")
    curses.wrapper(simulation)

def starter(p, s, t, stdscr):
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


    max_y, max_x = stdscr.getmaxyx()
    if max_y < 52 or max_x < 80:
        sys.exit("Terminal size is too small !")


    cx = round(max_x/2)
    cy = round(max_y/2)
    Two_PI = 2 * math.pi
    oldmax_y, oldmax_x = stdscr.getmaxyx()
    stdscr.nodelay(True)
    orbit = orbit_planet(cx ,cy ,planets ,Two_PI)
    while True:
        key = stdscr.getch()
        if key == ord("q"):
            sys.exit()
        if key == ord("=") or key == ord("+"):
            if 0.001 <= s - 0.05 <= 1 :
                s -= 0.05
            else :
                pass
        if key == ord("-") or key == ord("_"):
            if 0.001 <= s + 0.05 <= 1 :
                s += 0.05

        max_y, max_x = stdscr.getmaxyx()
        while max_y < 52 or max_x < 80 :
            max_y, max_x = stdscr.getmaxyx()
            stdscr.addstr(1 , 1 , "Terminal size too low! , Increase size to continue")
            stdscr.refresh()
            time.sleep(0.1)
        if oldmax_y != max_y or oldmax_x != max_x:
            cx = round(max_x/2)
            cy = round(max_y/2)
            orbit = orbit_planet(cx ,cy ,planets ,Two_PI)
            oldmax_y = max_y
            oldmax_x = max_x

        update_planet(p , cx ,cy ,planets ,Two_PI)
        draw_grid(orbit , cx , cy ,planets ,stdscr ,max_y, max_x)
        score(planets ,stdscr ,max_y , p)
        time.sleep(s)
        timer(t,planets)


def draw_grid(orbit , cx , cy, planets , stdscr ,max_y, max_x):
    stdscr.erase()
    occupied = set()
    for ox , oy in orbit:
        if 0 <= oy < max_y and 0 <= ox < max_x - 1:
            stdscr.addch(oy ,ox ,".",curses.color_pair(10) )

    if 0 <= cy < max_y and 0 <= cx < max_x - 1:
        stdscr.addch(cy ,cx ,"*" ,curses.color_pair(9) )

    for pl in planets:
        if 0 <= pl['py'] < max_y and 0 <= pl['px'] < max_x - 1 :
                cord = pl['py'] , pl['px']
                if cord in occupied:
                    stdscr.addch(pl['py'] ,pl['px'] ,"X" ,curses.color_pair(pl['no']) )
                elif cord not in occupied:
                    stdscr.addch(pl['py'] ,pl['px'] ,pl['symbol'] ,curses.color_pair(pl['no']) )
                    occupied.add(cord)

    stdscr.refresh()


def score(planets ,stdscr ,max_y , p):
        if "earth" in p or "all" in p:
            title = f"Time: {(planets[2])['revolutions']}years"
            stdscr.addstr(max_y - 10, 1, title )
        else :
            stdscr.addstr(max_y - 10, 1, "Time: NO refrence cause earth dosen't exist! " )

        y = max_y - 8
        for planet in planets:
            stdscr.addstr(y,1,f"{str(planet['name']).title()} revolutions: {planet['revolutions']}")
            y += 1
        stdscr.refresh()


def update_planet(p ,cx ,cy, planets ,Two_PI):
    for planet in planets:
        if "all" in p or planet["name"] in p:
            planet_old_angle = planet["angle"]
            planet["angle"] += planet["speed"]
            planet["px"] = round(cx + planet["radius"] * math.cos(planet["angle"]) * 2)
            planet["py"] = round(cy + planet["radius"] * math.sin(planet["angle"]))
            revolution(planet, Two_PI , planet_old_angle)


def revolution(planet, Two_PI , planet_old_angle):
    if int(planet["angle"] / Two_PI) > int(planet_old_angle / Two_PI) :
        planet["revolutions"] += 1

def orbit_planet(cx ,cy, planets ,Two_PI):
    orbits = set()
    for pl in planets:
        temp_angle = 0
        while temp_angle < Two_PI:
            px = round(cx + pl['radius'] * math.cos(temp_angle) *2 )
            py = round(cy + pl["radius"] * math.sin(temp_angle))
            combo = px , py
            orbits.add(combo)
            temp_angle += 0.05
    return orbits


def timer(t, planets):
    if int(planets[2]["revolutions"]) == t:
        sys.exit(f"\n{t}years has been passed")



if __name__ == "__main__":
    main()
