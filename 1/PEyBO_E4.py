# -*- coding: utf-8 -*-
from manim import *

#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################

#####################################################################################
###############################  Cuarta escena  #####################################
#####################  versión: Manim Community v0.12.0   ###########################
#####################################################################################

ROJO = '#FF0000'
AZUL = '#0087FF'
NARANJA = '#FF7700'
VERDE = '#1FFF00'
MAGENTA = '#FF00FF'
AMARILLO = "#FFFF00"
GRIS = "#505050"
MAGENTA_CLARO = "#FF67FF"
AZUL_CLARO = "#9CDCEB"
AZUL_OSCURO = "#1C758A"
TEAL_A = "#ACEAD7"
TEAL_E = "#49A88F"
MOSTAZA_OSCURO = "#FFD025"
MOSTAZA_CLARO = "#FFE072"

tau = 2*np.pi

# Consturcción de ClockwiseTransform y CounterclockwiseTransform por herencia de ReplacementTransform
# en vez de Transform

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

class SE1(MovingCameraScene):
    def construct(self):
        #----------------------------------- ESPACIO V EN GENERAL
        dim_V = MathTex("\\text{dim}\\left(V\\right)=k<\\infty").scale(0.8).to_edge(UP)
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
                         combination, coeficientes_c).scale(0.8)
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
        coeficientes_d = Tex("¿", r"$d_i$", "?")
        group_2 = VGroup(base_gamma, base_gamma_propiedades,
                         combination_dg, coeficientes_d).scale(0.8)
        group_2.arrange(1*DOWN, center=False, aligned_edge=LEFT)
        coeficientes_d.set_y(coeficientes_c.get_y())

        groups = VGroup(group_1, group_2).scale(0.8).shift(2*UP)
        groups.arrange_in_grid(rows=1, cols=2, buff=1, row_heights=None)
        groups[1].align_to(groups[0], UP)

        #----------------------------------- COEFICIENTES d_i
        def align_t12(text1: Mobject, text2: Mobject, char: str, buff: float) -> None:
            '''
            Función para alinear text1 y text2 de acuerdo al primer signo "char" que aparece
            en el text1. Si el signo char no está en text1 alinea respecto al primer elemento de text1
            buff es un float que indica el desplazamiento vertical de la alineación
            '''
            #encontrar índice de aparición de char en text1
            index = 0
            for i, sub_text in enumerate(text1):
                if str(sub_text) == "SingleStringMathTex('"+char+"')":
                    index = i
                    break
            #encontrar posición del signo = en text1
            position_1 = text1[index].get_center()
            #encontrar índice de aparición de signo = en text2
            idx = 0
            for j, sub_text in enumerate(text2):
                if str(sub_text) == "SingleStringMathTex('"+char+"')":
                    idx = j
                    break
            #encontrar posición del signo = en text2
            position_2 = text2[idx].get_center()
            #position_2 + vec = position_1 ---> vec = position_1-position_2
            #Alineación de text_2
            text2.shift((position_1-position_2)+np.array([0, buff, 0]))

        #----------------------------------- TEXTO PARA HACER ÁLGEBRA
        producto_5_within_group_2 = MathTex(
            r"d_i"  # 0
            r"=",  # 1
            r"{",  # 2
            r"\langle",  # 3
            r"\vec{v}",  # 4
            r",",  # 5
            r"\vec{g}_i",  # 6
            r"\rangle",  # 7
            r"\over",  # 8
            r"\langle",  # 9
            r"\vec{g}_i",  # 10
            r",",  # 11
            r"\vec{g}_i",  # 12
            r"\rangle",  # 13
            r"}",  # 14
            r",",  # 15
            r"\quad 1\leq i\leq k"
        )

        producto_5 = MathTex(
            r"{",  # 0
            r"\langle",  # 1
            r"\vec{v}",  # 2
            r",",  # 3
            r"\vec{g}_i",  # 4
            r"\rangle",  # 5
            r"\over",  # 6
            r"\langle",  # 7
            r"\vec{g}_i",  # 8
            r",",  # 9
            r"\vec{g}_i",  # 10
            r"\rangle",  # 11
            r"}",  # 12
            r"=",  # 13
            r"d_i"  # 14
        )
        producto_4 = MathTex(
            r"\langle",  # 0
            r"\vec{v}",  # 1
            r",",  # 2
            r"\vec{g}_i",  # 3
            r"\rangle",  # 4
            r"=",  # 5
            r"d_i",  # 6
            r"\langle",  # 7
            r"\vec{g}_i",  # 8
            r",",  # 9
            r"\vec{g}_i",  # 10
            r"\rangle",  # 11
        )
        producto_3 = MathTex(
            r"\langle",  # 0
            r"\vec{v}",  # 1
            r",",  # 2
            r"\vec{g}_i",  # 3
            r"\rangle",  # 4
            r"=",  # 5
            r"\sum_{j = 1}^{k}",  # 6
            r"d_j",  # 7
            r"\langle",  # 8
            r"\vec{g}_j",  # 9
            r",",  # 10
            r"\vec{g}_i",  # 11
            r"\rangle",  # 12
        )
        producto_2_swap = MathTex(
            r"\langle",  # 0
            r"\vec{v}",  # 1
            r",",  # 2
            r"\vec{g}_i",  # 3
            r"\rangle",  # 4
            r"=",  # 5
            r"\sum_{j = 1}^{k}",  # 6
            r"\langle",  # 7
            r"d_j",  # 8
            r"\vec{g}_j",  # 9
            r",",  # 10
            r"\vec{g}_i",  # 11
            r"\rangle",  # 12
        )
        producto_2 = MathTex(
            r"\langle",  # 0
            r"\vec{v}",  # 1
            r",",  # 2
            r"\vec{g}_i",  # 3
            r"\rangle",  # 4
            r"=",  # 5
            r"\left\langle",  # 6
            r"\sum_{j = 1}^{k}",  # 7
            r"d_j",  # 8
            r"\vec{g}_j",  # 9
            r",",  # 10
            r"\vec{g}_i",  # 11
            r"\right\rangle",  # 12
        )
        producto_1 = MathTex(
            r"\langle",  # 0
            r"\vec{v}",  # 1
            r",",  # 2
            r"\vec{g}_i",  # 3
            r"\rangle",  # 4
            r"=",  # 5
            r"\left\langle",  # 6
            r"d_1",  # 7
            r"\vec{g}_1",  # 8
            r"+...+",  # 9
            r"d_k",  # 10
            r"\vec{g}_k",  # 11
            r",",  # 12
            r"\vec{g}_i",  # 13
            r"\right\rangle",  # 14
        )
        operador_gi = MathTex(
            r"\langle",  # 0
            r"\cdot",  # 1
            r",",  # 2
            r"\vec{g}_i",  # 3
            r"\rangle",  # 4
        ).scale(0.8)
        comb_v_g = MathTex(
            r"\vec{v}",  # 0
            r"=",  # 1
            r"d_1",  # 2
            r"\vec{g}_1",  # 3
            r"+...+",  # 4
            r"d_k",  # 5
            r"\vec{g}_k"  # 6
        )
        #escalamiento del texto
        producto_5_within_group_2[:].scale(0.8)  # Para escalar al tamaño de los groups
        for text in [producto_1, producto_2, producto_2_swap, producto_3, producto_4, producto_5, comb_v_g, producto_5_within_group_2]:
            text.scale(0.8)
        #Mover hacia abajo
        for i in [producto_1, producto_2, producto_2_swap, producto_3, producto_4, producto_5, comb_v_g]:
            i.shift(DOWN)
        #Alineación con respecto a "comb_v_g"
        for i in [comb_v_g, producto_2, producto_2_swap, producto_3, producto_4, producto_5]:
            align_t12(text1=producto_1, text2=i, char="=", buff=0)
        #Alineación de ¿di? con la expresión en términos del producto escalar dentrode group_2
        align_t12(text1=group_2[-1][:],
                  text2=producto_5_within_group_2[:], char="$d_i$", buff=-0.5)

        #----------------------------------- COMPARACIÓN V vs. V CON PROD. ESCALAR
        combinacion_explicita = MathTex(
            "\\vec{v}",  # 0
            "=",  # 1
            r"{",  # 2 ----------------
            r"\langle",  # 3
            r"\vec{v}",  # 4
            r",",  # 5
            r"\vec{g}_1",  # 6
            r"\rangle",  # 7
            r"\over",  # 8
            r"\langle",  # 9
            r"\vec{g}_1",  # 10
            r",",  # 11
            r"\vec{g}_1",  # 12
            r"\rangle",  # 13
            r"}",  # 14 ----------------
            "\\vec{g}_1",  # 15
            "+",  # 16
            "\\cdots",  # 17
            "+",  # 18
            r"{",  # 19 ----------------
            r"\langle",  # 20
            r"\vec{v}",  # 21
            r",",  # 22
            r"\vec{g}_k",  # 23
            r"\rangle",  # 24
            r"\over",  # 25
            r"\langle",  # 26
            r"\vec{g}_k",  # 27
            r",",  # 28
            r"\vec{g}_k",  # 29
            r"\rangle",  # 30
            r"}",  # 31 ----------------
            r"\vec{g}_k"  # 32
        ).scale(0.8).scale(0.8)
        combinacion_explicita_sum = MathTex(
            r"\vec{v}",  # 0
            r"=",  # 1
            r"\sum_{i = 1}^{k}",  # 2
            r"{",  # 3 ----------------
            r"\langle",  # 4
            r"\vec{v}",  # 5
            r",",  # 6
            r"\vec{g}_i",  # 7
            r"\rangle",  # 8
            r"\over",  # 9
            r"\langle",  # 10
            r"\vec{g}_i",  # 11
            r",",  # 12
            r"\vec{g}_i",  # 13
            r"\rangle",  # 14
            r"}",  # 15 ----------------
            r"\vec{g}_i",  # 16
        ).scale(0.8).scale(0.8)
        for text_com in [combinacion_explicita, combinacion_explicita_sum]:
            align_t12(text1=group_2[-2], text2=text_com, char="=", buff=0)

        ver_ejercicio = Tex("*", "Ver el ", "Ejercicio 1.7", ".").scale(0.8).scale(0.8).to_corner(LEFT+DOWN).shift(0.5*RIGHT)
        ver_ejercicio[0].set_color(AMARILLO)
        ver_ejercicio[2].set_color(AZUL)

        #----------------------------------- ANIMACIONES
        #--------------------------------
        self.camera.frame.shift(0.5*RIGHT)
        self.play(
            FadeIn(groups[0][:]),
            run_time=2)

        self.wait(4)
        self.play(Write(groups[1][0][:]))
        self.play(Write(groups[1][1][:]))
        self.wait(5)
        self.play(Write(groups[1][2][:]))
        self.wait(1)
        self.play(Write(groups[1][3][:]))
        self.wait(2)
        #-----------------------------------
        self.play(
            groups[0][:].animate.set_color(GRIS),
            groups[1][:].animate.set_color(GRIS),
        )
        #Desplazamiento de la combinación lineal para llevar a cabo el proceso algebraico.
        self.play(ReplacementTransform(groups[1][2][:].copy(), comb_v_g[:]))
        self.wait(2)
        #Primera tranformación
        self.play(
            FadeIn(operador_gi[3]),
            run_time=1
        )
        self.wait(2)
        self.play(
            ReplacementTransform(comb_v_g[0], producto_1[1]),
            ReplacementTransform(comb_v_g[2:], producto_1[7:12]),
            FadeIn(operador_gi[:3]),
            FadeIn(operador_gi[4]),
            run_time=1.5
        )
        self.play(FadeOut(operador_gi[1]))
        self.play(
            ReplacementTransform(comb_v_g[1], producto_1[5]),
            #LHS de la ecuación
            ReplacementTransform(operador_gi[0], producto_1[:1]),
            ReplacementTransform(operador_gi[2:], producto_1[2:5]),
            #RHS de la ecuación
            ReplacementTransform(operador_gi[0].copy(), producto_1[6]),
            ReplacementTransform(operador_gi[2:].copy(), producto_1[12:]),
            run_time=1.5
        )
        #Segunda transformación
        self.wait(1.25)
        self.play(
            FadeOut(producto_1[9:12]),
            run_time=0.5
        )
        self.play(
            ReplacementTransform(producto_1[:6], producto_2[:6]),
            ReplacementTransform(producto_1[6], producto_2[6]),
            ReplacementTransform(producto_1[7:9], producto_2[8:10]),
            ReplacementTransform(producto_1[12:], producto_2[10:]),
            run_time=1
        )
        self.play(
            FadeIn(producto_2[7]),
            run_time=1
        )
        self.wait()
        #Tercera transformación, apertura de las sumas
        self.play(
            ReplacementTransform(producto_2[:6], producto_2_swap[:6]),
            ReplacementTransform(producto_2[8:], producto_2_swap[8:]),
            CounterclockwiseTransform(producto_2[7], producto_2_swap[6]),
            CounterclockwiseTransform(producto_2[6], producto_2_swap[7]),
            run_time=1.5
        )
        #Cuarta transformación, "sacando" los escalares
        self.play(
            ReplacementTransform(producto_2_swap[:7], producto_3[:7]),
            ReplacementTransform(producto_2_swap[9:], producto_3[9:]),
            CounterclockwiseTransform(producto_2_swap[8], producto_3[7]),
            CounterclockwiseTransform(producto_2_swap[7], producto_3[8]),
            run_time=1.5
        )
        self.wait(2.5)
        #Cuarta transformación (esta sí está chida)
        self.play(
            gj_gi.animate.set_color(WHITE), run_time=1.5
        )
        self.wait()
        self.play(
            FadeOut(producto_3[6]),
            ReplacementTransform(producto_3[:6], producto_4[:6]),
            ReplacementTransform(producto_3[7:], producto_4[6:]),
            run_time=1
        )
        self.wait(2)
        #Sexta transformación (división)
        #Transform(producto_4[7:], producto_5[2]),
        #Transform(producto_4[:5], producto_5[0]),
        self.play(
            ReplacementTransform(producto_4[:5], producto_5[1:6]),
            ReplacementTransform(producto_4[5], producto_5[13]),
            ReplacementTransform(producto_4[6], producto_5[14]),
            ClockwiseTransform(producto_4[7:], producto_5[7:12]),
            FadeIn(producto_5[6]),
            run_time=1
        )
        self.play(
            gj_gi.animate.set_color(GRIS),
            run_time=1
        )
        self.wait()
        self.play(
            Circumscribe(producto_5, fade_out=True),
            run_time=3
        )
        #Incorporación del resultado al texto principal
        self.play(
            groups[0][:].animate.set_color(WHITE),
            groups[1][:].animate.set_color(WHITE),
        )
        self.wait()
        self.play(
            FadeOut(group_2[-1][0]),
            ReplacementTransform(group_2[-1][1][:], producto_5_within_group_2[0]),
            ReplacementTransform(group_2[-1][2][:], producto_5_within_group_2[1:15]),
            run_time=1.5
        )
        self.wait(3.5)
        self.play(
            FadeOut(producto_5[:]),
        )
        self.play(
            Write(producto_5_within_group_2[15:]),
            run_time=2
        )
        #Expresiones explícitas y comparación entre espacios vectoriales y espacios vectoriales con
        #producto escalar
        self.play(
            FadeOut(group_1[:2]),
            FadeOut(group_2[:2]),
            group_1[-1][:].animate.align_to(group_2[-1][:], DOWN),
            run_time=1
        )
        #Integración del resultado para los coeficientes d_i en group_2
        self.play(
            ReplacementTransform(group_2[-2][:2], combinacion_explicita[:2]),
            ReplacementTransform(group_2[-2][2], combinacion_explicita[2:15]),
            ReplacementTransform(group_2[-2][3], combinacion_explicita[15]),
            # Símbolos de suma
            ReplacementTransform(group_2[-2][4][0], combinacion_explicita[16:19][0]),
            ReplacementTransform(group_2[-2][4][1:4], combinacion_explicita[16:19][1]),
            ReplacementTransform(group_2[-2][4][4], combinacion_explicita[16:19][2]),


            ReplacementTransform(group_2[-2][5], combinacion_explicita[19:32]),
            ReplacementTransform(group_2[-2][6], combinacion_explicita[32]),
            run_time=3
        )
        self.wait(8.5)
        self.play(
            FadeOut(combinacion_explicita[16:]),
            ReplacementTransform(
                combinacion_explicita[:2], combinacion_explicita_sum[:2]),
            ReplacementTransform(
                combinacion_explicita[2:15], combinacion_explicita_sum[3:16]),
            ReplacementTransform(
                combinacion_explicita[15], combinacion_explicita_sum[16]),
            FadeIn(combinacion_explicita_sum[2]),
            run_time=1.5
        )
        self.play(
            Circumscribe(combinacion_explicita_sum[:], fade_out=False),
            run_time=3
        )
        self.wait(1.5)
        self.play(
            Write(ver_ejercicio)
        )
        self.wait(1.5)
        self.play(FadeOut(ver_ejercicio), run_time=0.5)
        self.wait(29)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class SE2(Scene):
    def construct(self):
        #-------------------------------------------- Variables que definen al sistema coordenado
        escala_plano = 0.4
        origen_plano = np.array([-3, 1, 0])

        #-------------------------------------------- Texto
        vec_v_u = MathTex(
            "\\vec{u}, \\vec{v}\\in V, \\quad \\text{dim}(V)<\\infty"
        ).scale(0.8).shift(2.5*UP+4*RIGHT)
        vec_v_u[0][0:2].set_color(AZUL)
        vec_v_u[0][3:5].set_color(VERDE)
        sea_Gamma_base = Tex("$\\Gamma$ es base ortogonal de $V$").scale(0.8)
        v_in_Gamma = MathTex(r"\vec{v}\in\Gamma").scale(0.8)
        v_in_Gamma[0][:2].set_color(VERDE)
        group1 = VGroup(sea_Gamma_base, v_in_Gamma)
        group1.arrange_in_grid(rows=2, columns=1, buff=0.2).next_to(vec_v_u, DOWN)
        group1.align_to(vec_v_u, LEFT)

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
                                 ).set_color(AMARILLO).scale(0.8).move_to(origen_plano).shift(0.7*LEFT+0.5*UP).set_z_index(3)
        conclusion = MathTex(
            r"{\langle \vec{v},\vec{u}\rangle\over \langle \vec{u},\vec{u}\rangle}\vec{u} = \vec{0}",
            r"\Longleftrightarrow",
            r"\langle\vec{v},\vec{u}\rangle = 0",
            r"\Longleftrightarrow",
            r"\langle\vec{u},\vec{v}\rangle = 0",
            r"\Longleftrightarrow",
            r"{\langle \vec{u},\vec{v}\rangle\over \langle \vec{v},\vec{v}\rangle}\vec{v} = \vec{0}",
        ).scale(0.9).shift(2.5*DOWN)

        #-------------------------------------------- Vectores u y v
        v = 0.4*np.array([3, -1, 0])
        u = 0.4*np.array([2, 1.5, 0])
        #--------------------------------------------

        v_vect = Vector(v, buff=0, color=VERDE).shift(origen_plano).set_z_index(3)
        u_vect = Vector(u, buff=0, color=AZUL).shift(origen_plano).set_z_index(3)

        distancia_v_label = 0.4*v/(np.linalg.norm(v))
        distancia_u_label = 0.4*u/(np.linalg.norm(u))

        v_label = MathTex(r"\vec{v}").scale(0.8).move_to(
            v_vect.get_end()+distancia_v_label).set_z_index(3)
        v_label[0].set_color(VERDE)
        u_label = MathTex(r"\vec{u}").scale(0.8).move_to(
            u_vect.get_end()+distancia_u_label).set_z_index(3)
        u_label[0].set_color(AZUL)

        aux_vect = origen_plano+(np.dot(v, u)/np.dot(v, v))*v
        proy_u_v_arrow = Arrow(start=origen_plano, end=aux_vect, stroke_width=8, buff=0, color=AMARILLO).set_z_index(4)
        proy_u_v_arrow_2 = proy_u_v_arrow.copy()
        dashedline = DashedLine(
            u_vect.get_end(), proy_u_v_arrow.get_end(), color=AMARILLO
        ).set_z_index(5)

        subesp_v = Line([-0.58*7-2.9, 0.58*7/3+1, 0], [0.58*7-3.05, -0.58*7/3+1, 0], color=GRIS).set_z_index(2)

        grid = NumberPlane(x_range=[-10, 10, 1], y_range=[-6, 6, 1],
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
                obj.become(Dot(origen_plano, radius=0.05, color=AMARILLO))

        def upd_for_label(obj):
            v_ = v-t.get_value()*u/np.linalg.norm(u)**2
            distancia = 0.4*v_/(np.linalg.norm(v_))
            obj.move_to(v_vect.get_end()+distancia)

        def upd_for_dashedline(obj):
            new_dashedline = DashedLine(
                u_vect.get_end(), proy_u_v_arrow.get_end(), color=AMARILLO
            ).set_z_index(5)
            obj.become(new_dashedline)

        #-------------------------------------------- Animaciones
        self.next_section()
        self.wait(10)
        self.play(
            Write(grid),
            run_time=2.5
        )
        self.wait(4)
        self.play(
            Write(u_vect),
            Write(u_label),
            run_time=0.5
        )
        self.play(
            Write(v_vect),
            Write(v_label),
            run_time=0.5
        )

        self.play(
            Write(vec_v_u),
        )
        self.wait(7)
        self.play(
            Write(group1[0]),
            run_time=3
        )
        justificación = Tex("*", r"\mbox{La justificación se explica en el video ", "\emph{Ortogonalización y ortonormalización (Teorema de Gram-Schmidt) }", "de Animathica.}").scale(0.8).scale(0.6).to_corner(LEFT+DOWN)
        justificación[0].set_color(AMARILLO)
        justificación[2].set_color(AMARILLO)
        self.play(Write(group1[1]))
        self.play(Write(justificación), run_time=2)
        self.wait(2)
        self.play(FadeOut(justificación))
        self.wait(4)
        self.play(Write(proy_u_v_arrow))
        self.wait(5)
        self.play(FadeIn(label_proy_u_v[:]))
        self.wait(2)
        self.play(
            FadeOut(group1),
            FadeOut(vec_v_u)
        )
        self.play(
            label_proy_u_v[6:12].animate.set_opacity(0.3),
            label_proy_u_v[13].animate.set_opacity(0.3),
            proy_u_v_arrow.animate.set_opacity(0.3),
            run_time=2
        )
        self.wait(3)
        self.play(
            label_proy_u_v[6:12].animate.set_opacity(1),
            proy_u_v_arrow.animate.set_opacity(0.2),
            run_time=2
        )
        self.play(label_proy_u_v[13].animate.set_opacity(1))
        self.wait()
        self.play(GrowArrow(proy_u_v_arrow_2), run_time=2)
        self.wait(0.5)
        self.play(Write(subesp_v))
        self.wait(5)
        self.play(FadeOut(label_proy_u_v, proy_u_v_arrow_2, subesp_v))

        # Proyección vectorial con fuente de luz
        #self.next_section(skip_animations=True)
        coords_fuente = [0.58-3, 0.58*2.2+1.05, 0]
        fuente = Dot(coords_fuente, color=YELLOW)
        self.wait(5)
        self.play(GrowFromCenter(fuente))
        self.play(Flash(point=coords_fuente, line_length=0.075, num_lines=12, flash_radius=0.15),
                  Flash(point=coords_fuente, line_length=0.075, num_lines=12, flash_radius=0.3),
                  Flash(point=coords_fuente, line_length=0.075, num_lines=12, flash_radius=0.45),
                  Flash(point=coords_fuente, line_length=0.075, num_lines=12, flash_radius=0.6)
                  )
        self.play(Flash(point=coords_fuente, line_length=0.075, num_lines=12, flash_radius=0.15),
                  Flash(point=coords_fuente, line_length=0.075, num_lines=12, flash_radius=0.3),
                  Flash(point=coords_fuente, line_length=0.075, num_lines=12, flash_radius=0.45),
                  Flash(point=coords_fuente, line_length=0.075, num_lines=12, flash_radius=0.6)
                  )
        self.play(Write(subesp_v))
        self.wait(5)

        norma_u = np.linalg.norm(u,2)
        tupla_u = (ORIGIN, u)

        normal_v = 0.4*np.array([0.01, 0.03, 0])
        tupla_v = (ORIGIN, v)
        tupla_normal = (normal_v, 2*normal_v)

        # ValueTracker para el desplazamiento de la fuente
        VT = ValueTracker(1)

        # ValueTracker para el desplazamiento de la fuente
        VT_2 = ValueTracker(0.1)

        # Función para el desplazamiento de la fuente
        def upd_for_fuente(obj):
            obj.become(Dot(coords_fuente + VT.get_value()*normal_v, color=YELLOW))

        fuente.add_updater(upd_for_fuente)

        self.play(VT.animate.set_value(1000), rate_func=smooth)

        esquina0 = [-0.58*7-2.9, 0.58*7/3+1, 0]
        esquina1 = [0.58*7-3.05, -0.58*7/3+1, 0]
        esquina2 = [7*0.58-3.05, 0.58*4+1.1, 0]
        esquina3 = [-7*0.58-2.9, 0.58*4+1.1, 0]
        tupla_lado0 = (esquina0, esquina1)
        tupla_lado1 = (esquina1, esquina2)
        tupla_lado2 = (esquina2, esquina3)
        tupla_lado3 = (esquina3, esquina0)

        n = 44

        ends = []
        for i in range(0,n+1):
            ends.append(np.array(esquina0) + i/n*(np.array(esquina1)-np.array(esquina0)))

        rayos = VGroup()
        for i in range(0, len(ends)):

            end_i = ends[i]

            if (21 < i) & (i < 25):
                rayos.add(DashedLine(line_intersection([end_i, end_i+normal_v], [esquina3, esquina2]),
                          line_intersection([end_i, end_i+normal_v], [esquina3, esquina2]) + (line_intersection([end_i, end_i+normal_v], [origen_plano, origen_plano+u])-line_intersection([end_i, end_i+normal_v], [esquina3, esquina2])),
                          dash_length=0.1,
                          color=AMARILLO))

            elif i > 37:
                rayos.add(DashedLine(line_intersection([end_i, end_i+normal_v], [esquina1, esquina2]),
                          line_intersection([end_i, end_i+normal_v], [esquina1, esquina2]) + (line_intersection([end_i, end_i+normal_v], [origen_plano, origen_plano+v])-line_intersection([end_i, end_i+normal_v], [esquina1, esquina2])),
                          dash_length=0.1,
                          color=AMARILLO))

            else:
                rayos.add(DashedLine(line_intersection([end_i, end_i+normal_v], [esquina3, esquina2]),
                          line_intersection([end_i, end_i+normal_v], [esquina3, esquina2]) + (line_intersection([end_i, end_i+normal_v], [origen_plano, origen_plano+v])-line_intersection([end_i, end_i+normal_v], [esquina3, esquina2])),
                          dash_length=0.1,
                          color=AMARILLO))

        self.wait(3)
        self.play(FadeIn(rayos), FadeOut(u_label, v_label))
        self.wait(5.5)
        self.play(GrowArrow(proy_u_v_arrow_2))
        self.wait(9)
        self.play(FadeOut(rayos, proy_u_v_arrow_2, subesp_v), FadeIn(u_label, v_label))
        self.wait(3.5)

        # Interpretación de ortogonalidad
        #self.next_section(skip_animations=True)
        label_proy_u_v[:].set_opacity(1),
        dashedline.set_opacity(1),
        proy_u_v_arrow.set_opacity(1),
        self.play(FadeIn(label_proy_u_v, dashedline, proy_u_v_arrow))
        self.wait(2)

        v_label.add_updater(upd_for_label)
        proy_u_v_arrow.add_updater(upd_for_proy_u_v_arrow)
        v_vect.add_updater(upd_for_v)
        dashedline.add_updater(upd_for_dashedline)
        self.wait(5)
        self.play(Write(conclusion[4]), run_time=1.5)
        self.play(Write(conclusion[5]), run_time=1.25)
        self.play(t.animate.set_value(np.dot(u, v)), Write(conclusion[6]), run_time=3.5)
        self.wait(5)
        s = conclusion[:4].copy()
        s.invert(recursive=True)
        self.play(Write(conclusion[3]))
        self.play(Write(conclusion[2]))
        self.wait(0.25)
        self.play(Write(conclusion[1]))
        dashedline2 = DashedLine(
            v_vect.get_end(), origen_plano, color=AMARILLO
        ).set_z_index(5)
        self.play(Write(conclusion[0]), FadeOut(dashedline), FadeIn(dashedline2), run_time=3)
        self.wait(12.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], FadeOut(proy_u_v_arrow, v_vect))
