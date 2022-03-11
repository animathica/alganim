from manim import *
from alganim import *

ROJO = '#FF0000'
ROSA = '#E95771'
AZUL = '#0087FF'
NARANJA = '#FF7700'
VERDE = '#1FFF00'
MAGENTA = '#FF00FF'
AMARILLO = "#FFFF00"
GRIS = "#888888"
MAGENTA_CLARO = "#FF67FF"
AZUL_CLARO = "#9CDCEB"
AZUL_OSCURO = "#1C758A"
TEAL_A = "#ACEAD7"
TEAL_E = "#49A88F"
MOSTAZA_OSCURO = "#FFD025"
MOSTAZA_CLARO = "#FFE072"

class DemoSpanArrow(ThreeDScene):

    grid = NumberPlane()

    def cosas(self):

        a,b = 2,5
        c,d = 6,4
        e,f,g = -5,-1,2

        def up1(obj):
            t = VT.get_value()
            New = SpanArrow((a*t,b*t,0),color=ROJO)
            obj.become(New)

        def up2(obj):
            t = VT2.get_value()
            New = DoubleSpanArrow((-c*t,-d*t,0),(c*t,d*t,0), number_tips=20).set_color(color=MAROON)
            obj.become(New)

        sA = SpanArrow((a,b,0),color=ROJO)
        VT = ValueTracker(1)
        VT2 = ValueTracker(1)

        s2A = DoubleSpanArrow((-c,-d,0),(c,d,0), number_tips=20).set_color(color=MAROON)
        s2A2 = DoubleSpanArrow((e,g,0),(f,g,0)).set_color(color=[AZUL,MAGENTA])

        VT3=ValueTracker(PI)
        def up3(obj):
            t = VT3.get_value()
            norma = np.linalg.norm((e-f,0))/2
            m = ((e+f)/2,g)
            E ,F = (norma * np.cos(t)) + m[0], (norma * np.sin(t)) + m[1]
            G ,H = -(norma * np.cos(t)) + m[0], -(norma * np.sin(t)) + m[1]
            new = DoubleSpanArrow((E,F,0),(G,H,0)).set_color(color=[AZUL,MAGENTA])
            obj.become(new)

        self.play(Create(sA))
        self.wait()
        sA.add_updater(up1)
        self.wait()
        self.play(VT.animate.set_value(0.5),run_time=2)
        self.wait()
        self.play(Create(s2A))
        self.wait()
        self.play(Create(s2A2))
        s2A.add_updater(up2)
        self.wait()
        self.play(VT2.animate.set_value(2),run_time=2)
        self.wait()
        s2A2.add_updater(up3)
        self.play(VT3.animate.increment_value(2*PI),run_time=4)


    def construct(self):
        self.play(Write(self.grid))
        self.cosas()
        self.wait(2)

if __name__ == '__main__':
    import os
    os.system('manim -pqh D:/dariortizq/Dario/Animathica/alganim/alganimPy/demoSpanArrow.py')