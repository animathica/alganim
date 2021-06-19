from manimlib.imports import *


#####################################################################################
######################  Ortogonalización y ortonormalización  #######################
#####################################################################################

#####################################################################################
#################################  Primera escena  ##################################
###############################  versión manimlib  ##################################
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

# Clase de flechas con guiones.
# Sólo es modificación de clase de flecha normal, heredada de "DashedLine", en vez de "Line".
class DashedArrow(DashedLine):
    CONFIG = {
        "stroke_width": 6,
        "buff": MED_SMALL_BUFF,
        "max_tip_length_to_length_ratio": 0.25,
        "max_stroke_width_to_length_ratio": 5,
        "preserve_tip_size_when_scaling": True,
    }

    def __init__(self, *args, **kwargs):
        DashedLine.__init__(self, *args, **kwargs)
        # TODO, should this be affected when
        # Arrow.set_stroke is called?
        self.initial_stroke_width = self.stroke_width
        self.add_tip()
        self.set_stroke_width_from_length()

    def scale(self, factor, **kwargs):
        if self.get_length() == 0:
            return self

        has_tip = self.has_tip()
        has_start_tip = self.has_start_tip()
        if has_tip or has_start_tip:
            old_tips = self.pop_tips()

        VMobject.scale(self, factor, **kwargs)
        self.set_stroke_width_from_length()

        # So horribly confusing, must redo
        if has_tip:
            self.add_tip()
            old_tips[0].points[:, :] = self.tip.points
            self.remove(self.tip)
            self.tip = old_tips[0]
            self.add(self.tip)
        if has_start_tip:
            self.add_tip(at_start=True)
            old_tips[1].points[:, :] = self.start_tip.points
            self.remove(self.start_tip)
            self.start_tip = old_tips[1]
            self.add(self.start_tip)
        return self

    def get_normal_vector(self):
        p0, p1, p2 = self.tip.get_start_anchors()[:3]
        return normalize(np.cross(p2 - p1, p1 - p0))

    def reset_normal_vector(self):
        self.normal_vector = self.get_normal_vector()
        return self

    def get_default_tip_length(self):
        max_ratio = self.max_tip_length_to_length_ratio
        return min(
            self.tip_length,
            max_ratio * self.get_length(),
        )

    def set_stroke_width_from_length(self):
        max_ratio = self.max_stroke_width_to_length_ratio
        self.set_stroke(
            width=min(
                self.initial_stroke_width,
                max_ratio * self.get_length(),
            ),
            family=False,
        )
        return self

    # TODO, should this be the default for everything?
    def copy(self):
        return self.deepcopy()

class Escena1(ThreeDScene):

    def construct(self):

        # Texto de prodcto escalar y su rectángulo.
        Text1 = TextMobject('''$ \\langle \\vec{a},\\vec{b} \\rangle \\ \\ \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT)
        Text1[0][-2].set_color(BLACK)
        Text1c = TextMobject('''$ \\langle \\vec{a},\\vec{b} \\rangle \\ \\ \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT)
        Text1.bg = SurroundingRectangle(Text1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text1.group = VGroup(Text1.bg,Text1)
        Text1_1 = VGroup()
        for i in range(0,7):
            Text1_1.add(Text1[0][i])

        # Texto de proyección y su rectángulo.#Text2 = TextMobject('''$ \\frac{ \\langle \\vec{a} , \\vec{b} \\rangle} { \\norm{ \\vec{b} } ^2} \\vec{b} \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT).scale(1.2)
        Text2 = TextMobject('''$ \\frac{ \\langle \\vec{a} , \\vec{b} \\rangle} { \\norm{ \\vec{b}} } \\hat{b} \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT).scale(1.2)
        Text2.set_color(AMARILLO)
        Text2.bg = SurroundingRectangle(Text2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text2.group = VGroup(Text2.bg,Text2)
        Text2_1 = VGroup()
        for i in range(0,9):
            Text2_1.add(Text2[0][i])
        Text2_2 = VGroup()
        for i in range(7,14):
            Text2_2.add(Text2[0][i])

        # Texto de conjunto inicial y su rectángulo.
        Cto = TextMobject('''$ I = \\{ \\vec{a}, \\vec{b} \\} $''').move_to(3*DOWN + 4*LEFT)
        for i in range(3,5):
            Cto[0][i].set_color(AZUL)
        for i in range(6,8):
            Cto[0][i].set_color(ROJO)
        Cto.bg = SurroundingRectangle(Cto,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Cto.group = VGroup(Cto.bg,Cto)

        # Texto de conjunto ortogonal y su rectángulo, con las variaciones usadas.
        CtoO = TextMobject('''$ \\Gamma_2 = \\{ \\vec{b} \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            CtoO[0][i].set_color(BLACK)
        CtoO.bg = SurroundingRectangle(CtoO,color=WHITE,fill_color=BLACK,fill_opacity=1)
        CtoO.group = VGroup(CtoO.bg,CtoO)
        CtoO_1_1 = TextMobject('''$ \\Gamma_2 = \\{ \\vec{b} \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            CtoO_1_1[0][i].set_color(ROJO)
        CtoO_2 = TextMobject('''$ \\Gamma_2 = \\{ \\vec{b} , \\vec{a}' \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            CtoO_2[0][i].set_color(ROJO)
        for i in range(6,10):
            CtoO_2[0][i].set_color(BLACK)
        CtoO_2_1 = TextMobject('''$ \\Gamma_2 = \\{ \\vec{b} , \\vec{a}' \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            CtoO_2_1[0][i].set_color(ROJO)
        for i in range(7,10):
            CtoO_2_1[0][i].set_color(VERDE)
        CtoO_3 = VGroup(CtoO_2[0][6],CtoO_2[0][7],CtoO_2[0][8])
        CtoO_2.bg = SurroundingRectangle(CtoO_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        CtoOF = VGroup(CtoO_2.bg, CtoO_2_1)

        # Texto para conjunto ortonormal y su  recángulo, con las variaciones usadas.
        CtoON = TextMobject(''' $ N = \{ \hat{b} \} $ ''').move_to(2.5*DOWN + 3.5*RIGHT)
        CtoON.bg = SurroundingRectangle(CtoON,color=WHITE,fill_color=BLACK,fill_opacity=1)
        CtoON.group = VGroup(CtoON.bg,CtoON)
        for i in range(3,5):
            CtoON[0][i].set_color(BLACK)
        CtoON_1 = TextMobject(''' $ N = \{ \hat{b} \} $ ''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(3,5):
            CtoON_1[0][i].set_color(ROJO)
        CtoON_2 = TextMobject(''' $ N = \{ \hat{b},\hat{a}' \} $ ''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(3,5):
            CtoON_2[0][i].set_color(ROJO)
        for i in range(6,9):
            CtoON_2[0][i].set_color(VERDE)
        CtoON_2.bg = SurroundingRectangle(CtoON_2,color=WHITE,fill_color=BLACK,fill_opacity=1)

        # Texto para <a,b> = _<b,a> y su rectángulo.
        TCon = TextMobject('''$ \\langle \\vec{a}, \\vec{b} \\rangle \\neq 0 $''').move_to(0.5*UP + 4*LEFT)
        TCon.bg = SurroundingRectangle(TCon, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        TCon.group = VGroup(TCon.bg,TCon)
        TCon_1 = TextMobject('''$ \\langle \\vec{b}, \\vec{a} \\rangle = \\overline{ \\langle \\vec{a}, \\vec{b} \\rangle } $''').move_to(0.5*DOWN + 4*LEFT)
        TCon_1.bg = SurroundingRectangle(TCon_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        TCon_1.group = VGroup(TCon_1.bg,TCon_1)
        TCon_2 = TextMobject('''$ \\Rightarrow \\langle \\vec{b}, \\vec{a} \\rangle \\neq 0 $''').move_to(1.5*DOWN + 4*LEFT)
        TCon_2.bg = SurroundingRectangle(TCon_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        TCon_2.group = VGroup(TCon_2.bg,TCon_2)
        Tsilo = VGroup(TCon,TCon_1,TCon_2)
        Tsilo.bg = SurroundingRectangle(VGroup(TCon,TCon_2,TCon_1), color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Tsilo.group = VGroup(Tsilo.bg,Tsilo)

        # Texto para proyección de b sobre a.
        Text5 = TextMobject('''$ \\frac{ \\langle \\vec{b} , \\vec{a} \\rangle} { \\norm{ \\vec{a}} } \\hat{a} \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT).scale(1.2)
        Text5[0][0:14].set_color(AMARILLO)
        Text5.bg = SurroundingRectangle(Text5, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text5.group = VGroup(Text5.bg,Text5)

        # Texto para segundo conjunto ortonormal, su rectángulo, y las variaciones usadas.
        Text6 = TextMobject('''$ \\Gamma_1 = \{ \\vec{a} \} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            Text6[0][i].set_color(BLACK)
        Text6.bg = SurroundingRectangle(Text6, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text6.group = VGroup(Text6.bg,Text6)
        Text6_1 = TextMobject('''$ \\Gamma_1 = \{ \\vec{a} \} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            Text6_1[0][i].set_color(AZUL)
        Text6_2 = TextMobject('''$ \\Gamma_1 = \{ \\vec{a}, \\vec{b}' \} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            Text6_2[0][i].set_color(AZUL)
        for i in range(7,10):
            Text6_2[0][i].set_color(VERDE)
        Text6_2.bg = SurroundingRectangle(Text6_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)

        # Textos para los generados y sus rectángulos.
        Text9 = TextMobject('''$ \\langle I \\rangle $''').move_to(1.5*DOWN + 4*LEFT).set_color(MAGENTA_CLARO)
        Text9.bg = SurroundingRectangle(Text9, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text9.group = VGroup(Text9.bg,Text9)
        Text9_1 = TextMobject('''$ \\langle I \\rangle = \\langle \\Gamma_1 \\rangle $''').move_to(1.5*DOWN + 4*LEFT)
        Text9_1[0][0:3].set_color(MAGENTA_CLARO)
        Text9_1[0][4:8].set_color(TEAL_A)
        Text9_1.bg = SurroundingRectangle(Text9_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text9_1.group = VGroup(Text9_1.bg,Text9_1)
        Text9_2 = TextMobject('''$ \\langle I \\rangle = \\langle \\Gamma_1 \\rangle = \\langle \\Gamma_2 \\rangle $''').move_to(1.5*DOWN + 4*LEFT)
        Text9_2[0][0:3].set_color(MAGENTA_CLARO)
        Text9_2[0][4:8].set_color(TEAL_A)
        Text9_2[0][9:13].set_color(MOSTAZA_CLARO)
        Text9_2.bg = SurroundingRectangle(Text9_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text9_2.group = VGroup(Text9_2.bg,Text9_2)
        Text9_3 = TextMobject('''$ \\langle I \\rangle = \\langle N \\rangle $''').move_to(1.5*DOWN + 4*LEFT)
        Text9_3[0][0:3].set_color(MAGENTA_CLARO)
        Text9_3[0][4:7].set_color(AZUL_CLARO)
        Text9_3.bg = SurroundingRectangle(Text9_3, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text9_3.group = VGroup(Text9_3.bg, Text9_3)

        # Texto para mostrar operaciones de espacio.
        Text10 = TextMobject('''$ \\vec{u} + \\vec{v} $''').move_to(UP+4*LEFT)
        Text10_1 = TextMobject('''$ c \\vec{u} $''').move_to(4*LEFT)
        Text10_2 = TextMobject('''$ \\langle \\vec{u} , \\vec{v} \\rangle $''').move_to(DOWN+4*LEFT)
        Text10_group = VGroup(Text10,Text10_1,Text10_2)
        Text10.bg = SurroundingRectangle(Text10_group, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text10.group = VGroup(Text10.bg,Text10_group)

        grid = NumberPlane()

        # Coordenadas de vector A
        a_1 = 1
        a_2 = 2
        
        # Coordenadas de vector B
        b_1 = 4
        b_2 = 1

        # Vectores A y B, con sus etiquetas.
        VecA = Arrow((0, 0, 0), a_1 * RIGHT + a_2*UP, buff=0,color=AZUL)
        VecB = Arrow((0, 0, 0),b_1 * RIGHT + b_2*UP, buff=0,color=ROJO)
        VecALab=TexMobject("\\vec{a}").move_to(VecA.get_end()+0.4*RIGHT+0.2*UP).set_color(AZUL)
        VecBLab=TexMobject("\\vec{b}").move_to(VecB.get_end()+0.5*RIGHT).set_color(ROJO)

        # Copia de VecB.
        VecBc = Arrow((0, 0, 0),b_1 * RIGHT + b_2*UP, buff=0,color=ROJO)
        VecBcLab=TexMobject("\\vec{b}").move_to(VecBc.get_end()+0.5*RIGHT).set_color(ROJO)

        # Texto para los vectores, con su rectángulo correspondiente.
        Text_B = TextMobject('''$\\vec{b} = (5,2)$''').move_to(3*DOWN + 4*LEFT)
        Text_A = TextMobject('''$\\vec{a} = (1,3)$''').next_to(Text_B, UP)
        Text_Vec = VGroup(Text_B,Text_A)
        VecBox = SurroundingRectangle(Text_Vec,color=WHITE,fill_color=BLACK,fill_opacity=1)
        VecBox.group = VGroup(VecBox,Text_Vec)

        # Función para calcular intersección entre rectas.
        def line_intersection(line1, line2):
            xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
            ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

            def det(a, b):
                return a[0] * b[1] - a[1] * b[0]

            div = det(xdiff, ydiff)

            d = (det(*line1), det(*line2))
            x = det(d, xdiff) / div
            y = det(d, ydiff) / div
            return([x, y])

        # Función para la luz usada para la proyección.
        # (x1,y1) es el vector proyectado, (x2,y2) es sobre el que se proyecta.
        # n es la cantidad de líneas que se generan para colorear la zona iluminada.
        def light(x1,y1,x2,y2,n = 10):
            # Coordenadas de un vector ortogonal a (x2,y2)
            x2o = -y2
            y2o = x2
            # Lista donde se guarda cada "rayo" de luz.
            rays = []
            # Lista donde se guardan las coordenadas de cada rayo:
            rayc = []
            # Se calcula la proyección.
            p1 = ((x1*x2 + y1*y2)/(x2**2 + y2**2)) * x2
            p2 = ((x1*x2 + y1*y2)/(x2**2 + y2**2)) * y2
            proy = [p1,p2]
            norma_proy = np.sqrt(p1**2 + p2**2)
            # Se generan las coordenadas de cada rayo y se agregan a la lista.
            for i in range(0,n+1):
                r1 = 0 + i*(x2/n)
                r2 = 0 + i*(y2/n)
                nr = np.sqrt(r1**2 + r2**2)
                if nr < norma_proy:
                    inter = line_intersection(((0,0),(x1,y1)),((r1,r2),(r1 + x2o,r2 + y2o)))
                    rayc.append([inter[0],inter[1]])                
                else:
                    rayc.append([r1,r2])
            # Se genera cada rayo.
            for i in rayc:
                rayo = DashedLine( [i[0]+x2o,i[1]+y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(AMARILLO)
                rays.append(rayo)
            # Se hace un VGroup con los rayos.
            grupo = VGroup()
            for i in rays:
                grupo.add(i)
            return(grupo)

        # Objeto usado para la luz.
        luz = light(a_1,a_2,b_1,b_2,25)

        # Pared para primera proyección.
        pared = Line((-10*b_1,-10*b_2,0),(10*b_1,10*b_2,0), color = GRIS)

        # Flecha de la proyección de a sobre b.
        p1 = ((a_1*b_1 + a_2*b_2)/(b_1**2 + b_2**2)) * b_1
        p2 = ((a_1*b_1 + a_2*b_2)/(b_1**2 + b_2**2)) * b_2
        VecP = Arrow((0, 0, 0),(p1,p2,0), color = AMARILLO, buff = 0)
        VecPnaranja = Arrow((0, 0, 0),(p1,p2,0), color = AMARILLO, buff = 0)
        VecPc = VecP.copy()
                
        # Copia de proyección de a sobre b usada para la resta.
        VecPC = Arrow((a_1,a_2,0),(a_1-p1,a_2-p2,0), color = AMARILLO, buff = 0)

        # Texto para penúltima proyección.
        Text13 = TextMobject('''$ \\frac{ \\langle \\vec{a} , \\vec{b} \\rangle} { \\norm{ \\vec{b}} } \\hat{b} $''').move_to(VecPnaranja.get_end()+0.9*DOWN).set_color(AMARILLO)
        Text13_2 = TextMobject('''$ - \\frac{ \\langle \\vec{a} , \\vec{b} \\rangle} { \\norm{ \\vec{b}} } \\hat{b} $''').move_to(VecPC.get_end()+0.9*UP).set_color(AMARILLO)

        # Texto para última proyección.
        Text12 = TextMobject('''$ \\frac{ \\langle \\vec{a} , \\hat{b} \\rangle} { \\norm{ \\hat{b}} } \\hat{b} $''').move_to(1*LEFT).set_color(AMARILLO)
        Text12_1 = TextMobject('''$ - \\langle \\vec{a} , \\hat{b} \\rangle \\hat{b} $''').move_to(1*LEFT).set_color(AMARILLO)
        Text12_1[0][0].set_color(BLACK)
        Text12_3 = TextMobject('''$ - \\langle \\vec{a} , \\hat{b} \\rangle  \\hat{b} $''').move_to(VecPC.get_end()+0.6*UP).set_color(AMARILLO)
        
        # Texto mostrado junto con el primer generado.
        Text14 = TextMobject('''$ \\{ \\vec{a} + c_2 \\vec{b} : c_2 \\in \\mathbb{R}^2 \\} $''').move_to(1.5*DOWN + 4*LEFT)
        Text14[0][1:8].set_color(MAGENTA_CLARO)
        Text14.bg = SurroundingRectangle(Text14,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text14.group = VGroup(Text14.bg, Text14)
        Text14_2 = TextMobject('''$ \\{ c_1 \\vec{a} + c_2 \\vec{b} : c_1, c_2 \\in \\mathbb{R}^2 \\} $''').move_to(1.5*DOWN + 4*LEFT)
        Text14_2[0][1:10].set_color(MAGENTA_CLARO)
        Text14_2.bg = SurroundingRectangle(Text14_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text14_2.group = VGroup(Text14_2.bg, Text14_2)

        # Texto para explicar vectores normalizados.
        Text15_1 = TextMobject('''$ \\vec{b} \\neq \\vec{0} $''').move_to(0.5*UP + 4*LEFT)
        Text15_2 = TextMobject('''$ \\hat{v} := \\frac{\\vec{v}}{\\norm{\\vec{v}}} $''').move_to(0.5*DOWN + 4*LEFT)
        Text15_3 = TextMobject('''$ \\Rightarrow \\frac{\\langle \\vec{u}, \\vec{v} \\rangle}{\\langle \\vec{v}, 
        \\vec{v} \\rangle} \\vec{v} $''').move_to(1.5*DOWN + 4*LEFT)
        Text15_4 = TextMobject('''$ \\Rightarrow \\frac{\\langle \\vec{u}, \\vec{v} \\rangle}{\\norm{\\vec{v}}^2} = 
        \\langle \\vec{u}, \\frac{\\vec{v}}{\\norm{\\vec{v}}} \\rangle \\frac{\\vec{v}}{\\norm{\\vec{v}}} $''').move_to(1.5*DOWN + 4*LEFT)
        Text15_5 = TextMobject('''$ \\Rightarrow \\frac{\\langle \\vec{u}, \\vec{v} \\rangle}{\\norm{\\vec{v}}^2} =
        \\langle \\vec{u}, \\hat{v} \\rangle \\hat{v} $ ''').move_to(1.5*DOWN + 4*LEFT)
        Text15bg = SurroundingRectangle(VGroup(Text15_1,Text15_2,Text15_4),color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text15group = VGroup(Text15bg,Text15_1,Text15_2,Text15_5)

        # Vector resultante de la resta y su etiqueta.
        VecR = Arrow((0, 0, 0),(a_1-p1,a_2-p2,0), color = VERDE, buff = 0)
        VecRLab = TextMobject('''$ \\vec{a}' $''').move_to(VecR.get_end()+0.5*LEFT).set_color(VERDE)
        VecRc = Arrow((0, 0, 0),(a_1-p1,a_2-p2,0), color = VERDE, buff = 0)
        VecRcLab = TextMobject('''$ \\vec{a}' $''').move_to(VecR.get_end()+0.5*LEFT).set_color(VERDE)

        # Función para luz de segunda proyección.
        def light2(x1,y1,x2,y2,n = 10):
            # Coordenadas de un vector ortogonal a (x2,y2)
            x2o = y2
            y2o = -x2
            # Lista donde se guarda cada "rayo" de luz.
            rays = []
            # Lista donde se guardan las coordenadas de cada rayo:
            rayc = []
            # Se calcula la proyección.
            p1 = ((x1*x2 + y1*y2)/(x2**2 + y2**2)) * x2
            p2 = ((x1*x2 + y1*y2)/(x2**2 + y2**2)) * y2
            proy = [p1,p2]
            norma_proy = np.sqrt(p1**2 + p2**2)
            # Se generan las coordenadas de cada rayo y se agregan a la lista.
            for i in range(0,n+1):
                r1 = 0 + i*((x2/n)*1.3)
                r2 = 0 + i*((y2/n)*1.3)
                nr = np.sqrt(r1**2 + r2**2)
                if nr < norma_proy:
                    inter = line_intersection(((0,0),(x1,y1)),((r1,r2),(r1 + x2o,r2 + y2o)))
                    rayc.append([inter[0],inter[1]])                
                else:
                    rayc.append([r1,r2])
            # Se genera cada rayo.
            for i in rayc:
                rayo = DashedLine( [i[0]+10*x2o,i[1]+10*y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(AMARILLO)
                rays.append(rayo)
            # Se hace un VGroup con los rayos.
            grupo = VGroup()
            for i in rays:
                grupo.add(i)
            return(grupo)

        # Objeto usado para segunda luz.
        luz2 = light2(b_1,b_2,a_1,a_2,25)

        # Pared para segunda proyección.
        pared2 = Line((-10*a_1,-10*a_2,0),(10*a_1,10*a_2,0), color = GRIS)

        # Flecha de la proyección de b sobre a.
        p1_1 = ((b_1*a_1 + b_2*a_2)/(a_1**2 + a_2**2)) * a_1
        p2_1 = ((b_1*a_1 + b_2*a_2)/(a_1**2 + a_2**2)) * a_2

        # Flecha para segundo uso de proyección de b sobre a.
        VecP_2 = Arrow((0, 0, 0),(p1_1,p2_1,0), color = AMARILLO, buff = 0)

        # Copia de proyección de b sobre a usada para la resta.
        VecPC_1 = Arrow((b_1,b_2,0),(b_1-p1_1,b_2-p2_1,0), color = AMARILLO, buff = 0)

        # Vector resultante de la segunda resta y su etiqueta.
        VecR_1 = Arrow((0, 0, 0),(b_1-p1_1,b_2-p2_1,0), color = VERDE, buff = 0)
        VecRLab_1 = TextMobject('''$ \\vec{b}' $''').move_to(VecR_1.get_end()+0.3*DOWN+0.5*LEFT).set_color(VERDE)

        # Eje para normalizar vector.
        Eje = DashedLine((0-5*b_1, 0-5*b_2, 0),(5*b_1,5*b_2,0), color = MAGENTA, buff = 0)

        # Se normaliza vector B.
        # Norma de vector B.
        NorB = np.sqrt(b_1**2 + b_2**2)
        # Coordenadas de B normalizado.
        nb_1 = b_1/NorB
        nb_2 = b_2/NorB

        # Vector B' normalizado y su etiqueta.
        VecBN = Arrow((0,0,0),(nb_1,nb_2,0), color = ROJO, buff = 0)
        VecBNLab = TextMobject(''' $ \\hat{b} $ ''').move_to(VecBN.get_end()+0.5*UP).set_color(ROJO)

        # Copias de ector VecBN y su etiqueta.
        VecBNc = Arrow((0,0,0),(nb_1,nb_2,0), color = ROJO, buff = 0)
        VecBNcLab = TextMobject(''' $ \\hat{b} $ ''').move_to(VecBN.get_end()+0.5*UP).set_color(ROJO)

        # Ejes para mostrar independencia lineal.
        Eje1 = DashedLine((0-5*b_1, 0-5*b_2, 0),(5*b_1,5*b_2,0), color = MAGENTA, buff = 0)
        Eje2 = DashedLine((0-5*a_1, 0-5*a_2, 0),(5*a_1,5*a_2,0), color = MAGENTA, buff = 0)
        Ejes = VGroup(Eje1,Eje2)

        #Se normaliza vector B'.
        # Norma de vector B'.
        NorBP = np.sqrt((a_1-p1)**2 + (a_2-p2)**2)
        # Coordenadas de B' normalizado
        nbp_1 = (a_1-p1)/NorBP
        nbp_2 = (a_2-p2)/NorBP
        
        #Se normaliza vector VecR_1.
        # Norma de vector VecR_1.
        NorVR1 = np.sqrt((b_1-p1_1)**2 + (b_2-p2_1)**2)
        # Coordenadas de VecRN_1.
        nvr_2 = (b_1-p1_1)/NorVR1
        nvr_1 = (b_2-p2_1)/NorVR1   

        # Se normliza vector VecR.
        # Norma de VecR.
        NorVR = np.sqrt((a_1-p1)**2 + (a_2-p2)**2)   
        # Coordenadas de VecRN.
        nr_1 = (a_1-p1)/NorVR
        nr_2 = (a_2-p2)/NorVR

        # Vector B' normalizado y su etiqueta.
        VecBPN = Arrow((0,0,0),(nbp_1,nbp_2,0), color = VERDE, buff = 0)
        VecBPNLab = TextMobject(''' $ \\hat{a}' $ ''').move_to(VecBPN.get_end()+0.5*UP).set_color(VERDE)

        # Vector VecR_1 normalizado y su etiqueta.
        VecRN_1 = Arrow((0,0,0),(nvr_2,nvr_1,0), color = VERDE, buff = 0)
        #VecRN_1Lab = TextMobject(''' $ \\hat{b}' $ ''').move_to(VecRN_1.get_end()+0.5*UP).set_color(VERDE)
        VecRN_1Lab = TextMobject(''' $ \\hat{b}' $ ''').move_to(VecRN_1.get_end()+0.5*DOWN).set_color(VERDE)

        # Vector VecR normalizado y su etiqueta.
        VecRN = Arrow((0,0,0),(nr_1,nr_2,0), color = VERDE, buff = 0)
        VecRNLab = TextMobject(''' $ \\hat{a}' $ ''').move_to(VecRN.get_end()+0.5*LEFT).set_color(VERDE)

        # Función para primer generado.
        # Aquí ya se encuentran los self.play.
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
            self.play(ShowCreation(VGroup(Vec1c,Vec2c)))
            # Vector resultante de la combinación lineal.
            VecRCL = DashedArrow((0,0,0), Vec2c.get_end(), buff=0, color = MAGENTA).set_fill(opacity=1)
            self.play(ShowCreation(VecRCL))
            # ValueTrackers
            vt1 = ValueTracker(0)
            self.play(FadeOut(Vec1c))
            # Primera función para cambios de Vec2.
            def upd_for_vec2_1(obj):
                t = vt1.get_value()
                NewVec2 = Arrow((0,0,0),(B1+t*B1,B2+t*B2,0),buff=0, color = Vec2.get_color())
                obj.become(NewVec2)
            # Primera función para cambios de Vec2c.
            def upd_for_vec2c_1(obj):
                t = vt1.get_value()
                NewVec2c = DashedArrow(Vec1.get_end(),Vec1.get_end()+(B1+t*B1,B2+t*B2,0), buff=0, color = Vec2.get_color()).set_fill(opacity=0.5)
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
                new_linea = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP,Vec1.get_end()+(B1+t*B1,B2+t*B2,0), color = MAGENTA).set_fill(opacity=0.5)
                obj.become(new_linea)
            self.play(ShowCreation(Linea1),ShowCreation(Linea2))
            self.bring_to_back(Linea1)
            self.bring_to_back(Linea2)
            Vec2.add_updater(upd_for_vec2_1)
            Vec2c.add_updater(upd_for_vec2c_1)
            VecRCL.add_updater(upd_for_vecrcl_1)
            Linea1.add_updater(upd_for_linea)
            Linea2.add_updater(upd_for_linea)
            self.play(Write(Text14.group))
            self.add_foreground_mobjects(Text14.group)
            self.play(vt1.set_value,7.5,run_time=1.3)
            Linea1.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            self.play(vt1.set_value,-9,run_time=1.3)
            Linea2.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            self.remove_foreground_mobjects(Text14.group)
            Vec2.remove_updater(upd_for_vec2_1)
            Vec2c.remove_updater(upd_for_vec2c_1)
            VecRCL.remove_updater(upd_for_vecrcl_1)
            self.wait(0.65)
            self.play(ShowCreation(Vec1c))
            self.play(FadeOut(Vec2c))
            # Primera función para cambios de Vec1.
            def upd_for_vec1_1(obj):
                t = vt1.get_value()
                NewVec1 = Arrow((0,0,0),(A1+t*A1,A2+t*A2,0),buff=0, color = Vec1.get_color())
                obj.become(NewVec1)
            # Primera función para cambios de Vec1c.
            def upd_for_vec1c_1(obj):
                t = vt1.get_value()
                NewVec1c = DashedArrow(Vec2.get_end(),Vec2.get_end()+(A1+t*A1,A2+t*A2,0), buff=0, color = Vec1.get_color()).set_fill(opacity=0.5)
                obj.become(NewVec1c)
            # Segunda función para cambios de VecRCL.
            def upd_for_vecrcl_2(obj):
                t = vt1.get_value()
                NewVecRCL = DashedArrow((0,0,0),Vec2.get_end()+(A1+t*A1,A2+t*A2,0), buff=0, color = MAGENTA).set_fill(opacity=1)
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
                vert3 = Linea2.get_end()+(t*A1,t*A2,0)
                vert4 = Linea1.get_end()+(t*A1,t*A2,0)
                New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA_CLARO, opacity = 1)
                obj.become(New_plano)
                self.bring_to_back(obj)
            Vec1.add_updater(upd_for_vec1_1)
            Vec1c.add_updater(upd_for_vec1c_1)
            VecRCL.add_updater(upd_for_vecrcl_2)
            Plano1.add_updater(upd_for_plano)
            self.play(ReplacementTransform(Text14.group,Text14_2.group))
            self.add_foreground_mobjects(Text14_2.group)
            self.play(ShowCreation(Plano1), run_time=0.05)
            self.play(ShowCreation(Plano2), run_time = 0.05)
            self.play(FadeOut(VGroup(Linea1,Linea2)), run_time=0.05)
            self.add_foreground_mobject(Cto.group)
            self.play(vt1.set_value,3,run_time=1.5,rate_func=linear)
            Plano1.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0,rate_func=linear)
            Plano2.add_updater(upd_for_plano)
            self.play(vt1.set_value,-5,run_time=1.5,rate_func=linear)
            Plano2.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0,rate_func=linear)
            Vec1.remove_updater(upd_for_vec1_1)
            Vec1c.remove_updater(upd_for_vec1c_1)
            VecRCL.remove_updater(upd_for_vecrcl_2)
            self.wait(0.65)
            self.play(FadeOut(Vec1c))
            #self.play(Write(Text9.group))
            self.remove_foreground_mobjects(Text14_2.group)
            self.play(ReplacementTransform(Text14_2.group,Text9.group))
            self.add_foreground_mobject(Text9.group)
            self.wait(0.65)
            Punto = Dot(radius=0.01, color = MAGENTA).set_fill(MAGENTA)
            self.add_foreground_mobject(VecRCL)
            self.play(FadeOut(VGroup(Plano1,Plano2),FadeOut(Text9.group)))
            self.remove_foreground_mobject(Text9.group)
            self.remove_foreground_mobject(VecRCL)
            self.play(FadeOut(Text9.group))
            self.play(FadeOut(VGroup(VecRCL,Punto)))
            self.play(Write(VGroup(Lab1,Lab2)))

        # Función para mostrar el segundo generado.
        # Aquí ya se encuentran los self.play.
        def gen2(Vec1,Vec2,Lab1,Lab2):
            #self.add_foreground_mobject(Text9_1.group)
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
            self.play(ShowCreation(VGroup(Vec1c,Vec2c)))
            # Vector resultante de la combinación lineal.
            VecRCL = DashedArrow((0,0,0), Vec2c.get_end(), buff=0, color = MOSTAZA_OSCURO).set_fill(opacity=1)
            self.play(ShowCreation(VecRCL))
            # ValueTrackers
            vt1 = ValueTracker(0)
            self.play(FadeOut(Vec1c),runtime=0.2)
            # Primera función para cambios de Vec2.
            def upd_for_vec2_1(obj):
                t = vt1.get_value()
                NewVec2 = Arrow((0,0,0),(B1+t*B1,B2+t*B2,0),buff=0, color = Vec2.get_color())
                obj.become(NewVec2)
            # Primera función para cambios de Vec2c.
            def upd_for_vec2c_1(obj):
                t = vt1.get_value()
                NewVec2c = DashedArrow(Vec1.get_end(),Vec1.get_end()+(B1+t*B1,B2+t*B2,0), buff=0, color = Vec2.get_color()).set_fill(opacity=0.5)
                obj.become(NewVec2c)
            # Primera función para cambios de VecRCL.
            def upd_for_vecrcl_1(obj):
                t = vt1.get_value()
                NewVecRCL = DashedArrow((0,0,0),Vec2c.get_end(), buff=0, color = MOSTAZA_OSCURO).set_fill(opacity=1)
                obj.become(NewVecRCL)
            # Primera línea usada.
            Linea1 = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP, Vec2c.get_end(), color = MOSTAZA_OSCURO).set_fill(opacity=0.5)
            # Segunda línea usada.
            Linea2 = Line(Vec1.get_end(), Vec1.get_end()-(0.01*B1,0.01*B2,0), color = MOSTAZA_OSCURO).set_fill(opacity=0.5)
            # Función para cambiar tamaño de las líneas.
            def upd_for_linea(obj):
                t = vt1.get_value()
                new_linea = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP,Vec1.get_end()+(B1+t*B1,B2+t*B2,0), color = MOSTAZA_OSCURO).set_fill(opacity=0.5)
                obj.become(new_linea)
            self.play(ShowCreation(Linea1),ShowCreation(Linea2))
            self.bring_to_back(Linea1)
            self.bring_to_back(Linea2)
            Vec2.add_updater(upd_for_vec2_1)
            Vec2c.add_updater(upd_for_vec2c_1)
            VecRCL.add_updater(upd_for_vecrcl_1)
            Linea1.add_updater(upd_for_linea)
            Linea2.add_updater(upd_for_linea)
            self.play(vt1.set_value,7.5,run_time=0.85)
            Linea1.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            self.play(vt1.set_value,-9,run_time=0.85)
            Linea2.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            Vec2.remove_updater(upd_for_vec2_1)
            Vec2c.remove_updater(upd_for_vec2c_1)
            VecRCL.remove_updater(upd_for_vecrcl_1)
            self.wait(0.65)
            self.play(ShowCreation(Vec1c),FadeOut(Vec2c),runtime = 0.5)
            # Primera función para cambios de Vec1.
            def upd_for_vec1_1(obj):
                t = vt1.get_value()
                NewVec1 = Arrow((0,0,0),(A1+t*A1,A2+t*A2,0),buff=0, color = Vec1.get_color())
                obj.become(NewVec1)
            # Primera función para cambios de Vec1c.
            def upd_for_vec1c_1(obj):
                t = vt1.get_value()
                NewVec1c = DashedArrow(Vec2.get_end(),Vec2.get_end()+(A1+t*A1,A2+t*A2,0), buff=0, color = Vec1.get_color()).set_fill(opacity=0.5)
                obj.become(NewVec1c)
            # Segunda función para cambios de VecRCL.
            def upd_for_vecrcl_2(obj):
                t = vt1.get_value()
                NewVecRCL = DashedArrow((0,0,0),Vec2.get_end()+(A1+t*A1,A2+t*A2,0), buff=0, color = MOSTAZA_OSCURO).set_fill(opacity=1)
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
                vert3 = Linea2.get_end()+(t*A1,t*A2,0)
                vert4 = Linea1.get_end()+(t*A1,t*A2,0)
                New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MOSTAZA_CLARO, opacity = 1)
                obj.become(New_plano)
                self.bring_to_back(obj)
            Vec1.add_updater(upd_for_vec1_1)
            Vec1c.add_updater(upd_for_vec1c_1)
            VecRCL.add_updater(upd_for_vecrcl_2)
            Plano1.add_updater(upd_for_plano)
            self.play(ShowCreation(Plano1), run_time=0.05)
            self.play(ShowCreation(Plano2), run_time = 0.05)
            self.play(FadeOut(VGroup(Linea1,Linea2)), run_time=0.05)
            self.add_foreground_mobject(CtoOF)
            self.play(vt1.set_value,5,run_time=0.85,rate_func=linear)
            Plano1.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0,rate_func=linear)
            Plano2.add_updater(upd_for_plano)
            self.play(vt1.set_value,-7,run_time=0.85,rate_func=linear)
            Plano2.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0,rate_func=linear)
            Vec1.remove_updater(upd_for_vec1_1)
            Vec1c.remove_updater(upd_for_vec1c_1)
            VecRCL.remove_updater(upd_for_vecrcl_2)
            self.wait(0.65)
            self.play(FadeOut(Vec1c))
            self.play(Write(Text9_2.group))
            self.add_foreground_mobjects(Text9_2.group)
            self.wait(0.65)
            Punto = Dot(radius=0.01, color = MOSTAZA_OSCURO).set_fill(MOSTAZA_OSCURO)
            self.play(FadeOut(VGroup(Plano1,Plano2)))
            self.remove_foreground_mobjects(Text9_2.group,CtoOF)
            self.play(FadeOut(VGroup(VecRCL,Punto)))
            self.play(Write(VGroup(Lab1,Lab2)))


        # Función para mostrar el tercer generado.
        # Aquí ya se encuentran los self.play.
        def gen3(Vec1,Vec2,Lab1,Lab2):
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
            self.play(ShowCreation(VGroup(Vec1c,Vec2c)))
            # Vector resultante de la combinación lineal.
            VecRCL = DashedArrow((0,0,0), Vec2c.get_end(), buff=0, color = TEAL_E).set_fill(opacity=1)
            self.play(ShowCreation(VecRCL))
            # ValueTrackers
            vt1 = ValueTracker(0)
            self.play(FadeOut(Vec1c),runtime=0.2)
            # Primera función para cambios de Vec2.
            def upd_for_vec2_1(obj):
                t = vt1.get_value()
                NewVec2 = Arrow((0,0,0),(B1+t*B1,B2+t*B2,0),buff=0, color = Vec2.get_color())
                obj.become(NewVec2)
            # Primera función para cambios de Vec2c.
            def upd_for_vec2c_1(obj):
                t = vt1.get_value()
                NewVec2c = DashedArrow(Vec1.get_end(),Vec1.get_end()+(B1+t*B1,B2+t*B2,0), buff=0, color = Vec2.get_color()).set_fill(opacity=0.5)
                obj.become(NewVec2c)
            # Primera función para cambios de VecRCL.
            def upd_for_vecrcl_1(obj):
                t = vt1.get_value()
                NewVecRCL = DashedArrow((0,0,0),Vec2c.get_end(), buff=0, color = TEAL_E).set_fill(opacity=1)
                obj.become(NewVecRCL)
            # Primera línea usada.
            Linea1 = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP, Vec2c.get_end(), color = TEAL_E).set_fill(opacity=0.5)
            # Segunda línea usada.
            Linea2 = Line(Vec1.get_end(), Vec1.get_end()-(0.01*B1,0.01*B2,0), color = TEAL_E).set_fill(opacity=0.5)
            # Función para cambiar tamaño de las líneas.
            def upd_for_linea(obj):
                t = vt1.get_value()
                new_linea = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP,Vec1.get_end()+(B1+t*B1,B2+t*B2,0), color = TEAL_E).set_fill(opacity=0.5)
                obj.become(new_linea)
            self.play(ShowCreation(Linea1),ShowCreation(Linea2))
            self.bring_to_back(Linea1)
            self.bring_to_back(Linea2)
            Vec2.add_updater(upd_for_vec2_1)
            Vec2c.add_updater(upd_for_vec2c_1)
            VecRCL.add_updater(upd_for_vecrcl_1)
            Linea1.add_updater(upd_for_linea)
            Linea2.add_updater(upd_for_linea)
            self.play(vt1.set_value,7.5,run_time=0.85)
            Linea1.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            self.play(vt1.set_value,-9,run_time=0.85)
            Linea2.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            Vec2.remove_updater(upd_for_vec2_1)
            Vec2c.remove_updater(upd_for_vec2c_1)
            VecRCL.remove_updater(upd_for_vecrcl_1)
            self.wait(0.65)
            self.play(ShowCreation(Vec1c),FadeOut(Vec2c),runtime = 0.5)
            # Primera función para cambios de Vec1.
            def upd_for_vec1_1(obj):
                t = vt1.get_value()
                NewVec1 = Arrow((0,0,0),(A1+t*A1,A2+t*A2,0),buff=0, color = Vec1.get_color())
                obj.become(NewVec1)
            # Primera función para cambios de Vec1c.
            def upd_for_vec1c_1(obj):
                t = vt1.get_value()
                NewVec1c = DashedArrow(Vec2.get_end(),Vec2.get_end()+(A1+t*A1,A2+t*A2,0), buff=0, color = Vec1.get_color()).set_fill(opacity=0.5)
                obj.become(NewVec1c)
            # Segunda función para cambios de VecRCL.
            def upd_for_vecrcl_2(obj):
                t = vt1.get_value()
                NewVecRCL = DashedArrow((0,0,0),Vec2.get_end()+(A1+t*A1,A2+t*A2,0), buff=0, color = TEAL_E).set_fill(opacity=1)
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
                vert3 = Linea2.get_end()+(t*A1,t*A2,0)
                vert4 = Linea1.get_end()+(t*A1,t*A2,0)
                New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(TEAL_A, opacity = 1)
                obj.become(New_plano)
                self.bring_to_back(obj)
            Vec1.add_updater(upd_for_vec1_1)
            Vec1c.add_updater(upd_for_vec1c_1)
            VecRCL.add_updater(upd_for_vecrcl_2)
            Plano1.add_updater(upd_for_plano)
            self.play(ShowCreation(Plano1), run_time=0.05)
            self.play(ShowCreation(Plano2), run_time = 0.05)
            self.play(FadeOut(VGroup(Linea1,Linea2)), run_time=0.05)
            self.play(vt1.set_value,5,run_time=0.85,rate_func=linear)
            Plano1.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0,rate_func=linear)
            Plano2.add_updater(upd_for_plano)
            self.play(vt1.set_value,-7,run_time=0.85,rate_func=linear)
            Plano2.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0,rate_func=linear)
            Vec1.remove_updater(upd_for_vec1_1)
            Vec1c.remove_updater(upd_for_vec1c_1)
            VecRCL.remove_updater(upd_for_vecrcl_2)
            self.wait(0.65)
            self.play(FadeOut(Vec1c))
            self.play(Write(Text9_1.group))
            self.add_foreground_mobject(Text9_1.group)
            self.wait(0.65)
            Punto = Dot(radius=0.01, color = TEAL_E).set_fill(TEAL_A)
            self.play(FadeOut(VGroup(Plano1,Plano2)))
            self.play(FadeOut(Text9_1.group))
            self.remove_foreground_mobject(Text9_1.group)
            self.play(FadeOut(VGroup(VecRCL,Punto)))
            self.play(Write(VGroup(Lab1,Lab2)))

        # Función para mostrar el segundo generado.
        # Aquí ya se encuentran los self.play.
        def gen4(Vec1,Vec2,Lab1,Lab2):
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
            self.play(ShowCreation(VGroup(Vec1c,Vec2c)))
            # Vector resultante de la combinación lineal.
            VecRCL = DashedArrow((0,0,0), Vec2c.get_end(), buff=0, color = AZUL_OSCURO).set_fill(opacity=1)
            self.play(ShowCreation(VecRCL))
            # ValueTrackers
            vt1 = ValueTracker(0)
            self.play(FadeOut(Vec1c),runtime=0.2)
            # Primera función para cambios de Vec2.
            def upd_for_vec2_1(obj):
                t = vt1.get_value()
                NewVec2 = Arrow((0,0,0),(B1+t*B1,B2+t*B2,0),buff=0, color = Vec2.get_color())
                obj.become(NewVec2)
            # Primera función para cambios de Vec2c.
            def upd_for_vec2c_1(obj):
                t = vt1.get_value()
                NewVec2c = DashedArrow(Vec1.get_end(),Vec1.get_end()+(B1+t*B1,B2+t*B2,0), buff=0, color = Vec2.get_color()).set_fill(opacity=0.5)
                obj.become(NewVec2c)
            # Primera función para cambios de VecRCL.
            def upd_for_vecrcl_1(obj):
                t = vt1.get_value()
                NewVecRCL = DashedArrow((0,0,0),Vec2c.get_end(), buff=0, color = AZUL_OSCURO).set_fill(opacity=1)
                obj.become(NewVecRCL)
            # Primera línea usada.
            Linea1 = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP, Vec2c.get_end(), color = AZUL_OSCURO).set_fill(opacity=0.5)
            # Segunda línea usada.
            Linea2 = Line(Vec1.get_end(), Vec1.get_end()-(0.01*B1,0.01*B2,0), color = AZUL_OSCURO).set_fill(opacity=0.5)
            # Función para cambiar tamaño de las líneas.
            def upd_for_linea(obj):
                t = vt1.get_value()
                new_linea = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP,Vec1.get_end()+(B1+t*B1,B2+t*B2,0), color = AZUL_OSCURO).set_fill(opacity=0.5)
                obj.become(new_linea)
            self.play(ShowCreation(Linea1),ShowCreation(Linea2))
            self.bring_to_back(Linea1)
            self.bring_to_back(Linea2)
            Vec2.add_updater(upd_for_vec2_1)
            Vec2c.add_updater(upd_for_vec2c_1)
            VecRCL.add_updater(upd_for_vecrcl_1)
            Linea1.add_updater(upd_for_linea)
            Linea2.add_updater(upd_for_linea)
            self.play(vt1.set_value,12,run_time=0.85)
            Linea1.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            self.play(vt1.set_value,-15,run_time=0.85)
            Linea2.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            Vec2.remove_updater(upd_for_vec2_1)
            Vec2c.remove_updater(upd_for_vec2c_1)
            VecRCL.remove_updater(upd_for_vecrcl_1)
            self.wait(0.65)
            self.play(ShowCreation(Vec1c),FadeOut(Vec2c),runtime = 0.5)
            # Primera función para cambios de Vec1.
            def upd_for_vec1_1(obj):
                t = vt1.get_value()
                NewVec1 = Arrow((0,0,0),(A1+t*A1,A2+t*A2,0),buff=0, color = Vec1.get_color())
                obj.become(NewVec1)
            # Primera función para cambios de Vec1c.
            def upd_for_vec1c_1(obj):
                t = vt1.get_value()
                NewVec1c = DashedArrow(Vec2.get_end(),Vec2.get_end()+(A1+t*A1,A2+t*A2,0), buff=0, color = Vec1.get_color()).set_fill(opacity=0.5)
                obj.become(NewVec1c)
            # Segunda función para cambios de VecRCL.
            def upd_for_vecrcl_2(obj):
                t = vt1.get_value()
                NewVecRCL = DashedArrow((0,0,0),Vec2.get_end()+(A1+t*A1,A2+t*A2,0), buff=0, color = AZUL_OSCURO).set_fill(opacity=1)
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
                vert3 = Linea2.get_end()+(t*A1,t*A2,0)
                vert4 = Linea1.get_end()+(t*A1,t*A2,0)
                New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(AZUL_CLARO, opacity = 1)
                obj.become(New_plano)
                self.bring_to_back(obj)
            Vec1.add_updater(upd_for_vec1_1)
            Vec1c.add_updater(upd_for_vec1c_1)
            VecRCL.add_updater(upd_for_vecrcl_2)
            Plano1.add_updater(upd_for_plano)
            self.play(ShowCreation(Plano1), run_time=0.05)
            self.play(ShowCreation(Plano2), run_time = 0.05)
            self.play(FadeOut(VGroup(Linea1,Linea2)), run_time=0.05)
            self.play(vt1.set_value,10,run_time=0.85,rate_func=linear)
            Plano1.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0,rate_func=linear)
            Plano2.add_updater(upd_for_plano)
            self.play(vt1.set_value,-12,run_time=0.85,rate_func=linear)
            Plano2.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0,rate_func=linear)
            Vec1.remove_updater(upd_for_vec1_1)
            Vec1c.remove_updater(upd_for_vec1c_1)
            VecRCL.remove_updater(upd_for_vecrcl_2)
            self.wait(0.65)
            self.play(FadeOut(Vec1c))
            self.play(Write(Text9_3.group))
            self.add_foreground_mobjects(Text9_3.group,CtoON_2.bg,CtoON_2)
            self.wait(0.65)
            Punto = Dot(radius=0.01, color = AZUL_CLARO).set_fill(AZUL_CLARO)
            self.play(FadeOut(VGroup(Plano1,Plano2)))
            self.remove_foreground_mobjects(Text9_3.group,CtoON_2.bg,CtoON_2)
            self.play(FadeOut(Text9_3.group))
            self.play(FadeOut(VGroup(VecRCL,Punto)))
            self.play(Write(VGroup(Lab1,Lab2)))

        VecAc = Arrow((0, 0, 0), a_1 * RIGHT + a_2*UP, buff=0,color=AZUL)



        ######################
        ####### Escena #######
        ######################
        
       
        self.play(Write(grid))
        self.wait(0.5)
        self.play(ShowCreation(VecA),Write(VecALab))
        self.wait(0.65)
        self.play(ShowCreation(VecB),Write(VecBLab))
        self.add_foreground_mobjects(VecA,VecB)
        self.wait(0.65)
        self.play(Write(Cto.group))
        self.wait(0.65)
        self.play(ShowCreation(Ejes))
        self.wait(0.65)
        self.play(Write(VGroup(Text10.bg,Text10)))
        self.play(Write(Text10_1))
        self.play(Write(Text10_2))
        self.wait(0.65)
        self.play(FadeOut(Text10.group))
        self.wait(0.65)
        self.play(FadeOut(Ejes))
        gen1(VecA,VecB,VecALab,VecBLab)
        self.wait(0.65)
        self.play(Write(Text1.group))
        self.wait(0.65)
        self.play(FadeOut(VecALab))
        self.bring_to_back(pared)
        self.play(ShowCreation(pared))
        self.bring_to_back(luz)
        self.play(ShowCreation(luz))
        self.wait(0.65)
        self.add_foreground_mobject(VecP)
        self.play(ShowCreation(VecP), runtime=2)
        self.add_foreground_mobject(Text1)
        self.wait(0.65)
        self.play(ReplacementTransform(Text1.bg,Text2.bg),ReplacementTransform(Text1[0][-2],Text1c[0][-2]), runtime = 0.5)
        self.remove_foreground_mobject(Text1)
        self.play(ReplacementTransform(Text1_1,Text2_1),Write(Text2_2))
        self.wait(0.65)
        self.play(FadeOut(luz),FadeOut(pared))
        self.play(Write(VecALab))
        self.wait(0.65)
        self.play(Write(Tsilo.bg))
        self.play(Write(TCon))
        self.play(Write(TCon_1))
        self.play(Write(TCon_2))
        self.wait(0.65)
        self.bring_to_back(pared2)
        self.play(ShowCreation(pared2))
        self.play(FadeOut(VecBLab))
        self.bring_to_back(luz2)
        self.play(ShowCreation(luz2))
        self.remove_foreground_mobject(VecA)
        self.play(ShowCreation(VecP_2))
        self.play(ReplacementTransform(VGroup(Text1c[0][-2],Text1,Text2.bg,Text2_2,Text2_1),Text5.group))
        self.wait(0.65)
        self.play(FadeOut(luz2),FadeOut(pared2))
        self.play(Write(VecBLab))
        self.wait(0.65)
        self.play(FadeOut(VecP), FadeOut(Tsilo.group), FadeOut(Text5.group))
        self.wait(0.65)
        self.play(Write(Text6.group))
        self.wait(0.65)
        self.play(ReplacementTransform(Text6,Text6_1))
        self.wait(0.65)
        self.play(ReplacementTransform(VecP_2,VecPC_1))
        self.play(ShowCreation(VecR_1))
        self.play(ShowCreation(VecRLab_1))
        self.remove_foreground_mobject(VecB)
        self.play(FadeOut(VGroup(VecPC_1,VecB,VecBLab)))
        self.wait(0.65)
        self.add_foreground_mobject(Text6_1)
        self.play(ReplacementTransform(Text6.bg,Text6_2.bg))
        self.remove_foreground_mobject(Text6_1)
        self.play(ReplacementTransform(Text6_1,Text6_2))
        self.wait(0.65)
        self.add_foreground_mobjects(Text6_2.bg,Text6_2)
        gen3(VecA,VecR_1,VecALab,VecRLab_1)
        self.wait(0.65)
        self.remove_foreground_mobjects(Text5.group,Text6_2.bg,Text6_2)
        self.wait(0.65)
        self.play(ReplacementTransform(VGroup(VecR_1,VecRLab_1),VGroup(VecB,VecBLab)),FadeOut(VGroup(Text6_2.bg,Text6_2)))
        self.play(Write(CtoO.group))
        self.play(ReplacementTransform(CtoO,CtoO_1_1))
        self.bring_to_back(pared)
        self.play(ShowCreation(pared))
        self.play(FadeOut(VecALab))
        self.bring_to_back(luz)
        self.play(ShowCreation(luz))
        self.remove_foreground_mobject(VecA)
        self.play(ShowCreation(VecPnaranja))
        self.play(Write(Text13))
        self.play(FadeOut(luz),FadeOut(pared))
        self.play(Write(VecALab))
        self.play(ReplacementTransform(VecPnaranja,VecPC),ReplacementTransform(Text13,Text13_2))
        self.wait(0.65)
        self.play(ShowCreation(VecR),Write(VecRLab),FadeOut(Text13_2))
        self.add_foreground_mobject(CtoO_1_1)
        self.play(ReplacementTransform(CtoO.bg,CtoO_2.bg))
        self.remove_foreground_mobject(CtoO_1_1)
        self.play(ReplacementTransform(CtoO_1_1,CtoO_2_1))
        self.play(FadeOut(VGroup(VecPC,VecA,VecALab)))
        self.wait(0.65)
        gen2(VecR,VecB,VecRLab,VecBLab)
        self.play(FadeOut(VGroup(Text9_2.group,CtoOF)))

        self.play(Write(Text15bg))
        self.play(Write(Text15_1))
        self.wait(0.65)
        self.play(Write(Text15_2))
        self.wait(0.65)
        self.play(Write(Text15_3))
        self.wait(0.65)
        self.play(ReplacementTransform(Text15_3,Text15_4))
        self.wait(0.65)
        self.play(ReplacementTransform(Text15_4,Text15_5))
        self.wait(0.65)
        self.play(FadeOut(Text15group))

        self.play(ReplacementTransform(VecB,VecBN),ReplacementTransform(VecBLab,VecBNLab))
        self.play(ReplacementTransform(VecR,VecRN),ReplacementTransform(VecRLab,VecRNLab))
        self.wait(0.65)
        self.play(ReplacementTransform(VecRN,VecA),ReplacementTransform(VecRNLab,VecALab),ReplacementTransform(VecBN,VecBc),ReplacementTransform(VecBNLab,VecBcLab))
        self.wait(0.65)
        self.play(Write(CtoON.group))
        self.wait(0.65)
        self.bring_to_back(Eje)
        self.play(ShowCreation(Eje))
        self.play(ReplacementTransform(VecBc,VecBNc))
        self.play(ReplacementTransform(VecBcLab,VecBNcLab))
        self.play(FadeOut(Eje))
        self.play(ReplacementTransform(CtoON,CtoON_1))
        self.wait(0.65)
        self.add_foreground_mobject(VecPc)
        self.play(ShowCreation(VecPc),Write(Text12))
        self.play(ReplacementTransform(Text12,Text12_1))
        self.wait(0.65)
        self.play(ReplacementTransform(VecPc,VecPC),ReplacementTransform(Text12_1,Text12_3))
        self.remove_foreground_mobject(VecPc)
        self.wait(0.65)
        self.play(ShowCreation(VecRc),Write(VecRcLab),FadeOut(Text12_3))
        self.wait(0.65)
        self.play(FadeOut(VecPC),FadeOut(VGroup(VecAc,VecALab,VecA)))
        self.play(ReplacementTransform(VecRc,VecBPN))
        self.wait(0.65)
        self.play(ReplacementTransform(VecRcLab,VecBPNLab))
        self.wait(0.65)
        self.add_foreground_mobject(CtoON_1)
        self.play(ReplacementTransform(CtoON.bg,CtoON_2.bg))
        self.play(ReplacementTransform(CtoON_1,CtoON_2))
        self.remove_foreground_mobject(CtoON_1)
        self.wait(0.65)
        gen4(VecBPN,VecBNc,VecBPNLab,VecBNcLab)
        self.wait(2)
        self.play( *[FadeOut(mob)for mob in self.mobjects] )
        self.wait(2)