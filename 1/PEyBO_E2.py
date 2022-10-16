# -*- coding: utf-8 -*-

from manim import *
#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################

#####################################################################################
###############################  Segunda escena  ####################################
#####################  versión: Manim Community v0.15.2  ############################
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

class SE1(MovingCameraScene):

    #-------------------------------------------------------Propiedades del producto escalar en un campo K
     def propiedades(self):
         
         t0 = Tex("Producto escalar").scale(.8)
         t1 =  MathTex("\langle\cdot, \cdot\\rangle:V\\times V\\to K ").scale(.8).shift(LEFT)

         p1 =  MathTex("\\forall \ \\vec{u}, \\vec{v}, \\vec{w}&\in V, \ \\forall \ a\in K ").scale(.6)


         p2 = MathTex("  \langle\\vec{u}+\\vec{w},\\vec{v}\\rangle").scale(.6)
         p2_2 = MathTex(" = \langle \\vec{u} , \\vec{v} \\rangle + \langle \\vec{w} , \\vec{v} \\rangle \\").scale(.6)


         p3 = MathTex("  \langle a\\vec{u} , \\vec{v} \\rangle").scale(.6)
         p3_2 = MathTex("&= a \langle \\vec{u} , \\vec{v} \\rangle\\").scale(.6)


         p4 = MathTex("  \langle \\vec{u} , \\vec{v} \\rangle").scale(.6)
         p4_2= MathTex("= \overline{ \langle \\vec{v} , \\vec{u} \\rangle}\\").scale(.6)


         p5 = MathTex(" \\vec{u}\\neq \\vec{0}").scale(.6)
         p5_2= MathTex("\Rightarrow \langle \\vec{u} , \\vec{u} \\rangle > 0 ").scale(.6)

         g1 = VGroup( p2, p2_2, p3, p3_2, p4, p4_2, p5, p5_2 ).arrange(buff=.13, direction=DOWN, aligned_edge = LEFT).shift(RIGHT+0.3*DOWN)
         p2.next_to(p2_2, LEFT)
         p3.next_to(p3_2, LEFT)
         p4.next_to(p4_2, LEFT)
         p5.next_to(p5_2, LEFT)


         g3 =VGroup(p2, p2_2, p3, p3_2, color=WHITE)
         b1 = Brace(g3, direction=RIGHT)
         t2 = MathTex("\langle a\\vec{u}+\\vec{w} , \\vec{v} \\rangle = a \langle \\vec{u} , \\vec{v} \\rangle + \langle \\vec{w} , \\vec{v} \\rangle\ ").scale(.6)
         t3 = MathTex("\langle \\vec{u} , a\\vec{w}+\\vec{v} \\rangle = \overline{a} \langle \\vec{u} , \\vec{w} \\rangle + \langle \\vec{u} , \\vec{v} \\rangle \\").scale(.6)
         t4 = Tex("\\textit{Linealidad} en la entrada izquierda").scale(.56)
         t5 = Tex("\\textit{Antilinealidad} en la entrada derecha").scale(.55)
         t6 = Tex("Positivo definido").scale(.55)
         t7 = Tex("Simetria conjugada").scale(.55)
         g4 = VGroup(g3,p4, color=WHITE)
         b2 = Brace(g4, direction=LEFT)



         #ANIMACIONES#
         self.play(self.camera.frame.animate.move_to(UP))
         t0.move_to(3.5*UP).shift(.2*LEFT)
         self.play(Write(t0))
         t1.next_to(g1, 7*UP).shift(.45*LEFT)
         self.play(Write(t1))
         p1.next_to(t1, DOWN)
         self.play(Write(p1))
         self.wait(3)
         g1.move_to(.1*UP)
         for element in g1:
          self.play(Write(element),run_time=2.3)
         t6.next_to(p5_2, 3.2*RIGHT)
         t7.next_to(p4_2, 5.6*RIGHT) 
        
         
         b1.next_to(p2_2, RIGHT*UP).shift(1.5*RIGHT+.3*DOWN)
         self.play(Write(b1))
         self.wait()
         t2.next_to(b1, direction=RIGHT)
         self.play(FadeIn(t2))
         t4.next_to(t2, DOWN)
         self.play(Write(t4))               
         self.wait(3)
         self.play(Write(t7))
         self.play(Write(t6))
         b2.next_to(p3, LEFT*2*UP).shift(1.2*LEFT)
         self.play(Write(b2))
         t3.next_to(b2, direction=LEFT).shift(0.2*LEFT)
         self.play(Write(t3))
         t5.next_to(t3, DOWN)
         self.play(Write(t5))
         self.wait(23)
         self.play(FadeOut(b1, b2, t2, t3,t4,t5,t6,t7))
         self.wait(18)
         self.play(FadeOut(g1))
         self.play(FadeOut(t1,p1))

     def construct(self):
            self.propiedades()


#-------------------------------------------Definición de ortogonalidad
class SE2(MovingCameraScene):
 

     def ortogonalidad(self):
     
       o1 = MathTex("\\vec{u},\\vec{v}\in V \ \\text{son \emph{ortogonales}} \ ").scale(.5)
       o1_2 = MathTex(" (\\vec{u}\perp\\vec{v}) \ \\text{si} \ \langle \\vec{u} , \\vec{v} \\rangle = 0 \ ").scale(.5)
       o1_3 = MathTex("\\text{ó, equivalentemente,} \ \langle \\vec{v} , \\vec{u} \\rangle = 0.").scale(.5)

       go_1=VGroup(o1, o1_2, o1_3).arrange(direction=RIGHT, center=True)
       o1_2.next_to(o1, RIGHT)
       o1_3.next_to(o1_2, RIGHT)
       go_1.move_to(3*UP)


       o2 = MathTex("\\text{O=}\{\\vec{o}_1,...,\\vec{o}_k\}\subseteq V ").scale(.5)
       o2_2=MathTex("\\text{es \emph{ortogonal} si} \ \langle \\vec{o}_i , \\vec{o}_j \\rangle = 0 ").scale(.5)
       o2_3= MathTex(" \\text{para} \ i\\neq j, \ \\text{con} \ 1\le i,j\le k.").scale(.5)

       go_2 =VGroup(o2, o2_2, o2_3).arrange(direction=RIGHT, center=True)
       go_2.move_to(2*UP)


      
       o3 = MathTex("  \Gamma=\{\\vec{g}_1,...,\\vec{g}_k\}" ).scale(.5)
       o4 = Tex("base  \\textit{ortogonal} de V").scale(.5)
       o5 = MathTex(r"\langle\Gamma\rangle = V, ").scale(.5)
       o5_c1 = Tex("$\\langle \\vec{g}_i, \\vec{g}_i\\rangle > 0 \\ $~", "si~","$j = i,$").scale(.6)
       o5_c2 = Tex("$0 \\ $~", " si~", " $j \\neq i.$").scale(.6)
       for i, item in enumerate(o5_c2):
          item.align_to(o5_c1[i], LEFT)
       o5_c1g = VGroup(*o5_c1)
       o5_c2g = VGroup(*o5_c2)
       o5_c2g.next_to(o5_c1g, DOWN)
       o5_g = VGroup(o5_c1g, o5_c2g)
       b3 = Brace(o5_g, .1*LEFT)
       P_ij = b3.get_text("$\\langle \\vec{g}_i, \\vec{g}_j\\rangle$ =").scale(.6)
       gj_gi = VGroup(P_ij, b3, o5_g).arrange(direction=RIGHT, buff=.15)
       
       gamma_Prop = VGroup(o5, gj_gi).arrange(direction=RIGHT, buff=0.75, center=True)
       
        
       self.wait()
       self.play(self.camera.frame.animate.move_to(1.5*UP))
       for element in go_1:
         self.play(Write(element), run_time=2)
        
       for element in go_2:
         self.play(Write(element), run_time=2)

       o3.move_to(1.25*UP, aligned_edge=RIGHT)
       self.play(Write(o3))
       o4.move_to(3*UP)
       o4.next_to(o3, direction=RIGHT)
       self.play(Write(o4))
       self.wait(2)
       gamma_Prop[0].move_to(2*LEFT)

       self.play(Write(gamma_Prop[0]))
       self.play(Write(gamma_Prop[1]))

     def construct(self):
      self.ortogonalidad()
