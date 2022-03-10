from typing_extensions import runtime
from manim import *


#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################


#####################################################################################
###############################  Tercera escena ####################################
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

u = np.array([5,4,0])
v = np.array([8,-3,0])

class Subescena1 (Scene):
  def construct(self):

      #-------------------------------------------- Variables que definen al sistema coordenado
      escala_plano = 0.4
      origen_plano = np.array([-3, 0, 0])


      #--------------------------------------------Textos
      texto_0 = MathTex(r" \vec{u},\vec{v}\in V, \vec{v}\neq \vec{0} ").shift(3*RIGHT + 2*UP).scale(0.6)
      texto_1 = MathTex(r"\frac{\langle \vec{u} , \vec{v} \rangle}{\langle \vec{v} , \vec{v} \rangle} \vec{v}").next_to(texto_0, DOWN).scale(0.6)
      texto_2 = MathTex(r"= \frac{\langle \vec{u} , \vec{v} \rangle}{\big(\sqrt{\langle \vec{v} , \vec{v} \rangle}\big)^2} \vec{v} ").next_to(texto_1,RIGHT).scale(0.6).shift(0.6*LEFT)
      texto_3 = MathTex(r"= \frac{\langle \vec{u} , \vec{v} \rangle}{||\vec{v}||^2} \vec{v}").scale(0.6)
      texto_4 = MathTex(r"= \frac{\langle \vec{u} , \vec{v} \rangle}{||\vec{v}||} \bigg( \frac{1}{||\vec{v}||} \vec{v} \bigg)").scale(0.6)
      texto_5 = MathTex(r"= \frac{\langle \vec{u} , \vec{v} \rangle}{||\vec{v}||} \hat{v}").scale(0.6)
      texto_n = MathTex(r"= \frac{\langle \vec{u} , \vec{v} \rangle}{||\vec{v}||} \hat{v}").next_to(texto_1,RIGHT).scale(0.6).shift(0.6*LEFT)

      texto0 = VGroup(texto_2, texto_3, texto_4, texto_5)\
       .arrange(DOWN, center=False, aligned_edge=LEFT)

      texto_m = MathTex(r"= ",
                        r"{",  # 1
                        r"\langle",  # 2
                        r"\vec{u}",  # 3
                        r",",  # 4
                        r"\vec{v}",  # 5
                        r"\rangle",  # 6
                        r"\over",  # 7
                        r"||\vec{v}||",  # 8
                        r"}",  # 9
                        r"\hat{v}",  #10
                        ).next_to(texto_1,RIGHT).scale(0.6).shift(0.6*LEFT)

      texto_o = MathTex(r"= ",
                        r"{",  # 1
                        r"\langle",  # 2
                        r"\vec{u}",  # 3
                        r",",  # 4
                        r"\vec{v}",  # 5
                        r"\rangle",  # 6
                        r"\over",  # 7
                        r"||\vec{v}||",  # 8
                        r"}",  # 9
                        r"\hat{v}",  #10
                        ).next_to(texto_1,RIGHT).scale(0.6).shift(0.6*LEFT)

      texto_p = MathTex(r"= ",
                        r"{",  # 1
                        r"\langle",  # 2
                        r"\vec{u}",  # 3
                        r",",  # 4
                        r"\vec{v}",  # 5
                        r"\rangle",  # 6
                        r"\over",  # 7
                        r"||\vec{v}||",  # 8
                        r"}",  # 9
                        r"\hat{v}",  #10
                        ).next_to(texto_1,RIGHT).scale(0.6).shift(0.6*LEFT)

      texto_q = MathTex(r"= ",
                        r"{",  # 1
                        r"\langle",  # 2
                        r"\vec{u}",  # 3
                        r",",  # 4
                        r"\vec{v}",  # 5
                        r"\rangle",  # 6
                        r"\over",  # 7
                        r"||\vec{v}||",  # 8
                        r"}",  # 9
                        r"\hat{v}",  #10
                        ).next_to(texto_1,RIGHT).scale(0.6).shift(0.6*LEFT)



      texto_p[2:7].set_color(AMARILLO)
      texto_q[8].set_color(AMARILLO)
      texto_o[10].set_color(AMARILLO)

      #-------------------------------------------- Vectores u y v
      v = np.array([3, -1, 0])
      u = np.array([2, 1.5, 0])
      #--------------------------------------------

      v_vect = Vector(v, buff=0, color=VERDE).shift(origen_plano)
      u_vect = Vector(u, buff=0, color=AZUL).shift(origen_plano)

      distancia_v_label = 0.4*v/(np.linalg.norm(v))
      distancia_u_label = 0.4*u/(np.linalg.norm(u))

      v_label = MathTex(r"\vec{v}").scale(0.8).move_to(
      v_vect.get_end()+distancia_v_label).set_color(VERDE)
      u_label = MathTex(r"\vec{u}").scale(0.8).move_to(
      u_vect.get_end()+distancia_u_label).set_color(AZUL)


      aux_vect = origen_plano+(np.dot(v, u)/np.dot(v, v))*v
      proy_u_v_arrow = Arrow(start=origen_plano, end=aux_vect, buff=0, color=AMARILLO)
      dashedline = DashedLine(
      u_vect.get_end(), proy_u_v_arrow.get_end(), color=AMARILLO
      )


      label_proy_u_v = MathTex(r"{",  # 0
                               r"\langle",  # 1
                               r"\vec{u}",  # 2
                               r",",  # 3
                               r"\vec{v}",  # 4
                               r"\rangle",  # 5
                               r"\over",  # 6
                               r"\langle",  # 7
                               r"\vec{v}",  # 8
                               r",",  # 9
                               r"\vec{v}",  # 10
                               r"\rangle",  # 11
                               r"}",  # 12
                               r"\vec{v}",  # 13
                               ).set_color(AMARILLO).scale(0.8).move_to(origen_plano).shift(0.7*LEFT+0.5*UP)


      label_c = MathTex(r"{",  # 0
                        r"\langle",  # 1
                        r"\vec{u}",  # 2
                        r",",  # 3
                        r"\vec{v}",  # 4
                        r"\rangle",  # 5
                        r"\over",  # 6
                        r"||", #7
                        r"\vec{v}" #8
                        r"||",  #9
                        r"", #10
                        r"", #11
                        r"}",  # 12
                        r"\hat{v}",  #13
                        ).set_color(AMARILLO).scale(0.8).move_to(origen_plano).shift(0.7*LEFT+0.5*UP)



      grid = NumberPlane(x_range=[-10, 10, 1], y_range=[-9, 9, 1],
      background_line_style={
      "stroke_width": 1, "stroke_opacity": 0.5}
      ).scale(escala_plano).shift(origen_plano)

      t = ValueTracker(0)

      def upd_for_v(obj):
          new_vec = Vector(v-(t.get_value()/np.linalg.norm(u)**2)*u,
                           buff=0, color=VERDE).shift(origen_plano)
          obj.become(new_vec)

      def upd_for_proy_u_v_arrow(obj):
          if(np.abs(t.get_value()-np.dot(u, v)) > 0.05):
              v_ = v-t.get_value()*u/np.linalg.norm(u)**2
              aux = origen_plano+(np.dot(v_, u)/np.dot(v_, v_))*v_
              new_arrow = Arrow(start=origen_plano, end=aux, buff=0, color=AMARILLO)
              obj.become(new_arrow)
          else:
              obj.become(Dot(origen_plano, radius=0.1, color=AMARILLO))

      def upd_for_label(obj):
          v_ = v-t.get_value()*u/np.linalg.norm(u)**2
          distancia = 0.4*v_/(np.linalg.norm(v_))
          obj.move_to(v_vect.get_end()+distancia)

      def upd_for_dashedline(obj):
          new_dashedline = DashedLine(
              u_vect.get_end(), proy_u_v_arrow.get_end(), color=AMARILLO
          )
          obj.become(new_dashedline)

      #-------------------------------------------- Animaciones
      self.play(
          Write(grid)
      )

      self.wait(2)
      self.play(
          Write(u_vect),
          Write(u_label)
      )
      self.wait(1)
      self.play(
          Write(v_vect),
          Write(v_label),
      )

      self.wait(2)
      self.play(
          Write(dashedline),
          Write(proy_u_v_arrow),
          FadeIn(label_proy_u_v[:]),
          run_time=1
      )

      self.wait(2)

      self.add_foreground_mobjects(texto_0)
      self.play(Write(texto_0))
      self.wait(0.5)
      self.add_foreground_mobjects(texto_1)
      self.play(Write(texto_1))
      self.wait(0.5)
      self.add_foreground_mobjects(texto_2)
      self.play(Write(texto_2))
      self.wait(0.5)
      self.add_foreground_mobjects(texto_3)
      self.play(Write(texto_3))
      self.wait(0.5)
      self.add_foreground_mobjects(texto_4)
      self.play(Write(texto_4))
      self.wait(0.5)
      self.add_foreground_mobjects(texto_5)
      self.play(Write(texto_5))
      self.wait(3)

      self.play( FadeOut(texto_2), FadeOut(texto_3),FadeOut(texto_4))
      self.play(ReplacementTransform(texto_5,texto_n))
      self.remove(texto_n)
      self.add(texto_m)
      self.play(ReplacementTransform(texto_m,texto_o))
      self.play(ReplacementTransform(texto_o,texto_p))
      self.play(ReplacementTransform(texto_p,texto_q))

      self.play(ReplacementTransform(label_proy_u_v[7:12], label_c[7:12]), FadeOut(label_proy_u_v[12:]),FadeIn(label_c[12:]))
