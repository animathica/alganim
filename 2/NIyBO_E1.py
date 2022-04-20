from manim import*


class Subeescena1(Scene):
  def propiedades(self):
     t0 = Tex("Norma")
     t1 = MathTex("||\\cdot||:V \\to \\mathbb{R}").scale(.6)
     p1 = MathTex("\\forall \ \\vec{u}\\in V \ \\forall \ a\\in K").scale(.6)

     p2 = MathTex("||a\\vec{u}||" , "=", "|a| \ ||\\vec{u}||").scale(.6).move_to(2*LEFT)
     p3 = MathTex("||\\vec{u}|| = 0 ", " \\Longleftrightarrow", " \\vec{u} = \\vec{0}").scale(.6).next_to(p2, DOWN)
     p4 = MathTex("||\\vec{u}+\\vec{v}|| ", "\\le", " ||\\vec{u}|| + ||\\vec{v}||").scale(.6).next_to(p3, DOWN)

     pe2 = p2.get_part_by_tex("=")
     pe3 = p3.get_part_by_tex("\\Longleftrightarrow").align_to(pe2, LEFT)
     pe4 = p4.get_part_by_tex("\\le").align_to(pe3, LEFT)
     p2.get_part_by_tex("||a\\vec{u}||").next_to(pe2, LEFT)
     p2.get_part_by_tex("|a| \ ||\\vec{u}||").next_to(pe2, RIGHT)
     p3.get_part_by_tex("||\\vec{u}|| = 0 ").next_to(pe3,LEFT)
     p3.get_part_by_tex(" \\vec{u} = \\vec{0}").next_to(pe3, RIGHT)
     p4.get_part_by_tex("||\\vec{u}+\\vec{v}|| ").next_to(pe4, LEFT)
     p4.get_part_by_tex(" ||\\vec{u}|| + ||\\vec{v}||").next_to(pe4, RIGHT)

     tinv = Tex("aaaa", color = BLACK).scale(0.6).next_to(p3, RIGHT)
     t2 = Tex("Estabilidad absoluta").scale(0.6)
     t3 = Tex("Distinción del vector nulo").scale(0.6)
     t4 = Tex("Desigualdad del triángulo").scale(0.6)

     g= VGroup(t2,t3,t4).arrange(direction=DOWN, aligned_edge= LEFT)
     g.next_to(tinv, RIGHT)
     t0.move_to(2.5*UP)
     self.play(Write(t0))
     t1.move_to(2*UP)
     p1.move_to(1.3*UP)
     self.play(Write(t1))
     self.play(Write(p1))

     self.play(Write(p2))
     self.play(Write(p3))
     self.play(Write(p4))
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


class Demos(MovingCameraScene):
    def demostracion(self):

              
     t1=MathTex("\\vec{v}\in V, \\vec{v}\\neq \\vec{0} \Rightarrow ||\\vec{v}||>0").scale(.8)
     t2 =MathTex("\\frac{1}{||\\vec{v}||}\\vec{v}").scale(.8)
     t3 = MathTex("|\\frac{1}{||\\vec{v}||}|").scale(.8)
     t3_2=MathTex("=|\\frac{1}{||\\vec{v}||}|||\\vec{v}||").scale(.8)
     t4 = MathTex("= \\frac{1}{||\\vec{v}||}||\\vec{v}||").scale(.8)
     t5 = MathTex("= 1.").scale(.8)
     t6 = MathTex("=\\hat{v}").scale(.8)
     g1=VGroup(t3_2,t4,t5,t6).arrange(direction=DOWN, aligned_edge=LEFT).shift(DOWN)
     t7 = MathTex("U={\\vec{u_{1}},...,\\vec{u_{k}}} \\subseteq V").scale(.6)
     t8 = Tex("Es normal si").scale(.6)
     t9 = MathTex("||\\vec{u_i}||=1 \ si \  1<i<k ").scale(.6)
     t10 =MathTex("\\vec{0} \\notin {{\\vec{v_1},...,\\vec{v_i}}} \\subseteq V").scale(.6)
     t11 = MathTex("\Rightarrow {{\\vec{v_1},...,\\vec{v_k}}} \Rightarrow \\subseteq ").scale(.6)
     t12 = Tex("V es un conjunto normal").scale(.6)
     t13 = MathTex("\\vec{v}=||\\vec{v}||\\hat{v}").scale(.6)

     t1.move_to(UP+.02*LEFT)
     t2.next_to(t1, DOWN).shift(.01*RIGHT)
     t3.next_to(t2, DOWN+.05*LEFT)            
     t3_2.next_to(t3, RIGHT)
     t4.next_to(t3_2, DOWN).shift(.1*LEFT)
     t5.next_to(t4, DOWN).shift(.53*LEFT)
     
     t6.next_to(t2, RIGHT).shift(.94*LEFT)
     self.play(Write(t1))
     self.play(Write(t2))
     self.play(Write(t3))
     t2.move_to(.75*LEFT)
     for element in g1:
         self.play(Write(element), run_time=2.3)

     self.play(self.camera.frame.animate.move_to(2*DOWN))
    
     self.play(FadeOut(t3,t3_2,t4,t5))
     t7.next_to(t2, DOWN).shift(LEFT)
     self.play(Write(t7))
     t8.next_to(t7, RIGHT)
     self.play(Write(t8))
     t9.next_to(t8, RIGHT)
     self.play(Write(t9))
     t10.next_to(t7, DOWN).shift(.1*LEFT)
     self.play(Write(t10))
     t11.next_to(t10, RIGHT)
     self.play(Write(t11))
     t12.next_to(t11, RIGHT).shift(.1*LEFT)
     self.play(Write(t12))
     self.play(FadeOut(t7,t8,t9,t10,t11,t12,t6))
     self.play(Transform(t2,t13))


    def construct(self):
            self.demostracion()
      
      
      
      

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
