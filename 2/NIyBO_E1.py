from manim import*


class Subeescena1(Scene):
  def propiedades(self):
     t0 = Tex("Norma")
     t1 = MathTex("||\\cdot||:V \\to \\mathbb{R}").scale(.6)
     p1 = MathTex("\\forall \ \\vec{u}\\in V \ \\forall \ a\\in K").scale(.6)
     p2 = MathTex("||a\\vec{u}||= |a| \ ||\\vec{u}||").scale(.6)
     p3 = MathTex("||\\vec{u}|| = 0  \\Longleftrightarrow  \\vec{u} = \\vec{0}").scale(.6)
     p4 = MathTex("||\\vec{u}+\\vec{v}|| \\le  ||\\vec{u}|| + ||\\vec{v}||").scale(.6)
     g1 = VGroup(p1, p2, p3, p4).arrange(buff=.15, direction=DOWN, aligned_edge=LEFT )
     t2 = Tex("Estabilidad absoluta").scale(.5)
     t3 = Tex("Distinción del vector nulo").scale(.5) 
     t4 = Tex("Desigualdad del triángulo").scale(.5)

     t0.move_to(3*UP) 
     self.play(Write(t0))
     t1.move_to(2.5*UP)
     self.play(Write(t1))
     for element in g1:
         self.play(Write(element), run_time=2.3)
     t2.next_to(p2, 2*RIGHT)
     t3.next_to(p3, 2*RIGHT)
     t4.next_to(p4, 2*RIGHT)
     self.play(Write(t2))    
     self.play(Write(t3))
     self.play(Write(t4))


  def construct(self):
             self.propiedades()


class Subescena2(Scene):
  def ecuaciones(self):
    e1 = MathTex("\\vec{u}\in V, \\vec{u} \\neq 0 \Rightarrow ||\\vec{u}|| > 0 ")
    e2 = MathTex("\\frac{1}{||\\vec{v}||} \\vec{v}")
    e3 = MathTex("||\\frac{1}{||\\vec{v}||}|| = |\\frac{1}{||\\vec{v}||}| ||\\vec{v}||")

    self.play(Write(e1))
    e1.move_to(2*UP)
    self.play(Write(e2))
    e2.move_to(UP)
    self.play(Write(e3))


  def construct(self):
             self.ecuaciones()
 from manim import*
AZUL = '#0087FF'
ROJO = '#FF0000'

class EscenaGeomtrica(MovingCameraScene):
    def construct(self):
     plano = NumberPlane(
         x_range=[-10,10],
         y_range=[-10,10],
         background_line_style={
             "stroke_color": TEAL,
             "stroke_width": 3,
             "stroke_opacity":.07
         }
     )
     t1 = MathTex("\\frac{1}{||\\vec{u}||}=\\vec{u}")
     t2 = MathTex("\\vec{u}=||\\vec{u}||\\vec{u}")
     t3 = MathTex("||\\vec{u}||")
     v1 = Vector ([1,1], color=AZUL)
     v2 = Vector([2,2], color=ROJO)
     p_1 =(0,0,0)
     p_2 =(1,1,0)
     b1 = BraceBetweenPoints(p_1, p_2)


     
     self.play(Write(t1))
     t2.next_to(t1, DOWN)
     self.wait(6)
     self.play(Write(t2))
     self.wait(5)
     t1.move_to(2*LEFT+3*UP)
     t2.move_to(2*LEFT+2*UP)
     self.play(self.camera.frame.animate.move_to(RIGHT+1.5*UP))
     self.play(Write(plano))
     self.play(Write(v1))
     self.play(Write(v2))
     self.play(Write(b1))
     t3.next_to(b1, .3*RIGHT+.01*DOWN)
     self.play(Write(t3))     
