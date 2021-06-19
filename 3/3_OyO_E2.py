from manimlib.imports import *


#####################################################################################
######################  Ortogonalización y ortonormalización  #######################
#####################################################################################
	
#####################################################################################
#################################  Segunda escena  ##################################
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

class TipableVMobject(VMobject):
    """
    Meant for shared functionality between Arc and Line.
    Functionality can be classified broadly into these groups:

        * Adding, Creating, Modifying tips
            - add_tip calls create_tip, before pushing the new tip
                into the TipableVMobject's list of submobjects
            - stylistic and positional configuration

        * Checking for tips
            - Boolean checks for whether the TipableVMobject has a tip
                and a starting tip

        * Getters
            - Straightforward accessors, returning information pertaining
                to the TipableVMobject instance's tip(s), its length etc

    """
    CONFIG = {
        "tip_length": DEFAULT_ARROW_TIP_LENGTH,
        # TODO
        "normal_vector": OUT,
        "tip_style": {
            "fill_opacity": 1,
            "stroke_width": 0,
        }
    }
    
    # Adding, Creating, Modifying tips

    def add_tip(self, tip_length=None, at_start=False):
        """
        Adds a tip to the TipableVMobject instance, recognising
        that the endpoints might need to be switched if it's
        a 'starting tip' or not.
        """
        tip = self.create_tip(tip_length, at_start)
        self.reset_endpoints_based_on_tip(tip, at_start)
        self.asign_tip_attr(tip, at_start)
        self.add(tip)
        return self

    def create_tip(self, tip_length=None, at_start=False):
        """
        Stylises the tip, positions it spacially, and returns
        the newly instantiated tip to the caller.
        """
        tip = self.get_unpositioned_tip(tip_length)
        self.position_tip(tip, at_start)
        return tip

    def get_unpositioned_tip(self, tip_length=None):
        """
        Returns a tip that has been stylistically configured,
        but has not yet been given a position in space.
        """
        if tip_length is None:
            tip_length = self.get_default_tip_length()
        color = self.get_color()
        style = {
            "fill_color": color,
            "stroke_color": color
        }
        style.update(self.tip_style)
        tip = ArrowTip(length=tip_length, **style)
        return tip

    def position_tip(self, tip, at_start=False):
        # Last two control points, defining both
        # the end, and the tangency direction
        if at_start:
            anchor = self.get_start()
            handle = self.get_first_handle()
        else:
            handle = self.get_last_handle()
            anchor = self.get_end()
        tip.rotate(
            angle_of_vector(handle - anchor) -
            PI - tip.get_angle()
        )
        angle = angle_of_vector(handle - anchor) + PI/2

        a = np.array([np.cos(angle),np.sin(angle),0])

        tip.rotate(-phi_of_vector(handle - anchor),a)

        tip.shift(anchor - tip.get_tip_point())
        return tip

    def reset_endpoints_based_on_tip(self, tip, at_start):
        if self.get_length() == 0:
            # Zero length, put_start_and_end_on wouldn't
            # work
            return self

        if at_start:
            self.put_start_and_end_on(
                tip.get_base(), self.get_end()
            )
        else:
            self.put_start_and_end_on(
                self.get_start(), tip.get_base(),
            )
        return self

    def asign_tip_attr(self, tip, at_start):
        if at_start:
            self.start_tip = tip
        else:
            self.tip = tip
        return self

    # Checking for tips

    def has_tip(self):
        return hasattr(self, "tip") and self.tip in self

    def has_start_tip(self):
        return hasattr(self, "start_tip") and self.start_tip in self


    # Getters

    def pop_tips(self):
        start, end = self.get_start_and_end()
        result = VGroup()
        if self.has_tip():
            result.add(self.tip)
            self.remove(self.tip)
        if self.has_start_tip():
            result.add(self.start_tip)
            self.remove(self.start_tip)
        self.put_start_and_end_on(start, end)
        return result

    def get_tips(self):
        """
        Returns a VGroup (collection of VMobjects) containing
        the TipableVMObject instance's tips.
        """
        result = VGroup()
        if hasattr(self, "tip"):
            result.add(self.tip)
        if hasattr(self, "start_tip"):
            result.add(self.start_tip)
        return result

    def get_tip(self):
        """Returns the TipableVMobject instance's (first) tip,
        otherwise throws an exception."""
        tips = self.get_tips()
        if len(tips) == 0:
            raise Exception("tip not found")
        else:
            return tips[0]

    def get_default_tip_length(self):
        return self.tip_length

    def get_first_handle(self):
        return self.points[1]

    def get_last_handle(self):
        return self.points[-2]

    def get_end(self):
        if self.has_tip():
            return self.tip.get_start()
        else:
            return VMobject.get_end(self)

    def get_start(self):
        if self.has_start_tip():
            return self.start_tip.get_start()
        else:
            return VMobject.get_start(self)

    def get_length(self):
        start, end = self.get_start_and_end()
        return get_norm(start - end)

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

def phi_of_vector(vector):
    vector += 1e-8
    xy = complex(*vector[:2])
    if xy == 0:
        return 0
    a = ((vector[:1])**2 + (vector[1:2])**2)**(1/2)
    vector[0] = a
    vector[1] = vector[2]
    return np.angle(complex(*vector[:2]))



class SegundaEscena(ThreeDScene):

    def parte1(self, a, b, c):
                text1 = TexMobject(r"I = \qty\big{\vec{a}, \vec{b}, \vec{c} \ }").move_to(DOWN+5*RIGHT)
                text1[0][3:5].set_color(AZUL)
                text1[0][6:8].set_color(ROJO)
                text1[0][9:11].set_color(NARANJA)
                text1_bg=SurroundingRectangle(text1, color=WHITE, fill_color=BLACK, fill_opacity=1)
                text2 = TexMobject(r'''\Gamma_1 = \qty\big{ \vec{a}, \vec{b} ', \vec{c} \hspace{0.1cm} '  } ''').next_to(text1, 1.3*DOWN)
                text2[0][4:6].set_color(AZUL)
                text2[0][7:10].set_color(VERDE)
                text2[0][11:14].set_color(MAGENTA)
                text2_bg=SurroundingRectangle(text2, color=WHITE, fill_color=BLACK, fill_opacity=1)
                text3 = TexMobject(r"\langle \ I \ \rangle").move_to(DOWN-5*RIGHT)
                text3.set_color(MAGENTA)
                text3_bg=SurroundingRectangle(text3, color=WHITE, fill_color=BLACK, fill_opacity=1)
                text4 = TextMobject("¿", "?").scale(5).to_edge(UL)
                text5 = TexMobject(r"\langle \ I \ \rangle \ ", r" = ", r" \langle \ \Gamma_1 \ \rangle").move_to(DOWN-4.3*RIGHT)
                text5[0].set_color(MAGENTA)
                text5[2].set_color(TEAL_A)
                text5_bg=SurroundingRectangle(text5, color=WHITE, fill_color=BLACK, fill_opacity=1)
                
                #axb = [-8.5, 5, -0.25]
                a_vec = Vector(direction = a, color = AZUL)
                b_vec = Vector(direction = b, color = ROJO)
                c_vec = Vector(direction = c, color = NARANJA)
                a_vec_label = TexMobject(r"\vec{a}").move_to(0.8*RIGHT+2.3*UP)
                a_vec_label[0].set_color(AZUL)
                b_vec_label = TexMobject(r"\vec{b}").move_to(1.5*RIGHT+1.3*UP)
                b_vec_label[0].set_color(ROJO)
                c_vec_label = TexMobject(r"\vec{c}").move_to(-1.2*RIGHT+0.9*UP)
                c_vec_label[0].set_color(NARANJA)
                a_vec.save_state()
                b_vec.save_state()
                c_vec.save_state()
                a_li = DashedLine(-10*a, 10*a, color=MAGENTA).set_opacity(0.7)
                b_li = DashedLine(-10*b, 10*b, color=MAGENTA).set_opacity(0.7)
                c_li = DashedLine(-10*c, 10*c, color=MAGENTA).set_opacity(0.7)


                #PROYECCION DE B SOBRE A 
                plane1 = plane()
                y_axis = DoubleArrow(start=np.array([0,-8,0]), end=np.array([0,8,0]), color=WHITE, stroke_width=3)
                z_axis = DoubleArrow(start=np.array([0,0,-4]), end=np.array([0,0,4]), color=WHITE, stroke_width=3)

                a_pro = projection_of_a_along_b(b, a)
                a_vec_pro = Vector(direction = a_pro, color = YELLOW, buff=0)
                a_vec_pro_label=TexMobject(r"-", r" \frac{\langle \ \vec{b}, \vec{a} \ \rangle}{||\vec{a}||}\hat{a} ").move_to(1.5*RIGHT+2.7*UP).scale(0.7)
                a_vec_pro_label[0].set_color(BLACK)                
                a_vec_pro_labelc=TexMobject(r" -  ").move_to(1.8*RIGHT+0.5*DOWN).scale(0.7)
                a_vec_pro_label[1].set_color(YELLOW)
                a_vec_pro_labelc.set_color(YELLOW)
                a_ort = Vector(direction = b-a_pro, color = VERDE, buff=0)
                a_ort_label=TexMobject(r"\vec{b}'")
                a_ort.save_state()
                a_ort_label.set_color(VERDE).move_to(1.3*RIGHT+1.4*DOWN)
                suma_a = Arrow(start = b, end = b-a_pro, color = YELLOW, buff=0)

                #PROYECCION DE C SOBRE A 
                c_pro = projection_of_a_along_b(c, a)
                c_vec_pro = Vector(direction = c_pro, color = YELLOW, buff=0)
                c_vec_pro_label=TexMobject(r"-", r" \frac{\langle \ \vec{c}, \vec{a} \ \rangle}{||\vec{a}||}\hat{a} ").move_to(0.2*RIGHT+1.65*UP).scale(0.7)
                c_vec_pro_label[0].set_color(BLACK)  
                c_vec_pro_labelc=TexMobject(r" -  ").move_to(2.8*LEFT+0.6*DOWN).scale(0.7)
                c_vec_pro_labelc.set_color(YELLOW)
                c_vec_pro_label[1].set_color(YELLOW)
                line_c_perp = DashedLine(c, c_pro, width=5, buff=0, color=YELLOW)
                c_ort = Vector(direction = c-c_pro, color = MAGENTA, buff=0)
                suma_c = Arrow(start = c, end = c-c_pro, color = YELLOW, buff=0)
                t1 = Line(ORIGIN, [-1,-1,0], color = ROJO)
                t2 = Line([0,-1,0], [-1,0,0], color = ROJO)
                tache = VGroup(t1, t2).scale(0.3).move_to(0.6*LEFT+0.3*DOWN)

                #PROYECCION DE C SOBRE B'
                b_pro = projection_of_a_along_b(c, b-a_pro)
                b_vec_pro = Vector(direction = b_pro, color = YELLOW, buff=0, max_tip_length_to_length_ratio = 0.4)
                b_vec_pro_label=TexMobject(r"-", r" \frac{\langle \ \vec{c}, \vec{b'} \ \rangle}{||\vec{b'}||}\hat{b'} ").move_to(1.4*RIGHT+0.3*DOWN).scale(0.7)
                b_vec_pro_label[0].set_color(BLACK)  
                b_vec_pro_labelc=TexMobject(r" -  ").move_to(3.1*LEFT+0.65*DOWN).scale(0.7)
                b_vec_pro_label[1].set_color(YELLOW)
                b_vec_pro_labelc.set_color(YELLOW)
                line_b_perp = DashedLine(c, b_pro, width=5, buff=0, color= YELLOW)
                suma_b = Arrow(start = c-c_pro, end = c-c_pro-b_pro, color = YELLOW, buff=0, max_tip_length_to_length_ratio = 0.4)
                cb_ort = Vector(direction = c-c_pro-b_pro, color = MAGENTA, buff=0)
                cb_ort.save_state()
                cb_ort_label=TexMobject(r"\vec{c}\hspace{0.1cm}'")
                cb_ort_label.set_color(MAGENTA).move_to(1.7*LEFT-0.5*DOWN)
                p1 = Line(ORIGIN, [1,1,0], color = VERDE)
                p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE)
                paloma = VGroup(p1,p2).scale(0.3).move_to(0.6*LEFT+0.1*UP)


            
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
                self.play(Write(a_li))
                self.play(Write(b_li))
                self.add_foreground_mobject(c_vec)
                self.play(Write(c_li))
                self.wait(2)
                self.play(FadeOut(a_li), FadeOut(b_li), FadeOut(c_li))
                self.add_foreground_mobjects(text1_bg, text1)
                self.add_fixed_in_frame_mobjects(text1_bg)
                self.add_fixed_in_frame_mobjects(text1)
                self.play(Write(text1_bg), Write(text1))
                
                #SUBESPACIOS
                
                self.play(a_vec_label.set_opacity, 0, b_vec_label.set_opacity, 0, c_vec_label.set_opacity, 0)
                self.move_camera(phi=20*DEGREES, theta=-15*DEGREES, gamma = 0*DEGREES, run_time=1)
                self.subespacios(a,b,c,a_vec,b_vec,c_vec, -21.7, 23.5, 84.5*DEGREES, text3, text3_bg, MAGENTA)
                self.move_camera(phi=85*DEGREES, theta=40*DEGREES, run_time = 1)
                self.play(a_vec_label.set_opacity, 1, b_vec_label.set_opacity, 1, c_vec_label.set_opacity, 1,
                        run_time=1.5)
                
                
                #PROYECCION DE B SOBRE A
                
                self.move_camera(phi=90*DEGREES, theta=0*DEGREES, gamma=0*DEGREES)
                #self.play(b_vec_label.move_to, 2.7*RIGHT+1.4*UP, a_vec_label.move_to, 0.85*RIGHT+2.2*UP)
                self.add_foreground_mobject(plane1)
                self.add_foreground_mobjects(y_axis, z_axis, a_vec, b_vec)
                self.play(ShowCreation(plane1), FadeIn(y_axis), FadeIn(z_axis), c_vec.set_opacity, 0, c_vec_label.set_opacity, 0)
                self.add_foreground_mobjects(text2_bg, text2[0][:7], text2[0][-1])
                self.add_fixed_in_frame_mobjects(text2_bg)
                self.add_fixed_in_frame_mobjects(text2[0][:7])
                self.add_fixed_in_frame_mobjects(text2[0][-1])
                self.play(Write(text2_bg), Write(text2[0][:7]), Write(text2[0][-1].move_to(2*DOWN+5.8*RIGHT)))
                self.add_foreground_mobjects(luz, text1_bg, text1, text2_bg, text2[0][:7], text2[0][-1])
                self.play(ShowCreation(luz))
                self.add_foreground_mobjects(a_vec_pro_label, a_vec_pro)
                self.add_fixed_in_frame_mobjects(a_vec_pro_label)
                self.play(GrowArrow(a_vec_pro), Write(a_vec_pro_label))
                self.wait(1.5)
                self.play(FadeOut(luz), b_vec_label.set_opacity, 1)
                self.add_foreground_mobjects(a_vec_pro_labelc)
                self.add_fixed_in_frame_mobjects(a_vec_pro_labelc)
                self.play(Transform(a_vec_pro, suma_a), AnimationGroup(ApplyMethod(a_vec_pro_label.move_to, 2.5*RIGHT+0.5*DOWN), Write(a_vec_pro_labelc), lag_ratio = 0.3), run_time=3)
                #self.play(Transform(a_vec_pro, suma_a), a_vec_pro_label.move_to, 2.5*RIGHT+0.5*DOWN, a_vec_pro_label[0].set_color, YELLOW,  run_time=3)
                self.add_foreground_mobject(a_ort_label)
                self.add_foreground_mobject(a_ort)
                self.add_fixed_in_frame_mobjects(a_ort_label)
                self.play(GrowArrow(a_ort), Write(a_ort_label))
                self.play(FadeOut(a_vec_pro),FadeOut(a_vec_pro_label),FadeOut(a_vec_pro_labelc))
                self.add_foreground_mobject(text2[0][7:10])
                self.add_fixed_in_frame_mobjects(text2[0][7:10])
                self.play(Write(text2[0][7:10]))
                self.wait()
                self.play(FadeOut(plane1), FadeOut(y_axis), FadeOut(z_axis))
                self.play(c_vec.set_opacity, 1, c_vec_label.set_opacity, 1)
                self.move_camera(phi=85*DEGREES, theta=40*DEGREES, run_time=2)
                self.play(a_ort_label.move_to, 1*RIGHT+1.2*DOWN, text2[0][-1].move_to, 2*DOWN+6.6*RIGHT)
                self.remove_foreground_mobjects(a_vec_pro_label, a_vec, b_vec_pro_label, b_vec, text2_bg, text2[0][:7], text2[0][-1])
                
                #PROYECCION DE C SOBRE A
                self.play(Write(line_c_perp))
                self.wait()
                self.add_fixed_in_frame_mobjects(c_vec_pro_label)
                self.play(GrowArrow(c_vec_pro), Write(c_vec_pro_label))
                self.play(FadeOut(line_c_perp))
                self.wait(1.5)
                self.add_fixed_in_frame_mobjects(c_vec_pro_labelc)
                self.play(Transform(c_vec_pro, suma_c), AnimationGroup(ApplyMethod(c_vec_pro_label.move_to, 2.1*LEFT+0.6*DOWN), Write(c_vec_pro_labelc), lag_ratio = 0.3), run_time=3)
                #self.play(Transform(c_vec_pro, suma_c), c_vec_pro_label.move_to, 2.1*LEFT+0.6*DOWN, c_vec_pro_label[0].set_color, YELLOW,  run_time=3)
                self.play(GrowArrow(c_ort))
                self.add_fixed_in_frame_mobjects(tache)
                self.play(Write(tache))
                self.wait()
                self.play(FadeOut(c_ort), FadeOut(c_vec_pro_label), FadeOut(tache), FadeOut(c_vec_pro_labelc))
            
                
                #PROYECCION DE C SOBRE B'
                self.add_foreground_mobjects(line_b_perp)
                self.play(Write(line_b_perp))
                self.wait()
                self.add_foreground_mobjects(b_vec_pro)
                self.add_fixed_in_frame_mobjects(b_vec_pro_label)
                self.play(GrowArrow(b_vec_pro), Write(b_vec_pro_label))
                self.play(FadeOut(line_b_perp))
                self.wait(1.5)
                self.add_fixed_in_frame_mobjects(b_vec_pro_labelc)
                self.play(Transform(b_vec_pro, suma_b), AnimationGroup(ApplyMethod(b_vec_pro_label.move_to, 2.3*LEFT+0.65*DOWN), Write(b_vec_pro_labelc), lag_ratio = 0.3), run_time=3)
                #self.play(Transform(b_vec_pro, suma_b), b_vec_pro_label.move_to, 2.3*LEFT+0.65*DOWN, b_vec_pro_label[0].set_color, YELLOW,  run_time=3)
                self.add_fixed_in_frame_mobjects(cb_ort_label)
                self.play(GrowArrow(cb_ort), Write(cb_ort_label))
                self.add_fixed_in_frame_mobjects(paloma)
                self.play(Write(paloma))
                self.wait()
                self.play(FadeOut(b_vec_pro), FadeOut(b_vec_pro_label),FadeOut(paloma), FadeOut(c_vec_pro), FadeOut(b_vec), FadeOut(b_vec_label), FadeOut(c_vec), FadeOut(c_vec_label), FadeOut(b_vec_pro_labelc))
                self.add_fixed_in_frame_mobjects(text2[0][10:14])
                self.play(Write(text2[0][10:14]))
                self.wait()
                self.add_foreground_mobjects(text2_bg, text2)
                
                #SUBESPACIOS
                
                self.play(a_vec_label.set_opacity, 0, a_ort_label.set_opacity, 0, cb_ort_label.set_opacity, 0)
                self.move_camera(phi=50*DEGREES, theta=53*DEGREES, gamma=0*DEGREES, run_time=2)
                self.subespacios(a,b-a_pro,c-c_pro-b_pro, a_vec, a_ort, cb_ort, -23.6, -42, 81.7*DEGREES, text5, text5_bg, TEAL_A)
                self.move_camera(phi=85*DEGREES, theta=40*DEGREES, run_time=1)
                self.play(a_vec.restore, a_ort.restore, cb_ort.restore, 
                        a_vec_label.set_opacity, 1, a_ort_label.set_opacity, 1, cb_ort_label.set_opacity, 1,
                        run_time=1.5)
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
                a_n = Vector(direction = a_vec_norm, color=AZUL, buff=0, max_tip_length_to_length_ratio = 0.4)

                #PROYECCION DE B SOBRE A 
                a_pro = projection_of_a_along_b(b, a)
                a_vec_pro = Vector(direction = a_pro, color = YELLOW, buff=0)
                line_a = DashedLine(ORIGIN, a_pro, width=5, buff = 0, color= YELLOW)
                line_a_perp = DashedLine(b, a_pro, width=5, buff=0, color= YELLOW)
                suma_a = Arrow(start = b, end = b-a_pro, color = YELLOW, buff=0)
                a_ort = Vector(direction = b-a_pro, color = VERDE, buff=0)
                a_ort_norm = vector_normal(b-a_pro)
                a_ort_n = Vector(direction = a_ort_norm, color=VERDE, buff=0, max_tip_length_to_length_ratio = 0.4)

                #PROYECCION DE C SOBRE A 
                c_pro = projection_of_a_along_b(c, a)
                c_vec_pro = Vector(direction = c_pro, color = YELLOW, buff=0)
                line_c = DashedLine(ORIGIN, c_pro, width=5, buff = 0, color= YELLOW)
                line_c_perp = DashedLine(c, c_pro, width=5, buff=0, color= YELLOW)
                c_ort = Vector(direction = c-c_pro, color = MAGENTA, buff=0)
                suma_c = Arrow(start = c, end = c-c_pro, color = YELLOW, buff=0)

                #PROYECCION DE C SOBRE B'
                b_pro = projection_of_a_along_b(c, b-a_pro)
                b_vec_pro = Vector(direction = b_pro, color = YELLOW, buff=0, max_tip_length_to_length_ratio = 0.4)
                line_b = DashedLine(ORIGIN, b_pro, width=5, buff = 0, color= YELLOW)
                line_b_perp = DashedLine(c, b_pro, width=5, buff=0, color= YELLOW)
                suma_b = Arrow(start = c-c_pro, end = c-c_pro-b_pro, color = YELLOW, buff=0, max_tip_length_to_length_ratio = 0.4)
                cb_ort = Vector(direction = c-c_pro-b_pro, color = MAGENTA, buff=0)
                cb_ort_norm = vector_normal(c-c_pro-b_pro)
                cb_ort_n = Vector(direction = cb_ort_norm, color=MAGENTA, buff=0, max_tip_length_to_length_ratio = 0.4)
                ref=Dot(color=YELLOW,radius=0.003)

                self.play(GrowArrow(a_vec))
                self.play(GrowArrow(b_vec))
                self.play(GrowArrow(c_vec))
                self.play(Transform(a_vec, a_n), run_time=2)

                
                #PROYECCION DE B SOBRE A
                self.play(Write(line_a_perp))
                self.play(GrowArrow(a_vec_pro))
                self.play(FadeOut(line_a), FadeOut(line_a_perp))
                self.play(Transform(a_vec_pro, suma_a), run_time=1.5)
                self.play(GrowArrow(a_ort))
                self.play(FadeOut(a_vec_pro))
                self.play(Transform(a_ort, a_ort_n), run_time=2)
                
                #PROYECCION DE C SOBRE A
                self.play(Write(line_c_perp))
                self.play(GrowArrow(c_vec_pro))
                self.play(FadeOut(line_c), FadeOut(line_c_perp))
                self.play(Transform(c_vec_pro, suma_c), run_time=1.5)
                self.play(GrowArrow(c_ort))
                self.wait()
                self.play(FadeOut(c_ort))
            
                
                #PROYECCION DE C SOBRE B'
                self.play(Write(line_b_perp))
                self.play(GrowArrow(b_vec_pro))
                self.play(FadeOut(line_b), FadeOut(line_b_perp))
                self.play(Transform(b_vec_pro, suma_b), run_time=1.5)
                self.play(GrowArrow(cb_ort))
                self.play(FadeOut(b_vec_pro), FadeOut(c_vec_pro), FadeOut(b_vec), FadeOut(c_vec))
                self.play(Transform(cb_ort, cb_ort_n), run_time=2)
                self.wait()
                self.wait()
                self.play(
                    *[FadeOut(mob)for mob in self.mobjects]
                    # All mobjects in the screen are saved in self.mobjects
                )
                        
    def projection_of_b_and_c_along_a(self, a, b, c, a_vec, b_vec, c_vec):


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

                #PROYECCION DE C SOBRE B'
                b_pro = projection_of_a_along_b(c, b-a_pro)
                b_vec_pro = Vector(direction = b_pro, color = YELLOW, buff=0, max_tip_length_to_length_ratio = 0.4)
                line_b = DashedLine(ORIGIN, b_pro, width=5, buff = 0)
                line_b_perp = DashedLine(c, b_pro, width=5, buff=0)
                suma_b = Arrow(start = c-c_pro, end = c-c_pro-b_pro, color = YELLOW, buff=0, max_tip_length_to_length_ratio = 0.4)
                cb_ort = Vector(direction = c-c_pro-b_pro, color = MAGENTA, buff=0)

                self.play(GrowArrow(a_vec))
                self.play(GrowArrow(b_vec))
                self.play(GrowArrow(c_vec))
                self.play(a_vec.set_color, [WHITE, MAROON_A, YELLOW_C], rate_func = there_and_back, run_time = 3 )
                
                #PROYECCION DE B SOBRE A
                self.play(Write(line_a_perp))
                self.play(GrowArrow(a_vec_pro))
                self.play( FadeOut(line_a_perp))
                self.play(Transform(a_vec_pro, suma_a), run_time=1.5)
                self.play(GrowArrow(a_ort))
                self.play(FadeOut(a_vec_pro))
                
                #PROYECCION DE C SOBRE A
                self.play(Write(line_c_perp))
                self.play(GrowArrow(c_vec_pro))
                self.play( FadeOut(line_c_perp))
                self.play(Transform(c_vec_pro, suma_c), run_time=1.5)
                self.play(GrowArrow(c_ort))
                self.wait()
                self.play(FadeOut(c_ort))
            
                
                #PROYECCION DE C SOBRE B'
                self.play(Write(line_b_perp))
                self.play(GrowArrow(b_vec_pro))
                self.play( FadeOut(line_b_perp))
                self.play(Transform(b_vec_pro, suma_b), run_time=1.5)
                self.play(GrowArrow(cb_ort))
                self.play(FadeOut(b_vec_pro), FadeOut(c_vec_pro), FadeOut(b_vec), FadeOut(c_vec),)
                self.play(
                    *[FadeOut(mob)for mob in self.mobjects]
                    # All mobjects in the screen are saved in self.mobjects
                )

    def subespacios(self, a, b, c, a_vec1, b_vec1, c_vec1, anguloz, angulox, cameraphi, text, text_bg, COLOR):
        
                
                a_vec1_suma = Arrow(start = b+c, end = a+b+c, color = a_vec1.get_color(), buff = 0).set_opacity(0.5)
                b_vec1_suma = Arrow(start = c, end = b+c, color = b_vec1.get_color(), buff = 0).set_opacity(0.5)
                c_vec1_suma = Arrow(start = b, end = b+c, color = c_vec1.get_color(), buff = 0).set_opacity(0.5)
                suma = Vector(direction = a+b+c, color = COLOR, buff = 0)


                dotb = Dot(point = b, color = RED).set_opacity(0)
                dotc = Dot(point = c, color = RED).set_opacity(0)
                dota = Dot(point = a, color = RED).set_opacity(0)
                estela1 = Line(ORIGIN, ORIGIN, color = COLOR, fill_opacity = 0)
                estela2 = Line(ORIGIN, ORIGIN, color = COLOR, fill_opacity = 0)
                plano_estela1 = Rectangle( color = COLOR, buff = 0).set_opacity(0.2)
                plano_estela1.set_width(1,stretch=True)
                plano_estela1.set_height(30,stretch=True)
                plano_estela2 = Rectangle( color = COLOR, buff = 0).set_opacity(0.2)
                plano_estela2.set_width(1,stretch=True)
                plano_estela2.set_height(30,stretch=True)
                cubo1 = Prism().set_color(COLOR).set_opacity(0.3)
                cubo2 = Prism().set_color(COLOR).set_opacity(0.3)
                cubo1.set_height(30,stretch=True)
                cubo1.set_width(18,stretch=True)
                cubo1.set_depth(0.08,stretch=True)
                cubo2.set_height(30,stretch=True)
                cubo2.set_width(18,stretch=True)
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
                    new_vec=Vector(direction = dota.get_center(), color = a_vec1.get_color())
                    obj.become(new_vec)

                def update_b(obj):
                    new_vec=Vector(direction = dotb.get_center(), color = b_vec1.get_color())
                    obj.become(new_vec)
                
                def update_c(obj):
                    new_vec=Vector(direction = dotc.get_center(), color = c_vec1.get_color())
                    obj.become(new_vec)

                def update_a_s(obj):
                    new_vec=Arrow(start = b_vec1.get_end()+c_vec1.get_end(), end = a_vec1.get_end()+b_vec1.get_end()+c_vec1.get_end(), color = a_vec1.get_color(), buff = 0).set_opacity(0.5)
                    obj.become(new_vec)

                def update_b_s(obj):
                    new_vec=Arrow(start = c_vec1.get_end(), end = b_vec1.get_end()+c_vec1.get_end(), color = b_vec1.get_color(), buff = 0).set_opacity(0.5)
                    obj.become(new_vec)
                
                def update_c_s(obj):
                    new_vec=Arrow(start = b_vec1.get_end(), end = b_vec1.get_end()+c_vec1.get_end(), color = c_vec1.get_color(), buff = 0).set_opacity(0.5)
                    obj.become(new_vec)

                def update_sa(obj):
                    new_vec=Vector(direction = a_vec1.get_end()+b+c, color = COLOR, buff = 0)
                    obj.become(new_vec)

                def update_sb(obj):
                    new_vec=Vector(direction = a+b_vec1.get_end()+c, color = COLOR, buff = 0)
                    obj.become(new_vec)

                def update_sc(obj):
                    new_vec=Vector(direction = a+b+c_vec1.get_end(), color = COLOR, buff = 0)
                    obj.become(new_vec)

                def update_estela1(obj):
                    new_line = Line(a+b+c, a+b_vec1.get_end()+c, color = COLOR).set_opacity(0.4)
                    obj.become(new_line)

                def update_estela2(obj):
                    new_line = Line(a+c+b, a+b_vec1.get_end()+c, color = COLOR).set_opacity(0.4)
                    obj.become(new_line)

                def update_ps(mob,alpha):
                    mob.become(mob.target)
                    mob.set_width(alpha*9, stretch=True)
                    mob.next_to(estela1.get_start(), RIGHT, buff = 0).rotate(anguloz*DEGREES, axis = Z_AXIS, about_point= estela1.get_start()).rotate(angulox*DEGREES, axis = X_AXIS, about_point= estela1.get_start())

                def update_ps2(mob,alpha):
                    mob.become(mob.target)
                    mob.set_width(alpha*9, stretch=True)
                    mob.next_to(estela1.get_start(), LEFT, buff = 0).rotate(anguloz*DEGREES, axis = Z_AXIS, about_point= estela1.get_start()).rotate(angulox*DEGREES, axis = X_AXIS, about_point= estela1.get_start())

                def update_cs(mob,alpha):
                    mob.become(mob.target)
                    mob.set_depth(alpha*6, stretch=True)
                    mob.next_to(estela2.get_start()-[0,13,0], UP+[0,0,1.5], buff=0).rotate(anguloz*DEGREES, axis = Z_AXIS, about_point= estela1.get_start()).rotate(angulox*DEGREES, axis = X_AXIS, about_point= estela1.get_start())
                        
                def update_cs2(mob,alpha):
                    mob.become(mob.target)
                    mob.set_depth(alpha*6, stretch=True)
                    mob.next_to(estela2.get_start()+[0,13,0], DOWN+[0,0,-1.5], buff=0).rotate(anguloz*DEGREES, axis = Z_AXIS, about_point= estela1.get_start()).rotate(angulox*DEGREES, axis = X_AXIS, about_point= estela1.get_start())

                
                self.play(Write(a_vec1_suma), Write(b_vec1_suma), Write(c_vec1_suma), Write(dotb), GrowArrow(suma), run_time=3)
                self.add_foreground_mobjects(b_vec1_suma)
                self.play(  UpdateFromFunc(b_vec1,update_b), 
                            UpdateFromFunc(a_vec1_suma,update_a_s),
                            UpdateFromFunc(b_vec1_suma,update_b_s), 
                            UpdateFromFunc(c_vec1_suma,update_c_s),
                            UpdateFromFunc(suma,update_sb),
                            UpdateFromFunc(estela1,update_estela1),
                            dotb.move_to, 8*(b), run_time=1) 
                self.add_foreground_mobjects(b_vec1_suma)
                self.play(  UpdateFromFunc(b_vec1,update_b), 
                            UpdateFromFunc(a_vec1_suma,update_a_s),
                            UpdateFromFunc(b_vec1_suma,update_b_s), 
                            UpdateFromFunc(c_vec1_suma,update_c_s), 
                            UpdateFromFunc(suma,update_sb),
                            UpdateFromFunc(estela2,update_estela2),
                            dotb.move_to, -8*(b), run_time=1) 
                self.play(b_vec1.restore, b_vec1_suma.restore, a_vec1_suma.restore, c_vec1_suma.restore, suma.restore, run_time = 0.5)


                self.add_foreground_mobjects(c_vec1)
                self.add(plano_estela1)
                plano_estela1.generate_target()
                self.play(  UpdateFromFunc(c_vec1,update_c), 
                            UpdateFromFunc(a_vec1_suma,update_a_s),
                            UpdateFromFunc(b_vec1_suma,update_b_s), 
                            UpdateFromFunc(c_vec1_suma,update_c_s), 
                            UpdateFromFunc(suma,update_sc),
                            UpdateFromAlphaFunc(plano_estela1, update_ps),
                            dotc.move_to, 5*c, run_time=1) 
                self.play(c_vec1.restore, c_vec1_suma.restore, a_vec1_suma.restore, b_vec1_suma.restore, suma.restore, dotc.restore, run_time = 0.5)
                self.add_foreground_mobjects(c_vec1)
                self.add(plano_estela2)
                plano_estela2.generate_target()
                # FadeOut(estela1), FadeOut(estela2),
                self.play(  FadeOut(estela1), FadeOut(estela2),
                            UpdateFromFunc(c_vec1,update_c), 
                            UpdateFromFunc(a_vec1_suma,update_a_s),
                            UpdateFromFunc(b_vec1_suma,update_b_s), 
                            UpdateFromFunc(c_vec1_suma,update_c_s), 
                            UpdateFromFunc(suma,update_sc),
                            UpdateFromAlphaFunc(plano_estela2, update_ps2),
                            dotc.move_to, -4*c, run_time=1) 
                self.play(c_vec1.restore, c_vec1_suma.restore, a_vec1_suma.restore, b_vec1_suma.restore, suma.restore, run_time = 0.5)

                


                self.move_camera(phi=cameraphi, theta=-0*DEGREES, gamma=0*DEGREES, run_time=2)
                self.wait(1)
                self.add_foreground_mobjects(a_vec1)
                self.add(cubo1)
                cubo1.generate_target()
                self.play(  FadeOut(plano_estela1), FadeOut(plano_estela2),
                            UpdateFromFunc(a_vec1,update_a), 
                            UpdateFromFunc(a_vec1_suma,update_a_s),
                            UpdateFromFunc(b_vec1_suma,update_b_s), 
                            UpdateFromFunc(c_vec1_suma,update_c_s), 
                            UpdateFromFunc(suma,update_sa),
                            UpdateFromAlphaFunc(cubo1, update_cs), 
                            dota.move_to, 3.5*a, run_time=1) 
                self.play(a_vec1.restore, a_vec1_suma.restore, b_vec1_suma.restore, c_vec1_suma.restore, suma.restore, dota.restore, run_time = 0.5)
                self.add_foreground_mobjects(a_vec1)
                self.add(cubo2)
                cubo2.generate_target()
                self.play(  UpdateFromFunc(a_vec1,update_a), 
                            UpdateFromFunc(a_vec1_suma,update_a_s),
                            UpdateFromFunc(b_vec1_suma,update_b_s), 
                            UpdateFromFunc(c_vec1_suma,update_c_s), 
                            UpdateFromFunc(suma,update_sa),
                            UpdateFromAlphaFunc(cubo2, update_cs2), 
                            dota.move_to, -5*a, run_time=1)
                self.play(c_vec1.restore, c_vec1_suma.restore, a_vec1.restore, a_vec1_suma.restore, b_vec1.restore, b_vec1_suma.restore, suma.restore, run_time = 0.5)

                self.add_fixed_in_frame_mobjects(text_bg)
                self.add_fixed_in_frame_mobjects(text)
                self.play(Write(text_bg), Write(text)) 
                self.wait(1.5)

                self.play( FadeOut(cubo1), FadeOut(cubo2), FadeOut(suma), FadeOut(a_vec1_suma), FadeOut(b_vec1_suma), FadeOut(c_vec1_suma), FadeOut(text), FadeOut(text_bg), run_time = 0.5)
                

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
        a = np.array([0.5, 1.5, 2])
        b = np.array([1, 2.3, 1])
        c = np.array([2, 1, 1])  
        


        #self.set_camera_orientation(phi=75*DEGREES, theta=40*DEGREES)
        #self.set_camera_orientation(phi=100*DEGREES, theta=40*DEGREES)
        #self.set_camera_orientation(phi=95*DEGREES, theta=43*DEGREES)
        self.set_camera_orientation(phi=85*DEGREES, theta=40*DEGREES)
        self.play(ShowCreation(axes))
        self.parte1(a,b,c)
        self.set_camera_orientation(phi=85*DEGREES, theta=40*DEGREES)
        self.play(ShowCreation(axes))
        self.parte2(a,b,c)
       