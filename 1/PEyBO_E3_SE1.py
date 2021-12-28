# -*- coding: utf-8 -*-

from typing_extensions import runtime
from manim import *


#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################


#####################################################################################
###############################  Terecera escena ####################################
###############################  versión: Manim Community v0.8.0   ##################
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

v = np.array([-4,-2,0])
g1 = np.array([0.5,-0.5,0])
g2 = np.array([-1,-1,0])

class Subescena_1(Scene):
   '''
    Esta subescena presenta la solución del problema de los coeficientes haciendo uso del producto punto en R2 como producto
    interno. Consta de una parte geométrica (lado izquierdo) y una parte algebráica (lado derecho), que se complementan para
    ilustrar la solución del problema en un caso particular.
   '''

   def gen_plano(self, vec1, vec2):

      origen = np.array([0,0,0])
      g1 = np.array([0.5,-0.5,0])
      g2 = np.array([-1,-1,0])

      plano_1 = Polygon(origen, g1, g2, g1+g2, stroke_width = 0).shift(2.5*LEFT+1.5*UP)
      plano_2  = Polygon(origen, g1, g2, origen, stroke_width=0).shift(2.5*LEFT+1.5*UP)

      vt1 = ValueTracker(1)

      # Función que rellena plano.
      def upd_for_plano(obj):
         t = vt1.get_value()
         vert4 = t*(g1+g2)
         New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA_CLARO, opacity = 1)
         obj.become(New_plano)
         #self.bring_to_back(obj)

   def construct(self):

      ###########
      # OBJETOS #
      ###########

      ###### OBJETOS conj_ortogonal
      gamma_c_og = MathTex(r"\Gamma \text{ es }", r"\text{un conjunto \textit{ortogonal}}")\
         .scale(0.6).shift(4.5*RIGHT + DOWN)


      ppunto_1 = MathTex(r" \langle \vec{g}_1, \vec{g}_2 \rangle").shift(3*RIGHT + 2*UP).scale(0.6)
      ppunto_2 = MathTex(r" = \begin{pmatrix} 1 \\ -1 \end{pmatrix} \cdot \
          \begin{pmatrix} -2 \\ -2 \end{pmatrix}").next_to(ppunto_1,RIGHT).scale(0.6).shift(0.6*LEFT)
      ppunto_3 = MathTex(r"= (1)(-2) + (-1)(-2)").scale(0.6)
      ppunto_4 = MathTex(r"= 0 ").scale(0.6)
      ppunto_5 = MathTex(r"= \langle \vec{g}_2 , \vec{g}_1 \rangle ").scale(0.6)

      ppunto = VGroup(ppunto_2, ppunto_3, ppunto_4, ppunto_5)\
         .arrange(DOWN, center=False, aligned_edge=LEFT)


         # Se declaran los vectores que aparecen en el grid para usarlos posteriormente
         # y dibujar su generado
      g1 = np.array([1,-1,0])
      g2 = np.array([-2,-2,0])

      vec_g1 = Arrow((0, 0, 0),(0.5,-0.5,0), buff = 0, color = ROJO).shift(2.5*LEFT)
      g1_label = MathTex(r"\vec{g}_1").move_to(vec_g1.get_end()+(0.4/(np.linalg.norm(g1)))*g1).scale(0.7)

      vec_g2 = Arrow((0, 0, 0), (-1,-1,0), buff = 0, color = AZUL).shift(2.5*LEFT)
      g2_label = MathTex(r"\vec{g}_2").move_to(vec_g2.get_end()+(0.4/(np.linalg.norm(g2)))*g2).scale(0.7)

      # OBJETOS base_ortogonal
      gamma_li = MathTex(r"\vec{g}_1\ \text{y}\ \vec{g}_2\ \text{son \textit{l. i.} ,}").shift(4.5*RIGHT+2*UP).scale(0.6)

      ld_g1 = DashedLine(-2*g1, 3.5*g1).set_color(MAGENTA).set_opacity(0.5).shift(2.5*LEFT+1.5*UP)
      ld_g2 = DashedLine(-1*g2, 1.75*g2).set_color(MAGENTA).set_opacity(0.5).shift(2.5*LEFT+1.5*UP)

      gamma_gen = MathTex(r"\langle \Gamma \rangle = \mathbb{R}^2,").shift(4.5*RIGHT+0.5*UP).scale(0.6)

      gamma_b_og = MathTex(r" \text{ una }", r"\textit{base ortogonal}}").scale(0.6).next_to(gamma_c_og[0], RIGHT).shift(0.03*DOWN+0.1*LEFT)

      #### OBJETOS calc_c1
      vg1_11 = MathTex(r" \langle \vec{v}, \vec{g}_1 \rangle").shift(3*RIGHT + 3*UP).scale(0.6)
      ppig1 = MathTex(r"= ").scale(0.6).next_to(vg1_11,RIGHT)

      pp11 = MathTex(r"\begin{pmatrix} -8 \\ -4 \end{pmatrix} \cdot \
         \begin{pmatrix} 1 \\ -1 \end{pmatrix}").scale(0.6).next_to(ppig1,RIGHT)
      pp21 = MathTex(r" (-8)(1) + (-4)(-1)").scale(0.6).move_to(pp11).shift(0.2*RIGHT)
      pp31 = MathTex(r" -8 + 4").scale(0.6).move_to(pp21).shift(0.7*LEFT)
      pp41 = MathTex(r" -4\ ,").scale(0.6).move_to(pp21).shift(LEFT)


      vg1_21 = MathTex(r" \langle \vec{v}, \vec{g}_1 \rangle").shift(3*RIGHT + 2*UP).scale(0.6)
      ppl_11 = MathTex(r" = \langle c_1\vec{g}_1 + c_2\vec{g}_2\
         , \vec{g}_1 \rangle").scale(0.6).next_to(vg1_21,RIGHT)
      ppl_ig1 = MathTex(r"= ").scale(0.6)
      ppl_21 = MathTex(r" c_1 \langle \vec{g}_1, \vec{g}_1 \rangle", r"+" r"\
         c_2\langle \vec{g}_2, \vec{g}_1 \rangle").scale(0.6)
      ppl_31 = MathTex(r"  c_1 \langle \vec{g}_1, \vec{g}_1 \rangle", r"+" r"\
         c_2 (0)").scale(0.6)
      ppl_41 = MathTex(r"  c_1 \langle \vec{g}_1, \vec{g}_1 \rangle", r"+" r"\
          0").scale(0.6)
      ppl_51 = MathTex(r"  c_1 \langle \vec{g}_1, \vec{g}_1 \rangle").scale(0.6)
      ppl_ig21 = MathTex(r"= ").scale(0.6)
      ppl_61 = MathTex(r" c_1 \begin{pmatrix} 1 \\ -1 \end{pmatrix} \cdot \
         \begin{pmatrix} 1 \\ -1 \end{pmatrix}").scale(0.6)
      ppl_71 = MathTex(r" c_1 \big((1)(1)+(-1)(-1)\big)").scale(0.6)
      ppl_81 = MathTex(r"  c_1 \big( 2 \big)").scale(0.6)
      ppl_91 = MathTex(r" = 2c_1\ ,").scale(0.6)

      ppl1 = VGroup(ppl_11, ppl_ig1, ppl_ig21, ppl_91).arrange(DOWN, center = False, aligned_edge=LEFT)

      ppl_21.next_to(ppl_ig1, RIGHT)
      ppl_31.move_to(ppl_21).shift(0.25*LEFT)
      ppl_41.move_to(ppl_21).shift(0.5*LEFT)
      ppl_51.move_to(ppl_21).shift(0.85*LEFT)

      ppl_ig21.shift(0.3*DOWN)
      ppl_91.shift(0.4*DOWN)
      ppl_61.next_to(ppl_ig21, RIGHT)
      ppl_71.move_to(ppl_61).shift(0.2*RIGHT)
      ppl_81.move_to(ppl_61).shift(0.8*LEFT)

      c1_eq1 = MathTex(r"\Rightarrow -4 = 2c_1 \Rightarrow").scale(0.6).shift(3.7*RIGHT + DOWN)
      c1_11 = MathTex(r" c_1 = - ", r" \frac{4}{2} ").next_to(c1_eq1).scale(0.6).shift(0.4*LEFT)
      c11 = MathTex(r" c_1 = - " , r" 2 ").next_to(c1_eq1).scale(0.6).shift(0.4*LEFT)

      srct_11 = SurroundingRectangle(c11, color = AMARILLO)

      #### OBJETOS calc_c2
      vg1_1 = MathTex(r" \langle \vec{v}, \vec{g}_2 \rangle").shift(3*RIGHT + 3*UP).scale(0.6)
      ppig = MathTex(r"= ").scale(0.6).next_to(vg1_1,RIGHT)

      pp1 = MathTex(r"\begin{pmatrix} -8 \\ -4 \end{pmatrix} \cdot \
         \begin{pmatrix} -2 \\ -2 \end{pmatrix}").scale(0.6).next_to(ppig,RIGHT)
      pp2 = MathTex(r" (-8)(-2) + (-4)(-2)").scale(0.55).move_to(pp1).shift(0.2*RIGHT)
      pp3 = MathTex(r" 16 + 8").scale(0.6).move_to(pp2).shift(0.7*LEFT)
      pp4 = MathTex(r" 24\ ,").scale(0.6).move_to(pp2).shift(LEFT)


      vg1_2 = MathTex(r" \langle \vec{v}, \vec{g}_2 \rangle").shift(3*RIGHT + 2*UP).scale(0.6)
      ppl_1 = MathTex(r" = \langle c_1\vec{g}_1 + c_2\vec{g}_2\
         , \vec{g}_2 \rangle").scale(0.6).next_to(vg1_2,RIGHT)
      ppl_ig = MathTex(r"= ").scale(0.6)
      ppl_2 = MathTex(r" c_1", r"\langle \vec{g}_1, \vec{g}_2 \rangle", r"+" r"\
         c_2\langle \vec{g}_2, \vec{g}_2 \rangle").scale(0.6)
      ppl_3 = MathTex(r"  c_1" ,r"(0)", r"+" r"\
         c_2 \langle \vec{g}_2, \vec{g}_2 \rangle").scale(0.6)
      ppl_4 = MathTex(r" 0" ,r" ",r"+" ,r"c_2 \langle \vec{g}_2, \vec{g}_2 \rangle").scale(0.6)
      ppl_5 = MathTex(r"  c_2 \langle \vec{g}_2, \vec{g}_2 \rangle").scale(0.6)
      ppl_ig2 = MathTex(r"= ").scale(0.6)
      ppl_6 = MathTex(r" c_2 \begin{pmatrix} -2 \\ -2 \end{pmatrix} \cdot \
         \begin{pmatrix} -2 \\ -2 \end{pmatrix}").scale(0.6)
      ppl_7 = MathTex(r" c_2 \big((-2)(-2)+(-2)(-2)\big)").scale(0.5)
      ppl_8 = MathTex(r"  c_2 \big( 8 \big)").scale(0.6)
      ppl_9 = MathTex(r" = 8c_2\ ,").scale(0.6)

      ppl = VGroup(ppl_1, ppl_ig, ppl_ig2, ppl_9).arrange(DOWN, center = False, aligned_edge=LEFT)

      ppl_2.next_to(ppl_ig, RIGHT)
      ppl_3.move_to(ppl_2).shift(0.25*LEFT)
      ppl_4.move_to(ppl_2).shift(0.5*LEFT)
      ppl_5.move_to(ppl_2).shift(0.85*LEFT)

      ppl_ig2.shift(0.3*DOWN)
      ppl_9.shift(0.4*DOWN)
      ppl_6.next_to(ppl_ig2, RIGHT)
      ppl_7.move_to(ppl_6).shift(0.2*RIGHT)
      ppl_8.move_to(ppl_6).shift(0.8*LEFT)

      c1_eq2 = MathTex(r"\Rightarrow 24 = 8c_2 \Rightarrow").scale(0.6).shift(3.7*RIGHT + DOWN)
      c1_12 = MathTex(r" c_2 = ", r" \frac{24}{8} ").next_to(c1_eq2).scale(0.6).shift(0.4*LEFT)
      c12 = MathTex(r" c_2 = " , r" 3 ").next_to(c1_eq2).scale(0.6).shift(0.4*LEFT)


      srct_1 = SurroundingRectangle(c12, color = AMARILLO)

       # Separación de la pantalla en grid y pizarrón

      grid = NumberPlane(x_range = [-9,9,1],y_range = [-7,4,1],
         background_line_style={"stroke_width": 1, "stroke_opacity": 0.5}).scale(0.5)
      borde_der = Line(start = [4.5,2.75,0], end = [4.5,-2.75,0], stroke_width = 1)
      borde_izq = Line(start = [-4.5,2.75,0], end = [-4.5,-2.75,0], stroke_width = 1 )
      borde_sup = Line(start = [-4.5,2.75,0], end = [4.5,2.75,0], stroke_width = 1 )
      borde_inf = Line(start = [-4.5,-2.75,0], end = [4.5,-2.75,0], stroke_width = 1 )
      lilgrid = VGroup(grid, borde_sup, borde_der, borde_inf, borde_izq).shift(2.5*LEFT).shift(0.75*UP)

      dot = Dot().shift(3*LEFT+0.5*UP) #OBJETO DE JUGUETE PARA UBICAR COORDENADAS

      # Textos del nuevo planteamiento del problema

      vec_obj_tex = MathTex(r" \vec{v} = \begin{pmatrix} -8 \\ -4 \end{pmatrix}").shift(6*LEFT+2.5*DOWN).scale(0.4)

      gamma_tex = MathTex(r" \Gamma = \{ \vec{g}_1, \vec{g}_2\} = \Bigg\{\begin{pmatrix} 1 \\ -1 \end{pmatrix},\
          \begin{pmatrix} -2 \\ -2 \end{pmatrix} \Bigg\}").next_to(vec_obj_tex, DOWN).scale(0.4).shift(1*RIGHT + 0.5*UP)

      comblin_abs = MathTex(r" \vec{v} " , r"=" ,r"c_1" ,r"\vec{g}_1" ,r"+" ,r"c_2", r"\vec{g}_2")\
         .shift(2.5*DOWN).scale(0.5)

      print("LCA", len(comblin_abs))
      comblin_R2 = MathTex(r"\begin{pmatrix} -8 \\ -4 \end{pmatrix}\ " , r"\ =" ,r"c_1\ ", r"\begin{pmatrix} 1 \\ -1 \end{pmatrix}", r"\ +", r"\ c_2 \ " ,r"\begin{pmatrix} -2\\ -2 \end{pmatrix}")\
         .move_to(comblin_abs).scale(0.4)

      print("LCR", len(comblin_R2))

      coefs_incog = MathTex(r"  \text{¿}", r"c_1, " , r" c_2\text{?}").next_to(comblin_abs, DOWN).scale(0.5).shift(0.2*DOWN)
      c2_incog = MathTex( r" ", r"c_1 = -2,  ", r"\text{¿}c_2\text{?}").next_to(comblin_abs, DOWN).scale(0.5).shift(0.2*DOWN)
      no_incog = MathTex( r" ", r" c_1 = -2, ", r"\   c_2 = 3").next_to(comblin_abs, DOWN).scale(0.5).shift(0.2*DOWN)


      grupo_intro = VGroup(vec_obj_tex, gamma_tex, comblin_abs, comblin_R2, coefs_incog)

      # Vectores que se muestran en el NumberPlane
      v = np.array([-4,-2,0])
      g1 = np.array([0.5,-0.5,0])
      g2 = np.array([-1,-1,0])

      vec_obj = Arrow((0, 0, 0), (-4,-2,0), buff = 0, color = NARANJA, max_tip_length_to_length_ratio=0.4).shift(2.5*LEFT+1.5*UP)
      v_label = MathTex(r"\vec{v}").move_to(vec_obj.get_end()+(0.3/(np.linalg.norm(v)))*v)\
         .scale(0.7)
      v_label2 = MathTex(r"c_1",r"\vec{g}_1", r"+", r"c_2", r"\vec{g}_2").move_to(vec_obj.get_end()+(0.3/(np.linalg.norm(v)))*v)\
         .scale(0.5).shift(RIGHT+0.1*DOWN)
      v_label3 = MathTex(r"-2",r"\vec{g}_1", r"+", r"3", r"\vec{g}_2").move_to(vec_obj.get_end()+(0.3/(np.linalg.norm(v)))*v)\
         .scale(0.5).shift(RIGHT+0.1*DOWN)   

      vec_g1 = Arrow((0, 0, 0),(0.5,-0.5,0), buff = 0, color = ROJO, max_tip_length_to_length_ratio=0.4).shift(2.5*LEFT+1.5*UP)
      g1_label = MathTex(r"\vec{g}_1").move_to(vec_g1.get_end()+(0.4/(np.linalg.norm(g1)))*g1).scale(0.5)

      vec_g2 = Arrow((0, 0, 0), (-1,-1,0), buff = 0, color = AZUL, max_tip_length_to_length_ratio=0.4).shift(2.5*LEFT+1.5*UP)
      g2_label = MathTex(r"\vec{g}_2").move_to(vec_g2.get_end()+(0.4/(np.linalg.norm(g2)))*g2).scale(0.5)

      c1g1_label_1 = MathTex(r"c_1\vec{g}_1 = -2\vec{g}_1").move_to(np.array([-1,1,0])+(0.4/(np.linalg.norm(-2*g1)))*(-2)*g1).scale(0.5)\
         .shift(2.5*LEFT+1.5*UP)
      c2g2_label_1 = MathTex(r"c_2\vec{g}_2 = 3\vec{g_2}").move_to(np.array([-3,-3,0])+(0.4/(np.linalg.norm(3*g2)))*3*g2).scale(0.5)\
         .shift(1.5*LEFT+1.75*UP)

      c1g1_label_2 = MathTex(r"\begin{pmatrix} -2 \\ 2 \end{pmatrix}").move_to(np.array([-1,1,0])+(0.5/(np.linalg.norm(-2*g1)))*(-2)*g1).scale(0.4)\
         .shift(2.5*LEFT+1.5*UP)

      c2g2_label_2 = MathTex(r"\begin{pmatrix} -6 \\ -6 \end{pmatrix}").move_to(np.array([-3,-3,0])+(0.5/(np.linalg.norm(3*g2)))*3*g2).scale(0.4)\
         .shift(1.5*LEFT+1.75*UP)

      # Vectores fantasma para mostrar paralelogramo
      ghost1 = Arrow((0, 0, 0), (-1,1,0), buff = 0, color = ROJO, max_tip_length_to_length_ratio=0.4).set_opacity(0.3).shift(5.5*LEFT+1.5*DOWN)
      ghost2 = Arrow((0, 0, 0), (-3,-3,0), buff = 0, color = AZUL, max_tip_length_to_length_ratio=0.4).set_opacity(0.3).shift(3.5*LEFT+2.5*UP)
      # ValueTrackers y funciones de Updater para transformar los vectores de la base con re-escalamientos

      t_1 = ValueTracker(1)
      t_2 = ValueTracker(1)

      def upd_g1(obj):
         newvec = Arrow((0, 0, 0), t_1.get_value()*g1, buff = 0, color = ROJO, max_tip_length_to_length_ratio=0.4)\
            .shift(2.5*LEFT+1.5*UP)
         obj.become(newvec)

      def upd_g2(obj):
         newvec_2 = Arrow((0, 0, 0), t_2.get_value()*g2, buff = 0, color = AZUL, max_tip_length_to_length_ratio=0.4)\
            .shift(2.5*LEFT+1.5*UP)
         obj.become(newvec_2)

      vec_g1.add_updater(upd_g1)
      vec_g2.add_updater(upd_g2)

      # OBJETOS PARA LA CONFIRMACIÓN DE LA IGUALDAD, ÚLTIMA PARTE DE LA ANIMACIÓN

      c1 = MathTex(r" c_1 = -2 ").scale(0.6).shift(3.5*RIGHT + 3*UP)
      c2 = MathTex(r" c_2 = 3 ").next_to(c1, RIGHT).scale(0.6).shift(.3*RIGHT)

      comblin_abs_c  = MathTex(r" (-2) \vec{g}_1 + (3) \vec{g}_2")\
         .next_to(c2, DOWN).scale(0.5).shift(2*LEFT+DOWN)

      comblin_R2_c = MathTex(r" = (-2) \begin{pmatrix} 1 \\ -1 \end{pmatrix} + (3) \begin{pmatrix} -2\\ -2 \end{pmatrix}")\
         .next_to(comblin_abs_c,RIGHT).scale(0.5).shift(1.5*LEFT)

      comblin_R2_c1 = MathTex(r" =  \begin{pmatrix} -2 \\ 2 \end{pmatrix} + (3) \begin{pmatrix} -2\\ -2 \end{pmatrix}")\
         .scale(0.6)

      comblin_R2_c2 = MathTex(r" = \begin{pmatrix} -2 \\ 2 \end{pmatrix} + \begin{pmatrix} -6\\ -6 \end{pmatrix}")\
         .scale(0.6)

      suma = MathTex(r" = \begin{pmatrix} -8 \\ -4 \end{pmatrix}\
          = \vec{v}")\
         .scale(0.6)

      confirm = VGroup(comblin_R2_c, comblin_R2_c1, comblin_R2_c2, suma).arrange(DOWN, center = False, aligned_edge=LEFT)

      ###############
      # ANIMACIONES #
      ###############

      self.add(lilgrid)
      self.play(Write(vec_obj_tex))
      self.wait()
      self.play(FadeIn(vec_obj))
      self.play(FadeIn(v_label)) # Agregar label v_obj
      self.add_foreground_mobjects(vec_obj,v_label)

      self.wait()
      self.play(Write(gamma_tex))
      self.wait()
      self.play(Write(vec_g1), Write(vec_g2))
      self.play(FadeIn(g1_label), FadeIn(g2_label))

      self.add_foreground_mobjects(vec_g1 , vec_g2, g1_label, g2_label)

      self.play(Write(comblin_abs))
      self.wait()

      # Transformación CUIDADOSA de la combinación lineal
      self.play(ReplacementTransform(comblin_abs[0],comblin_R2[0]), ReplacementTransform(comblin_abs[1],comblin_R2[1]),
      ReplacementTransform(comblin_abs[2],comblin_R2[2]), ReplacementTransform(comblin_abs[3],comblin_R2[3]),
      ReplacementTransform(comblin_abs[4],comblin_R2[4]), ReplacementTransform(comblin_abs[5],comblin_R2[5]),
      ReplacementTransform(comblin_abs[6],comblin_R2[6]))

      self.play(ReplacementTransform(v_label,v_label2))

      # Transformar label v_obj
      self.play(Write(coefs_incog))

      ########## ANIMACIONES conj_ortog

      self.play(Write(ppunto_1))
      self.play(Write(ppunto_2))
      self.play(Write(ppunto_3))
      self.play(Write(ppunto_4))
      self.play(Write(ppunto_5))

      self.wait()
      self.play(Write(gamma_c_og))
      self.wait()
      self.play(gamma_c_og.animate.shift(9.5*LEFT+2.75*DOWN).scale(0.7))


      self.play(FadeOut(ppunto), FadeOut(ppunto_1))


      # ANIMACIONES base_ortogonal
      self.play(Create(ld_g1))
      self.play(Create(ld_g2))
      self.wait(1)
      self.play(Write(gamma_li))
      self.wait(2)
      self.play( FadeOut(ld_g1), FadeOut(ld_g2))
      self.play(Write(gamma_gen))
      self.wait(2)
         # Animación del espacio generado
      self.play(gamma_c_og.animate.shift(9.5*RIGHT+2.75*UP).scale(1/0.7))
      self.wait()
      self.play(FadeOut(gamma_c_og[1]))
      self.play(Write(gamma_b_og))
      self.wait()
      self.play(FadeOut(gamma_c_og[0]), gamma_b_og.animate.shift(9.5*LEFT+2.75*DOWN).scale(0.7))
      self.play(FadeOut(gamma_li), FadeOut(gamma_gen))



      ##### ANIMACIONES calc_c1

      self.play(Write(vg1_11))
      self.play(Write(ppig1),Write(pp11))
      self.play(ReplacementTransform(pp11,pp21))
      self.wait()
      self.play(ReplacementTransform(pp21,pp31))
      self.wait()
      self.play(ReplacementTransform(pp31,pp41))
      self.wait()

      self.play(Write(vg1_21))
      self.play(Write(ppl_11))
      self.play(Write(ppl_ig1),Write(ppl_21))
      self.wait()
      self.play(ReplacementTransform(ppl_21,ppl_31))
      self.wait()
      self.play(ReplacementTransform(ppl_31,ppl_41))
      self.wait()
      self.play(ReplacementTransform(ppl_41,ppl_51))
      self.play(Write(ppl_ig21),Write(ppl_61))
      self.wait()
      self.play(ReplacementTransform(ppl_61, ppl_71))
      self.wait()
      self.play(ReplacementTransform(ppl_71, ppl_81))
      self.play(Write(ppl_91))

      self.wait()
      self.play(Write(c1_eq1))
      self.play(Write(c1_11))
      self.play(ReplacementTransform(c1_11, c11))
      self.play(Write(srct_11))

      self.play(ReplacementTransform(coefs_incog,c2_incog))

      self.play(FadeOut(vg1_11),FadeOut(vg1_21),FadeOut(pp31), FadeOut(ppl1),
       FadeOut(c1_eq1), FadeOut(c11), FadeOut(srct_11), FadeOut(ppig1), FadeOut(pp41),
       FadeOut(ppl_51), FadeOut(ppl_81))


      self.play(Write(vg1_1))
      self.play(Write(ppig),Write(pp1))
      self.play(ReplacementTransform(pp1,pp2))
      self.wait()
      self.play(ReplacementTransform(pp2,pp3))
      self.wait()
      self.play(ReplacementTransform(pp3,pp4))
      self.wait()

      self.play(Write(vg1_2))
      self.play(Write(ppl_1))
      self.play(Write(ppl_ig),Write(ppl_2))
      self.wait()
      self.play(ReplacementTransform(ppl_2,ppl_3))
      self.wait()
      self.play(ReplacementTransform(ppl_3,ppl_4))
      self.wait()
      self.play(ReplacementTransform(ppl_4,ppl_5))
      self.play(Write(ppl_ig2),Write(ppl_6))
      self.wait()
      self.play(ReplacementTransform(ppl_6, ppl_7))
      self.wait()
      self.play(ReplacementTransform(ppl_7, ppl_8))
      self.play(Write(ppl_9))

      self.wait()
      self.play(Write(c1_eq2))
      self.play(Write(c1_12))
      self.play(ReplacementTransform(c1_12, c12))
      self.play(Write(srct_1))

      self.play(ReplacementTransform(c2_incog, no_incog))


      self.play(FadeOut(vg1_1),FadeOut(vg1_2),FadeOut(pp3), FadeOut(ppl),
       FadeOut(c1_eq2), FadeOut(c12), FadeOut(srct_1), FadeOut(ppig), FadeOut(pp4),
       FadeOut(ppl_5), FadeOut(ppl_8))

      self.wait()
      self.play(Write(c1), Write(c2))
      self.play(Write(comblin_abs_c))
      self.play(Write(comblin_R2_c))

      self.play(FadeOut(g1_label))
      self.play(FadeOut(g2_label))

      self.play(
         t_1.animate.set_value(-2),
         run_time = 2
      )

      self.play(
         t_2.animate.set_value(3),
         run_time = 2
      )

      self.play(Write(c1g1_label_1))
      self.play(Write(c2g2_label_1))

      self.play(Write(comblin_R2_c1))

      self.wait()
      self.play(ReplacementTransform(c1g1_label_1, c1g1_label_2))
      self.play(ReplacementTransform(c2g2_label_1, c2g2_label_2))

      self.play(FadeIn(ghost1),FadeIn(ghost2))
      self.play(ReplacementTransform(v_label2, v_label3))
      self.add_foreground_mobjects(v_label3)
      
      self.wait()
      self.play(Write(comblin_R2_c2))
      self.play(Write(suma))
      
