
from manimlib.imports import *


#####################################################################################
######################  Ortogonalización y ortonormalización  #######################
#####################################################################################

#####################################################################################
#################################  Primera escena  ##################################
#####################################################################################

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

class OO1(ThreeDScene):

    def construct(self):

        # Constantes de los colores usados.
        ROJO = '#FF0000'
        AZUL = '#0087FF'
        NARANJA = '#FF7700'
        VERDE = '#1FFF00'
        MAGENTA = '#FF00FF'
        AMARILLO = "#FFFF00"
        GRIS = "#888888"
        MAGENTA_CLARO = "#FFCEFF"

        # Texto de prodcto escalar y su rectángulo.
        Text1 = TextMobject('''$ \\langle \\vec{a},\\vec{b} \\rangle \\ \\ \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT)
        Text1.bg = SurroundingRectangle(Text1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text1.group = VGroup(Text1.bg,Text1)
        Text1_1 = VGroup()
        for i in range(0,7):
            Text1_1.add(Text1[0][i])
        Text1_2 = VGroup(Text1[0][-1],Text1[0][-2],Text1[0][-3],Text1[0][-4])

        # Texto de proyección y su rectángulo.
        Text2 = TextMobject('''$ \\frac{ \\langle \\vec{a} , \\vec{b} \\rangle} { \\norm{ \\vec{b} } ^2} \\vec{b} \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT).scale(1.2)
        Text2.bg = SurroundingRectangle(Text2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text2.group = VGroup(Text2.bg,Text2)
        Text2_1 = VGroup()
        for i in range(0,7):
            Text2_1.add(Text2[0][i])
        Text2_2 = VGroup()
        for i in range(7,15):
            Text2_2.add(Text2[0][i])

        # Texto de conjunto inicial y su rectángulo.
        Cto = TextMobject('''$ I = \\{ \\vec{a}, \\vec{b} \\} $''').move_to(1.5*DOWN + 3.5*RIGHT)
        for i in range(3,5):
            Cto[0][i].set_color(AZUL)
        for i in range(6,8):
            Cto[0][i].set_color(ROJO)
        Cto.bg = SurroundingRectangle(Cto,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Cto.group = VGroup(Cto.bg,Cto)
        Cto_1 = VGroup(Cto[0][6].copy(),Cto[0][7].copy())

        # Texto de conjunto ortogonal y su rectángulo, con las variaciones usadas.
        CtoO = TextMobject('''$ \\Gamma_1 = \\{ \\vec{b} \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            CtoO[0][i].set_color(BLACK)
        CtoO.bg = SurroundingRectangle(CtoO,color=WHITE,fill_color=BLACK,fill_opacity=1)
        CtoO.group = VGroup(CtoO.bg,CtoO)
        CtoO_1 = VGroup(CtoO[0][4],CtoO[0][5])
        CtoO_1_1 = TextMobject('''$ \\Gamma_1 = \\{ \\vec{b} \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            CtoO_1_1[0][i].set_color(ROJO)
        CtoO_2 = TextMobject('''$ \\Gamma_1 = \\{ \\vec{b} , \\vec{b}' \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            CtoO_2[0][i].set_color(ROJO)
        for i in range(6,10):
            CtoO_2[0][i].set_color(BLACK)
        CtoO_2_1 = TextMobject('''$ \\Gamma_1 = \\{ \\vec{b} , \\vec{b}' \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            CtoO_2_1[0][i].set_color(ROJO)
        for i in range(7,10):
            CtoO_2_1[0][i].set_color(VERDE)
        CtoO_3 = VGroup(CtoO_2[0][6],CtoO_2[0][7],CtoO_2[0][8])
        CtoO_2.bg = SurroundingRectangle(CtoO_2,color=WHITE,fill_color=BLACK,fill_opacity=1)

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
        TCon = TextMobject('''$ \\langle \\vec{a}, \\vec{b} \\rangle \\neq 0 $''').move_to(1*DOWN + 4*LEFT)
        TCon.bg = SurroundingRectangle(TCon, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        TCon.group = VGroup(TCon.bg,TCon)
        TCon_1 = TextMobject('''$ \\langle \\vec{b}, \\vec{a} \\rangle = \\overline{ \\langle \\vec{a}, \\vec{b} \\rangle } $''').move_to(2*DOWN + 4*LEFT)
        TCon_1.bg = SurroundingRectangle(TCon_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        TCon_1.group = VGroup(TCon_1.bg,TCon_1)
        TCon_2 = TextMobject('''$ \\Rightarrow \\langle \\vec{b}, \\vec{a} \\rangle \\neq 0 $''').move_to(3*DOWN + 4*LEFT)
        TCon_2.bg = SurroundingRectangle(TCon_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        TCon_2.group = VGroup(TCon_2.bg,TCon_2)
        Tsilo = VGroup(TCon,TCon_1,TCon_2)
        Tsilo.bg = SurroundingRectangle(VGroup(TCon,TCon_2,TCon_1), color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Tsilo.group = VGroup(Tsilo.bg,Tsilo)

        # Texto para proyección de b sobre a.
        Text5 = TextMobject('''$ \\frac{ \\langle \\vec{b} , \\vec{a} \\rangle} { \\norm{ \\vec{a} } ^2} \\vec{a} \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT).scale(1.2)
        Text5.bg = SurroundingRectangle(Text5, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text5.group = VGroup(Text5.bg,Text5)

        # Texto para segundo conjunto ortonormal, su rectángulo, y las variaciones usadas.
        Text6 = TextMobject('''$ \\Gamma_2 = \{ \\vec{a} \} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            Text6[0][i].set_color(BLACK)
        Text6.bg = SurroundingRectangle(Text6, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text6.group = VGroup(Text6.bg,Text6)
        Text6_1 = TextMobject('''$ \\Gamma_2 = \{ \\vec{a} \} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            Text6_1[0][i].set_color(AZUL)
        Text6_2 = TextMobject('''$ \\Gamma_2 = \{ \\vec{a}, \\vec{a}' \} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(4,6):
            Text6_2[0][i].set_color(AZUL)
        for i in range(7,10):
            Text6_2[0][i].set_color(VERDE)
        Text6_2.bg = SurroundingRectangle(Text6_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)

        # Textos para los generados y sus rectángulos.
        Text9 = TextMobject('''$ \\langle I \\rangle $''').move_to(2*DOWN + 4*LEFT)
        Text9.bg = SurroundingRectangle(Text9, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text9.group = VGroup(Text9.bg,Text9)
        Text9_1 = TextMobject('''$ \\langle I \\rangle = \\langle \\Gamma_1 \\rangle $''').move_to(2*DOWN + 4*LEFT)
        Text9_1.bg = SurroundingRectangle(Text9_1, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text9_1.group = VGroup(Text9_1.bg,Text9_1)
        Text9_2 = TextMobject('''$ \\langle I \\rangle = \\langle \\Gamma_1 \\rangle = \\langle \\Gamma_2 \\rangle $''').move_to(2*DOWN + 4*LEFT)
        Text9_2.bg = SurroundingRectangle(Text9_2, color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Text9_2.group = VGroup(Text9_2.bg,Text9_2)
        Text9_3 = TextMobject('''$ \\langle I \\rangle = \\langle N \\rangle $''').move_to(2*DOWN + 4*LEFT)
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
                #rayo = Line( [i[0]+x2o,i[1]+y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(WHITE).set_color(color=[WHITE,"#8f8f8f"])
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
        VecP = Arrow((0, 0, 0),(p1,p2,0), color = NARANJA, buff = 0)
        VecPc = VecP.copy()
                
        # Copia de proyección de a sobre b usada para la resta.
        VecPC = Arrow((a_1,a_2,0),(a_1-p1,a_2-p2,0), color = NARANJA, buff = 0)

        # Vector resultante de la resta y su etiqueta.
        VecR = Arrow((0, 0, 0),(a_1-p1,a_2-p2,0), color = VERDE, buff = 0)
        VecRLab = TextMobject('''$ \\vec{b}' $''').move_to(VecR.get_end()+0.5*LEFT).set_color(VERDE)

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
                #rayo = Line( [i[0]+x2o,i[1]+y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(WHITE).set_color(color=[WHITE,"#8f8f8f"])
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
        VecP_1 = Arrow((0, 0, 0),(p1_1,p2_1,0), color = MAGENTA, buff = 0)

        # Flecha para segundo uso de proyección de b sobre a.
        VecP_2 = Arrow((0, 0, 0),(p1_1,p2_1,0), color = NARANJA, buff = 0)

        # Copia de proyección de b sobre a usada para la resta.
        VecPC_1 = Arrow((b_1,b_2,0),(b_1-p1_1,b_2-p2_1,0), color = NARANJA, buff = 0)

        # Vector resultante de la segunda resta y su etiqueta.
        VecR_1 = Arrow((0, 0, 0),(b_1-p1_1,b_2-p2_1,0), color = VERDE, buff = 0)
        VecRLab_1 = TextMobject('''$ \\vec{a}' $''').move_to(VecR_1.get_end()+0.3*DOWN+0.5*LEFT).set_color(VERDE)

        # Eje para normalizar vector.
        Eje = DashedLine((0-5*b_1, 0-5*b_2, 0),(5*b_1,5*b_2,0), color = MAGENTA, buff = 0)

        # Se normaliza vector B.
        # Norma de vector B.
        NorB = np.sqrt(b_1**2 + b_2**2)
        # Coordenadas de B normalizado.
        nb_1 = b_1/NorB
        nb_2 = b_2/NorB

        #Vector B' normalizado y su etiqueta.
        VecBN = Arrow((0,0,0),(nb_1,nb_2,0), color = ROJO, buff = 0)
        VecBNLab = TextMobject(''' $ \\hat{b} $ ''').move_to(VecBN.get_end()+0.5*UP).set_color(ROJO)

        # Ejes para mostrar independencia lineal.
        Eje1 = DashedLine((0-5*b_1, 0-5*b_2, 0),(5*b_1,5*b_2,0), color = MAGENTA, buff = 0)
        Eje2 = DashedLine((0-5*a_1, 0-5*a_2, 0),(5*a_1,5*a_2,0), color = MAGENTA, buff = 0)
        Ejes = VGroup(Eje1,Eje2)
        Eje1copy = DashedLine((0-5*b_1, 0-5*b_2, 0),(5*b_1,5*b_2,0), color = MAGENTA, buff = 0)
        Eje2copy = DashedLine((0-5*a_1, 0-5*a_2, 0),(5*a_1,5*a_2,0), color = MAGENTA, buff = 0)
        Ejescopy = VGroup(Eje1copy,Eje2copy)

        # Copia de ejes, más grande.
        Eje1c = DashedLine((0-5*b_1, 0-5*b_2, 0),(5*b_1,5*b_2,0), color = MAGENTA, buff = 0).scale(2)
        Eje2c = DashedLine((0-5*a_1, 0-5*a_2, 0),(5*a_1,5*a_2,0), color = MAGENTA, buff = 0).scale(2)
        Ejesc = VGroup(Eje1c,Eje2c)

        #Se normaliza vector B'.
        # Norma de vector B'.
        NorBP = np.sqrt((a_1-p1)**2 + (a_2-p2)**2)
        # Coordenadas de B' normalizado
        nbp_1 = (a_1-p1)/NorBP
        nbp_2 = (a_2-p2)/NorBP

        #Vector B' normalizado y su etiqueta.
        VecBPN = Arrow((0,0,0),(nbp_1,nbp_2,0), color = VERDE, buff = 0)
        VecBPNLab = TextMobject(''' $ \\hat{a}' $ ''').move_to(VecBPN.get_end()+0.5*UP).set_color(VERDE)

        # Función para primer generado.
        # Aquí ya se encuentran los self.play.
        def gen1(Vec1,Vec2,Lab1,Lab2):
            self.play(FadeOut(VGroup(Lab1,Lab2)))
            # Copias de vectores.
            Copia1 = Vec1.copy()
            Copia2 = Vec2.copy()
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
            #VecRCL = Arrow((0,0,0), (A1+B1)*UP+(A2+B2)*RIGHT, buff=0, color = MAGENTA, opacity = 0.7)
            VecRCL = DashedArrow((0,0,0), Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
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
                NewVecRCL = DashedArrow((0,0,0),Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
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
            self.play(vt1.set_value,7.5,run_time=1.75,rate_func=rush_into)
            Linea1.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            #self.bring_to_back(Linea1)
            #self.play(ShowCreation(Linea1))
            #Linea2.add_updater(upd_for_linea)
            self.play(vt1.set_value,-9,run_time=1.75,rate_func=rush_into)
            Linea2.remove_updater(upd_for_linea)
            #self.bring_to_back(Linea2)
            #self.play(ShowCreation(Linea2))
            self.play(vt1.set_value,0)
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
                NewVecRCL = DashedArrow((0,0,0),Vec1c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
                obj.become(NewVecRCL)
            # Rectangulos usados para rellenar plano.
            Vertice1 = Linea1.get_end()
            Vertice2 = Linea2.get_end()
            Vertice3 = Linea2.get_end()+(0.05*A1,0.025*A2,0)
            Vertice4 = Linea1.get_end()+(0.05*A1,0.025*A2,0)
            Vertice5 = Linea2.get_end()-(0.05*A1,0.025*A2,0)
            Vertice6 = Linea1.get_end()-(0.05*A1,0.025*A2,0)
            Plano1 = Polygon(Vertice1,Vertice2,Vertice3,Vertice4,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
            Plano2 = Polygon(Vertice1,Vertice2,Vertice5,Vertice6,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
            # Función que rellena plano.
            def upd_for_plano(obj):
                t = vt1.get_value()
                vert1 = Linea1.get_end()
                vert2 = Linea2.get_end()
                vert3 = Linea2.get_end()+(t*A1,t*A2,0)
                vert4 = Linea1.get_end()+(t*A1,t*A2,0)
                New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA_CLARO, opacity = 1)
                #New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
                obj.become(New_plano)
                self.bring_to_back(obj)
            Vec1.add_updater(upd_for_vec1_1)
            Vec1c.add_updater(upd_for_vec1c_1)
            VecRCL.add_updater(upd_for_vecrcl_2)
            Plano1.add_updater(upd_for_plano)
            self.play(ShowCreation(Plano1), run_time=0.05)
            self.play(ShowCreation(Plano2), run_time = 0.05)
            self.play(FadeOut(VGroup(Linea1,Linea2)), run_time=0.05)
            self.play(vt1.set_value,5,run_time=1.75,rate_func=rush_into)
            Plano1.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0)
            Plano2.add_updater(upd_for_plano)
            self.play(vt1.set_value,-7,run_time=1.75,rate_func=rush_into)
            Plano2.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0)
            Vec1.remove_updater(upd_for_vec1_1)
            Vec1c.remove_updater(upd_for_vec1c_1)
            VecRCL.remove_updater(upd_for_vecrcl_2)
            self.wait(0.65)
            self.play(Write(Text9.group))
            self.add_foreground_mobject(Text9.group)
            self.wait(0.65)
            Punto = Dot(radius=0.01, color = MAGENTA).set_fill(MAGENTA)
            #self.remove(VGroup(Plano1,Plano2))
            self.play(FadeOut(VGroup(Plano1,Plano2)))
            self.remove_foreground_mobject(Text9.group)
            #self.play(ReplacementTransform(VGroup(Plano1,Plano2),Punto))
            self.play(FadeOut(VGroup(Vec1c,VecRCL,Punto)))
            self.play(Write(VGroup(Lab1,Lab2)))

        # Función para mostrar el segundo generado.
        # Aquí ya se encuentran los self.play.
        def gen2(Vec1,Vec2,Lab1,Lab2):
            self.play(FadeOut(VGroup(Lab1,Lab2)))
            # Copias de vectores.
            Copia1 = Vec1.copy()
            Copia2 = Vec2.copy()
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
            #VecRCL = Arrow((0,0,0), (A1+B1)*UP+(A2+B2)*RIGHT, buff=0, color = MAGENTA, opacity = 0.7)
            VecRCL = DashedArrow((0,0,0), Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
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
                NewVecRCL = DashedArrow((0,0,0),Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
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
            self.play(vt1.set_value,7.5,run_time=0.85,rate_func=rush_into)
            Linea1.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            #self.bring_to_back(Linea1)
            #self.play(ShowCreation(Linea1))
            #Linea2.add_updater(upd_for_linea)
            self.play(vt1.set_value,-9,run_time=0.85,rate_func=rush_into)
            Linea2.remove_updater(upd_for_linea)
            #self.bring_to_back(Linea2)
            #self.play(ShowCreation(Linea2))
            self.play(vt1.set_value,0)
            Vec2.remove_updater(upd_for_vec2_1)
            Vec2c.remove_updater(upd_for_vec2c_1)
            VecRCL.remove_updater(upd_for_vecrcl_1)
            self.wait(0.65)
            self.play(ShowCreation(Vec1c),FadeOut(Vec2c),runtime = 0.5)
            #self.play(FadeOut(Vec2c))
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
                NewVecRCL = DashedArrow((0,0,0),Vec1c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
                obj.become(NewVecRCL)
            # Rectangulos usados para rellenar plano.
            Vertice1 = Linea1.get_end()
            Vertice2 = Linea2.get_end()
            Vertice3 = Linea2.get_end()+(0.05*A1,0.025*A2,0)
            Vertice4 = Linea1.get_end()+(0.05*A1,0.025*A2,0)
            Vertice5 = Linea2.get_end()-(0.05*A1,0.025*A2,0)
            Vertice6 = Linea1.get_end()-(0.05*A1,0.025*A2,0)
            Plano1 = Polygon(Vertice1,Vertice2,Vertice3,Vertice4,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
            Plano2 = Polygon(Vertice1,Vertice2,Vertice5,Vertice6,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
            # Función que rellena plano.
            def upd_for_plano(obj):
                t = vt1.get_value()
                vert1 = Linea1.get_end()
                vert2 = Linea2.get_end()
                vert3 = Linea2.get_end()+(t*A1,t*A2,0)
                vert4 = Linea1.get_end()+(t*A1,t*A2,0)
                New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA_CLARO, opacity = 1)
                #New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
                obj.become(New_plano)
                self.bring_to_back(obj)
            Vec1.add_updater(upd_for_vec1_1)
            Vec1c.add_updater(upd_for_vec1c_1)
            VecRCL.add_updater(upd_for_vecrcl_2)
            Plano1.add_updater(upd_for_plano)
            self.play(ShowCreation(Plano1), run_time=0.05)
            self.play(ShowCreation(Plano2), run_time = 0.05)
            self.play(FadeOut(VGroup(Linea1,Linea2)), run_time=0.05)
            self.play(vt1.set_value,5,run_time=0.85,rate_func=rush_into)
            Plano1.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0)
            Plano2.add_updater(upd_for_plano)
            self.play(vt1.set_value,-7,run_time=0.85,rate_func=rush_into)
            Plano2.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0)
            Vec1.remove_updater(upd_for_vec1_1)
            Vec1c.remove_updater(upd_for_vec1c_1)
            VecRCL.remove_updater(upd_for_vecrcl_2)
            self.wait(0.65)
            self.play(Write(Text9_1.group))
            self.add_foreground_mobjects(Text9_1.group,Text2.bg,Text1,Text2_2,Text2_1)
            self.wait(0.65)
            Punto = Dot(radius=0.01, color = MAGENTA).set_fill(MAGENTA)
            #self.remove(VGroup(Plano1,Plano2))
            self.play(FadeOut(VGroup(Plano1,Plano2)))
            self.remove_foreground_mobjects(Text9_1.group,Text2.bg,Text1,Text2_2,Text2_1)
            #self.play(ReplacementTransform(VGroup(Plano1,Plano2),Punto))
            self.play(FadeOut(VGroup(Vec1c,VecRCL,Punto)))
            self.play(Write(VGroup(Lab1,Lab2)))


        # Función para mostrar el tercer generado.
        # Aquí ya se encuentran los self.play.
        def gen3(Vec1,Vec2,Lab1,Lab2,Texto,Textobg,Texto_viejo,Texto_viejobg):
            Texto.group = VGroup(Textobg,Texto)
            Texto_viejo.group = VGroup(Texto_viejobg,Texto_viejo)
            self.play(FadeOut(VGroup(Lab1,Lab2)))
            # Copias de vectores.
            Copia1 = Vec1.copy()
            Copia2 = Vec2.copy()
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
            #VecRCL = Arrow((0,0,0), (A1+B1)*UP+(A2+B2)*RIGHT, buff=0, color = MAGENTA, opacity = 0.7)
            VecRCL = DashedArrow((0,0,0), Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
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
                NewVecRCL = DashedArrow((0,0,0),Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
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
            self.play(vt1.set_value,7.5,run_time=0.85,rate_func=rush_into)
            Linea1.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            #self.bring_to_back(Linea1)
            #self.play(ShowCreation(Linea1))
            #Linea2.add_updater(upd_for_linea)
            self.play(vt1.set_value,-9,run_time=0.85,rate_func=rush_into)
            Linea2.remove_updater(upd_for_linea)
            #self.bring_to_back(Linea2)
            #self.play(ShowCreation(Linea2))
            self.play(vt1.set_value,0)
            Vec2.remove_updater(upd_for_vec2_1)
            Vec2c.remove_updater(upd_for_vec2c_1)
            VecRCL.remove_updater(upd_for_vecrcl_1)
            self.wait(0.65)
            self.play(ShowCreation(Vec1c),FadeOut(Vec2c),runtime = 0.5)
            #self.play(FadeOut(Vec2c))
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
                NewVecRCL = DashedArrow((0,0,0),Vec1c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
                obj.become(NewVecRCL)
            # Rectangulos usados para rellenar plano.
            Vertice1 = Linea1.get_end()
            Vertice2 = Linea2.get_end()
            Vertice3 = Linea2.get_end()+(0.05*A1,0.025*A2,0)
            Vertice4 = Linea1.get_end()+(0.05*A1,0.025*A2,0)
            Vertice5 = Linea2.get_end()-(0.05*A1,0.025*A2,0)
            Vertice6 = Linea1.get_end()-(0.05*A1,0.025*A2,0)
            Plano1 = Polygon(Vertice1,Vertice2,Vertice3,Vertice4,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
            Plano2 = Polygon(Vertice1,Vertice2,Vertice5,Vertice6,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
            # Función que rellena plano.
            def upd_for_plano(obj):
                t = vt1.get_value()
                vert1 = Linea1.get_end()
                vert2 = Linea2.get_end()
                vert3 = Linea2.get_end()+(t*A1,t*A2,0)
                vert4 = Linea1.get_end()+(t*A1,t*A2,0)
                New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA_CLARO, opacity = 1)
                #New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
                obj.become(New_plano)
                self.bring_to_back(obj)
            Vec1.add_updater(upd_for_vec1_1)
            Vec1c.add_updater(upd_for_vec1c_1)
            VecRCL.add_updater(upd_for_vecrcl_2)
            Plano1.add_updater(upd_for_plano)
            self.play(ShowCreation(Plano1), run_time=0.05)
            self.play(ShowCreation(Plano2), run_time = 0.05)
            self.play(FadeOut(VGroup(Linea1,Linea2)), run_time=0.05)
            self.play(vt1.set_value,5,run_time=0.85,rate_func=rush_into)
            Plano1.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0)
            Plano2.add_updater(upd_for_plano)
            self.play(vt1.set_value,-7,run_time=0.85,rate_func=rush_into)
            Plano2.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0)
            Vec1.remove_updater(upd_for_vec1_1)
            Vec1c.remove_updater(upd_for_vec1c_1)
            VecRCL.remove_updater(upd_for_vecrcl_2)
            self.wait(0.65)
            self.play(ReplacementTransform(Texto_viejo.group,Texto.group))
            self.add_foreground_mobject(Texto.group)
            self.wait(0.65)
            Punto = Dot(radius=0.01, color = MAGENTA).set_fill(MAGENTA)
            #self.remove(VGroup(Plano1,Plano2))
            self.play(FadeOut(VGroup(Plano1,Plano2)))
            self.remove_foreground_mobject(Texto.group)
            #self.play(ReplacementTransform(VGroup(Plano1,Plano2),Punto))
            self.play(FadeOut(VGroup(Vec1c,VecRCL,Punto)))
            self.play(Write(VGroup(Lab1,Lab2)))

        # Función para mostrar el segundo generado.
        # Aquí ya se encuentran los self.play.
        def gen4(Vec1,Vec2,Lab1,Lab2):
            self.play(FadeOut(VGroup(Lab1,Lab2)))
            # Copias de vectores.
            Copia1 = Vec1.copy()
            Copia2 = Vec2.copy()
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
            #VecRCL = Arrow((0,0,0), (A1+B1)*UP+(A2+B2)*RIGHT, buff=0, color = MAGENTA, opacity = 0.7)
            VecRCL = DashedArrow((0,0,0), Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
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
                NewVecRCL = DashedArrow((0,0,0),Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
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
            self.play(vt1.set_value,7.5,run_time=0.85,rate_func=rush_into)
            Linea1.remove_updater(upd_for_linea)
            self.play(vt1.set_value,0)
            #self.bring_to_back(Linea1)
            #self.play(ShowCreation(Linea1))
            #Linea2.add_updater(upd_for_linea)
            self.play(vt1.set_value,-9,run_time=0.85,rate_func=rush_into)
            Linea2.remove_updater(upd_for_linea)
            #self.bring_to_back(Linea2)
            #self.play(ShowCreation(Linea2))
            self.play(vt1.set_value,0)
            Vec2.remove_updater(upd_for_vec2_1)
            Vec2c.remove_updater(upd_for_vec2c_1)
            VecRCL.remove_updater(upd_for_vecrcl_1)
            self.wait(0.65)
            self.play(ShowCreation(Vec1c),FadeOut(Vec2c),runtime = 0.5)
            #self.play(FadeOut(Vec2c))
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
                NewVecRCL = DashedArrow((0,0,0),Vec1c.get_end(), color = MAGENTA).set_fill(opacity=0.5)
                obj.become(NewVecRCL)
            # Rectangulos usados para rellenar plano.
            Vertice1 = Linea1.get_end()
            Vertice2 = Linea2.get_end()
            Vertice3 = Linea2.get_end()+(0.05*A1,0.025*A2,0)
            Vertice4 = Linea1.get_end()+(0.05*A1,0.025*A2,0)
            Vertice5 = Linea2.get_end()-(0.05*A1,0.025*A2,0)
            Vertice6 = Linea1.get_end()-(0.05*A1,0.025*A2,0)
            Plano1 = Polygon(Vertice1,Vertice2,Vertice3,Vertice4,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
            Plano2 = Polygon(Vertice1,Vertice2,Vertice5,Vertice6,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
            # Función que rellena plano.
            def upd_for_plano(obj):
                t = vt1.get_value()
                vert1 = Linea1.get_end()
                vert2 = Linea2.get_end()
                vert3 = Linea2.get_end()+(t*A1,t*A2,0)
                vert4 = Linea1.get_end()+(t*A1,t*A2,0)
                New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA_CLARO, opacity = 1)
                #New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA, opacity = 0.5)
                obj.become(New_plano)
                self.bring_to_back(obj)
            Vec1.add_updater(upd_for_vec1_1)
            Vec1c.add_updater(upd_for_vec1c_1)
            VecRCL.add_updater(upd_for_vecrcl_2)
            Plano1.add_updater(upd_for_plano)
            self.play(ShowCreation(Plano1), run_time=0.05)
            self.play(ShowCreation(Plano2), run_time = 0.05)
            self.play(FadeOut(VGroup(Linea1,Linea2)), run_time=0.05)
            self.play(vt1.set_value,5,run_time=0.85,rate_func=rush_into)
            Plano1.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0)
            Plano2.add_updater(upd_for_plano)
            self.play(vt1.set_value,-7,run_time=0.85,rate_func=rush_into)
            Plano2.remove_updater(upd_for_plano)
            self.play(vt1.set_value,0)
            Vec1.remove_updater(upd_for_vec1_1)
            Vec1c.remove_updater(upd_for_vec1c_1)
            VecRCL.remove_updater(upd_for_vecrcl_2)
            self.wait(0.65)
            self.play(Write(Text9_3.group))
            self.add_foreground_mobjects(Text9_3.group,CtoON_2.bg,CtoON_2,Cto.group)
            self.wait(0.65)
            Punto = Dot(radius=0.01, color = MAGENTA).set_fill(MAGENTA)
            #self.remove(VGroup(Plano1,Plano2))
            self.play(FadeOut(VGroup(Plano1,Plano2)))
            self.remove_foreground_mobjects(Text9_3.group,CtoON_2.bg,CtoON_2,Cto.group)
            #self.play(ReplacementTransform(VGroup(Plano1,Plano2),Punto))
            self.play(FadeOut(VGroup(Vec1c,VecRCL,Punto)))
            self.play(Write(VGroup(Lab1,Lab2)))

        # Grupos que se quitan.
        Quitar = VGroup(VecR,Text2.bg,CtoO_2.bg,CtoO_2_1,Text1,Text2_2,Text2_1,VecRLab)
        Quitar2 = VGroup(Text6_2.bg,Text6_2,VecRLab_1,Text9_2.group,VecR_1,Text5.group)



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
        #self.play(ReplacementTransform(Ejes,Ejesc),runtime = 0.5)
        #self.wait(0.5)
        #self.play(ReplacementTransform(Ejesc,Ejescopy),runtime = 0.5)
        #self.wait()
        self.play(FadeOut(Ejes))
        self.play(Write(VGroup(Text10.bg,Text10)))
        self.play(Write(Text10_1))
        self.play(Write(Text10_2))
        self.wait(0.65)
        self.play(FadeOut(Text10.group))
        self.add_foreground_mobject(Cto.group)
        gen1(VecA,VecB,VecALab,VecBLab)
        #self.play(Write(Text9.group))
        self.remove_foreground_mobject(Cto.group)
        self.wait(0.65)
        self.play(Write(CtoO.group))
        self.wait(0.65)
        self.play(ReplacementTransform(CtoO,CtoO_1_1))
        self.wait(0.65)
        self.play(Write(Text1.group))
        self.add_foreground_mobject(Text1)
        self.wait(0.65)
        self.play(ReplacementTransform(Text1.bg,Text2.bg), runtime = 0.5)
        self.remove_foreground_mobject(Text1)
        self.play(ReplacementTransform(Text1_1,Text2_1),Write(Text2_2))
        self.wait(0.65)
        self.bring_to_back(pared)
        self.play(ShowCreation(pared))
        self.bring_to_back(luz)
        self.play(ShowCreation(luz))
        self.wait(0.65)
        self.add_foreground_mobject(VecP)
        self.play(ShowCreation(VecP), runtime=2)
        self.wait(0.65)
        self.play(FadeOut(luz),FadeOut(pared))
        self.wait(0.65)
        self.play(FadeOut(Text9.group))
        self.play(Write(Tsilo.bg))
        self.play(Write(TCon))
        self.play(Write(TCon_1))
        self.play(Write(TCon_2))
        self.wait(0.65)
        self.add_foreground_mobject(Cto.group)
        self.bring_to_back(pared2)
        self.play(ShowCreation(pared2))
        self.bring_to_back(luz2)
        self.play(ShowCreation(luz2))
        self.add_foreground_mobject(VecP_1)
        self.play(ShowCreation(VecP_1))
        self.play(FadeOut(luz2),FadeOut(pared2))
        self.remove_foreground_mobject(Cto.group)
        self.wait(0.65)
        self.remove_foreground_mobject(VecP_1)
        self.play(FadeOut(VGroup(Tsilo.group,VecP_1)))
        self.wait(0.65)
        self.play(ReplacementTransform(VecP,VecPC))
        self.remove_foreground_mobject(VecP)
        self.wait(0.65)
        self.play(ShowCreation(VecR),Write(VecRLab))
        self.remove_foreground_mobjects(VecA,VecALab)
        self.play(FadeOut(VGroup(VecPC,VecA,VecALab)))
        self.wait(0.65)
        self.add_foreground_mobject(CtoO_1_1)
        self.play(ReplacementTransform(CtoO.bg,CtoO_2.bg))
        self.remove_foreground_mobject(CtoO_1_1)
        self.play(ReplacementTransform(CtoO_1_1,CtoO_2))
        self.wait(0.65)
        self.play(ReplacementTransform(CtoO_2,CtoO_2_1))
        self.wait(0.65)
        self.add_foreground_mobjects(Cto.group,CtoO_2.bg,CtoO_2_1)
        gen2(VecR,VecB,VecRLab,VecBLab)
        #self.play(Write(Text9_1.group))
        self.remove_foreground_mobjects(Cto.group,CtoO_2.bg,CtoO_2_1)
        self.wait(0.65)
        self.play(FadeOut(Quitar),ShowCreation(VecA),Write(VecALab),Write(VecBLab))
        self.wait(0.65)
        self.play(Write(Text6.group))
        self.wait(0.65)
        self.play(ReplacementTransform(Text6,Text6_1))
        self.play(Write(Text5.group))
        self.wait(0.65)
        self.play(FadeOut(Cto.group))
        self.bring_to_back(pared2)
        self.play(ShowCreation(pared2))
        self.bring_to_back(luz2)
        self.play(ShowCreation(luz2))
        self.play(ShowCreation(VecP_2))
        self.play(FadeOut(luz2),FadeOut(pared2))
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
        self.add_foreground_mobjects(Text5.group,Text6_2.bg,Text6_2)
        gen3(VecA,VecR_1,VecALab,VecRLab_1,Text9_2,Text9_2.bg,Text9_1,Text9_1.bg)
        self.add_foreground_mobject(Text9_1)
        self.play(ReplacementTransform(Text9_1.bg,Text9_2.bg))
        self.remove_foreground_mobjects(Text9_1)
        self.play(ReplacementTransform(Text9_1,Text9_2))
        self.remove_foreground_mobjects(Text5.group,Text6_2.bg,Text6_2)
        self.wait(0.65)
        self.play(FadeOut(Quitar2),ShowCreation(VecB),Write(VecBLab),Write(VecALab),Write(Cto.group))
        self.wait(0.65)
        self.play(Write(CtoON.group))
        self.wait(0.65)
        self.bring_to_back(Eje)
        self.play(ShowCreation(Eje))
        self.play(ReplacementTransform(VecB,VecBN))
        self.play(ReplacementTransform(VecBLab,VecBNLab))
        self.play(FadeOut(Eje))
        self.play(ReplacementTransform(CtoON,CtoON_1))
        self.wait(0.65)
        self.add_foreground_mobject(VecPc)
        self.play(ShowCreation(VecPc))
        self.wait(0.65)
        self.play(ReplacementTransform(VecPc,VecPC))
        self.remove_foreground_mobject(VecPc)
        self.wait(0.65)
        self.play(ShowCreation(VecR),Write(VecRLab))
        self.wait(0.65)
        self.play(FadeOut(VecPC),FadeOut(VGroup(VecA,VecALab)))
        self.play(ReplacementTransform(VecR,VecBPN))
        self.wait(0.65)
        self.play(ReplacementTransform(VecRLab,VecBPNLab))
        self.wait(0.65)
        self.add_foreground_mobject(CtoON_1)
        self.play(ReplacementTransform(CtoON.bg,CtoON_2.bg))
        self.play(ReplacementTransform(CtoON_1,CtoON_2))
        self.remove_foreground_mobject(CtoON_1)
        self.wait(0.65)
        gen4(VecBPN,VecBN,VecBPNLab,VecBNLab)
        self.play(Write(Text9_3.group))
        self.wait(2)
        self.play( *[FadeOut(mob)for mob in self.mobjects] )
        self.wait(2)
        
	
#####################################################################################
#################################  Segunda escena  ##################################
#####################################################################################



class plane(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -8,
        "u_max": 8,
        "v_min": -8,
        "v_max": 8,
        "surface_piece_config": {},
        "stroke_color": BLUE_D,
        "stroke_width": 0.8,
        "checkerboard_colors": [BLACK]
        }
        ParametricSurface.__init__(self, self.func3, **kwargs)
    def func3(self, u, v):
        return np.array([0,u,v])

class plane_ab(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -5,
        "u_max": 5,
        "v_min": -2,
        "v_max": 2,
        "surface_piece_config": {},
        "stroke_width": 0,
        "stroke_color": WHITE,
        "checkerboard_colors": [BLUE_C]
        }
        ParametricSurface.__init__(self, self.func3, **kwargs)
    def func3(self, u, v):
        return np.array([0.5*u+2*v,u+3.5*v,3*u+2*v])

def norma(vector):
    return 1/np.sqrt(vector[0]**2+vector[1]**2+vector[2]**2) 
def vector_normal(vector):
    return norma(vector)*vector

def projection_of_a_along_b(vector_a, vector_b):
    vector_b_norm = np.sqrt(sum(vector_b**2))
    return (np.dot(vector_a, vector_b)/vector_b_norm**2)*vector_b

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
    
def light_2(x1,y1,x2,y2,n = 10):
            ''' Función para la luz usada para la proyección.
            (x1,y1) es el vector proyectado, (x2,y2) es sobre el que se proyecta.
            n es la cantidad de líneas que se generan para colorear la zona iluminada. '''
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
                #rayo = Line( [i[0]+x2o,i[1]+y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(WHITE).set_color(color=[WHITE,"#8f8f8f"])
                rayo = DashedLine( [0,i[0]+10*x2o,i[1]+10*y2o], [0,i[0],i[1]], width=5, stroke_width=5 , buff = 0.05).set_color(YELLOW)
                rays.append(rayo)
            # Se hace un VGroup con los rayos.
            grupo = VGroup()
            for i in rays:
                grupo.add(i)
            return(grupo)


class segundaescena(ThreeDScene):

    def parte1(self, a, b, c):
        text1 = TexMobject(r"I = \qty\Big{\vec{a}, \vec{b}, \vec{c}}").move_to(DOWN+5*RIGHT)
        text1[0][3:6].set_color(AZUL)
        text1[0][6:8].set_color(ROJO)
        text1[0][9:11].set_color(NARANJA)
        text1_bg=SurroundingRectangle(text1, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text2 = TexMobject(r'''\Gamma_1 = \qty\Big{ \vec{a}, \vec{b} ', \vec{c} \hspace{0.1cm} '  } ''').next_to(text1, 1.3*DOWN)
        text2[0][7:10].set_color(VERDE)
        text2[0][11:14].set_color(MAGENTA)
        text2_bg=SurroundingRectangle(text2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text3 = TexMobject(r"\langle \ I \ \rangle").move_to(DOWN-5*RIGHT)
        text3_bg=SurroundingRectangle(text3, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text4 = TextMobject("¿", "?").scale(5).to_edge(UL)

        
        #axb = [-8.5, 5, -0.25]
        a_vec = Vector(direction = a, color = AZUL)
        b_vec = Vector(direction = b, color = ROJO)
        c_vec = Vector(direction = c, color = NARANJA)
        a_vec_label = TexMobject(r"\vec{a}").move_to(1*RIGHT+2.7*UP)
        a_vec_label[0].set_color(AZUL)
        b_vec_label = TexMobject(r"\vec{b}").move_to(2.6*RIGHT+1.4*UP)
        b_vec_label[0].set_color(ROJO)
        c_vec_label = TexMobject(r"\vec{c}").move_to(-1.5*RIGHT+1*UP)
        c_vec_label[0].set_color(NARANJA)
        a_vec.save_state()
        b_vec.save_state()
        c_vec.save_state()
        a_li = DashedLine(-10*a, 10*a, color=WHITE)
        b_li = DashedLine(-10*b, 10*b, color=WHITE)
        c_li = DashedLine(-10*c, 10*c, color=WHITE)


        #PROYECCION DE B SOBRE A 
        plane1 = plane()
        y_axis = DoubleArrow(start=np.array([0,-8,0]), end=np.array([0,8,0]), color=WHITE, stroke_width=3)
        z_axis = DoubleArrow(start=np.array([0,0,-4]), end=np.array([0,0,4]), color=WHITE, stroke_width=3)

        a_pro = projection_of_a_along_b(b, a)
        a_vec_pro = Vector(direction = a_pro, color = YELLOW, buff=0)
        a_vec_pro_label=TexMobject(r" \frac{\langle \ \vec{b}, \vec{a} \ \rangle}{||\vec{a}||^2}\vec{a} ").move_to(1.8*RIGHT+2.0*UP).scale(0.7)
        a_vec_pro_label.set_color(YELLOW)
        line_a = DashedLine(ORIGIN, a_pro, width=5, buff = 0)
        line_a_perp = DashedLine(b, a_pro, width=5, buff=0)
        a_ort = Vector(direction = b-a_pro, color = VERDE, buff=0)
        a_ort_label=TexMobject(r"\vec{b}'")
        a_ort_label.set_color(VERDE).move_to(2.3*RIGHT+1.3*DOWN)
        suma_a = Arrow(start = b, end = b-a_pro, color = YELLOW, buff=0)

        #PROYECCION DE C SOBRE A 
        c_pro = projection_of_a_along_b(c, a)
        c_vec_pro = Vector(direction = c_pro, color = YELLOW, buff=0)
        c_vec_pro_label=TexMobject(r" \frac{\langle \ \vec{c}, \vec{a} \ \rangle}{||\vec{a}||^2}\vec{a} ").move_to(1.2*RIGHT+1.4*UP).scale(0.7)
        c_vec_pro_label.set_color(YELLOW)
        line_c = DashedLine(ORIGIN, c_pro, width=5, buff = 0)
        line_c_perp = DashedLine(c, c_pro, width=5, buff=0)
        c_ort = Vector(direction = c-c_pro, color = MAGENTA, buff=0)
        suma_c = Arrow(start = c, end = c-c_pro, color = YELLOW, buff=0)

        #PROYECCION DE C SOBRE B
        b_pro = projection_of_a_along_b(c, b)
        b_vec_pro = Vector(direction = b_pro, color = YELLOW, buff=0)
        b_vec_pro_label=TexMobject(r" \frac{\langle \ \vec{c}, \vec{b} \ \rangle}{||\vec{b}||^2}\vec{b} ").move_to(1.9*RIGHT+0.4*UP).scale(0.7)
        b_vec_pro_label.set_color(YELLOW)
        line_b = DashedLine(ORIGIN, b_pro, width=5, buff = 0)
        line_b_perp = DashedLine(c, b_pro, width=5, buff=0)
        suma_b = Arrow(start = c-c_pro, end = c-c_pro-b_pro, color = YELLOW, buff=0)
        cb_ort = Vector(direction = c-c_pro-b_pro, color = MAGENTA, buff=0)
        cb_ort_label=TexMobject(r"\vec{c}\hspace{0.1cm}'")
        cb_ort_label.set_color(MAGENTA).move_to(2.2*LEFT+2*DOWN)


    
        luz = light_2(b[1],b[2],a[1],a[2],25)
        
        
        self.add_foreground_mobject(a_vec)
        self.play(GrowArrow(a_vec))
        self.wait()
        self.add_foreground_mobject(a_vec_label)
        self.add_fixed_in_frame_mobjects(a_vec_label)
        self.play(Write(a_vec_label))
        self.wait()
        self.add_foreground_mobjects(b_vec)
        self.play(GrowArrow(b_vec))
        self.wait()
        self.add_foreground_mobject(b_vec_label)
        self.add_fixed_in_frame_mobjects(b_vec_label)
        self.play(Write(b_vec_label))
        self.wait()
        self.play(GrowArrow(c_vec))
        self.add_fixed_in_frame_mobjects(c_vec_label)
        self.play(Write(c_vec_label))
        self.wait()
        self.play(Write(a_li), Write(b_li), Write(c_li))
        self.wait(2)
        self.play(FadeOut(a_li), FadeOut(b_li), FadeOut(c_li))
        self.begin_ambient_camera_rotation(rate=0.08)
        self.add_fixed_in_frame_mobjects(text4[0])
        self.play(Write(text4[0]))
        self.wait()
        self.add_fixed_in_frame_mobjects(text4[1])
        self.play(Write(text4[1]))
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(text4))
        self.add_foreground_mobjects(text1_bg, text1)
        self.add_fixed_in_frame_mobjects(text1_bg)
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Write(text1_bg), Write(text1))
        
        #SUBESPACIOS

        self.play(a_vec_label.set_opacity, 0, b_vec_label.set_opacity, 0, c_vec_label.set_opacity, 0)
        self.move_camera(phi=45*DEGREES, theta=-45*DEGREES, gamma=0*DEGREES, run_time=2)
        self.play(FadeOut( b_vec), FadeOut(c_vec), FadeOut( a_vec), run_time=3)
        self.subespacios(a,b,c, text3, text3_bg)
        self.play(b_vec.restore, a_vec.restore, c_vec.restore, 
                  a_vec_label.set_opacity, 1, b_vec_label.set_opacity, 1, c_vec_label.set_opacity, 1,
                  run_time=1.5)
        
        
        #PROYECCION DE B SOBRE A
        
        self.move_camera(phi=90*DEGREES, theta=0*DEGREES, gamma=0*DEGREES)
        self.play(b_vec_label.move_to, 3*RIGHT+1.8*UP, a_vec_label.move_to, 0.4*RIGHT+2.7*UP)
        self.add_foreground_mobject(plane1)
        self.add_foreground_mobjects(y_axis, z_axis, a_vec, b_vec)
        self.play(ShowCreation(plane1), FadeIn(y_axis), FadeIn(z_axis), c_vec.set_opacity, 0, c_vec_label.set_opacity, 0)
        self.add_foreground_mobjects(text2_bg, text2[0][:7], text2[0][-1])
        self.add_fixed_in_frame_mobjects(text2_bg)
        self.add_fixed_in_frame_mobjects(text2[0][:7])
        self.add_fixed_in_frame_mobjects(text2[0][-1])
        self.play(Write(text2_bg), Write(text2[0][:7]), Write(text2[0][-1]))
        self.add_foreground_mobjects(luz, text1_bg, text1, text2_bg, text2[0][:7], text2[0][-1])
        self.play(ShowCreation(luz))
        self.add_foreground_mobject(a_vec_pro_label)
        self.add_foreground_mobject(a_vec_pro)
        self.add_fixed_in_frame_mobjects(a_vec_pro_label)
        self.play(GrowArrow(a_vec_pro), Write(a_vec_pro_label))
        self.wait(1.5)
        self.play(FadeOut(luz))
        self.play(Transform(a_vec_pro, suma_a), a_vec_pro_label.move_to, 1.8*RIGHT+0.2*DOWN, run_time=3)
        self.add_foreground_mobject(a_ort_label)
        self.add_foreground_mobject(a_ort)
        self.add_fixed_in_frame_mobjects(a_ort_label)
        self.play(GrowArrow(a_ort), Write(a_ort_label))
        self.play(FadeOut(a_vec_pro), FadeOut(a_vec_pro_label))
        self.add_foreground_mobject(text2[0][7:11])
        self.add_fixed_in_frame_mobjects(text2[0][7:11])
        self.play(Write(text2[0][7:11]))
        self.wait()
        self.play(FadeOut(plane1), FadeOut(y_axis), FadeOut(z_axis))
        self.move_camera(phi=80 * DEGREES, theta=30*DEGREES, run_time=2)
        self.play(c_vec.set_opacity, 1, c_vec_label.set_opacity, 1, b_vec_label.move_to, 2.9*RIGHT+1.4*UP, a_vec_label.move_to, 1*RIGHT+2.7*UP)
        self.remove_foreground_mobjects(a_vec_pro_label, a_vec, b_vec_pro_label, b_vec, text2_bg, text2[0][:7], text2[0][-1])
        
        #PROYECCION DE C SOBRE A
        self.play(Write(line_c_perp))
        self.wait()
        self.play(Write(line_c))
        self.wait()
        self.add_fixed_in_frame_mobjects(c_vec_pro_label)
        self.play(GrowArrow(c_vec_pro), Write(c_vec_pro_label))
        self.play(FadeOut(line_c), FadeOut(line_c_perp))
        self.wait(1.5)
        self.play(Transform(c_vec_pro, suma_c), c_vec_pro_label.move_to, 2.5*LEFT+0*DOWN, run_time=3)
        self.play(GrowArrow(c_ort))
        self.play(FadeOut(c_vec_pro), FadeOut(c_vec_pro_label))
    
        
        #PROYECCION DE C SOBRE B
        self.play(Write(line_b_perp))
        self.wait()
        self.play(Write(line_b))
        self.wait()
        self.add_fixed_in_frame_mobjects(b_vec_pro_label)
        self.play(GrowArrow(b_vec_pro), Write(b_vec_pro_label))
        self.play(FadeOut(line_b), FadeOut(line_b_perp))
        self.wait(1.5)
        self.play(Transform(b_vec_pro, suma_b), b_vec_pro_label.move_to, 2.8*LEFT+0.8*DOWN, run_time=3)
        self.add_fixed_in_frame_mobjects(cb_ort_label)
        self.play(GrowArrow(cb_ort), Write(cb_ort_label))
        self.play(FadeOut(b_vec_pro), FadeOut(b_vec_pro_label), FadeOut(c_ort), FadeOut(b_vec), FadeOut(b_vec_label), FadeOut(c_vec), FadeOut(c_vec_label))
        self.add_fixed_in_frame_mobjects(text2[0][11:14])
        self.play(Write(text2[0][11:14]))
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
         
            # All mobjects in the screen are saved in self.mobjects
        )
        
    def parte2(self, a, b, c):

        a_vec = Vector(direction = a, color = AZUL)
        b_vec = Vector(direction = b, color = ROJO)
        c_vec = Vector(direction = c, color = NARANJA)
        a_vec_norm = vector_normal(a)
        a_n = Vector(direction = a_vec_norm, color=AZUL, buff=0)

        #PROYECCION DE B SOBRE A 
        a_pro = projection_of_a_along_b(b, a)
        a_vec_pro = Vector(direction = a_pro, color = YELLOW, buff=0)
        line_a = DashedLine(ORIGIN, a_pro, width=5, buff = 0)
        line_a_perp = DashedLine(b, a_pro, width=5, buff=0)
        suma_a = Arrow(start = b, end = b-a_pro, color = YELLOW, buff=0)
        a_ort = Vector(direction = b-a_pro, color = VERDE, buff=0)
        a_ort_norm = vector_normal(b-a_pro)
        a_ort_n = Vector(direction = a_ort_norm, color=VERDE, buff=0)

        #PROYECCION DE C SOBRE A 
        c_pro = projection_of_a_along_b(c, a)
        c_vec_pro = Vector(direction = c_pro, color = YELLOW, buff=0)
        line_c = DashedLine(ORIGIN, c_pro, width=5, buff = 0)
        line_c_perp = DashedLine(c, c_pro, width=5, buff=0)
        c_ort = Vector(direction = c-c_pro, color = MAGENTA, buff=0)
        suma_c = Arrow(start = c, end = c-c_pro, color = YELLOW, buff=0)

        #PROYECCION DE C SOBRE B
        b_pro = projection_of_a_along_b(c, b)
        b_vec_pro = Vector(direction = b_pro, color = YELLOW, buff=0)
        line_b = DashedLine(ORIGIN, b_pro, width=5, buff = 0)
        line_b_perp = DashedLine(c, b_pro, width=5, buff=0)
        suma_b = Arrow(start = c-c_pro, end = c-c_pro-b_pro, color = YELLOW, buff=0)
        cb_ort = Vector(direction = c-c_pro-b_pro, color = MAGENTA, buff=0)
        cb_ort_norm = vector_normal(c-c_pro-b_pro)
        cb_ort_n = Vector(direction = cb_ort_norm, color=MAGENTA, buff=0)
        ref=Dot(color=YELLOW,radius=0.003)

        self.play(GrowArrow(a_vec))
        self.play(GrowArrow(b_vec))
        self.play(GrowArrow(c_vec))
        self.play(Transform(a_vec, a_n), run_time=2)

        
        #PROYECCION DE B SOBRE A
        self.play(Write(line_a_perp))
        self.play(Write(line_a))
        self.play(GrowArrow(a_vec_pro))
        self.play(FadeOut(line_a), FadeOut(line_a_perp))
        self.play(Transform(a_vec_pro, suma_a), run_time=1.5)
        self.play(GrowArrow(a_ort))
        self.play(Transform(a_ort, a_ort_n), run_time=2)
        self.play(FadeOut(a_vec_pro))
        
        #PROYECCION DE C SOBRE A
        self.play(Write(line_c_perp))
        self.play(Write(line_c))
        self.play(GrowArrow(c_vec_pro))
        self.play(FadeOut(line_c), FadeOut(line_c_perp))
        self.play(Transform(c_vec_pro, suma_c), run_time=1.5)
        self.play(GrowArrow(c_ort))
        self.play(FadeOut(c_vec_pro))
    
        
        #PROYECCION DE C SOBRE B
        self.play(Write(line_b_perp))
        self.play(Write(line_b))
        self.play(GrowArrow(b_vec_pro))
        self.play(FadeOut(line_b), FadeOut(line_b_perp))
        self.play(Transform(b_vec_pro, suma_b), run_time=1.5)
        self.play(GrowArrow(cb_ort))
        self.play(Transform(cb_ort, cb_ort_n), run_time=2)
        self.play(FadeOut(b_vec_pro), FadeOut(c_ort), FadeOut(b_vec), FadeOut(c_vec))
        #Movimiento de camara
        self.camera.set_frame_width(FRAME_WIDTH*0.5)
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
                
    def projection_of_b_and_c_along_a(self, a, b, c):


        a_vec = Vector(direction = a, color = AZUL)
        b_vec = Vector(direction = b, color = ROJO)
        c_vec = Vector(direction = c, color = NARANJA)

        #PROYECCION DE B SOBRE A 
        a_pro = projection_of_a_along_b(b, a)
        a_vec_pro = Vector(direction = a_pro, color = YELLOW, buff=0)
        line_a = DashedLine(ORIGIN, a_pro, width=5, buff = 0)
        line_a_perp = DashedLine(b, a_pro, width=5, buff=0)
        a_ort = Vector(direction = b-a_pro, color = VERDE, buff=0)
        suma_a = Arrow(start = b, end = b-a_pro, color = YELLOW, buff=0)

        #PROYECCION DE C SOBRE A 
        c_pro = projection_of_a_along_b(c, a)
        c_vec_pro = Vector(direction = c_pro, color = YELLOW, buff=0)
        line_c = DashedLine(ORIGIN, c_pro, width=5, buff = 0)
        line_c_perp = DashedLine(c, c_pro, width=5, buff=0)
        c_ort = Vector(direction = c-c_pro, color = MAGENTA, buff=0)
        suma_c = Arrow(start = c, end = c-c_pro, color = YELLOW, buff=0)

        #PROYECCION DE C SOBRE B
        b_pro = projection_of_a_along_b(c, b)
        b_vec_pro = Vector(direction = b_pro, color = YELLOW, buff=0)
        line_b = DashedLine(ORIGIN, b_pro, width=5, buff = 0)
        line_b_perp = DashedLine(c, b_pro, width=5, buff=0)
        suma_b = Arrow(start = c-c_pro, end = c-c_pro-b_pro, color = YELLOW, buff=0)
        cb_ort = Vector(direction = c-c_pro-b_pro, color = MAGENTA, buff=0)

        self.play(GrowArrow(a_vec))
        self.play(GrowArrow(b_vec))
        self.play(GrowArrow(c_vec))
        
        #PROYECCION DE B SOBRE A
        self.play(Write(line_a))
        self.play(Write(line_a_perp))
        self.play(GrowArrow(a_vec_pro))
        self.play(FadeOut(line_a), FadeOut(line_a_perp))
        self.play(Transform(a_vec_pro, suma_a), run_time=1.5)
        self.play(GrowArrow(a_ort))
        self.play(FadeOut(a_vec_pro))
        
        #PROYECCION DE C SOBRE A
        self.play(Write(line_c))
        self.play(Write(line_c_perp))
        self.play(GrowArrow(c_vec_pro))
        self.play(FadeOut(line_c), FadeOut(line_c_perp))
        self.play(Transform(c_vec_pro, suma_c), run_time=1.5)
        self.play(GrowArrow(c_ort))
        self.play(FadeOut(c_vec_pro))
    
        
        #PROYECCION DE C SOBRE B
        self.play(Write(line_b))
        self.play(Write(line_b_perp))
        self.play(GrowArrow(b_vec_pro))
        self.play(FadeOut(line_b), FadeOut(line_b_perp))
        self.play(Transform(b_vec_pro, suma_b), run_time=1.5)
        self.play(GrowArrow(cb_ort))
        self.play(FadeOut(b_vec_pro), FadeOut(c_ort), FadeOut(b_vec), FadeOut(c_vec),)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def subespacios(self, a, b, c, text, text_bg):
        
        a_vec = Vector(direction = a, color = AZUL)
        b_vec = Vector(direction = b, color = ROJO)
        c_vec = Vector(direction = c, color = NARANJA)
        
        a_vec1 = Vector(direction = a/2, color = AZUL, buff = 0)
        b_vec1 = Vector(direction = b/2, color = ROJO, buff = 0)
        c_vec1 = Vector(direction = c/2, color = NARANJA, buff = 0)
        a_vec1_suma = Arrow(start = b/2+c/2, end = a/2+b/2+c/2, color = BLUE, buff = 0).set_opacity(0.5)
        b_vec1_suma = Arrow(start = c/2, end = b/2+c/2, color = ROJO, buff = 0).set_opacity(0.5)
        c_vec1_suma = Arrow(start = b/2, end = b/2+c/2, color = NARANJA, buff = 0).set_opacity(0.5)
        suma = Vector(direction = a/2+b/2+c/2, color = MAGENTA, buff = 0)


        dotb = Dot(point = b/2, color = RED).set_opacity(0)
        dotc = Dot(point = c/2, color = RED).set_opacity(0)
        dota = Dot(point = a/2, color = RED).set_opacity(0)
        estela1 = Line(ORIGIN, ORIGIN, color = VERDE, fill_opacity = 0)
        estela2 = Line(ORIGIN, ORIGIN, color = VERDE, fill_opacity = 0)
        plano_estela1 = Rectangle( color = VERDE, buff = 0).set_opacity(0.2)
        plano_estela1.set_width(1,stretch=True)
        plano_estela1.set_height(20,stretch=True)
        plano_estela2 = Rectangle( color = VERDE, buff = 0).set_opacity(0.2)
        plano_estela2.set_width(1,stretch=True)
        plano_estela2.set_height(20,stretch=True)
        cubo1 = Prism().set_color(GREEN).set_opacity(0.3)
        cubo2 = Prism().set_color(GREEN).set_opacity(0.3)
        cubo1.set_height(20,stretch=True)
        cubo1.set_width(12,stretch=True)
        cubo1.set_depth(0.08,stretch=True)
        cubo2.set_height(20,stretch=True)
        cubo2.set_width(12,stretch=True)
        cubo2.set_depth(0.08,stretch=True)

        a_vec1.save_state()
        b_vec1.save_state()
        c_vec1.save_state()
        a_vec1_suma.save_state()
        b_vec1_suma.save_state()
        c_vec1_suma.save_state()
        suma.save_state()
        dotc.save_state()
        dota.save_state()

        def update_a(obj):
            new_vec=Vector(direction = dota.get_center(), color = AZUL)
            obj.become(new_vec)

        def update_b(obj):
            new_vec=Vector(direction = dotb.get_center(), color = ROJO)
            obj.become(new_vec)
        
        def update_c(obj):
            new_vec=Vector(direction = dotc.get_center(), color = NARANJA)
            obj.become(new_vec)

        def update_a_s(obj):
            new_vec=Arrow(start = b_vec1.get_end()+c_vec1.get_end(), end = a_vec1.get_end()+b_vec1.get_end()+c_vec1.get_end(), color = BLUE, buff = 0).set_opacity(0.5)
            obj.become(new_vec)

        def update_b_s(obj):
            new_vec=Arrow(start = c_vec1.get_end(), end = b_vec1.get_end()+c_vec1.get_end(), color = ROJO, buff = 0).set_opacity(0.5)
            obj.become(new_vec)
        
        def update_c_s(obj):
            new_vec=Arrow(start = b_vec1.get_end(), end = b_vec1.get_end()+c_vec1.get_end(), color = NARANJA, buff = 0).set_opacity(0.5)
            obj.become(new_vec)

        def update_sa(obj):
            new_vec=Vector(direction = a_vec1.get_end()+b/2+c/2, color = MAGENTA, buff = 0)
            obj.become(new_vec)

        def update_sb(obj):
            new_vec=Vector(direction = a/2+b_vec1.get_end()+c/2, color = MAGENTA, buff = 0)
            obj.become(new_vec)

        def update_sc(obj):
            new_vec=Vector(direction = a/2+b/2+c_vec1.get_end(), color = MAGENTA, buff = 0)
            obj.become(new_vec)

        def update_estela1(obj):
            new_line = Line(a/2+c/2+b/2, a/2+b_vec1.get_end()+c/2, color = VERDE).set_opacity(0.3)
            obj.become(new_line)

        def update_estela2(obj):
            new_line = Line(a/2+c/2+b/2, a/2+b_vec1.get_end()+c/2, color = VERDE).set_opacity(0.3)
            obj.become(new_line)

        def update_ps(mob,alpha):
            mob.become(mob.target)
            mob.set_width(alpha*6, stretch=True)
            mob.next_to(estela1.get_start(), RIGHT, buff = 0).rotate(-15.2*DEGREES, axis = Z_AXIS, about_point= estela1.get_start()).rotate(33.6*DEGREES, axis = X_AXIS, about_point= estela1.get_start())

        def update_ps2(mob,alpha):
            mob.become(mob.target)
            mob.set_width(alpha*6, stretch=True)
            mob.next_to(estela1.get_start(), LEFT, buff = 0).rotate(-15.2*DEGREES, axis = Z_AXIS, about_point= estela1.get_start()).rotate(33.7*DEGREES, axis = X_AXIS, about_point= estela1.get_start())

        def update_cs(mob,alpha):
            mob.become(mob.target)
            mob.set_depth(alpha*6, stretch=True)
            mob.next_to(estela2.get_start()-[0,10,0], UP+[0,0,1.5], buff=0).rotate(-15.2*DEGREES, axis = Z_AXIS, about_point= estela1.get_start()).rotate(33.6*DEGREES, axis = X_AXIS, about_point= estela1.get_start())

        def update_cs2(mob,alpha):
            mob.become(mob.target)
            mob.set_depth(alpha*6, stretch=True)
            mob.next_to(estela2.get_start()+[0,10,0], DOWN+[0,0,-1.5], buff=0).rotate(-15.2*DEGREES, axis = Z_AXIS, about_point= estela1.get_start()).rotate(33.6*DEGREES, axis = X_AXIS, about_point= estela1.get_start())

        self.play(FadeIn( b_vec1), FadeIn(c_vec1), FadeIn( a_vec1), run_time=3)
        self.play(Write(a_vec1_suma), Write(b_vec1_suma), Write(c_vec1_suma), Write(dotb), GrowArrow(suma), run_time=3)
        self.add_foreground_mobjects(b_vec1_suma)
        self.play(  UpdateFromFunc(b_vec1,update_b), 
                    UpdateFromFunc(a_vec1_suma,update_a_s),
                    UpdateFromFunc(b_vec1_suma,update_b_s), 
                    UpdateFromFunc(c_vec1_suma,update_c_s),
                    UpdateFromFunc(suma,update_sb),
                    UpdateFromFunc(estela1,update_estela1),
                    dotb.move_to, 2*(b/2), run_time=2) 
        self.add_foreground_mobjects(b_vec1_suma)
        self.play(  UpdateFromFunc(b_vec1,update_b), 
                    UpdateFromFunc(a_vec1_suma,update_a_s),
                    UpdateFromFunc(b_vec1_suma,update_b_s), 
                    UpdateFromFunc(c_vec1_suma,update_c_s), 
                    UpdateFromFunc(suma,update_sb),
                    UpdateFromFunc(estela2,update_estela2),
                    dotb.move_to, -3*(b/2), run_time=2) 
        self.play(b_vec1.restore, b_vec1_suma.restore, a_vec1_suma.restore, c_vec1_suma.restore, suma.restore, run_time = 0.5)
        self.play(GrowArrow(c_vec1_suma), Write(dotc), run_time=0.5)
        self.move_camera(phi=70*DEGREES, theta=-45*DEGREES, gamma=0*DEGREES, run_time=1)
        self.add_foreground_mobjects(c_vec1)
        self.add(plano_estela1)
        plano_estela1.generate_target()
        self.play(  UpdateFromFunc(c_vec1,update_c), 
                    UpdateFromFunc(a_vec1_suma,update_a_s),
                    UpdateFromFunc(b_vec1_suma,update_b_s), 
                    UpdateFromFunc(c_vec1_suma,update_c_s), 
                    UpdateFromFunc(suma,update_sc),
                    UpdateFromAlphaFunc(plano_estela1, update_ps),
                    dotc.move_to, 3*c, run_time=2) 
        self.play(c_vec1.restore, c_vec1_suma.restore, a_vec1_suma.restore, b_vec1_suma.restore, suma.restore, dotc.restore, run_time = 0.5)
        self.add_foreground_mobjects(c_vec1)
        self.add(plano_estela2)
        plano_estela2.generate_target()
        self.play(  UpdateFromFunc(c_vec1,update_c), 
                    UpdateFromFunc(a_vec1_suma,update_a_s),
                    UpdateFromFunc(b_vec1_suma,update_b_s), 
                    UpdateFromFunc(c_vec1_suma,update_c_s), 
                    UpdateFromFunc(suma,update_sc),
                    UpdateFromAlphaFunc(plano_estela2, update_ps2),
                    dotc.move_to, -4*c, run_time=2) 
        self.play(c_vec1.restore, c_vec1_suma.restore, a_vec1_suma.restore, b_vec1_suma.restore, suma.restore, run_time = 0.5)
        self.play(GrowArrow(a_vec1_suma), Write(dotc), run_time=0.5)
        self.move_camera(phi=80*DEGREES, theta=-0*DEGREES, gamma=0*DEGREES, run_time=2)
        self.add_foreground_mobjects(a_vec1)
        self.add(cubo1)
        cubo1.generate_target()
        self.play(  estela1.set_opacity, 0, estela2.set_opacity, 0,
                    plano_estela1.set_opacity, 0, plano_estela2.set_opacity, 0,
                    UpdateFromFunc(a_vec1,update_a), 
                    UpdateFromFunc(a_vec1_suma,update_a_s),
                    UpdateFromFunc(b_vec1_suma,update_b_s), 
                    UpdateFromFunc(c_vec1_suma,update_c_s), 
                    UpdateFromFunc(suma,update_sa),
                    UpdateFromAlphaFunc(cubo1, update_cs), 
                    dota.move_to, 1.5*a, run_time=2) 
        self.play(a_vec1.restore, a_vec1_suma.restore, b_vec1_suma.restore, c_vec1_suma.restore, suma.restore, dota.restore, run_time = 0.5)
        self.add_foreground_mobjects(a_vec1)
        self.add(cubo1)
        cubo2.generate_target()
        self.play(  UpdateFromFunc(a_vec1,update_a), 
                    UpdateFromFunc(a_vec1_suma,update_a_s),
                    UpdateFromFunc(b_vec1_suma,update_b_s), 
                    UpdateFromFunc(c_vec1_suma,update_c_s), 
                    UpdateFromFunc(suma,update_sa),
                    UpdateFromAlphaFunc(cubo2, update_cs2), 
                    dota.move_to, -1.5*a, run_time=2)
        self.add_fixed_in_frame_mobjects(text_bg)
        self.add_fixed_in_frame_mobjects(text)
        self.play(Write(text_bg), Write(text)) 
        self.wait(1.5)
        self.move_camera(phi=80*DEGREES, theta=40*DEGREES, gamma=0*DEGREES, run_time=2)
        self.play(FadeOut(a_vec1), FadeOut(b_vec1), FadeOut(c_vec1), FadeOut(cubo1), FadeOut(cubo2), FadeOut(suma), FadeOut(a_vec1_suma), FadeOut(b_vec1_suma), FadeOut(c_vec1_suma), FadeOut(text), FadeOut(text_bg), run_time = 0.5)
        



    def construct(self):
        axis_config = {
            "y_max" : 3,
            "y_min" : 0,
            "x_max" : 3,
            "x_min" : 0,
            "z_max" : 3,
            "z_min" : 0,
        }
        axes = ThreeDAxes(**axis_config)
        a = np.array([0.5, 1, 3])
        b = np.array([1, 3, 2])
        c = np.array([3, 0, 1])           

        self.set_camera_orientation(phi=80 * DEGREES, theta=30*DEGREES)
        self.play(ShowCreation(axes))
        #self.wait()
        self.parte1(a,b,c)
        
        #self.wait()
        self.set_camera_orientation(phi=80 * DEGREES, theta=40*DEGREES)
        self.play(ShowCreation(axes))
        self.wait()
        self.parte2(a,b,c)
        


	
######################################################
##### Tercera escena #################################
##### versión: Manim Community v0.4.0 ################ 
######################################################

class TerceraEscena(GraphScene,Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)
    def FadeOutWrite(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.play(Write(objeto2))
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
    config.num_graph_anchor_points = 3000,
    def construct(self):
        #------------------------------------------------------------------- GRAM-SCHMIDT normal
        seaL = (Tex('''Sea $I$ un conjunto l.i.''').scale(0.7)).to_edge(1*UP)
        left_corner = 2.7*LEFT+2.8*UP
        proceso_GM = (Tex('''\\textbf{Proceso de Gram-Schmidt}''').scale(0.7)).move_to(left_corner+LEFT)
        proceso_GM.set_color('#0087FF')
        algoritmo_left_1_1 = (Tex('''\\texttt{1.- Tomar a un vector de $I$ y}''').scale(0.7)).move_to(left_corner+0.5*DOWN+1*LEFT)
        algoritmo_left_1_2 = Tex('''\\texttt{agregarlo a un nuevo conjunto $\\Gamma$}.''').scale(0.7)
        algoritmo_paso_1 = VGroup(algoritmo_left_1_1, algoritmo_left_1_2)
        algoritmo_paso_1.arrange(0.2*DOWN, center=False, aligned_edge=LEFT)

        algoritmo_left_2_1 = (Tex('''\\texttt{2.- Tomar a otro de los vectores}''').scale(0.7)).next_to(algoritmo_paso_1, 3.5*DOWN)
        algoritmo_left_2_2 = Tex('''\\texttt{de $I$, restarle sus proyecciones}''').scale(0.7)
        algoritmo_left_2_3 = Tex('''\\texttt{sobre todos los vectores de $\\Gamma$}''').scale(0.7)
        algoritmo_left_2_4 = Tex('''\\texttt{y después agregarlo a $\\Gamma$}.''').scale(0.7)
        algoritmo_paso_2 = VGroup(algoritmo_left_2_1, algoritmo_left_2_2, algoritmo_left_2_3, algoritmo_left_2_4)
        algoritmo_paso_2.arrange(0.2*DOWN, center=False, aligned_edge=LEFT)
        algoritmo_paso_2.align_to(algoritmo_paso_1, LEFT)

        algoritmo_left_3_1 = (Tex('''\\texttt{3.- Repetir el paso 2 hasta}''').scale(0.7)).next_to(algoritmo_paso_2, 3.4*DOWN)
        algoritmo_left_3_2 = Tex('''\\texttt{que $\\Gamma$ tenga tantos vectores}''').scale(0.7)
        algoritmo_left_3_3 = Tex('''\\texttt{como $I$.}''').scale(0.7)
        algoritmo_paso_3 = VGroup(algoritmo_left_3_1, algoritmo_left_3_2, algoritmo_left_3_3)
        algoritmo_paso_3.arrange(0.2*DOWN, center=False, aligned_edge=LEFT)
        algoritmo_paso_3.align_to(algoritmo_paso_2, LEFT)

        linea = Line((0,2.5,0),(0,-2,0))

        #------------------------------------------------------------------- GRAM-SCHMIDT modificado

        right_corner = 3*RIGHT+2.8*UP
        proceso_GMM = (Tex('''\\textbf{Gram-Schmidt \\textit{modificado}}''').scale(0.7)).move_to(right_corner)
        proceso_GMM.set_color('#4FFF00')
        algoritmo_right_1_1 = (Tex('''\\texttt{1.- Tomar a un vector de $I$,}''').scale(0.7)).move_to(right_corner+0.5*DOWN)
        algoritmo_right_1_2 = Tex('''\\texttt{\\textit{normalizarlo} }''', '''\\texttt{y agregarlo a}''').scale(0.7)
        algoritmo_right_1_2[0].set_color('#4FFF00')
        algoritmo_right_1_3 = Tex('''\\texttt{un nuevo conjunto $N$}.''').scale(0.7)
        algoritmor_paso_1 = VGroup(algoritmo_right_1_1, algoritmo_right_1_2, algoritmo_right_1_3)
        algoritmor_paso_1.arrange(0.2*DOWN, center=False, aligned_edge=LEFT)

        algoritmo_right_2_1 = (Tex('''\\texttt{2.- Tomar a otro de los vectores}''').scale(0.7)).next_to(algoritmor_paso_1, 2*DOWN)
        algoritmo_right_2_2 = Tex('''\\texttt{de $I$, restarle sus proyecciones}''').scale(0.7)
        algoritmo_right_2_3 = Tex('''\\texttt{sobre todos los vectores de $N$, }''').scale(0.7)
        algoritmo_right_2_4 = Tex('''\\texttt{\\textit{normalizarlo}''', '''\\texttt{, y después}''').scale(0.7)
        algoritmo_right_2_4[0].set_color('#4FFF00')
        algoritmo_right_2_5 = Tex('''\\texttt{agregarlo a $N$}.''').scale(0.7)
        algoritmor_paso_2 = VGroup(algoritmo_right_2_1, algoritmo_right_2_2, algoritmo_right_2_3, algoritmo_right_2_4, algoritmo_right_2_5)
        algoritmor_paso_2.arrange(0.2*DOWN, center=False, aligned_edge=LEFT)
        algoritmor_paso_2.align_to(algoritmor_paso_1, LEFT)

        algoritmo_right_3_1 = (Tex('''\\texttt{3.- Repetir el paso 2 hasta}''').scale(0.7)).next_to(algoritmor_paso_2, 2*DOWN)
        algoritmo_right_3_2 = Tex('''\\texttt{que $N$ tenga tantos vectores}''').scale(0.7)
        algoritmo_right_3_3 = Tex('''\\texttt{como $I$.}''').scale(0.7)
        algoritmor_paso_3 = VGroup(algoritmo_right_3_1, algoritmo_right_3_2, algoritmo_right_3_3)
        algoritmor_paso_3.arrange(0.2*DOWN, center=False, aligned_edge=LEFT)
        algoritmor_paso_3.align_to(algoritmor_paso_2, LEFT)
        

        conclusiones = (Tex(
            "\\quad", #0
            "¡$\\Gamma$ es ortogonal!", #1
            "\\quad\\quad\\quad", #2
            "$\\langle \\Gamma\\rangle = \\langle I\\rangle = \\langle N\\rangle$", #3
            "\\quad\\quad\\quad", #4
            "¡$N$ es ortonormal!" #5
        ).scale(0.7)).next_to(linea, 2*DOWN)

        framebox1 = SurroundingRectangle(conclusiones[1],color=YELLOW,fill_color=BLACK, buff = .1)
        framebox2 = SurroundingRectangle(conclusiones[3],color=YELLOW,fill_color=BLACK, buff = .1)
        framebox3 = SurroundingRectangle(conclusiones[5],color=YELLOW,fill_color=BLACK, buff = .1)
        #------------------------------------------------------------------- Teorema de Gram-Schmidt
        tex_8 = Tex("Teorema de Gram-Schmidt").scale(0.9).to_edge(UP)
        tex_1 = MathTex("\\text{dim}(V)=k<\\infty").scale(0.6).next_to(tex_8, DOWN)
        tex_2_1 = MathTex("\\beta = \\{\\vec{b}_1,..., \\vec{b}_k\\}").scale(0.6).move_to(left_corner+1.8*LEFT+0.7*DOWN)
        tex_2_2 = MathTex("\\langle\\beta\\rangle = V").scale(0.6).next_to(tex_2_1,DOWN)
        tex_2_3 = Tex("$\\beta$ es l.i.").scale(0.6).next_to(tex_2_2,DOWN)
        tex_2 = VGroup(tex_2_1, tex_2_2, tex_2_3)
        tex_4_1 = MathTex("\\Gamma = \\{\\vec{g}_1,..., \\vec{g}_k\\}").scale(0.6).next_to(tex_2[0], 5*RIGHT)
        tex_4_2 = MathTex("\\langle\\Gamma\\rangle = V").scale(0.6).next_to(tex_4_1,DOWN)
        tex_4_3 = Tex("$\\Gamma$ es l.i.").scale(0.6).next_to(tex_4_2,DOWN)
        tex_4 = VGroup(tex_4_1, tex_4_2, tex_4_3)
        tex_6_1 = MathTex("N = \\{\\hat{n}_1,..., \\hat{n}_k\\}").scale(0.6).next_to(tex_4[0], 14*RIGHT)
        tex_6_2 = MathTex("\\langle N\\rangle = V").scale(0.6).next_to(tex_6_1,DOWN)
        tex_6_3 = Tex("N es l.i.").scale(0.6).next_to(tex_6_2,DOWN)
        tex_6 = VGroup(tex_6_1, tex_6_2, tex_6_3)
        tex_3_1 = MathTex("\\vec{g}_1:=\\vec{b}_1").scale(0.6).next_to(tex_4,2.5*DOWN)
        tex_3_2 = MathTex("""\\vec{g}_j:=
                        \\vec{b}_j
                        -
                        \\displaystyle\\sum_{i=1}^{j-1}
                        \\dfrac{\\langle\\vec{b}_j, \\vec{g}_i\\rangle}
                        {\\left\\Vert\\vec{g}_i\\right\\Vert}
                        \\hat{g}_i,\\quad 1<j\\leq k
                        """).scale(0.6).next_to(tex_3_1,2.5*DOWN)
        tex_3 = VGroup(tex_3_1, tex_3_2)
        tex_5_1 = MathTex("\\hat{n}_1:=\\dfrac{\\vec{b}_1}{\\left\\Vert\\vec{b}_1\\right\\Vert}").scale(0.6).next_to(tex_6,1.5*DOWN)
        tex_5_2 = MathTex("""\\hat{n}_j:=
                        \\dfrac{
                        \\vec{b}_j
                        -
                        \\displaystyle\\sum_{i=1}^{j-1}
                        \\langle\\vec{b}_j, \\hat{n}_i\\rangle
                        \\hat{n}_i
                        }
                        {
                        \\left\\Vert
                        \\vec{b}_j
                        -
                        \\displaystyle\\sum_{i=1}^{j-1}
                        \\langle\\vec{b}_j, \\hat{n}_i\\rangle
                        \\hat{n}_i
                        \\right\\Vert
                        }
                        ,\\quad 1<j\\leq k
                        """).scale(0.6).next_to(tex_5_1,1.5*DOWN)
        tex_5 = VGroup(tex_5_1, tex_5_2)
        tex_7_1 = Tex("$\\beta$ es base de $V$").scale(0.6).next_to(tex_2, 16*DOWN )
        arrow = Tex("$\\Longrightarrow$").scale(0.6).next_to(tex_7_1,1.5*RIGHT)
        tex_7_2 = Tex("$\\Gamma$ es base ortogonal de $V$,").scale(0.6).align_to(tex_7_1,UP).align_to(tex_4,LEFT)
        tex_7_3 = Tex("$N$ es base ortonormal de $V$").scale(0.6).align_to(tex_7_1,UP).align_to(tex_5[1],LEFT)
        tex_7 = VGroup(tex_7_1, arrow, tex_7_2, tex_7_3)

        tex_teorema = [tex_1, tex_2, tex_3, tex_4, tex_5, tex_6, tex_7, tex_8]


        #------------------------------------------------------------------- Pregunta y ejercicios
        ejercicio_1_1 = Tex("Ejercicio 2.1. ","Demuestra que").scale(0.7)
        ejercicio_1_2 = MathTex("""\\Bigg\\langle
                                \\qty\\Bigg{
                                \\vec{u},\\vec{v}-\\dfrac{\\langle\\vec{u}, \\vec{v}\\rangle}
                                {\\left\\Vert\\vec{u}\\right\\Vert}\\hat{u}
                                """).scale(0.7)
        ejercicio_1_2_ = MathTex(
                                """
                                \\Bigg\\rangle 
                                = 
                                \\langle
                                \\{\\vec{u},\\vec{v}\\}
                                \\rangle
                                """).scale(0.7).next_to(ejercicio_1_2,0.3*RIGHT)
        ejercicio_1_2 = VGroup(ejercicio_1_2, ejercicio_1_2_)
        ejercicio_1_3 = Tex("para $\\vec{u},\\vec{v}\\in V$ con $\\vec{u},\\vec{v}\\neq\\vec{0}$ y dibuja un ejemplo en $\\mathbb{R}^2$.").scale(0.7)
        ejercicio_1_1[0].set_color('#0087FF')
        ejercicioG_1 = VGroup(ejercicio_1_1, ejercicio_1_2, ejercicio_1_3)
        ejercicioG_1.arrange(0.5*DOWN, center=False, aligned_edge=LEFT)
        ejercicioG_1.move_to(2*UP)

        ejercicio_2_1 = Tex("Ejercicio 2.2. ","Supongamos que $V$ tiene dimensión finita. \n").scale(0.7)
        ejercicio_2_2 = Tex("Demuestra que, para $1\\leq k\\leq \\text{dim}(V)$, cualquier conjunto\n").scale(0.7)
        ejercicio_2_3 = Tex("ortogonal de $k$ vectores es linealmente independiente.\n").scale(0.7)
        ejercicio_2_1[0].set_color('#0087FF')
        ejercicioG_2 = VGroup(ejercicio_2_1, ejercicio_2_2, ejercicio_2_3)
        ejercicioG_2.arrange(0.5*DOWN, center=False, aligned_edge=LEFT)
        ejercicioG_2.align_to(ejercicioG_1, LEFT)

        pregunta_1 = Tex("Pregunta: ",'''¿Qué sucedería si aplicáramos el proceso de\n''').scale(0.7)
        pregunta_2 = Tex("Gram-Schmidt a un conjunto linealmente \\textit{dependiente}\n").scale(0.7)
        pregunta_3 = Tex("de $k$ vectores?").scale(0.7)
        pregunta_1[0].set_color('#FF0000')
        preguntaG = VGroup(pregunta_1, pregunta_2, pregunta_3)
        preguntaG.arrange(0.5*DOWN, center=False, aligned_edge=LEFT)
        preguntaG.align_to(ejercicioG_2, LEFT)
        preguntaG.move_to(2*DOWN)


        
        
        
        
        
        ###ANIMACIONES
        #--------------------------------
        self.play(Write(seaL))
        self.play(Write(proceso_GM))
        self.play(Write(algoritmo_paso_1))
        self.wait(2)
        self.play(Write(algoritmo_paso_2))
        self.wait(2)
        self.play(Write(algoritmo_paso_3))
        self.wait(2)
        self.play(Create(linea))

        self.play(Write(proceso_GMM))
        self.wait(2)
        self.play(Write(algoritmor_paso_1))
        self.wait(2)
        self.play(Write(algoritmor_paso_2))
        self.wait(2)
        self.play(Write(algoritmor_paso_3))
        self.wait(3)

        self.play(
            FadeIn(conclusiones[1]),
            run_time = 2
        )
        self.play(
            FadeIn(conclusiones[5]),
            run_time = 2
        )
        self.play(
            FadeIn(conclusiones[3]),
            run_time = 2
        )

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        #--------------------------------
        '''

        Teorema

        '''
        #--------------------------------
        for j,i in enumerate(tex_teorema):
            if j == 6:
                for k in i:
                    self.play(Write(k))
                    self.wait(2)
            else:
                self.play(Write(i))
                self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        #--------------------------------
        '''

        Pregunta y ejercicios

        '''
        #--------------------------------
        self.play(Write(ejercicioG_1))
        self.wait(2)
        self.play(Write(ejercicioG_2))
        self.wait(2)
        self.play(Write(preguntaG))
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
