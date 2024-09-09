from flask import Flask, jsonify
import math
import pygame

app = Flask(__name__)

SCREEN_WIDTH = 1850
SCREEN_HEIGHT = 1850
PLANETS = [
    ("Mercury", 10, 100, 0.2, pygame.Color("#A9A9A9")),    # Gray
    ("Venus", 15, 150, 0.15, pygame.Color("#FFA500")),      # Orange
    ("Earth", 20, 200, 0.1, pygame.Color("#0000FF")),       # Blue
    ("Mars", 17, 250, 0.08, pygame.Color("#FF0000")),       # Red
    ("Jupiter", 40, 350, 0.05, pygame.Color("#FFD700")),    # Gold
    ("Saturn", 35, 450, 0.04, pygame.Color("#D2B48C")),     # Tan
    ("Uranus", 30, 550, 0.03, pygame.Color("#00FFFF")),     # Cyan
    ("Neptune", 30, 650, 0.02, pygame.Color("#00008B")),    # Dark Blue
    ("Pluto", 8, 750, 0.01, pygame.Color("#A0522D"))        # Brown
]

class CelestialBody:
    def __init__(self, name, radius, orbit_radius, orbit_speed, color):
        self.name = name
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.color = color
        self.angle = 0

    def update(self, dt):
        self.angle += self.orbit_speed * dt

    def get_position(self):
        x = SCREEN_WIDTH // 2 + math.cos(self.angle) * self.orbit_radius
        y = SCREEN_HEIGHT // 2 + math.sin(self.angle) * self.orbit_radius
        return {"x": x, "y": y, "name": self.name}

# إعداد البيانات
sun = CelestialBody("Sun", 50, 0, 0, pygame.Color("yellow"))
planets = [CelestialBody(*planet_data) for planet_data in PLANETS]

@app.route('/get_planet_positions', methods=['GET'])
def get_planet_positions():
    dt = 0.016  # نفترض مرور 16 مللي ثانية (تقريباً تساوي 60 إطار في الثانية)
    positions = []
    for planet in planets:
        planet.update(dt)
        positions.append(planet.get_position())
    
    return jsonify(positions)

if __name__ == '__main__':
    app.run(debug=True)
