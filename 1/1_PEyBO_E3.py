from manim import *
#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################


#####################################################################################
###############################  Tercera escena  ####################################
###############################  versión: Manim Community v0.8.0   ##################
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


'''
En esta escena, escencialmente se hace una comparación entre EV y EV con producto escalar,
y se lleva a cabo el proceso algebraico para obtener los coeficientes de una combinación
lineal en términos de una base ortogonal.
'''

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

class Subescena_1(Scene):
    def parte_1(self):
        #----------------------------------- ESPACIO V EN GENERAL
        dim_V = MathTex("\\text{dim}\\left(V\\right)=k<\\infty").scale(0.8).to_edge(UP)
        base_beta = Tex(
            "$\\beta = \\{\\vec{b}_1,..., \\vec{b}_k\\}$", #0
            " base de ", #1
            "$V$" #2
        ).move_to(UP)
        base_propiedades = Tex(
            "$\\langle \\beta\\rangle = V$",
            "$,\\,\\beta$ es l.i."
        )
        combination = MathTex(
                            "\\vec{v}", #0
                            "=", #1
                            "c_1", #2
                            "\\vec{b}_1", #3
                            "+", #4
                            "\\cdots", #5
                            "+", #6
                            "c_k", #7
                            "\\vec{b}_k" #8
                        )
        coeficientes_c = Tex("¿",
                            "$c_i$",
                            "?")
        group_1 = VGroup(base_beta, base_propiedades, combination, coeficientes_c).scale(0.8)
        group_1.arrange(1.8*DOWN, center=False, aligned_edge=LEFT)
        combination_copy = group_1[2].copy()
        #----------------------------------- ESPACIO V CON PRODUCTO INTERNO, BASE ORTOGONAL
        base_gamma = Tex(
            "$\\Gamma = \\{\\vec{g}_1,..., \\vec{g}_k\\}$", #0
            " base ortogonal de", #1
            " $V$" #2
        ).move_to(UP)
        
        gen_gamma = MathTex(r"\langle\Gamma\rangle = V, ")
        case_1 = Tex("$\\langle \\vec{g}_i, \\vec{g}_i\\rangle$", " si"," $j = i$")
        case_2 = Tex("$0$", " si", " $j \\neq i$")
        for i, item in enumerate(case_2):
            item.align_to(case_1[i],LEFT)
        case_1_g = VGroup(*case_1)
        case_2_g = VGroup(*case_2)
        case_2_g.next_to(case_1_g, DOWN)
        cases_group = VGroup(case_1_g, case_2_g)
        braces=Brace(cases_group,LEFT)
        producto_ij = braces.get_text("$\\langle \\vec{g}_i, \\vec{g}_j\\rangle$ =")
        gj_gi = VGroup(producto_ij, braces, cases_group)
        
        base_gamma_propiedades = VGroup(gen_gamma, gj_gi).arrange(direction=RIGHT, buff=0.20, center=False)

        combination_dg = MathTex(
            r"\vec{v}", #0
            r"=", #1
            r"d_1", #2
            r"\vec{g}_1", #3
            r"+...+", #4
            r"d_k", #5
            r"\vec{g}_k" #6
        )
        coeficientes_d = Tex("¿", r"$d_i$", "?")
        group_2 = VGroup(base_gamma, base_gamma_propiedades, combination_dg, coeficientes_d).scale(0.8)
        group_2.arrange(1*DOWN, center=False, aligned_edge=LEFT)

        groups = VGroup(group_1, group_2).scale(0.8).shift(2*UP)
        groups.arrange_in_grid(rows=1, cols = 2, buff=1, row_heights=None)
        groups[1].align_to(groups[0], UP)

        #----------------------------------- COEFICIENTES d_i 
        def align_t12(text1: Mobject, text2: Mobject, char: str, buff: float)->None:
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
            
        producto_5_within_group_2 = MathTex(
            r"d_i" #0
            r"=", #1
            r"{", #2
            r"\langle", #3
            r"\vec{v}", #4
            r",", #5
            r"\vec{g}_i", #6
            r"\rangle", #7
            r"\over", #8
            r"\langle", #9
            r"\vec{g}_i", #10
            r",", #11
            r"\vec{g}_i", #12
            r"\rangle", #13
            r"}", #14
            r",", #15
            r"\quad 1\leq i\leq k"
        )

        producto_5 = MathTex(
            r"{", #0
            r"\langle", #1
            r"\vec{v}", #2
            r",", #3
            r"\vec{g}_i", #4
            r"\rangle", #5
            r"\over", #6
            r"\langle", #7
            r"\vec{g}_i", #8
            r",", #9
            r"\vec{g}_i", #10
            r"\rangle", #11
            r"}", #12
            r"=", #13
            r"d_i" #14
        )
        producto_4 = MathTex(
            r"\langle", #0
            r"\vec{v}", #1
            r",", #2
            r"\vec{g}_i", #3
            r"\rangle", #4
            r"=", #5
            r"d_i",#6
            r"\langle", #7
            r"\vec{g}_i",#8
            r",",#9
            r"\vec{g}_i", #10
            r"\rangle", #11
        )
        producto_3 = MathTex(
            r"\langle", #0
            r"\vec{v}", #1
            r",", #2
            r"\vec{g}_i", #3
            r"\rangle", #4
            r"=", #5
            r"\sum_{j = 1}^{k}", #6
            r"d_j",#7
            r"\langle", #8
            r"\vec{g}_j",#9
            r",", #10
            r"\vec{g}_i", #11
            r"\rangle", #12
        )
        producto_2_swap = MathTex(
            r"\langle", #0
            r"\vec{v}", #1
            r",", #2
            r"\vec{g}_i", #3
            r"\rangle", #4
            r"=", #5
            r"\sum_{j = 1}^{k}", #6
            r"\langle", #7
            r"d_j", #8
            r"\vec{g}_j", #9
            r",", #10
            r"\vec{g}_i", #11
            r"\rangle", #12
        )
        producto_2 = MathTex(
            r"\langle", #0
            r"\vec{v}", #1
            r",", #2
            r"\vec{g}_i", #3
            r"\rangle", #4
            r"=", #5
            r"\left\langle", #6
            r"\sum_{j = 1}^{k}", #7
            r"d_j", #8
            r"\vec{g}_j", #9
            r",", #10
            r"\vec{g}_i", #11
            r"\right\rangle", #12
        )
        producto_1 = MathTex(
            r"\langle", #0
            r"\vec{v}", #1
            r",", #2
            r"\vec{g}_i", #3
            r"\rangle", #4
            r"=", #5
            r"\left\langle", #6
            r"d_1", #7
            r"\vec{g}_1", #8
            r"+...+", #9
            r"d_k", #10
            r"\vec{g}_k", #11
            r",", #12
            r"\vec{g}_i", #13
            r"\right\rangle", #14
        )
        operador_gi = MathTex(
            r"\langle", #0
            r"\cdot",#1
            r",", #2
            r"\vec{g}_i", #3
            r"\rangle", #4
        ).scale(0.8)
        comb_v_g = MathTex(
            r"\vec{v}", #0
            r"=", #1
            r"d_1", #2
            r"\vec{g}_1", #3
            r"+...+", #4
            r"d_k", #5
            r"\vec{g}_k" #6
        )
        #escalamiento del texto
        producto_5_within_group_2[:].scale(0.8) #Para escalar al tamaño de los groups
        for text in [producto_1, producto_2, producto_2_swap, producto_3, producto_4, producto_5, comb_v_g, producto_5_within_group_2]:
            text.scale(0.8)
        #Mover hacia abajo 
        for i in [producto_1, producto_2, producto_2_swap, producto_3, producto_4, producto_5, comb_v_g]:
            i.shift(DOWN)
        #Alineación con respecto a "comb_v_g"
        for i in [comb_v_g, producto_2, producto_2_swap, producto_3, producto_4, producto_5]:
            align_t12(text1 = producto_1, text2 = i, char = "=", buff = 0)
        #Alineación de ¿di? con la expresión en términos del producto escalar dentrode group_2
        align_t12(text1 = group_2[-1][:], text2 = producto_5_within_group_2[:], char = "$d_i$", buff = -0.5)

        #----------------------------------- COMPARACIÓN V vs. V CON PROD. ESCALAR  
        combinacion_explicita = MathTex(
                            "\\vec{v}", #0
                            "=", #1
                            r"{", #2 ----------------
                            r"\langle", #3
                            r"\vec{v}", #4
                            r",", #5
                            r"\vec{g}_1", #6
                            r"\rangle", #7
                            r"\over", #8
                            r"\langle", #9
                            r"\vec{g}_1", #10
                            r",", #11
                            r"\vec{g}_1", #12
                            r"\rangle", #13
                            r"}", #14 ----------------
                            "\\vec{g}_1", #15
                            "+", #16
                            "\\cdots", #17
                            "+", #18
                            r"{", #19 ----------------
                            r"\langle", #20
                            r"\vec{v}", #21
                            r",", #22
                            r"\vec{g}_k", #23
                            r"\rangle", #24
                            r"\over", #25
                            r"\langle", #26
                            r"\vec{g}_k", #27
                            r",", #28
                            r"\vec{g}_k", #29
                            r"\rangle", #30
                            r"}", #31 ----------------
                            r"\vec{g}_k" #32
                        ).scale(0.8).scale(0.8)
        combinacion_explicita_sum = MathTex(
                            r"\vec{v}", #0
                            r"=", #1
                            r"\sum_{i = 1}^{k}", #2
                            r"{", #3 ----------------
                            r"\langle", #4
                            r"\vec{v}", #5
                            r",", #6
                            r"\vec{g}_i", #7
                            r"\rangle", #8
                            r"\over", #9
                            r"\langle", #10
                            r"\vec{g}_i", #11
                            r",", #12
                            r"\vec{g}_i", #13
                            r"\rangle", #14
                            r"}", #15 ----------------
                            r"\vec{g}_i", #16
                        ).scale(0.8).scale(0.8)
        for text_com in [combinacion_explicita, combinacion_explicita_sum]:
            align_t12(text1 = group_2[-2], text2 = text_com, char = "=", buff = 0)
        #----------------------------------- ANIMACIONES
        #--------------------------------
        self.play(
                FadeIn(groups[0][:]),
        run_time = 2)

        self.wait(2)
        self.play(Write(groups[1][0][:]))
        self.wait(2)
        self.play(Write(groups[1][1][:]))
        self.wait(1)
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
            ReplacementTransform(comb_v_g[0], producto_1[1]),
            ReplacementTransform(comb_v_g[2:], producto_1[7:12]),
            FadeIn(operador_gi[:]),
            run_time = 1
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
            run_time = 3
        )
        self.wait(2)
        #Segunda transformación
        self.play(
            FadeOut(producto_1[9:12]),
            run_time = 2
        )
        self.play(
            ReplacementTransform(producto_1[:6], producto_2[:6]),
            ReplacementTransform(producto_1[6], producto_2[6]),
            ReplacementTransform(producto_1[7:9], producto_2[8:10]),
            ReplacementTransform(producto_1[12:], producto_2[10:]),
            run_time = 2
        )
        self.play(
            FadeIn(producto_2[7]),
            run_time = 2
        )
        #Tercera transformación, apertura de las sumas
        self.play(
            ReplacementTransform(producto_2[:6], producto_2_swap[:6]),
            ReplacementTransform(producto_2[8:], producto_2_swap[8:]),
            CounterclockwiseTransform(producto_2[7], producto_2_swap[6]), 
            CounterclockwiseTransform(producto_2[6], producto_2_swap[7]),
            run_time = 3
        )
        self.wait(2)
        #Cuarta transformación, "sacando" los escalares
        self.play(
            ReplacementTransform(producto_2_swap[:7], producto_3[:7]),
            ReplacementTransform(producto_2_swap[9:], producto_3[9:]),
            CounterclockwiseTransform(producto_2_swap[8], producto_3[7]), 
            CounterclockwiseTransform(producto_2_swap[7], producto_3[8]),
            run_time = 3
        )
        self.wait(2)
        #Cuarta transformación (esta sí está chida)
        self.play(
            group_2[1].animate.set_color(WHITE),
            run_time = 2
        )
        self.play(
            FadeOut(producto_3[6])
        )
        self.play(
            ReplacementTransform(producto_3[:6], producto_4[:6]),
            ReplacementTransform(producto_3[7:], producto_4[6:]),
            run_time = 3
        )
        self.play(
            group_2[1].animate.set_color(GRIS),
            run_time = 2
        )
        #Sexta transformación (división)
        #Transform(producto_4[7:], producto_5[2]),
        #Transform(producto_4[:5], producto_5[0]),
        self.play(
            ReplacementTransform(producto_4[:5], producto_5[1:6]),
            ReplacementTransform(producto_4[5], producto_5[13]),
            ReplacementTransform(producto_4[6], producto_5[14]),
            ClockwiseTransform(producto_4[7:], producto_5[7:12]),
            FadeIn(producto_5[6]),
            run_time = 3
        )
        self.play(
            Circumscribe(producto_5, fade_out=True),
            run_time = 3
        )
        #Incorporación del resultado al texto principal
        self.play(
            groups[0][:].animate.set_color(WHITE),
            groups[1][:].animate.set_color(WHITE),
        )
        self.wait(2)
        self.play(
            FadeOut(group_2[-1][0]),
            ReplacementTransform(group_2[-1][1][:], producto_5_within_group_2[0]),
            ReplacementTransform(group_2[-1][2][:], producto_5_within_group_2[1:15]),
            run_time = 3
        )
        self.play(
            FadeOut(producto_5[:]),
        )
        self.play(
            Write(producto_5_within_group_2[15:]),
            run_time = 2
        )
        #Expresiones explícitas y comparación entre espacios vectoriales y espacios vectoriales con
        #producto escalar
        self.play(
            FadeOut(group_1[:2]),
            FadeOut(group_2[:2]),
            run_time = 2
        )
        self.play(
            group_1[-1][:].animate.align_to(group_2[-1][:], DOWN),
            run_time = 2
        )
        #Integración del resultado para los coeficientes d_i en group_2
        self.play(
            ReplacementTransform(group_2[-2][:2], combinacion_explicita[:2]),
            ReplacementTransform(group_2[-2][2], combinacion_explicita[2:15]), 
            ReplacementTransform(group_2[-2][3], combinacion_explicita[15]),
            ReplacementTransform(group_2[-2][4], combinacion_explicita[16:19]),
            ReplacementTransform(group_2[-2][5], combinacion_explicita[19:32]),
            ReplacementTransform(group_2[-2][6], combinacion_explicita[32]),
            run_time = 3
        )
        self.play(
            FadeOut(combinacion_explicita[16:]),
            run_time = 3
        )
        self.play(
            ReplacementTransform(combinacion_explicita[:2], combinacion_explicita_sum[:2]),
            ReplacementTransform(combinacion_explicita[2:15], combinacion_explicita_sum[3:16]),
            ReplacementTransform(combinacion_explicita[15], combinacion_explicita_sum[16]),
            run_time = 3
        )
        self.play(
            FadeIn(combinacion_explicita_sum[2]),
            run_time = 3
        )
        self.play(
            Circumscribe(combinacion_explicita_sum[:], fade_out=False),
            run_time = 3
        )
    def construct(self):
        self.parte_1()