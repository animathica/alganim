#from typing_extensions import runtime
from manim import *
#####################################################################################
######################  Norma inducida y bases ortonormales  ########################
#####################################################################################

#####################################################################################
###############################  Cuarta escena ######################################
######################  versión: Manim Community v0.17.2   ##########################
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


class SE1 (Scene):
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


class SE2(MovingCameraScene):
     def bortonormal(self):

       texto1 = MathTex(r"N=\{\vec{n}_1,...,\vec{n}_k\}\subseteq V \ \text{es \emph{ortonormal}}").scale(.55)
       texto1_2 = MathTex(r"\text{si} \ \langle \vec{n}_i , \vec{n}_j \rangle =").scale(.55)
       texto1_3 = MathTex(r"0 \text{ para } i\neq j, \text{ con } 1\le i,j\le k,",r"\text{ y }", r"||" , r"\vec{n}_i" , r"||", r"=1" , r"\text{ para } 1\le i\le k.").scale(.55)

       texto_1=VGroup(texto1, texto1_2, texto1_3).arrange(direction=RIGHT, center=True)
       texto1_2.next_to(texto1, RIGHT)
       texto1_3.next_to(texto1_2, RIGHT)
       texto_1.move_to(3*UP)

       texto2_3 = MathTex(r"0 \text{ para } i\neq j, \text{ con } 1\le i,j\le k,",r"\text{ y }", r" \langle " , r"\vec{n}_i" , r", \vec{n}_i \rangle", r"=1" , r"\text{ para } 1\le i\le k.").scale(.55)
       texto2_3.next_to(texto1_2, RIGHT)

       texto3_3 = MathTex(r" \begin{cases} 1 &\text{si } j=i, \\ 0 &\text{si } j\neq i, \end{cases} \text{ con } 1\le i,j\le k.").scale(.55)
       texto3_3.next_to(texto1_2, RIGHT)


       texto3 = MathTex(r"N=\{\vec{n}_1,...,\vec{n}_k\}",r"\text{ es una base \emph{ortonormal} de } V \text{ si}").scale(.55)
       texto5 = MathTex(r"\langle N \rangle = V,").scale(.55)
       texto5_c1 = Tex("$1 \\ $~", "si~","$j = i,$").scale(.55)
       texto5_c2 = Tex("$0 \\ $~", " si~", " $j \\neq i.$").scale(.55)
       for i, item in enumerate(texto5_c2):
          item.align_to(texto5_c1[i], LEFT)
       texto5_c1g = VGroup(*texto5_c1)
       texto5_c2g = VGroup(*texto5_c2)
       texto5_c2g.next_to(texto5_c1g, DOWN)
       texto5_g = VGroup(texto5_c1g, texto5_c2g)
       b3 = Brace(texto5_g, .1*LEFT)
       P_ij = b3.get_text("$\\langle \\vec{n}_i, \\vec{n}_j\\rangle$ =").scale(.55)
       nj_ni = VGroup(P_ij, b3, texto5_g).arrange(direction=RIGHT, buff=.15)

       N_ort = VGroup(texto5, nj_ni).arrange(direction=RIGHT, buff=1.75, center=True)

       texto3.move_to(UP, aligned_edge=RIGHT)

       self.wait()
       self.play(self.camera.frame.animate.move_to(1.5*UP))

       for element in texto_1:
         self.play(Write(element), run_time=2)

       self.wait(2)
       self.play(ReplacementTransform(texto1_3, texto2_3))

       self.wait(2)
       self.play(FadeOut(texto2_3))
       self.play(Write(texto3_3))

       self.wait(2)
       texto3.shift(2.75*RIGHT)
       self.play(Write(texto3))

       self.wait(2)
       N_ort[1].move_to(0*LEFT)

       self.play(Write(N_ort[0]))
       self.play(Write(N_ort[1]))

     def construct(self):
      self.bortonormal()
      self.wait(2)


class SE3(MovingCameraScene):
    def construct(self):
        #----------------------------------- ESPACIO V EN GENERAL
        dim_V = MathTex("\\text{dim}\\left(V\\right)=k<\\infty").scale(0.6).to_edge(UP).shift(0.2*RIGHT).shift(0.5*UP)
        base_beta = Tex(
            "$\\beta = \\{\\vec{b}_1,..., \\vec{b}_k\\}$",  # 0
            " base de ",  # 1
            "$V$"  # 2
        ).move_to(UP)
        base_propiedades = Tex(
            "$\\langle \\beta\\rangle = V$",
            "$,\\,\\beta$ es l.i."
        )
        combination = MathTex(
            "\\vec{v}",  # 0
            "=",  # 1
            "c_1",  # 2
            "\\vec{b}_1",  # 3
            "+",  # 4
            "\\cdots",  # 5
            "+",  # 6
            "c_k",  # 7
            "\\vec{b}_k"  # 8
        )
        coeficientes_c = Tex("¿",
                             "$c_i$",
                             "?")
        group_1 = VGroup(base_beta, base_propiedades,
                         combination, coeficientes_c).scale(0.7)
        group_1.arrange(1.8*DOWN, center=False, aligned_edge=LEFT)
        combination_copy = group_1[2].copy()
        #----------------------------------- ESPACIO V CON PRODUCTO INTERNO, BASE ORTOGONAL
        base_gamma = Tex(
            "$\\Gamma = \\{\\vec{g}_1,..., \\vec{g}_k\\}$",  # 0
            " base ortogonal de",  # 1
            " $V$"  # 2
        ).move_to(UP)

        gen_gamma = MathTex(r"\langle\Gamma\rangle = V, ")
        case_1 = Tex("$\\langle \\vec{g}_i, \\vec{g}_i\\rangle \\neq 0$ \\ ", " si", " $j = i$,")
        case_2 = Tex("$0$", " si", " $j \\neq i$.")
        for i, item in enumerate(case_2):
            item.align_to(case_1[i], LEFT)
        case_1_g = VGroup(*case_1)
        case_2_g = VGroup(*case_2)
        case_2_g.next_to(case_1_g, DOWN)
        cases_group = VGroup(case_1_g, case_2_g)
        braces = Brace(cases_group, LEFT)
        producto_ij = braces.get_text("$\\langle \\vec{g}_i, \\vec{g}_j\\rangle$ =")
        gj_gi = VGroup(producto_ij, braces, cases_group)

        base_gamma_propiedades = VGroup(gen_gamma, gj_gi).arrange(
            direction=RIGHT, buff=0.20, center=False)

        combination_dg = MathTex(
            r"\vec{v}",  # 0
            r"=",  # 1
            r"d_1",  # 2
            r"\vec{g}_1",  # 3
            r"+\cdots+",  # 4
            r"d_k",  # 5
            r"\vec{g}_k"  # 6
        )
        coeficientes_d = MathTex(r"d_i = \frac{\langle \vec{v}, \vec{g}_i\rangle}{\langle \vec{g}_i, \vec{g}_i \rangle}, \quad 1\le i\le k")
        group_2 = VGroup(base_gamma, base_gamma_propiedades,
                         combination_dg, coeficientes_d).scale(0.7)
        group_2.arrange(1*DOWN, center=False, aligned_edge=LEFT)
        coeficientes_d.set_y(coeficientes_c.get_y()).shift(0.05*DOWN)

        #----------------------------------- BASE ORTONORMAL
        base_N = Tex(
            " $N = \\{\\hat{n}_1,..., \\hat{n}_k\\}$",  # 0
            " base ortonormal de",  # 1
            " $V$"  # 2
        ).move_to(UP)

        gen_N = MathTex(r"\langle N\rangle = V, ")
        case_1_N = Tex("$1$ \\ ", " si", " $j = i$,")
        case_2_N = Tex("$0$", " si", " $j \\neq i$.")
        for i, item in enumerate(case_2_N):
            item.align_to(case_1_N[i], LEFT)
        case_1_g_N = VGroup(*case_1_N)
        case_2_g_N = VGroup(*case_2_N)
        case_2_g_N.next_to(case_1_g_N, DOWN)
        cases_group_N = VGroup(case_1_g_N, case_2_g_N)
        braces_N = Brace(cases_group_N, LEFT)
        producto_ij_N = braces_N.get_text("$\\langle \\hat{n}_i, \\hat{n}_j\\rangle$ =")
        nj_ni = VGroup(producto_ij_N, braces_N, cases_group_N)

        base_N_propiedades = VGroup(gen_N, nj_ni).arrange(
            direction=RIGHT, buff=0.20, center=False)

        combination_fn = MathTex(
            r"\vec{v}",  # 0
            r"=",  # 1
            r"f_1",  # 2
            r"\hat{n}_1",  # 3
            r"+\cdots+",  # 4
            r"f_k",  # 5
            r"\hat{n}_k"  # 6
        )
        coeficientes_f = MathTex(r"f_i = \frac{\langle \vec{v}, \hat{n}_i\rangle}{\langle \hat{n}_i, \hat{n}_i\rangle}, \quad 1\le i\le k")
        group_3 = VGroup(base_N, base_N_propiedades,
                         combination_fn, coeficientes_f).scale(0.7)
        group_3.arrange(1*DOWN, center=False, aligned_edge=LEFT)
        uno = MathTex("1").scale(0.7).scale(0.8)

        #Alineación de grupos

        groups = VGroup(group_1, group_2, group_3).scale(0.8).shift(1.5*UP)
        groups.arrange_in_grid(rows=1, cols=3, buff=1, row_heights=None)
        groups[1].align_to(groups[0], UP).shift(0.5*LEFT+0.05*DOWN)
        groups[2].align_to(groups[1], UP).shift(1.0*LEFT)
        combination_fn.shift(0.05*DOWN)


        #----------------------------------- ANIMACIONES
        #--------------------------------

        self.camera.frame.shift(0.2*RIGHT+1.5*UP)
        self.play(Write(dim_V))
        self.play(
            FadeIn(groups[0][:]),
            run_time=2)
        self.wait()

        self.play(
            FadeIn(groups[1][:]),
            run_time=2)
        self.wait()

        self.play(Write(groups[2][0:3][:]))
        self.wait()
        self.play(Write(groups[2][3][:]))
        self.wait()

        #-----------------------------------

        uno.move_to(coeficientes_f[0][12:21].get_center())
        self.play(ReplacementTransform(coeficientes_f[0][12:21], uno))
        self.wait()

        self.play(coeficientes_f[0][11:21].animate.set_color(BLACK),
                  uno.animate.set_color(BLACK))
        self.play(coeficientes_f[0][3:11].animate.shift(0.2*DOWN+0.1*LEFT),
                  coeficientes_f[0][21].animate.shift(0.175*LEFT+0.075*DOWN))
        self.wait()
