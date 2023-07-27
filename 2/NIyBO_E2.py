from manim import*
#####################################################################################
######################  Norma inducida y bases ortonormales  ########################
#####################################################################################

#####################################################################################
###############################  Segunda escena  ####################################
######################  versión: Manim Community v0.17.3   ##########################
#####################################################################################

ROJO = '#FF0000'
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

SKIP_DEFAULT = False #Útil para lo siguiente: si sólo quieres renderizar una sección, cambia esta variable a 'True' y cambia el valor de 'skip_animations' de esa sección a 'not SKIP_DEFAULT'


class ClockwiseTransform(ReplacementTransform):
    def __init__(
        self,
        mobject: Mobject,
        target_mobject: Mobject,
        path_arc: float = -np.pi,
        **kwargs,
    ) -> None:
        super().__init__(mobject, target_mobject, path_arc=path_arc, **kwargs)

class CounterclockwiseTransform(ReplacementTransform):
    def __init__(
        self,
        mobject: Mobject,
        target_mobject: Mobject,
        path_arc: float = np.pi,
        **kwargs,
    ) -> None:
        super().__init__(mobject, target_mobject, path_arc=path_arc, **kwargs)

class E2(MovingCameraScene):
    def demostracion(self):
              
      #Texto
      t1=MathTex("\\forall \\ \\vec{v}\in V, \\vec{v}\\neq \\vec{0}").scale(.6).move_to(2.5*UP)
      t1[0][0].set_opacity(0)
      t1[0][1:3].set_color(VERDE)
      t1[0][6:8].set_color(VERDE)
      t2 = MathTex("\\hat{v}:=", "\\frac{1}{||\\vec{v}||}\\vec{v}", "\\text{ es \\emph{normal}}").scale(.6).next_to(t1, 3*DOWN).shift(0.75*RIGHT)
      t2[0][0:2].set_color(NARANJA)
      t3 = MathTex("\\bigg|\\bigg|\\frac{1}{||\\vec{v}||}\\vec{v}\\bigg|\\bigg|").scale(.6).next_to(t2[0], 3*DOWN).shift(0.65*LEFT)
      t3[0][12:14].set_color(VERDE)
      t3[0][16:18].set_color(VERDE)
      t3_2=MathTex("=\\bigg|\\frac{1}{||\\vec{v}||}\\bigg|||\\vec{v}|| \\hspace{2mm} \\text{(escalabilidad absoluta)}").scale(.6)
      t4 = MathTex("= \\frac{1}{||\\vec{v}||}||\\vec{v}|| \\hspace{4.5mm} \\text{(Ejercicio 2.1)}").scale(.6)
      t4[0][16:28].set_color(AZUL)
      t5 = MathTex("= 1.").scale(.6)
      t6 = BraceText(t2[0], "vector \\emph{normal}", brace_direction=LEFT).scale(0.6).shift(0.75*RIGHT)
      t6_2 = BraceText(t2, "\\emph{normalización}", brace_direction=RIGHT).scale(0.6).shift(2*LEFT)
      g1=VGroup(t3_2,t4,t5).arrange(direction=DOWN, aligned_edge=LEFT).shift(DOWN)
      t7 = MathTex("U=\{\\vec{u}_{1},...,\\vec{u}_{k}\} \\subseteq V", "\\text{ es \\emph{normal} }", "\\text{si } ||\\vec{u}_i||=1 \\text{ para }  1\\le i\\le k.").scale(.6)
      t10 = MathTex("\\vec{0} \\notin \{\\vec{v}_1,...,\\vec{v}_k\} \\subseteq V", "\\Rightarrow", "\{\\hat{v}_1,...,\\hat{v}_k\} \\subseteq V \\text{ es un conjunto normal.}").scale(.6)

      #Geometría
      grid = NumberPlane(x_range=[-3.25, 3.25, 1], y_range=[-3.25, 3.25, 1],
                         background_line_style={
                             "stroke_width": 1, "stroke_opacity": 0.5}
                         ).shift(6.3*LEFT)
      vec_v = Vector(direction = [2.5, 1, 0], color=VERDE).shift(6.3*LEFT)
      norma_v_neq_0 = Group(BraceBetweenPoints(6.3*LEFT+[2.5,1,0], 6.3*LEFT), MathTex("||\\vec{v}||\\neq0").shift(5.3*LEFT+1.25*UP).scale(0.6))
      norma_v_neq_0[1][0][2:4].set_color(VERDE)
      norma_v = Group(BraceBetweenPoints(6.3*LEFT+[2.5,1,0], 6.3*LEFT), MathTex("||\\vec{v}||").shift(5.3*LEFT+1.25*UP).scale(0.75))
      norma_v[1][0][2:4].set_color(VERDE)
      vec_v_hat = Vector(direction = [0.93, 0.37, 0], color=NARANJA).shift(6.3*LEFT)
      norma_v_hat = Group(BraceBetweenPoints(6.3*LEFT, 6.3*LEFT+[0.93, 0.37, 0]), MathTex("||\\hat{v}||=1").shift(5.65*LEFT+0.5*DOWN).scale(0.75))
      norma_v_hat[1][0][2:4].set_color(NARANJA)
      circ_v = Circle(radius=2.6925, color=VERDE, stroke_opacity=0.35, fill_opacity=0).shift(6.3*LEFT)
      circ_v_hat = Circle(radius=1, color=NARANJA, stroke_opacity=0.35, fill_opacity=0).shift(6.3*LEFT)

      #Alineación
      t3_2.next_to(t3, RIGHT)
      t4.next_to(t3_2[0], 2.5*DOWN).shift(.625*LEFT)
      t5.next_to(t4[0][:15], 2.5*DOWN).shift(.4*LEFT)
      
      #Animaciones
      self.play(self.camera.frame.animate.move_to(2.5*LEFT))
      
      self.next_section("Por lo pronto...", skip_animations=SKIP_DEFAULT) #Los nombres de las secciones corresponden a...
      self.play(Write(grid), run_time=1.5)  #...la parte del guión con las que deben ir...
      self.play(Write(t1))                  #...sincronizadas las animaciones.
      self.play(Write(vec_v), run_time=0.5)
      self.wait()
      self.next_section("...la norma de nuestro vector es un número real distinto de cero...", skip_animations=SKIP_DEFAULT)
      self.play(Write(norma_v_neq_0[0]))
      self.play(Write(norma_v_neq_0[1]))
      self.wait()
      self.next_section("...un inverso multiplicativo.", skip_animations=SKIP_DEFAULT)
      self.play(Write(t3[0][8:16]))
      self.play(FadeOut(norma_v_neq_0))
      self.wait()
      self.play(Write(t3[0][16:18]))
      self.wait()
      self.next_section("...por la propiedad de escalabilidad absoluta de la norma...", skip_animations=SKIP_DEFAULT)
      self.play(Write(t3[0][0:8]), Write(t3[0][18:]), t3[0][12:14].animate.set_color(WHITE), t3[0][16:18].animate.set_color(WHITE))
      self.play(Write(t3_2))
      self.play(Write(t4))
      self.wait()
      self.next_section("...es igual a uno.", skip_animations=SKIP_DEFAULT)
      self.play(Write(t5))
      self.wait()
      self.next_section("...obtenemos un vector normal.", skip_animations=SKIP_DEFAULT)
      self.play(Write(t2[1:]), run_time=2)
      self.wait()
      self.play(Unwrite(t2[2]))
      self.wait()
      self.next_section("...en la misma dirección y sentido que el vector original.", skip_animations=SKIP_DEFAULT)
      self.play(t2[1].animate.set_color(NARANJA), Write(vec_v_hat))
      self.wait()
      self.next_section("...de la siguiente manera:", skip_animations=SKIP_DEFAULT)
      self.play(Write(t2[0]))
      self.play(Write(t6))
      self.play(Write(norma_v_hat[0]))
      self.play(Write(norma_v_hat[1]))
      self.wait()
      self.next_section("...como normalización.", skip_animations=SKIP_DEFAULT)
      self.play(t1[0][0].animate.set_opacity(1))
      self.wait(4.5)
      self.play(Write(t6_2))
      self.wait()
      self.play(FadeOut(t3,t3_2,t4,t5,t6,t6_2))
      self.play(grid.animate.shift(4.5*LEFT),
                vec_v.animate.shift(4.5*LEFT),
                vec_v_hat.animate.shift(4.5*LEFT),
                norma_v_hat.animate.shift(4.5*LEFT),
                self.camera.frame.animate.move_to(ORIGIN)
                )
      self.wait()

      self.next_section("Decimos que un conjunto de vectores en un espacio normado...", skip_animations=SKIP_DEFAULT)
      t7.next_to(t2, 3*DOWN)
      self.play(Write(t7[0]))
      self.play(Write(t7[1]))
      self.play(Write(t7[2]))
      self.wait()

      self.next_section("...cualquier conjunto que no contenga al vector nulo...", skip_animations=SKIP_DEFAULT)
      t10.next_to(t7, 3*DOWN)
      self.play(Write(t10[0]))
      self.wait(2)
      self.play(Write(t10[1]))
      self.wait()
      self.play(Write(t10[2]))
      self.wait(2)
      self.play(FadeOut(t7,t10))
      self.wait()

      self.next_section("Volvamos ahora a la ecuación anterior.", skip_animations=SKIP_DEFAULT)
      self.play(grid.animate.shift(4.5*RIGHT),
                vec_v.animate.shift(4.5*RIGHT),
                vec_v_hat.animate.shift(4.5*RIGHT),
                t2[0][2].animate.set_opacity(0),
                norma_v_hat.animate.shift(4.5*RIGHT),
                self.camera.frame.animate.move_to(2.5*LEFT)
                )
      self.play(Circumscribe(t2[0:2]))
      self.play(FadeIn(t3, t3_2, t4, t5))
      self.wait()

      self.next_section("...por la norma de 'v'...", skip_animations=SKIP_DEFAULT)
      self.play(t2[1][:4].animate.set_color(WHITE),
                t2[1][4:6].animate.set_color(VERDE),
                t2[1][6:8].animate.set_color(WHITE),
                t2[1][8:].animate.set_color(VERDE)
                )
      self.wait()
      norm_v = MathTex("||\\vec{v}||").scale(0.5).next_to(t2, 0.5*LEFT)
      norm_v[0][2:4].set_color(VERDE)
      grupo = Group(norm_v, t2[0][0:2], t2[0][3], t2[1][8:])
      self.play(FadeOut(t2[0][2]),
                FadeOut(t2[1][0:2]),
                ClockwiseTransform(t2[1][2:8], norm_v),
                t2[1][8:].animate.shift(0.45*LEFT))
      self.wait()
      self.play(Circumscribe(grupo))
      self.wait()

      self.next_section("...por su norma.", skip_animations=SKIP_DEFAULT)
      self.play(Write(norma_v[0]))
      self.play(Write(norma_v[1]))
      self.wait()

      self.next_section("...magnitudes entre vectores...", skip_animations=SKIP_DEFAULT)
      self.play(Write(circ_v))
      self.wait()

      self.next_section("...unidad en esta escala.", skip_animations=SKIP_DEFAULT)
      self.play(Write(circ_v_hat))
      self.wait()

    def construct(self):
            self.demostracion()
