from manim import *
import numpy as np

class Pendulum(VGroup):
    def __init__(self, length=3, weight_diameter=0.2, top_point=np.array([0, 0, 0]), rod_style={"stroke_width": 3, "stroke_color": WHITE}, weight_style={"fill_color": BLUE, "fill_opacity": 1, "stroke_color": BLUE}, **kwargs):
        super().__init__(**kwargs)
        self.length = length
        self.weight_diameter = weight_diameter
        self.top_point = top_point
        self.rod_style = rod_style
        self.weight_style = weight_style
        self.create_rod()
        self.create_weight()
        self.time = 0

        # Agregar un updater para hacer que el péndulo oscile
        self.add_updater(self.update_pendulum)

    def create_rod(self):
        self.rod = Line(self.top_point, self.top_point + self.length * DOWN, **self.rod_style)
        self.add(self.rod)

    def create_weight(self):
        self.weight = Circle(radius=self.weight_diameter, **self.weight_style)
        self.weight.move_to(self.rod.get_end())
        self.add(self.weight)

    def update_pendulum(self, mobject, dt):
        self.time += dt
        angle_range = np.radians([0, 360])  # Oscilar entre el primer y cuarto cuadrante
        angle = np.mean(angle_range) + np.diff(angle_range)/2 * np.sin(2 * np.pi * 0.5 * self.time)  # 0.5 Hz frequency

        self.rod.set_angle(angle + PI / 2)
        self.weight.move_to(self.rod.get_end())

class PendulumScene(Scene):
    def construct(self):
        pendulum = Pendulum()
        self.add(pendulum)

        # Agregar la función de frecuencia en LaTeX
        frequency_function = MathTex(r"f(t) = \frac{1}{2} + \frac{180}{2} \sin(2\pi \cdot 0.5 \cdot t)")
        frequency_function.to_edge(UP)
        self.add(frequency_function)

        self.wait(10)  # Aumentar el tiempo de espera para ver más oscilaciones
        self.play(Write(frequency_function))
        self.wait(5)