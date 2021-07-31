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
        combination_0 = MathTex("\\vec{v}") #0
        combination_1 = MathTex("=") #1
        combination_2 = MathTex("c_1") #2
        combination_3 = MathTex("\\vec{b}_1") #3
        combination_4 = MathTex("+") #4
        combination_5 = MathTex("\\cdots") #5
        combination_6 = MathTex("+") #6
        combination_7 = MathTex("c_k") #7
        combination_8 = MathTex("\\vec{b}_k") #8

        combination = VGroup(combination_0, combination_1, combination_2, combination_3, combination_4,\
                        combination_5, combination_6, combination_7, combination_8).arrange(direction=RIGHT, buff=0.15, center=False)
        coeficientes_c = Tex("¿",
                            "$c_i$",
                            "?")
        group_1 = VGroup(base_beta, base_propiedades, combination, coeficientes_c).scale(0.8)
        group_1.arrange(1*DOWN, center=False, aligned_edge=LEFT)
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
        coeficientes_d = Tex(r"¿$d_i$?")
        group_2 = VGroup(base_gamma, base_gamma_propiedades, combination_dg, coeficientes_d).scale(0.8)
        group_2.arrange(1*DOWN, center=False, aligned_edge=LEFT)

        groups = VGroup(group_1, group_2).scale(0.8).shift(2*UP)
        groups.arrange_in_grid(rows=1, cols = 2, buff=1, row_heights=None)
        groups[1].align_to(groups[0], UP)

        descomp_v_ortg = MathTex(r"\vec{v} = \sum_{i=1}^{k}\dfrac{\langle\vec{v}, \vec{g}_i\rangle}{\langle\vec{g}_i, \vec{g}_i\rangle}\vec{g}_i").scale(0.8).move_to(DOWN+4.5*LEFT)
        #----------------------------------- COEFICIENTES d_i 
        producto_5_cop = MathTex(
            r"d_i", #4
            r"=", #3
            "{",
            r"\langle\vec{v}, \vec{g}_i\rangle", #0
            r"\over", #1
            r"\langle\vec{g}_i, \vec{g}_i\rangle", #
            "}"#2
        ).scale(0.8).scale(0.7)

        producto_5 = MathTex(
            "{"
            r"\langle\vec{v}, \vec{g}_i\rangle", #0
            r"\over", #1
            r"\langle\vec{g}_i, \vec{g}_i\rangle", #2
            "}"#
            r"=", #3
            r"d_i" #4
        ).scale(0.8)
        for_all_i = MathTex(
            "1 \\leq i \\leq k"
        ).scale(0.6).next_to(producto_5, 1.5*RIGHT)
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
        ).scale(0.8)
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
        ).scale(0.8)
        producto_2_swap = MathTex(
            r"\langle", #0
            r"\vec{v}", #1
            r",", #2
            r"\vec{g}_i", #3
            r"\rangle", #4
            r"=", #5
            r"d_1",#6
            r"\langle",#7
            r"\vec{g}_1", #8
            r",", #9
            r"\vec{g}_i", #10
            r"\rangle", #11
            r"+...+",#12
            r"d_k", #13
            r"\langle",#14
            r"\vec{g}_k",#15
            r",", #16
            r"\vec{g}_i", #17
            r"\rangle", #18
        ).scale(0.8)
        producto_2 = MathTex(
            r"\langle", #0
            r"\vec{v}", #1
            r",", #2
            r"\vec{g}_i", #3
            r"\rangle", #4
            r"=", #5
            r"\langle", #6
            r"d_1", #7
            r"\vec{g}_1", #8
            r",", #9
            r"\vec{g}_i", #10
            r"\rangle", #11
            r"+...+",#12
            r"\langle", #13
            r"d_k",#14
            r"\vec{g}_k",#15
            r",", #16
            r"\vec{g}_i", #17
            r"\rangle", #18
        ).scale(0.8)
        producto_1 = MathTex(
            r"\langle", #0
            r"\vec{v}", #1
            r",", #2
            r"\vec{g}_i", #3
            r"\rangle", #4
            r"=", #5
            r"\langle", #6
            r"d_1", #7
            r"\vec{g}_1", #8
            r"+...+", #9
            r"d_k", #10
            r"\vec{g}_k", #11
            r",", #12
            r"\vec{g}_i", #13
            r"\rangle", #14
        ).scale(0.8)
        comb_v_g = MathTex(
            r"\vec{v}", #0
            r"=", #1
            r"d_1", #2
            r"\vec{g}_1", #3
            r"+...+", #4
            r"d_k", #5
            r"\vec{g}_k" #6
        ).scale(0.8)
        for i in [comb_v_g, producto_5, producto_4, producto_3, producto_2, producto_2_swap, producto_1, for_all_i]:
            i.shift(DOWN)
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
        self.play(ReplacementTransform(groups[1][2][:].copy(), comb_v_g))
        self.wait(2)
        #Primera tranformación
        self.play(
            ReplacementTransform(comb_v_g[0], producto_1[1]),
            ReplacementTransform(comb_v_g[1], producto_1[5]),
            ReplacementTransform(comb_v_g[2:], producto_1[7:12]),
            FadeIn(producto_1[:1]),
            FadeIn(producto_1[2:5]),
            FadeIn(producto_1[5:7]),
            FadeIn(producto_1[12:]),
            run_time = 3
        )
        self.wait(2)
        #Segunda transformación
        self.play(
            ReplacementTransform(producto_1[:6], producto_2[:6]),
            ReplacementTransform(producto_1[6], producto_2[6]),
            ReplacementTransform(producto_1[7:9], producto_2[7:9]),
            ReplacementTransform(producto_1[12:].copy(),producto_2[9:12]),
            ReplacementTransform(producto_1[9],producto_2[12]),
            ReplacementTransform(producto_1[6].copy(), producto_2[13]),
            ReplacementTransform(producto_1[10:], producto_2[14:]),
            run_time = 3
        )
        self.wait(2)
        #Tercera transformación
        self.play(
            Transform(producto_2[6], producto_2_swap[6]),
            Transform(producto_2[7], producto_2_swap[7]),
            Transform(producto_2[13], producto_2_swap[13]),
            Transform(producto_2[14], producto_2_swap[14]),
            run_time = 3
        )
        self.wait(2)
        #Cuarta transformación (esta sí está chida)
        self.play(
            ReplacementTransform(producto_2[:6], producto_3[:6]),
            ReplacementTransform(producto_2[6:11], producto_3[6:]),
            ReplacementTransform(producto_2[11], producto_3[6]),
            ReplacementTransform(producto_2[12:], producto_3[7:]),
            run_time = 3
        )
        self.wait(2)
        #Quinta transformación
        self.play(
            ReplacementTransform(producto_3[:6], producto_4[:6]),
            ReplacementTransform(producto_3[6:], producto_4[6:]),
            run_time = 3
        )
        self.wait(2)
        #Sexta transformación 

        #Transform(producto_4[7:], producto_5[2]),
        #Transform(producto_4[:5], producto_5[0]),
        self.play(
            producto_4[:5].animate.move_to(producto_5[0].get_center()),
            ReplacementTransform(producto_4[5], producto_5[3]), #signo igual
            producto_4[7:].animate.move_to(producto_5[2].get_center()),
            ReplacementTransform(producto_4[6], producto_5[4]), #d_i
            FadeIn(producto_5[1]),
            run_time = 3
        )
        self.wait(2)
        self.play(Write(for_all_i))
        self.wait(2)
        producto_5_cop.align_to(group_2, LEFT)
        producto_5_cop.align_to(group_2[3], UP)
        self.play(FadeOut(for_all_i),
        FadeOut(producto_5[:]),
        FadeOut(producto_4[:5]),
        FadeOut(producto_4[7:])
        )
        self.play(
            group_1[:].animate.set_color(WHITE),
            group_2[:].animate.set_color(WHITE),
        )
        self.play(
            Transform(group_2[3], producto_5_cop[:])
        )
    def construct(self):
        self.parte_1()