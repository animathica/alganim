from manim import *
from manim.mobject.geometry import ArrowTriangleFilledTip
#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################


#####################################################################################
###############################  Primera escena  ####################################
###############################  versión: Manim Community v0.8.0   ##################
#####################################################################################

# Constantes de los colores usados.
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

'''
Esta primera escena consta de tres partes:
    Introducción
    Escena geométrica
    Planteamiento del problema en general 
'''
#Dashed arrow para escena geométrica, ahora heredada de DashedLine
class DashedArrow(DashedLine):
    """An arrow.

    Parameters
    ----------
    args : Any
        Arguments to be passed to :class:`Line`.
    stroke_width : :class:`float`, optional
        The thickness of the arrow. Influenced by :attr:`max_stroke_width_to_length_ratio`.
    buff : :class:`float`, optional
        The distance of the arrow from its start and end points.
    max_tip_length_to_length_ratio : :class:`float`, optional
        :attr:`tip_length` scales with the length of the arrow. Increasing this ratio raises the max value of :attr:`tip_length`.
    max_stroke_width_to_length_ratio : :class:`float`, optional
        :attr:`stroke_width` scales with the length of the arrow. Increasing this ratio ratios the max value of :attr:`stroke_width`.
    kwargs : Any
        Additional arguments to be passed to :class:`Line`.
    """
    def __init__(
        self,
        *args,
        stroke_width=6,
        buff=MED_SMALL_BUFF,
        max_tip_length_to_length_ratio=0.25,
        max_stroke_width_to_length_ratio=5,
        **kwargs,
    ):
        self.max_tip_length_to_length_ratio = max_tip_length_to_length_ratio
        self.max_stroke_width_to_length_ratio = max_stroke_width_to_length_ratio
        tip_shape = kwargs.pop("tip_shape", ArrowTriangleFilledTip)
        super().__init__(*args, buff=buff, stroke_width=stroke_width, **kwargs)
        # TODO, should this be affected when
        # Arrow.set_stroke is called?
        self.initial_stroke_width = self.stroke_width
        self.add_tip(tip_shape=tip_shape)
        self.set_stroke_width_from_length()
    def scale(self, factor, scale_tips=False, **kwargs):
        if self.get_length() == 0:
            return self

        if scale_tips:
            super().scale(factor, **kwargs)
            self.set_stroke_width_from_length()
            return self

        has_tip = self.has_tip()
        has_start_tip = self.has_start_tip()
        if has_tip or has_start_tip:
            old_tips = self.pop_tips()

        super().scale(factor, **kwargs)
        self.set_stroke_width_from_length()

        if has_tip:
            self.add_tip(tip=old_tips[0])
        if has_start_tip:
            self.add_tip(tip=old_tips[1], at_start=True)
        return self

    def get_normal_vector(self) -> np.ndarray:
        p0, p1, p2 = self.tip.get_start_anchors()[:3]
        return normalize(np.cross(p2 - p1, p1 - p0))

    def reset_normal_vector(self):
        """Resets the normal of a vector"""
        self.normal_vector = self.get_normal_vector()
        return self

    def get_default_tip_length(self) -> float:
        """Returns the default tip_length of the arrow.
        """
        max_ratio = self.max_tip_length_to_length_ratio
        return min(self.tip_length, max_ratio * self.get_length())

    def set_stroke_width_from_length(self):
        """Used internally. Sets stroke width based on length."""
        max_ratio = self.max_stroke_width_to_length_ratio
        if config.renderer == "opengl":
            self.set_stroke(
                width=min(self.initial_stroke_width, max_ratio * self.get_length()),
                recurse=False,
            )
        else:
            self.set_stroke(
                width=min(self.initial_stroke_width, max_ratio * self.get_length()),
                family=False,
            )
        return self


class Subescena_1(Scene):
    def parte_1(self):
        #----------------------------------- ESPACIO V EN GENERAL
        dim_V = MathTex("\\text{dim}\\left(V\\right)=k<\\infty").scale(0.9).to_edge(UP).shift(1*DOWN)
        base_beta = Tex(
                        "$\\beta$",
                        "$ = $", 
                        "$\\{$",
                        "$\\vec{b}_1$",
                        "$,\\dots,$",
                        "$\\vec{b}_k$",
                        "$\\}$", #0
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
                            "$c_1, \\dots, c_k$",
                            "?")
        group_1 = VGroup(base_beta, base_propiedades, combination, coeficientes_c).scale(0.9)
        group_1.arrange(1.5*DOWN, center=False, aligned_edge=LEFT)
        coeficientes_ci = Tex("¿",
                            "$c_i$",
                            "?").scale(0.9).align_to(group_1[3], LEFT).align_to(group_1[3], UP)
        combination_copy = group_1[2].copy()

        self.play(FadeIn(dim_V),
                run_time = 3       
        )
        self.wait(2)
        self.play(Write(group_1[0][:]),
                run_time = 0.5
        )
        self.play(Write(group_1[1][:]),
                run_time = 0.5
            )
        self.wait(3)
        self.play(Write(group_1[2][:]),
                run_time = 5
            )
        self.wait(3)
        self.wait(11)
        self.play(
            group_1[2][:].animate.set_color(AZUL),
            run_time = 1
        )
        self.play(
            group_1[2][:].animate.set_color(WHITE),
            run_time = 1
        )
        self.play(
            group_1[0][:].animate.set_color(AZUL),
            run_time = 2
        )
        self.play(
            group_1[0][:].animate.set_color(WHITE),
            run_time = 2
        )
        self.play(Write(group_1[3][:]),
            run_time = 5
        )
        self.wait(1)
        self.play(
            Transform(group_1[3][0], coeficientes_ci[0]),
            Transform(group_1[3][1], coeficientes_ci[1]),
            Transform(group_1[3][2], coeficientes_ci[2]),
            run_time = 2
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 1)

    def construct(self):
        self.parte_1()
#-------------------------------------------------------------------------------------------------------  
class Subescena_2(Scene):
    #Parámetros de CONFIG como asignación de los valores 
    #de los atributos
    config.x_min = -0.25,
    config.x_max = 1,
    config.x_axis_width = 5,
    config.x_tick_frequency = 10,
    config.x_leftmost_tick = None,  # Change if different from x_min
    config.x_labeled_nums = [],
    config.x_axis_label = "$x$",
    config.y_min = -1.5,
    config.y_max = 1.5,
    config.y_axis_height = 3*1.5,
    config.y_tick_frequency = 0.5,
    config.y_bottom_tick = None,  # Change if different from y_min
    config.y_labeled_nums = [-1,1],
    config.y_axis_label = "$y$",
    config.axes_color = BLUE,
    config.graph_origin = 4.5*LEFT+0.7*DOWN,
    config.exclude_zero_label = True,
    config.default_graph_colors = [BLUE, GREEN, YELLOW],
    config.default_derivative_color = GREEN,
    config.default_input_color = YELLOW,
    config.default_riemann_start_color = BLUE,
    config.default_riemann_end_color = GREEN,
    config.area_opacity = 0.8,
    config.num_rects = 50,
    config.num_graph_anchor_points = 3000
    def parte_2(self):
        # Texto mostrado junto con el generado.
        Text14 = Tex('''$ \\{ \\vec{b}_1 + c_2 \\vec{b}_2 : c_2 \\in \\mathbb{R} \\} $''').move_to(1.5*DOWN + 3.5*LEFT)
        Text14[0][1:10].set_color(MAGENTA_CLARO)
        Text14.bg = SurroundingRectangle(Text14,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text14.group = VGroup(Text14.bg, Text14)
        Text14_2 = Tex('''$ \\{ c_1 \\vec{b}_1 + c_2 \\vec{b}_2 : c_1, c_2 \\in \\mathbb{R} \\} $''').move_to(1.5*DOWN + 3.5*LEFT)
        Text14_2[0][1:12].set_color(MAGENTA_CLARO)
        Text14_2.bg = SurroundingRectangle(Text14_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text14_2.group = VGroup(Text14_2.bg, Text14_2)
        Text14_3 = Tex('''$\\langle\\vec{b}_1,\\vec{b}_2\\rangle = \\mathbb{R}^2$''').move_to(1.5*DOWN + 3.5*LEFT)
        Text14_3[0][1:4].set_color(MAGENTA_CLARO)
        Text14_3[0][5:8].set_color(MAGENTA_CLARO)
        Text14_3[0][-2:].set_color(MAGENTA_CLARO)
        Text14_3.bg = SurroundingRectangle(Text14_3,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text14_3.group = VGroup(Text14_3.bg, Text14_3) 
        #------------------------------------Animación del generado
        def gen1(Vec1,Vec2,Lab1,Lab2):
            self.play(FadeOut(VGroup(Lab1,Lab2)))
            # Copias de vectores.
            Copia1 = Vec1.copy()
            # Coordenadas de vectores
            A1 = Vec1.get_end()[0]
            A2 = Vec1.get_end()[1]
            B1 = Vec2.get_end()[0]
            B2 = Vec2.get_end()[1]
            # Vectores para el paralelogramo.
            Vec1c = DashedArrow(Vec2.get_end(),Vec2.get_end()+A1*RIGHT+A2*UP, buff=0, color = Vec1.get_color()).set_fill(opacity=0.5)
            Vec2c = DashedArrow(Vec1.get_end(),Vec1.get_end()+B1*RIGHT+B2*UP, buff=0, color = Vec2.get_color()).set_fill(opacity=0.5)
            self.play(Create(VGroup(Vec1c,Vec2c)))
            # Vector resultante de la combinación lineal.
            VecRCL = DashedArrow((0,0,0), Vec2c.get_end(), buff=0, color = MAGENTA).set_fill(opacity=1)
            self.play(Create(VecRCL))
            # ValueTrackers
            vt1 = ValueTracker(1)
            self.play(FadeOut(Vec1c))
            # Primera función para cambios de Vec2.
            def upd_for_vec2_1(obj):
                t = vt1.get_value()
                NewVec2 = Arrow((0,0,0),(t*B1,t*B2,0),buff=0, color = Vec2.get_color())
                obj.become(NewVec2)
            # Primera función para cambios de Vec2c.
            def upd_for_vec2c_1(obj):
                t = vt1.get_value()
                NewVec2c = DashedArrow(Vec1.get_end(),Vec1.get_end()+(t*B1,t*B2,0), buff=0, color = Vec2.get_color()).set_fill(opacity=0.5)
                obj.become(NewVec2c)
            # Primera función para cambios de VecRCL.
            def upd_for_vecrcl_1(obj):
                t = vt1.get_value()
                NewVecRCL = DashedArrow((0,0,0),Vec2c.get_end(), buff=0, color = MAGENTA).set_fill(opacity=1)
                obj.become(NewVecRCL)
            # Primera línea usada.
            Linea1 = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP, Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
            # Segunda línea usada.
            Linea2 = Line(Vec1.get_end(), Vec1.get_end()-(0.01*B1,0.01*B2,0), color = MAGENTA).set_fill(opacity=0.5)
            # Función para cambiar tamaño de las líneas.
            def upd_for_linea(obj):
                t = vt1.get_value()
                new_linea = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP,Vec1.get_end()+(t*B1,t*B2,0), color = MAGENTA).set_fill(opacity=0.5)
                obj.become(new_linea)  
            # Primera línea numérica
            Num_Lin_1 = NumberLine(rotation = PI/2, include_numbers = False, label_direction = RIGHT,
                                     x_range=[-9, 9, 1], numbers_to_exclude = [-9,9], tick_size=0.3, numbers_with_elongated_ticks=[0]).scale(0.15)
            Num_Lin_1.move_to(2*DOWN + 3*RIGHT)
            # Segunda línea numérica
            Num_Lin_2 = NumberLine(rotation = PI/2, include_numbers = False, label_direction = RIGHT,
                                     x_range=[-9, 9, 1], numbers_to_exclude = [-9,9], tick_size=0.3, numbers_with_elongated_ticks=[0]).scale(0.15)

            Num_Lin_2.move_to(2*DOWN + 1*RIGHT)
            # Paréntesis para conjunto abierto.
            ParSup1 = Tex(")").move_to(Num_Lin_1.get_end()+0.04*DOWN).scale(1).rotate(np.pi/2)
            ParInf1 = Tex(")").move_to(Num_Lin_1.get_start()+0.04*UP).scale(1).rotate(-np.pi/2)
            ParSup2 = Tex(")").move_to(Num_Lin_2.get_end()+0.04*DOWN).scale(1).rotate(np.pi/2)
            ParInf2 = Tex(")").move_to(Num_Lin_2.get_start()+0.04*UP).scale(1).rotate(-np.pi/2)
            # Símbolos de infinito
            Inf_1 = Tex("$ \\infty $").move_to(Num_Lin_1.get_end()+0.25*UP).scale(0.6)
            MInf_1 = Tex("$ - \\infty $").move_to(Num_Lin_1.get_start()+0.25*DOWN).scale(0.6)
            Inf_2 = Tex("$ \\infty $").move_to(Num_Lin_2.get_end()+0.25*UP).scale(0.6)
            MInf_2 = Tex("$ - \\infty $").move_to(Num_Lin_2.get_start()+0.25*DOWN).scale(0.6)
            # Linea con que se colorea primera recta numérica.
            LINEA_1 = Line(Num_Lin_1.number_to_point(1),Num_Lin_1.number_to_point(1.001))
            # Flecha para primera recta numérica.
            FLECHA_1 = Arrow(Num_Lin_1.number_to_point(0),np.array([2,Num_Lin_1.number_to_point(0)[1],0]),buff=0)
            # Linea con que se colorea segunda recta numérica.
            LINEA_2 = Line(Num_Lin_2.number_to_point(1),Num_Lin_2.number_to_point(1.001))
            # Flecha para segunda recta numérica. 
            FLECHA_2 = Arrow(Num_Lin_2.number_to_point(0),np.array([4,Num_Lin_2.number_to_point(0)[1],0]),buff=0)
            # Valores para primera recta numérica. 
            Coef_1 = (MathTex("c_2")).next_to(FLECHA_2.get_end(),RIGHT)
            # Valores para segunda recta numérica. 
            Coef_2 = (MathTex("c_1")).next_to(FLECHA_1.get_end(),RIGHT)
            def upd_for_coef_1(obj):
                t = vt1.get_value()
                obj.set_y(Num_Lin_1.number_to_point(t)[1])
            def upd_for_coef_2(obj):
                t = vt1.get_value()
                obj.set_y(Num_Lin_2.number_to_point(t)[1])
            def upd_for_LINEA_1(obj):
                t = vt1.get_value()
                if t > 0:
                    if Num_Lin_1.number_to_point(t)[1] > obj.get_end()[1]:
                        new_LINEA = Line(obj.get_start(),Num_Lin_1.number_to_point(t),color=ROJO, stroke_width=15)
                    else:
                        return None
                elif t < 0:
                    if Num_Lin_1.number_to_point(t)[1] < obj.get_start()[1]:
                        new_LINEA = Line(Num_Lin_1.number_to_point(t),obj.get_end(),color=ROJO, stroke_width=15)
                    else:
                        return None
                elif t == 0:
                    return None
                obj.become(new_LINEA)
                self.bring_to_front(obj)
            def upd_for_FLECHA_1(obj):
                t = vt1.get_value()
                new_FLECHA = Arrow(0.25*RIGHT,0.25*LEFT,buff=0).set_height(0.25).next_to(Num_Lin_1.number_to_point(t),RIGHT,buff=0.1)
                obj.become(new_FLECHA)
            def upd_for_LINEA_2(obj):
                t = vt1.get_value()
                if t > 0:
                    if Num_Lin_2.number_to_point(t)[1] > obj.get_end()[1]:
                        new_LINEA = Line(obj.get_start(),Num_Lin_2.number_to_point(t),color=AZUL, stroke_width=15)
                    else:
                        return None
                elif t < 0:
                    if Num_Lin_2.number_to_point(t)[1] < obj.get_start()[1]:
                        new_LINEA = Line(Num_Lin_2.number_to_point(t),obj.get_end(),color=AZUL, stroke_width=15)
                    else:
                        return None
                elif t == 0:
                    return None
                obj.become(new_LINEA)
                self.bring_to_front(obj)
            def upd_for_FLECHA_2(obj):
                t = vt1.get_value()
                new_FLECHA = Arrow(0.25*RIGHT,0.25*LEFT,buff=0).set_height(0.25).next_to(Num_Lin_2.number_to_point(t),RIGHT,buff=0.1)
                obj.become(new_FLECHA)

            self.play(Create(Linea1),Create(Linea2))
            self.bring_to_back(Linea1)
            self.bring_to_back(Linea2)
            Vec2.add_updater(upd_for_vec2_1)
            Vec2c.add_updater(upd_for_vec2c_1)
            VecRCL.add_updater(upd_for_vecrcl_1)
            Linea1.add_updater(upd_for_linea)
            Linea2.add_updater(upd_for_linea)
            self.add_foreground_mobjects(Num_Lin_1,Inf_1,MInf_1,ParSup1,ParInf1)
            LINEA_1.add_updater(upd_for_LINEA_1)
            FLECHA_1.add_updater(upd_for_FLECHA_1)
            Coef_1.add_updater(upd_for_coef_1)
            self.play(Create(Num_Lin_1),Write(ParSup1),
                    Write(ParInf1), Write(Inf_1),Write(MInf_1),
                    Create(LINEA_1),Create(FLECHA_1),Create(Coef_1),
                    Write(Text14.group)
            )
            self.add_foreground_mobjects(Text14.group)
            self.play(vt1.animate.set_value(9),run_time=1.3)
            Linea1.remove_updater(upd_for_linea)
            self.play(vt1.animate.set_value(1))
            self.play(vt1.animate.set_value(-9),run_time=1.3)
            Linea2.remove_updater(upd_for_linea)
            self.play(vt1.animate.set_value(1),run_time=1)
            self.remove_foreground_mobjects(Text14.group)
            Vec2.remove_updater(upd_for_vec2_1)
            Vec2c.remove_updater(upd_for_vec2c_1)
            VecRCL.remove_updater(upd_for_vecrcl_1)
            LINEA_1.remove_updater(upd_for_LINEA_1)
            FLECHA_1.remove_updater(upd_for_FLECHA_1)
            Coef_1.remove_updater(upd_for_coef_1)
            self.wait(0.65)
            self.remove_foreground_mobjects(FLECHA_1)
            self.play(FadeOut(Vec2c),FadeOut(FLECHA_1),FadeOut(Coef_1))

            self.play(Create(Vec1c))
            # Primera función para cambios de Vec1.
            def upd_for_vec1_1(obj):
                t = vt1.get_value()
                NewVec1 = Arrow((0,0,0),(t*A1,t*A2,0),buff=0, color = Vec1.get_color())
                obj.become(NewVec1)
            # Primera función para cambios de Vec1c.
            def upd_for_vec1c_1(obj):
                t = vt1.get_value()
                NewVec1c = DashedArrow(Vec2.get_end(),Vec2.get_end()+(t*A1,t*A2,0), buff=0, color = Vec1.get_color()).set_fill(opacity=0.5)
                obj.become(NewVec1c)
            # Segunda función para cambios de VecRCL.
            def upd_for_vecrcl_2(obj):
                t = vt1.get_value()
                NewVecRCL = DashedArrow((0,0,0),Vec2.get_end()+(t*A1,t*A2,0), buff=0, color = MAGENTA).set_fill(opacity=1)
                obj.become(NewVecRCL)
            # Rectangulos usados para rellenar plano.
            Vertice1 = Linea1.get_end()
            Vertice2 = Linea2.get_end()
            Vertice3 = Linea2.get_end()+(0.05*A1,0.025*A2,0)
            Vertice4 = Linea1.get_end()+(0.05*A1,0.025*A2,0)
            Vertice5 = Linea2.get_end()-(0.05*A1,0.025*A2,0)
            Vertice6 = Linea1.get_end()-(0.05*A1,0.025*A2,0)
            Plano1 = Polygon(Vertice1,Vertice2,Vertice3,Vertice4,stroke_width=0)
            Plano2 = Polygon(Vertice1,Vertice2,Vertice5,Vertice6,stroke_width=0)
            # Función que rellena plano.
            def upd_for_plano(obj):
                t = vt1.get_value()
                vert1 = Linea1.get_end()
                vert2 = Linea2.get_end()
                vert3 = (t*A1,t*A2,0)
                vert4 = (t*A1,t*A2,0)
                New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA_CLARO, opacity = 1)
                obj.become(New_plano)
                self.bring_to_back(obj)

            Vec1.add_updater(upd_for_vec1_1)
            Vec1c.add_updater(upd_for_vec1c_1)
            VecRCL.add_updater(upd_for_vecrcl_2)
            Plano1.add_updater(upd_for_plano)
            Coef_2.add_updater(upd_for_coef_2)
            LINEA_2.add_updater(upd_for_LINEA_2)
            FLECHA_2.add_updater(upd_for_FLECHA_2)
            self.play(Create(Num_Lin_2),Write(ParSup2),
                    Write(ParInf2),Write(Inf_2),Write(MInf_2),
                    Create(LINEA_2),Create(FLECHA_2),Create(Coef_2),
                    ReplacementTransform(Text14[0][:],Text14_2[0][:]),
                    ReplacementTransform(Text14.bg,Text14_2.bg)
            )
            self.add_foreground_mobjects(Text14_2)
            self.play(Create(Plano1), run_time=0.05)
            self.play(Create(Plano2), run_time = 0.05)

            self.add_foreground_mobjects(Num_Lin_2,Inf_2,MInf_2,ParSup2,ParInf2)

            self.play(vt1.animate.set_value(9),run_time=1.3)
            Plano1.remove_updater(upd_for_plano)
            self.play(vt1.animate.set_value(1))
            Plano2.add_updater(upd_for_plano)
            self.bring_to_back(Plano2)
            self.play(vt1.animate.set_value(-9),run_time=1.3)
            Plano2.remove_updater(upd_for_plano)
            self.play(vt1.animate.set_value(1),run_time=1.3)
            self.play(FadeOut(Linea1), FadeOut(Linea2))
            self.add_foreground_mobjects(Text14_2.group)
            Vec1.remove_updater(upd_for_vec1_1)
            Vec1c.remove_updater(upd_for_vec1c_1)
            VecRCL.remove_updater(upd_for_vecrcl_2)

            LINEA_2.remove_updater(upd_for_LINEA_2)
            FLECHA_2.remove_updater(upd_for_FLECHA_2)
            Coef_2.remove_updater(upd_for_coef_2)

            self.wait(0.65)
            self.remove_foreground_mobjects(FLECHA_2)
            self.play(FadeOut(Vec1c), FadeOut(FLECHA_2), FadeOut(Coef_2))
            self.remove_foreground_mobjects(Text14_2.group)
            self.play(
                    ReplacementTransform(Text14_2[0][:],Text14_3[0][:9]),
                    ReplacementTransform(Text14_2.bg,Text14_3.bg)
            )
            self.add_foreground_mobjects(Text14_3)
            self.play(
                    FadeIn(Text14_3[0][9:]),
                    run_time = 3
            )
            self.remove_foreground_mobjects(Text14_2)
            self.wait(3)
            Punto = Dot(radius=0.01, color = MAGENTA).set_fill(MAGENTA)
            self.add_foreground_mobject(VecRCL)
            self.remove_foreground_mobject(Text14_3)
            self.remove_foreground_mobject(Text14_3.group)
            self.remove_foreground_mobject(VecRCL)
            self.remove_foreground_mobjects(LINEA_1,LINEA_2,Num_Lin_1,Num_Lin_2,Inf_1,MInf_1,Inf_2,MInf_2,ParInf1,ParInf2,ParSup1,ParSup2)
            self.play(FadeOut(VGroup(Plano1,Plano2)),FadeOut(Text14_3.group),FadeOut(VGroup(VecRCL,Punto,LINEA_1,LINEA_2,Num_Lin_1,Num_Lin_2,Inf_1,MInf_1,Inf_2,MInf_2,ParInf1,ParInf2,ParSup1,ParSup2)))
            self.play(Write(VGroup(Lab1,Lab2)))

        #------------------------------------Animación en la que se buscan los escalares 
        def encontrar_escalares(vec1, vec_obj1, text_A, vec2, vec_obj2, text_B, vec_objetivo, text_vec_objetivo):
            '''
            vec: numpy array
            vec_obj: VMobject
            '''
            # Colores para los vectores escalados
            col1 = vec_obj1.get_color()
            col2 = vec_obj2.get_color()
            col3 = MAGENTA
            # ---------------------------------------- Recta numérica a lo largo de la cual se desplazan los escalares
            number_line = NumberLine(rotation = PI/2, include_numbers = True, label_direction = RIGHT,
                                     x_range=[-3, 3, 1], numbers_to_exclude = [-3,3]).move_to(np.array([5.5,-2.0,0])).scale(0.5)
            # Paréntesis para la recta numérica
            par_sup = Tex(")").move_to(number_line.get_end()+0.04*DOWN).scale(1).rotate(np.pi/2).scale(0.8)
            par_inf = Tex(")").move_to(number_line.get_start()+0.04*UP).scale(1).rotate(-np.pi/2).scale(0.8)
            # Símbolos de infinito para la recta numérica
            inf = Tex("$ \\infty $").move_to(number_line.get_end()+0.25*UP).scale(0.6)
            minf = Tex("$ - \\infty $").move_to(number_line.get_start()+0.25*DOWN).scale(0.6)
            # Flechas que apuntan al valor de los escalares
            pointer_vec_1 = Arrow(start=ORIGIN, end=RIGHT, max_tip_length_to_length_ratio=0.4)
            label_1 = MathTex("c_1").set_color(AZUL).add_updater(lambda m: m.next_to(pointer_vec_1, 0.3*LEFT))
            pointer_vec_2 = Arrow(start=ORIGIN, end=LEFT, max_tip_length_to_length_ratio=0.4)
            label_2 = MathTex("c_2").set_color(ROJO).add_updater(lambda m: m.next_to(pointer_vec_2, 0.3*RIGHT))
            # ValueTrackers para vector 1 y vector 2, respectivamente. Son utilizados para modificar muchos objetos
            # simultáneamente
            t1 = ValueTracker(1)
            t2 = ValueTracker(1)
            # Updaters para los sliders sobre la recta real 
            # Flecha para c_1
            pointer_vec_1.add_updater(
                lambda m: m.next_to(
                            number_line.n2p(t1.get_value()),
                            LEFT,
                            buff = 0.1
                )
            )
            # Flecha para c_2
            pointer_vec_2.add_updater(
                lambda m: m.next_to(
                            number_line.n2p(t2.get_value()),
                            RIGHT,
                            buff = 0.4
                )
            )
            # VGroup de la recta numérica completa
            complete_number_line = VGroup(number_line, par_sup, par_inf, inf, minf, pointer_vec_1, label_1, pointer_vec_2, label_2)

            # Box que contiene a la recta numérica
            sliders_box = Rectangle(width=2.5, height=3.9, fill_color=BLACK, fill_opacity=1).move_to(np.array([5.51,-2,0]))
            sliders = VGroup(sliders_box, complete_number_line)
            # ---------------------------------------- Vectores en el plano    
            # Texto de los escalares
            label1 = MathTex("c_1")
            label2 = MathTex("c_2")
            # Vector suma en numpy array y en arrow
            vec1_plus_vec2 = vec1+vec2
            vec_AplusB = Arrow((0, 0, 0), vec1_plus_vec2, buff=0, color = col3)
            # distancias de separación entre puntas de vectores y el correspondiente texto
            dist_1 = 0.4*vec1/(np.linalg.norm(vec1))
            dist_2 = 0.4*vec2/(np.linalg.norm(vec2))
            dist_3 = 0.4*vec1_plus_vec2/(np.linalg.norm(vec1_plus_vec2))
            # Etiqueta de la suma
            plus_sign = MathTex("+").move_to(vec_AplusB.get_end()+dist_3)
            label_sum1 = MathTex("c_2").next_to(plus_sign, 0.5*RIGHT)
            label_sum2 = text_B.copy().next_to(label_sum1, 0.5*RIGHT)
            label_sum3 = text_A.copy().next_to(plus_sign, 0.5*LEFT)
            label_sum4 = MathTex("c_1").next_to(label_sum3, 0.5*LEFT)
            label3 = VGroup(plus_sign, label_sum1, label_sum2, label_sum3, label_sum4).move_to(vec_AplusB.get_end()+dist_3)
            # Otros símbolos utilizados
            equal_sign = MathTex("=")
            # Vectores fantasma para la suma
            fantasma_flecha1 = DashedArrow(vec2, vec1_plus_vec2, buff = 0, stroke_opacity = 0.5, color = col1)
            fantasma_flecha2 = DashedArrow(vec1, vec1_plus_vec2, buff = 0, stroke_opacity = 0.5, color = col2)

            
            # Updaters
            def upd_for_vec1(obj):
                new_vec = Arrow((0,0,0), t1.get_value()*vec1, buff=0, color = col1)
                obj.become(new_vec)

            def upd_for_vec2(obj):
                new_vec = Arrow((0,0,0), t2.get_value()*vec2, buff=0, color = col2)
                obj.become(new_vec)

            def upd_for_vec3(obj):
                new_vec = Arrow((0,0,0), t1.get_value()*vec1+t2.get_value()*vec2, buff=0, color = col3)
                obj.become(new_vec)

            def upd_for_text1(obj):
                obj.move_to(vec_obj1.get_end()+dist_1)
                
            def upd_for_text2(obj):
                obj.move_to(vec_obj2.get_end()+dist_2)
            
            def upd_for_text3(obj):
                obj.move_to(vec_AplusB.get_end()+dist_3)

            def upd_for_label1(obj):
                obj.next_to(text_A, 0.5*LEFT)

            def upd_for_label2(obj):
                obj.next_to(text_B, 0.5*LEFT)

            def upd_for_fantasma_flecha1(obj):
                new_vec = DashedArrow(vec_obj2.get_end(), vec_AplusB.get_end(), buff = 0, color = col1, stroke_opacity = 0.5)
                obj.become(new_vec)

            def upd_for_fantasma_flecha2(obj):
                new_vec = DashedArrow(vec_obj1.get_end(), vec_AplusB.get_end(), buff = 0, color = col2, stroke_opacity = 0.5)
                obj.become(new_vec)

            vec_obj1.add_updater(upd_for_vec1)
            label1.add_updater(upd_for_label1)
            text_A.add_updater(upd_for_text1)

            vec_obj2.add_updater(upd_for_vec2)
            text_B.add_updater(upd_for_text2)
            label2.add_updater(upd_for_label2)

            vec_AplusB.add_updater(upd_for_vec3)
            label3.add_updater(upd_for_text3)

            fantasma_flecha1.add_updater(upd_for_fantasma_flecha1)
            fantasma_flecha2.add_updater(upd_for_fantasma_flecha2)

            # Obtención de los escalares resolviendo el sistema de ecuaciones:
            # A.c = b
            A = np.array([vec1[:2], vec2[:2]]).T
            b = np.array(vec_objetivo[:2]) # Vector objetivo
            c = np.linalg.solve(A,b) #Vector de coeficientes

            # ---------------------------------------- Animaciones
            
            self.add_foreground_mobjects(label1,label2)
            self.play(FadeIn(label1.next_to(text_A, 0.5*LEFT)),
            FadeIn(label2.next_to(text_B, 0.5*LEFT)),
            Write(fantasma_flecha1),
            Write(fantasma_flecha2),
            Write(vec_AplusB),
            FadeIn(label3),
            run_time = 2
            )
            self.play(FadeIn(sliders))
            # Moviendo solo el primer coeficiente
            self.play(t1.animate.set_value(0.5), 
            run_time = 1.3)
            self.play(t1.animate.set_value(0.9), 
            run_time = 1.3)
            # Moviendo solo el segundo coeficiente
            self.play(t2.animate.set_value(1.2), 
            run_time = 0.5)
            self.play(t2.animate.set_value(1.0), 
            run_time = 0.5)
            #Moviendo ambos coeficientes de forma simultánea
            self.play(t1.animate.set_value(1.6), 
            t2.animate.set_value(-0.8),
            run_time = 0.5)
            self.play(t1.animate.set_value(-0.5), 
            t2.animate.set_value(-1),
            run_time = 0.5)
            self.play(t1.animate.set_value(-1), 
            t2.animate.set_value(-1.8),
            run_time = 0.5)
            self.play(t1.animate.set_value(0.5), 
            t2.animate.set_value(-0.5),
            FadeOut(text_vec_objetivo),
            run_time = 0.5)
            self.play(t1.animate.set_value(0.6), 
            t2.animate.set_value(1.9),
            run_time = 0.5)
            self.play(t1.animate.set_value(0.6), 
            t2.animate.set_value(2.1),
            run_time = 0.5)
            self.play(t1.animate.set_value(0.4), 
            t2.animate.set_value(2.1),
            run_time = 0.2)
            self.play(t1.animate.set_value(0.4), 
            t2.animate.set_value(1.9),
            run_time = 0.2)
            # Valores correctos de los coeficientes
            self.play(t1.animate.set_value(c[0]), 
            t2.animate.set_value(c[1]),
            run_time = 1.0)
            fantasma_flecha1.remove_updater(upd_for_fantasma_flecha1)
            fantasma_flecha2.remove_updater(upd_for_fantasma_flecha2)
            self.play(
                FadeOut(fantasma_flecha1),
                FadeOut(fantasma_flecha2),
                run_time = 2
            )
            #-----------------------------------------
            self.wait(0.5)
            equal_sign.next_to(label3, 0.5*LEFT)
            text_vec_objetivo.next_to(equal_sign, 0.5*LEFT)
            #Puntos para destello
            dot1 = Dot(radius = 0, color=AMARILLO).next_to(label1, 2*UP)
            dot2 = Dot(radius = 0, color=AMARILLO).next_to(label2, 2*UP)
            self.play(
                    FadeIn(equal_sign),
                    FadeIn(text_vec_objetivo),
                    run_time = 3
            )
            self.play(Circumscribe(label1, fade_out=True), 
                    Circumscribe(label2, fade_out=True),
                    Flash(dot1), 
                    Flash(dot2),
                    run_time = 3
            )
            self.play(
            FadeOut(vec_obj1),
            FadeOut(vec_obj2),
            FadeOut(vec_AplusB),
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 2)

        # Coordenadas del vector objetivo
        vec = np.array([5,3,0])
        # Coordenadas de vector A
        vec_A = np.array([-2,2,0])
        # Coordenadas de vector B
        vec_B = np.array([3,1,0])

        grid = NumberPlane()
        vec_ = Arrow((0, 0, 0), vec, buff=0,color=NARANJA)
        vecA = Arrow((0, 0, 0), vec_A, buff=0,color=AZUL)
        vecB = Arrow((0, 0, 0), vec_B, buff=0,color=ROJO)

        text_vec = MathTex("\\vec{v}").move_to(vec_.get_end()+0.4*vec/(np.linalg.norm(vec)))
        text_A = MathTex("\\vec{b}_1").move_to(vecA.get_end()+0.4*vec_A/(np.linalg.norm(vec_A)))
        text_B = MathTex("\\vec{b}_2").move_to(vecB.get_end()+0.4*vec_B/(np.linalg.norm(vec_B)))

        # Ejes para mostrar independencia lineal de b_1 y b_2
        Eje1 = DashedLine(-5*vec_A,5*vec_A, color = MAGENTA, buff = 0)
        Eje2 = DashedLine(-5*vec_B,5*vec_B, color = MAGENTA, buff = 0)
        Ejes = VGroup(Eje1,Eje2)
        # ---------------------------------------- Animaciones iniciales
        self.play(Write(grid))
        self.wait(0.5)
        self.play(FadeIn(vec_))
        self.play(Write(text_vec))
        self.play(FadeIn(vecA), Write(text_A), FadeIn(vecB), Write(text_B))
        self.wait(0.5)
        self.play(FadeOut(
            vec_,
            text_vec
            ),
            run_time = 1
        )
        self.add_foreground_mobjects(vecA,vecB)
        self.wait(0.5)
        self.play(Create(Ejes))
        self.wait(1)
        self.play(FadeOut(Ejes))
        gen1(vecA, vecB, text_A, text_B)
        self.wait(0.5)
        self.play(FadeIn(vec_))
        self.play(Write(text_vec))
        encontrar_escalares(vec_A, vecA, text_A, vec_B, vecB, text_B, vec, text_vec)
        self.wait(0.5)
        
    def construct(self):
        self.parte_2()
#-------------------------------------------------------------------------------------------------------
class Subescena_3(Scene):
    def parte_3(self):
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
        #----------------------------------- ESPACIO V EN GENERAL
        base_beta = Tex(
                        "$\\beta $", #0
                        "$ = $", #1
                        "$ \\{$", #2
                        "$\\vec{b}_1$", #3
                        "$,\\dots,$", #4
                        "$\\vec{b}_k$", #5
                        "$\\}$", #6
                        " base de ", #7
                        "$V$" #8
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
                            r"$c_i$",
                            "?")
        group = VGroup(base_beta, #0
                        base_propiedades, #1
                        combination, #2
                        coeficientes_c #3
                        ).scale(0.8).shift(4*LEFT+UP)
        group.arrange(3*DOWN, center=False, aligned_edge=LEFT)

        #----------------------------------- TRANSFORMACIÓN DE VECTORES EN N-TUPLAS
        #Superíndice indica el número de vector, subíndice la entrada
        #______________________ dim(V) = k
        entries_vk_ntup = [["v_{1}"], ["v_{2}"],["\\vdots"],["v_{k}"]]  
        vk_ntup = Matrix(entries_vk_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)").set_column_colors(AZUL)

        entries_vk_1_ntup = [["v_{1}^1"], ["v_{2}^1"],["\\vdots"],["v_{k}^1"]]  
        vk_1_ntup = Matrix(entries_vk_1_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")

        entries_vk_k_ntup = [["v_{1}^k"], ["v_{2}^k"],["\\vdots"],["v_{k}^k"]]  
        vk_k_ntup = Matrix(entries_vk_k_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        
        base_beta_dimK_0 = MathTex("\\beta")
        base_beta_dimK_1 = MathTex("=")
        base_beta_dimK_3 = vk_1_ntup.copy()
        base_beta_dimK_2 = Brace(base_beta_dimK_3, LEFT)
        base_beta_dimK_4 = Tex("$,\\dots,$", "texto auxiliar") #Ayuda para las transformaciones
        base_beta_dimK_5 = vk_k_ntup.copy()
        base_beta_dimK_6 = Brace(base_beta_dimK_5, RIGHT)
        base_beta_dimK_7 = Tex(" base de ", "texto auxiliar") #Ayuda para las transformaciones
        base_beta_dimK_8 = MathTex("K^k")

        base_beta_dimK = VGroup(
                                base_beta_dimK_0,
                                base_beta_dimK_1,
                                base_beta_dimK_2,
                                base_beta_dimK_3,
                                base_beta_dimK_4[0],
                                base_beta_dimK_5,
                                base_beta_dimK_6,
                                base_beta_dimK_7[0],
                                base_beta_dimK_8,        
                        ).arrange(direction=RIGHT, buff=0.15, center=False).move_to(UP)

        base_beta_dimK_propiedades = Tex(
                                "$\\langle \\beta\\rangle = V$",
                                "$,\\,\\beta$ es l.i."
                                )
        combination_dimK_0 = vk_ntup.copy()
        combination_dimK_1 = MathTex("=")
        combination_dimK_2 = MathTex("c_1", "x").set_color(ROJO)
        combination_dimK_3 = vk_1_ntup.copy()
        combination_dimK_4 = MathTex("+")
        combination_dimK_5 = MathTex("\\cdots", "x")
        combination_dimK_6 = MathTex("+")
        combination_dimK_7 = MathTex("c_k", "x").set_color(ROJO)
        combination_dimK_8 = vk_k_ntup.copy()

        combination_dimK = VGroup(
                                combination_dimK_0,
                                combination_dimK_1,
                                combination_dimK_2[0],
                                combination_dimK_3,
                                combination_dimK_4,
                                combination_dimK_5[0],
                                combination_dimK_6,
                                combination_dimK_7[0],
                                combination_dimK_8,
                            ).arrange(direction=RIGHT, buff=0.15, center=False)
        coeficientes_c_dimK = Tex("¿",
                            r"$c_i$",
                            "?")
        group_dimK_ntuplas = VGroup(base_beta_dimK, #0
                                    base_beta_dimK_propiedades, #1
                                    combination_dimK, #2
                                    coeficientes_c_dimK #3
                                ).scale(0.6).shift(4*LEFT+UP)
        group_dimK_ntuplas.arrange(2.5*DOWN, center=False, aligned_edge=LEFT)
        #Alineacion de igualdades
        group_dimK_ntuplas[0][:].align_to(group[0][:],LEFT)
        group_dimK_ntuplas[2][:].align_to(group[2][:],LEFT)

        #______________________ dim(V) = k + 1
        
        entries_vk1_ntup = [["v_{1}"], ["v_{2}"],["\\vdots"],["v_{k}"],["v_{k+1}"]]  
        vk1_ntup = Matrix(entries_vk1_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)").set_column_colors(AZUL)
        
        entries_vk1_1_ntup = [["v_{1}^1"], ["v_{2}^1"],["\\vdots"],["v_{k}^1"],["v_{k+1}^1"]]  
        vk1_1_ntup = Matrix(entries_vk1_1_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")

        entries_vk1_k_ntup = [["v_{1}^k"], ["v_{2}^k"],["\\vdots"],["v_{k}^k"],["v_{k+1}^{k}"]]  
        vk1_k_ntup = Matrix(entries_vk1_k_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        
        entries_vk1_k1_ntup = [["v_{1}^{k+1}"], ["v_{2}^{k+1}"],["\\vdots"],["v_{k}^{k+1}"],["v_{k+1}^{k+1}"]]  
        vk1_k1_ntup = Matrix(entries_vk1_k1_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")

        base_beta_dimK1_0 = MathTex("\\beta")
        base_beta_dimK1_1 = MathTex("=")
        base_beta_dimK1_3 = vk1_1_ntup.copy()
        base_beta_dimK1_2 = Brace(base_beta_dimK1_3, LEFT)
        base_beta_dimK1_4 = Tex("$,\\dots,$", "texto auxiliar") #Ayuda para las transformaciones
        base_beta_dimK1_5 = vk1_k_ntup.copy()
        base_beta_dimK1_6 = Tex(",", ",")
        base_beta_dimK1_7 = vk1_k1_ntup.copy()
        base_beta_dimK1_8 = Brace(base_beta_dimK1_5, RIGHT)
        base_beta_dimK1_9 = Tex(" base de ", "texto auxiliar") #Ayuda para las transformaciones
        base_beta_dimK1_10 = MathTex("K}^{k+1}")

        base_beta_dimK1 = VGroup(
                                base_beta_dimK1_0,
                                base_beta_dimK1_1,
                                base_beta_dimK1_2,
                                base_beta_dimK1_3,
                                base_beta_dimK1_4[0],
                                base_beta_dimK1_5,
                                base_beta_dimK1_6[0],
                                base_beta_dimK1_7,
                                base_beta_dimK1_8,
                                base_beta_dimK1_9[0],
                                base_beta_dimK1_10        
                        ).arrange(direction=RIGHT, buff=0.15, center=False).move_to(UP)

        base_beta_dimK1_propiedades = Tex(
                                "$\\langle \\beta\\rangle = V$",
                                "$,\\,\\beta$ es l.i."
                                )
        combination_dimK1_0 = vk1_ntup.copy()
        combination_dimK1_1 = MathTex("=")
        combination_dimK1_2 = MathTex("c_1", "x").set_color(ROJO)
        combination_dimK1_3 = vk1_1_ntup.copy()
        combination_dimK1_4 = MathTex("+")
        combination_dimK1_5 = MathTex("\\cdots", "x")
        combination_dimK1_6 = MathTex("+")
        combination_dimK1_7 = MathTex("c_k", "x").set_color(ROJO)
        combination_dimK1_8 = vk1_k_ntup.copy()
        combination_dimK1_9 = MathTex("+")
        combination_dimK1_10 = MathTex("c_{k+1}", "x").set_color(ROJO)
        combination_dimK1_11 = vk1_k1_ntup.copy()

        combination_dimK1 = VGroup(
                                combination_dimK1_0,
                                combination_dimK1_1,
                                combination_dimK1_2[0],
                                combination_dimK1_3,
                                combination_dimK1_4,
                                combination_dimK1_5[0],
                                combination_dimK1_6,
                                combination_dimK1_7[0],
                                combination_dimK1_8,
                                combination_dimK1_9,
                                combination_dimK1_10[0],
                                combination_dimK1_11,
                            ).arrange(direction=RIGHT, buff=0.15, center=False)
        coeficientes_c_dimK1 = Tex("¿",
                            r"$c_i$",
                            "?")
        group_dimK1_ntuplas = VGroup(base_beta_dimK1, #0
                                    base_beta_dimK1_propiedades, #1
                                    combination_dimK1, #2
                                    coeficientes_c_dimK1 #3
                                ).scale(0.5).shift(4*LEFT+UP)
        group_dimK1_ntuplas.arrange(2.5*DOWN, center=False, aligned_edge=LEFT)
        #Alineacion de igualdades
        group_dimK1_ntuplas[0][:].align_to(group_dimK_ntuplas[0][:],UP).align_to(group[0][:],LEFT)
        group_dimK1_ntuplas[2][:].align_to(group_dimK_ntuplas[2][:],UP).align_to(group[2][:],LEFT)

         #______________________ dim(V) = k + 2
        
        entries_vk2_ntup = [["v_{1}"], ["v_{2}"],["\\vdots"],["v_{k}"],["v_{k+1}"],["v_{k+2}"]]  
        vk2_ntup = Matrix(entries_vk2_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)").set_column_colors(AZUL)
        
        entries_vk2_1_ntup = [["v_{1}^1"], ["v_{2}^1"],["\\vdots"],["v_{k}^1"],["v_{k+1}^1"],["v_{k+2}^1"]]  
        vk2_1_ntup = Matrix(entries_vk2_1_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")

        entries_vk2_k_ntup = [["v_{1}^k"], ["v_{2}^k"],["\\vdots"],["v_{k}^k"],["v_{k+1}^{k}"],["v_{k+2}^{k}"]]  
        vk2_k_ntup = Matrix(entries_vk2_k_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        
        entries_vk2_k1_ntup = [["v_{1}^{k+1}"], ["v_{2}^{k+1}"],["\\vdots"],["v_{k}^{k+1}"],["v_{k+1}^{k+1}"], ["v_{k+2}^{k+1}"]]  
        vk2_k1_ntup = Matrix(entries_vk2_k1_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")

        entries_vk2_k2_ntup = [["v_{1}^{k+2}"], ["v_{2}^{k+2}"],["\\vdots"],["v_{k}^{k+2}"],["v_{k+1}^{k+2}"], ["v_{k+2}^{k+2}"]]  
        vk2_k2_ntup = Matrix(entries_vk2_k2_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")

        base_beta_dimK2_0 = MathTex("\\beta")
        base_beta_dimK2_1 = MathTex("=")
        base_beta_dimK2_3 = vk2_1_ntup.copy()
        base_beta_dimK2_2 = Brace(base_beta_dimK2_3, LEFT)
        base_beta_dimK2_4 = Tex("$,\\dots,$", "texto auxiliar") #Ayuda para las transformaciones
        base_beta_dimK2_5 = vk2_k_ntup.copy()
        base_beta_dimK2_6 = Tex(",", ",")
        base_beta_dimK2_7 = vk2_k1_ntup.copy()
        base_beta_dimK2_8 = Tex(",", ",")
        base_beta_dimK2_9 = vk2_k2_ntup.copy()
        base_beta_dimK2_10 = Brace(base_beta_dimK2_9, RIGHT)
        base_beta_dimK2_11 = Tex(" base de ", "texto auxiliar") #Ayuda para las transformaciones
        base_beta_dimK2_12 = MathTex("K^{k+2}")

        base_beta_dimK2 = VGroup(
                                base_beta_dimK2_0,
                                base_beta_dimK2_1,
                                base_beta_dimK2_2,
                                base_beta_dimK2_3,
                                base_beta_dimK2_4[0],      
                                base_beta_dimK2_5,
                                base_beta_dimK2_6[0],
                                base_beta_dimK2_7,
                                base_beta_dimK2_8[0],
                                base_beta_dimK2_9,
                                base_beta_dimK2_10,
                                base_beta_dimK2_11[0],
                                base_beta_dimK2_12
                        ).arrange(direction=RIGHT, buff=0.15, center=False).move_to(UP)

        base_beta_dimK2_propiedades = Tex(
                                "$\\langle \\beta\\rangle = V$",
                                "$,\\,\\beta$ es l.i."
                                )
        combination_dimK2_0 = vk2_ntup.copy()
        combination_dimK2_1 = MathTex("=")
        combination_dimK2_2 = MathTex("c_1", "x").set_color(ROJO)
        combination_dimK2_3 = vk2_1_ntup.copy()
        combination_dimK2_4 = MathTex("+")
        combination_dimK2_5 = MathTex("\\cdots", "x")
        combination_dimK2_6 = MathTex("+")
        combination_dimK2_7 = MathTex("c_k", "x").set_color(ROJO)
        combination_dimK2_8 = vk2_k_ntup.copy()
        combination_dimK2_9 = MathTex("+")
        combination_dimK2_10 = MathTex("c_{k+1}", "x").set_color(ROJO)
        combination_dimK2_11 = vk2_k1_ntup.copy()
        combination_dimK2_12 = MathTex("+")
        combination_dimK2_13 = MathTex("c_{k+2}", "x").set_color(ROJO)
        combination_dimK2_14 = vk2_k2_ntup.copy()

        combination_dimK2 = VGroup(
                                combination_dimK2_0,
                                combination_dimK2_1,
                                combination_dimK2_2[0],
                                combination_dimK2_3,
                                combination_dimK2_4,
                                combination_dimK2_5[0],
                                combination_dimK2_6,
                                combination_dimK2_7[0],
                                combination_dimK2_8,
                                combination_dimK2_9,
                                combination_dimK2_10[0],
                                combination_dimK2_11,
                                combination_dimK2_12,
                                combination_dimK2_13[0],
                                combination_dimK2_14,
                            ).arrange(direction=RIGHT, buff=0.15, center=False)
        coeficientes_c_dimK2 = Tex("¿",
                            r"$c_i$",
                            "?")
        group_dimK2_ntuplas = VGroup(base_beta_dimK2, #0
                                    base_beta_dimK2_propiedades, #1
                                    combination_dimK2, #2
                                    coeficientes_c_dimK2 #3
                                ).scale(0.4).shift(4*LEFT+UP)
        group_dimK2_ntuplas.arrange(2.5*DOWN, center=False, aligned_edge=LEFT)
        #Alineacion de igualdades
        group_dimK2_ntuplas[0][:].align_to(group_dimK1_ntuplas[0][:],UP).align_to(group[0][:],LEFT)
        group_dimK2_ntuplas[2][:].align_to(group_dimK1_ntuplas[2][:],UP).align_to(group[2][:],LEFT)

        #----------------------------------- SISTEMA DE ECUACIONES
        #Sistema de ecuaciones
        sis_row1 = MathTex(r"v_1", #0
                            "=", #1
                            "c_1", #2
                            "v_{1}^{1}", #3
                            "+", #4
                            r"\cdots", #5
                            "+", #6
                            "c_{k}", #7
                            "v_{1}^{k}", #8
                            "+", #9
                            "c_{k+1}", #10
                            "v_{1}^{k+1}", #11
                            "+", #12
                            "c_{k+2}", #13
                            "v_{1}^{k+2}" #14
                            )
        sis_row2 = MathTex(r"v_2", "=","c_1","v_{2}^{1}","+",r"\cdots", "+", "c_{k}","v_{2}^{k}","+", "c_{k+1}","v_{2}^{k+1}",\
                            "+","c_{k+2}","v_{2}^{k+2}")

        sis_row3 = MathTex(r"v_1", r" \vdots ","c_1","v_{1}^{1}","+",r"\cdots", "+", "c_{k}","v_{1}^{k}","+", "c_{k+1}","v_{1}^{k+1}",\
                            "+","c_{k+2}","v_{1}^{k+2}").set_opacity(0)
        sis_row3[1].set_opacity(1)

        sis_row4 = MathTex(r"v_{k}", "=","c_1","v_{k}^{1}","+",r"\cdots", "+", "c_{k}","v_{k}^{k}","+", "c_{k+1}","v_{k}^{k+1}",\
                            "+","c_{k+2}","v_{k}^{k+2}")
        sis_row5 = MathTex(r"v_{k+1}", "=","c_1","v_{k+1}^{1}","+",r"\cdots", "+", "c_{k}","v_{k+1}^{k}","+", "c_{k+1}","v_{k+1}^{k+1}",\
                            "+","c_{k+2}","v_{k+1}^{k+2}")
        sis_row6 = MathTex(r"v_{k+2}", "=","c_1","v_{k+2}^{1}","+",r"\cdots", "+", "c_{k}","v_{k+2}^{k}","+", "c_{k+1}","v_{k+2}^{k+1}",\
                            "+","c_{k+2}","v_{k+2}^{k+2}")
        sist_group = VGroup(sis_row1, sis_row2, sis_row3, sis_row4, sis_row5, sis_row6).scale(0.5).move_to(3.5*RIGHT+3*UP)
        sist_group.arrange(0.7*DOWN, center=False, aligned_edge=LEFT)

        #Color para los coeficientes y las entradas del vector
        for line in [sis_row1, sis_row2, sis_row4, sis_row5, sis_row6]:
            line[0].set_color(AZUL)
            for index in [2,7,10,13]:
                line[index].set_color(ROJO)

        align_t12(text1 = sist_group[3], text2 = sist_group[4], char = "=", buff = -0.7)
        align_t12(text1 = sist_group[4], text2 = sist_group[5], char = "=", buff = -0.7)
        sist_group[4]

        list_braces = []
        list_braces.append(Brace(sist_group[:4], LEFT))

        for i in range(5, 7):
            list_braces.append(Brace(sist_group[:i], LEFT))
        
        #----------------------------------Animaciones
        self.play(
            FadeIn(group[:]),
            run_time = 3
        )
        self.play(
            FadeOut(group[1]),
            FadeOut(group[3]),
            run_time = 3
        )
        #Transformación vector -> ntuplas
        self.play(
            ReplacementTransform(group[0][:], group_dimK_ntuplas[0][:]), #Base de dimensión K
            ReplacementTransform(group[2][:], group_dimK_ntuplas[2][:]), #Combinación, dimV = k
            #Sistema de ecuaciones
            FadeIn(sist_group[0][:9]),
            FadeIn(sist_group[1][:9]),
            FadeIn(sist_group[2][:9]),
            FadeIn(sist_group[3][:9]),
            FadeIn(list_braces[0]),
            run_time = 4
        )
        #----------------------------------Aumento de la dimensión
        # k + 1
        # Base y combinación
        self.play(
            ReplacementTransform(group_dimK_ntuplas[0][:6], group_dimK1_ntuplas[0][:6]), #Base de dimensión K
            ReplacementTransform(group_dimK_ntuplas[0][6:], group_dimK1_ntuplas[0][8:]), #Base de dimensión K
            ReplacementTransform(group_dimK_ntuplas[2][:], group_dimK1_ntuplas[2][:9]), #Combinación, dimV = k
            run_time = 4
        )
        self.play(
            FadeIn(group_dimK1_ntuplas[0][6:8]),
            FadeIn(group_dimK1_ntuplas[2][9:]),
            # Sistema de ecuaciones
            FadeIn(sist_group[0][9:12]),
            FadeIn(sist_group[1][9:12]),
            FadeIn(sist_group[2][9:12]),
            FadeIn(sist_group[3][9:12]),
            FadeIn(sist_group[4][:12]),
            ReplacementTransform(list_braces[0], list_braces[1]),
            run_time = 3
        )
        # k + 2
        # Base y combinación
        self.play(
            ReplacementTransform(group_dimK1_ntuplas[0][:8], group_dimK2_ntuplas[0][:8]),
            ReplacementTransform(group_dimK1_ntuplas[0][8:], group_dimK2_ntuplas[0][10:]),
            ReplacementTransform(group_dimK1_ntuplas[2][:], group_dimK2_ntuplas[2][:12]),
            run_time = 4
        )
        self.play(
            FadeIn(group_dimK2_ntuplas[0][8:10]),
            FadeIn(group_dimK2_ntuplas[2][12:]),
            # Sistema de ecuaciones
            FadeIn(sist_group[0][12:]),
            FadeIn(sist_group[1][12:]),
            FadeIn(sist_group[2][12:]),
            FadeIn(sist_group[3][12:]),
            FadeIn(sist_group[4][12:]),
            FadeIn(sist_group[5][:]),
            ReplacementTransform(list_braces[1], list_braces[2]),
            run_time = 3
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 1)
    def construct(self):
        self.parte_3()
        
