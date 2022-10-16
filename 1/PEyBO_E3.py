# -*- coding: utf-8 -*-

from re import S
from manim import *
from alganim import DashedArrow


#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################

#####################################################################################
###############################  Terecera escena ####################################
#####################  versión: Manim Community v0.15.2   ###########################
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

class SE1(MovingCameraScene):
    '''
    La escena esta organizada de la siguiente forma: se definen cuatro funciones, cada una de ellas
    incluye la prueba de una de las propiedades. Al ejecutar cada una de estas funciones se anima la
    demostración de dicha propiedad en el lado derecho de la pantalla, sin afectar a los objetos
    que ya están definidos en el lado izquierdo.
    '''
    
    def demo_1(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la primer propiedad del producto punto
        '''
        #----------- OBJETOS                 

        obj_1 = MathTex(r"  \langle\vec{u}+\vec{w},\vec{v}\rangle ").scale(0.7).shift(2*UP+0.2*LEFT)
        obj_1_dup = MathTex(r"  \langle\vec{u}+\vec{w},\vec{v}\rangle ").move_to(obj_1).scale(0.7).shift(1.4*RIGHT)
        obj_2 = MathTex(r" \bigg( \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} + \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} \bigg)\cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}").move_to(obj_1).scale(0.6).\
            shift(0.5*RIGHT)

        obj_3 = MathTex(r" &= \begin{pmatrix} u_1+w_1 \\ u_2 + w_2 \end{pmatrix}\cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} ").next_to(obj_2, RIGHT).scale(0.6).shift(0.9*LEFT)
        obj_4 = MathTex(r" &= (u_1+w_1) v_1 + (u_2+w_2) v_2").scale(0.7)
        obj_5 = MathTex(r" &= u_1v_1 + w_1v_1 + u_2v_2 + w_2v_2").scale(0.7)
        obj_6 = MathTex(r" &= u_1v_1 + u_2v_2 + w_1v_1 + w_2v_2").scale(0.7)
        obj_7 = MathTex(r" &= (u_1v_1 + u_2v_2) + (w_1v_1 + w_2v_2)").scale(0.65)
        obj_8 = MathTex(r" &= \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} + \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} ").scale(0.6)

        grupo = VGroup(obj_3, obj_4, obj_5, obj_6, obj_7, obj_8).arrange(1.5*DOWN, center=False, aligned_edge=LEFT)
        obj_9 = MathTex(r" &= \langle \vec{u} , \vec{v} \rangle + \langle \vec{w} , \vec{v} \rangle ").move_to(obj_8).scale(0.7).shift(0.8*LEFT)
       

        srct_1 = SurroundingRectangle(obj_1_dup)
        srct_2 = SurroundingRectangle(obj_9)

        objs = VGroup(obj_1_dup, obj_2, obj_3, obj_4, obj_5, obj_6, obj_7, obj_8, obj_9, srct_1, srct_2)

        # PALOMA PARA ACOMPAÑAR A LA PROPIEDAD PROBADA
        p1 = Line(ORIGIN, [1,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(2*LEFT+1.4*DOWN)
        #####################
        ## ANIMACIONES DEMO 1 ###
        #####################
        self.play(Write(obj_1))
        self.wait(1)
        self.play(ReplacementTransform(obj_1,obj_2))
        self.play(Write(obj_3))
        self.play(Write(obj_4))
        self.play(Write(obj_5))
        self.play(Write(obj_6))
        self.play(Write(obj_7))
        self.play(Write(obj_8))
        self.wait(1)
        self.play(ReplacementTransform(obj_8,obj_9))
        self.wait(1)
        self.play(ReplacementTransform(obj_2, obj_1_dup))
        self.play(Write(srct_1), Write(srct_2))
        self.wait(2)
        self.play(paloma.animate.set_opacity(1))
        self.play(FadeOut(objs))


    def demo_2(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la segunda propiedad del producto punto
        '''
        #----------- OBJETOS

        obj_1 = MathTex(r"  \langle a\vec{u}},\vec{v}\rangle ").scale(0.7).shift(1.5*UP+RIGHT)
        inter = MathTex(r"a \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} ").scale(0.7).move_to(obj_1)
        inter2 = MathTex(r" \langle a\vec{u}},\vec{v}\rangle ").scale(0.7).move_to(obj_1).shift(0.5*RIGHT)
        obj_2 = MathTex(r" &= \begin{pmatrix} au_1 \\ au_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} ").scale(0.7).next_to(inter, RIGHT)
        obj_3 = MathTex(r" &= (au_1)v_1 + (au_2)v_2 ").scale(0.7)
        obj_4 = MathTex(r" &= a(u_1v_1) + a(u_2v_2)").scale(0.7)
        obj_5 = MathTex(r" &= a(u_1v_1 + u_2v_2)").scale(0.7)
        obj_6 = MathTex(r" &= a \left(\begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}\right)")\
            .scale(0.7)
        
        grupo = VGroup(obj_2, obj_3, obj_4, obj_5, obj_6).arrange(1.5*DOWN, center=False, aligned_edge=LEFT)
        obj_7 = MathTex(r" &= a \langle \vec{u} , \vec{v} \rangle").move_to(obj_6).scale(0.7).shift(0.85*LEFT)

        objs = VGroup( inter2, grupo, obj_7)

        
        srct_1 = SurroundingRectangle(inter2)
        srct_2 = SurroundingRectangle(obj_7)

        srects = VGroup(srct_1,srct_2)

        # PALOMA PARA ACOMPAÑAR A LA PROPIEDAD PROBADA
        p1 = Line(ORIGIN, [1,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(2.9*LEFT+2*DOWN)
        #####################
        ## ANIMACIONES DEMO 2 ###
        #####################
        
        # Animación de la demostración
        self.play(Write(obj_1))
        self.wait(1)        
        self.play(ReplacementTransform(obj_1,inter))
        self.play(Write(obj_2))
        self.play(Write(obj_3))
        self.play(Write(obj_4))
        self.play(Write(obj_5))
        self.play(Write(obj_6))
        self.wait(1)
        self.play(ReplacementTransform(obj_6,obj_7))
        self.wait(1)
        self.play(ReplacementTransform(inter, inter2))
        self.play(Write(srct_1), Write(srct_2))
        self.wait(2)
        self.play(paloma.animate.set_opacity(1))
        self.play(FadeOut(srects), FadeOut(objs) )


    def demo_3(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la tercer propiedad del producto punto
        '''
        #----------- OBJETOS       
        obj_1 = MathTex(r" \overline{ \langle \vec{v} , \vec{u} \rangle}").scale(0.8).shift(1.5*UP+1*RIGHT)
        obj_2 = MathTex(r" \overline{ \bigg(\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \cdot \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \bigg)}").scale(0.7).move_to(obj_1)
        obj_1_dup = MathTex(r" \overline{ \langle \vec{v} , \vec{u} \rangle}").scale(0.8).move_to(obj_2).shift(0.9*RIGHT)
        obj_3 = MathTex(r" &= \overline{ (v_1u_1 + v_2u_2)}").next_to(obj_2, 0.8*RIGHT).scale(0.8)
        obj_4 = MathTex(r" &= v_1u_1 + v_2u_2").scale(0.8)
        obj_5 = MathTex(r" &= u_1v_1 + u_2v_2").scale(0.8)
        obj_6 = MathTex(r" &= \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}").scale(0.8)

        grupo = VGroup(obj_3, obj_4, obj_5, obj_6).arrange(1.5*DOWN, center=False, aligned_edge=LEFT)
        obj_7 = MathTex(r" &= \langle \vec{u},\vec{v}\rangle ").move_to(obj_6).scale(0.8).shift(0.65*LEFT)

        srct_1 = SurroundingRectangle(obj_1_dup)
        srct_2 = SurroundingRectangle(obj_7)

        objs = VGroup(obj_1_dup, grupo, srct_1, srct_2, obj_7)
        
        # PALOMA PARA ACOMPAÑAR A LA PROPIEDAD PROBADA
        p1 = Line(ORIGIN, [0.95,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(3.1*LEFT+2.6*DOWN)

        #####################
        ## ANIMACIONES DEMO 3 ###
        #####################

        self.play(Write(obj_1))
        self.play(ReplacementTransform(obj_1, obj_2))
        self.play(Write(obj_3))
        self.play(Write(obj_4))
        self.play(obj_4.animate.scale(1.2))
        self.wait(1)
        self.play(obj_4.animate.scale(1/1.2))
        self.play(Write(obj_5))
        self.play(Write(obj_6))
        self.wait(1)
        self.play(ReplacementTransform(obj_6, obj_7))
        self.wait(2)
        self.play(ReplacementTransform(obj_2, obj_1_dup))
        self.play(Write(srct_1),Write(srct_2))
        self.wait(2)
        self.play(paloma.animate.set_opacity(1))
        self.play(FadeOut(objs))

    def demo_4(self):

        c_nonzero = MathTex(r" \forall \ c \in \mathbb{R}, c\neq0 &\Rightarrow c^2>0").shift(3*UP+3*RIGHT).scale(0.8)
        
        #----------- OBJETOS       
        obj_1 = MathTex(r" \vec{u}\neq \vec{0} ").scale(0.8).shift(1.5*UP+1*RIGHT)
        obj_2 = MathTex(r" \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \end{pmatrix}").scale(0.7).move_to(obj_1)
        obj_1_dup = MathTex(r" \vec{u}\neq \vec{0}").scale(0.8).move_to(obj_2).shift(0.5*RIGHT)
        obj_3 = MathTex(r" \Rightarrow u_1 \ \text{ó} \ u_2 \neq 0").next_to(obj_2, 0.8*RIGHT).scale(0.8).shift(0.3*LEFT)
        obj_4 = MathTex(r" \Rightarrow u_1^2 + u_2^2 > 0").scale(0.8)
        obj_5 = MathTex(r" \Rightarrow u_1u_1 + u_2u_2 > 0").scale(0.8)
        obj_6 = MathTex(r" \Rightarrow \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} > 0")\
            .scale(0.8)
        
        grupo = VGroup(obj_3, obj_4, obj_5, obj_6).arrange(1.5*DOWN, center=False, aligned_edge=LEFT)

        obj_7 = MathTex(r" \Rightarrow \langle \vec{u} , \vec{u} \rangle > 0 ").move_to(obj_6).scale(0.8).shift(0.65*LEFT)

        srct_1 = SurroundingRectangle(obj_1_dup)
        srct_2 = SurroundingRectangle(obj_7)

        objs = VGroup(obj_1_dup, grupo, srct_1, srct_2, obj_7, c_nonzero)

        # PALOMA PARA ACOMPAÑAR A LA PROPIEDAD PROBADA
        p1 = Line(ORIGIN, [1,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(2.5*LEFT+3.2*DOWN)

        #####################
        ## ANIMACIONES DEMO 4 ###
        #####################
        self.play(Write(c_nonzero))
        self.play(Write(obj_1))
        self.play(ReplacementTransform(obj_1, obj_2))
        self.play(Write(obj_3))
        self.play(Write(obj_4))
        self.play(Write(obj_5))
        self.play(Write(obj_6))
        self.wait(1)
        self.play(ReplacementTransform(obj_6, obj_7))
        self.wait(2)
        self.play(ReplacementTransform(obj_2, obj_1_dup))
        self.play(Write(srct_1),Write(srct_2))
        self.wait(2)
        self.play(paloma.animate.set_opacity(1))
        self.play(FadeOut(objs))

        
    def construct(self): # Cambiar a construct
        '''
        Aquí se definen objetos y animaciones que estarán a lo largo de toda la subescena, por lo que
        se definen en el método principal (construct). Siempre que queramos ver/omitir una de las pruebas
        podemos descomentar/comentar la línea donde se invoca la función.
        '''

        #-------------- DEFINICIÓN DEL PP EN ABSTRACTO: OPERACION Y PROPS (OBJETOS)
        pe_def = MathTex(r" \langle\cdot,\cdot\rangle:",r"V", r"\times ", r"V",r"\to ",r"K").shift(2*UP)
        pe_def_1 = MathTex(r" \forall \ \vec{u}, \vec{v}, \vec{w}&\in V, \ \forall \ a\in K ").next_to(pe_def, 1.1*DOWN)
        pe_def_2 = MathTex(r"  \langle\vec{u}+\vec{w},\vec{v}\rangle &= \langle \vec{u} , \vec{v} \rangle + \langle \vec{w} , \vec{v} \rangle ").next_to(pe_def_1.get_center(), 2*DOWN)\
            .shift(0.15*RIGHT)
        pe_def_3 = MathTex(r"  \langle a\vec{u} , \vec{v} \rangle &= a \langle \vec{u} , \vec{v} \rangle ").next_to(pe_def_2.get_center(), 1.5*DOWN).shift(0.45*LEFT)
        pe_def_4 = MathTex(r"  \langle \vec{u} , \vec{v} \rangle &= \overline{ \langle \vec{v} , \vec{u} \rangle} ").next_to(pe_def_3.get_center(), 1.5*DOWN)
        pe_def_5 = MathTex(r" \vec{u}\neq \vec{0} \Rightarrow \langle \vec{u} , \vec{u} \rangle > 0 ").next_to(pe_def_4.get_center(), 1.5*DOWN).shift(0.4*RIGHT)

        #VGroup que contiene las propiedades que debe satisfacer el P.E. en abstracto
        pe_group_2 = VGroup(pe_def_1, pe_def_2, pe_def_3, pe_def_4, pe_def_5).scale(0.8).shift(0.5*DOWN)
        
        #---------------- PASANDO DE LO ABSRTACTO AL CASO PARTICULAR en R2 (OJETOS)
        pp_def = MathTex(r" \langle\cdot,\cdot\rangle:",r"\mathbb{R}^2", r"\times ", r"\mathbb{R}^2",r"\to ",r"\mathbb{R}").shift(2*UP) # SE QUEDA
        pp_def[1].set_color(AMARILLO)
        pp_def[3].set_color(AMARILLO)
        pp_def[5].set_color(AZUL_CLARO)          
        pp_oper = MathTex(r"\langle \vec{v},\vec{w}\rangle = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \cdot \begin{pmatrix} w_1 \\ w_2 \end{pmatrix}= v_1w_1 + v_2w_2") #SE QUEDA

        #------------- REACOMODO DE LAS COSAS EN LA PANTALLA, DIBUJAMOS LÍNEAS (OBJETOS)
        
        linea_1 = Line(start = 7*LEFT + 0.5*UP, end = LEFT + 0.5*UP, buff= 0.5)
        linea_2 = Line(start = 4*UP + 1.5*LEFT, end = 4*DOWN + 1.5*LEFT, buff= 0.5)


        

    #####################
    ## ANIMACIONES   ###
    #####################

        # INTRODUCCION, PLANTEAMIENTO DEL CASO PARTICULAR Y DEFINICIÓN DEL PP 
        #self.next_section(skip_animations=True)
        self.play(Write(pe_def))
        self.play(Write(pe_group_2),run_time=4)
        self.wait()
        self.play(pe_group_2.animate.set_opacity(0))
        self.wait(3)
        self.play(ReplacementTransform(pe_def,pp_def))
        self.wait(6)
        self.play(Write(pp_oper))
        self.wait(2)

        #------ REACOMODO DE LOS OBJETOS Y DIBUJO DE LÍNEAS 
        #self.next_section(skip_animations=True)
        self.play(pp_def.animate.shift(4*LEFT+1*UP).scale(0.7))
        self.play(pp_oper.animate.shift(4.1*LEFT+1.8*UP).scale(0.6))
        self.play(Write(linea_1))
        self.play(Write(linea_2))

        
        self.play(pe_def_1.animate.shift(4.2*LEFT+0.8*DOWN).scale(0.7), run_time=0.1)
        self.play(pe_def_1.animate.set_opacity(1), run_time=0.5)
        self.play(pe_def_2.animate.next_to(pe_def_1.get_center(), 1.5*DOWN).shift(0.15*RIGHT).scale(0.8), run_time=0.1)
        self.play(pe_def_2.animate.set_opacity(1), run_time=0.5)
        self.play(pe_def_3.animate.next_to(pe_def_2.get_center(), 1.5*DOWN).shift(0.27*LEFT).scale(0.8), run_time=0.1)
        self.play(pe_def_3.animate.set_opacity(1), run_time=0.5)
        self.play(pe_def_4.animate.next_to(pe_def_3.get_center(), 1.5*DOWN).scale(0.8), run_time=0.1)
        self.play(pe_def_4.animate.set_opacity(1), run_time=0.5)
        self.play(pe_def_5.animate.next_to(pe_def_4.get_center(), 1.5*DOWN).shift(0.27*RIGHT).scale(0.8), run_time=0.1)
        self.play(pe_def_5.animate.set_opacity(1), run_time=0.5)

        #######################
        # ANIM PREVIAS A DEM 1 #
        #######################

        self.wait()
        self.play(pe_def_3.animate.set_opacity(0.3), pe_def_4.animate.set_opacity(0.3),
        pe_def_4.animate.set_opacity(0.3), pe_def_5.animate.set_opacity(0.3))
        self.play(pe_def_2.animate.scale(1.1))

        self.demo_1() # Llamamos a la animación completa de la primer demostración

        #######################
        # ANIM PREVIAS A DEM 2 #
        #######################

        self.play(pe_def_2.animate.scale(1/1.1))
        self.play(pe_def_2.animate.set_opacity(0.3))
        self.play(pe_def_3.animate.set_opacity(1).scale(1.2))

        self.demo_2() # Llamamos a la animación completa de la segunda demostración

        #######################
        # ANIM PREVIAS A DEM 3 #
        #######################

        self.play(pe_def_3.animate.scale(1/1.1))
        self.play(pe_def_3.animate.set_opacity(0.3))
        self.play(pe_def_4.animate.set_opacity(1).scale(1.1))

        self.demo_3() # Llamamos a la animación completa de la tercera demostración


        #######################
        # ANIM PREVIAS A DEM 4 #
        #######################

        self.play(pe_def_4.animate.scale(1/1.1))
        self.play(pe_def_4.animate.set_opacity(0.3))
        self.play(pe_def_5.animate.set_opacity(1).scale(1.1))

        self.demo_4() # Llamamos a la animación completa de la cuarta demostración

    

        #####################
        # ANIMACIONES FINALES
        #####################
        self.next_section()
        self.play(pe_def_5.animate.scale(1/1.1))

        self.play(pe_def_4.animate.set_opacity(1))
        self.play(pe_def_3.animate.set_opacity(1))
        self.play(pe_def_2.animate.set_opacity(1))

        self.wait(2.5)

        self.play(linea_1.animate.set_opacity(0),
                  linea_2.animate.set_opacity(0),
                  pe_def_1.animate.set_opacity(0),
                  self.camera.frame.animate.set(width=8).move_to(2.3*UP+4.15*LEFT)
                  )
        self.wait(3)

        suma_1 = MathTex(r"\sum_{i=1}^2 v_iw_i").scale(0.6).move_to(1.8*UP+2.75*LEFT)
        suma_n = MathTex(r"\sum_{i=1}^n v_iw_i").scale(0.6).move_to(1.8*UP+2.75*LEFT)
        barrita = MathTex(r"\overline{w_i}")[0][0].scale(0.6).move_to(1.95*UP+2.4*LEFT)
        n_1 = MathTex("n").set_color(YELLOW).scale(0.5).move_to(pp_def[1][1].get_center())
        n_2 = MathTex("n").set_color(YELLOW).scale(0.5).move_to(pp_def[3][1].get_center())
        C_1 = MathTex("\\mathbb{C}").set_color(YELLOW).scale(0.7).move_to(pp_def[1][0].get_center())
        C_2 = MathTex("\\mathbb{C}").set_color(YELLOW).scale(0.7).move_to(pp_def[3][0].get_center())
        C_3 = MathTex("\\mathbb{C}").set_color(AZUL_CLARO).scale(0.7).move_to(pp_def[5][0].get_center())

        self.play(ReplacementTransform(pp_oper[0][22:31],suma_1))
        self.wait(5)
        self.play(ReplacementTransform(pp_def[1][1],n_1),
                  ReplacementTransform(pp_def[3][1],n_2),
                  ReplacementTransform(suma_1,suma_n),
                  )

        self.wait(2.5)
        self.play(ReplacementTransform(pp_def[1][0],C_1),
                  ReplacementTransform(pp_def[3][0],C_2),
                  ReplacementTransform(pp_def[5][0],C_3),
                  Write(barrita)
                  )

        self.wait(7)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 1)

class SE2(Scene):
   '''
    Esta subescena presenta la solución del problema de los coeficientes haciendo uso del producto punto en R2 como producto
    interno. Consta de una parte geométrica (lado izquierdo) y una parte algebráica (lado derecho), que se complementan para
    ilustrar la solución del problema en un caso particular.
   '''

   def construct(self):

      def gen_simple(Vec1,Vec2):
         # Copias de vectores.
         Copia1 = Vec1.copy()
         # Coordenadas de vectores
         A1 = Vec1.get_end()[0]
         A2 = Vec1.get_end()[1]
         B1 = Vec2.get_end()[0]
         B2 = Vec2.get_end()[1]

         # Vectores para el paralelogramo.
         Vec1c = DashedArrow(Vec2.get_end(),Vec2.get_end()+A1*RIGHT+A2*UP, buff=0, color = Vec1.get_color()).set_fill(opacity=0.5).shift(2.5*LEFT+1.5*UP)
         Vec2c = DashedArrow(Vec1.get_end(),Vec1.get_end()+B1*RIGHT+B2*UP, buff=0, color = Vec2.get_color()).set_fill(opacity=0.5).shift(2.5*LEFT+1.5*UP)
         # Vector resultante de la combinación lineal.
         VecRCL = DashedArrow((0,0,0), (A1+B1)*RIGHT+(A2+B2)*UP, buff=0, color = MAGENTA).set_fill(opacity=1).shift(2.5*LEFT+1.5*UP)
         
         self.play(Create(Vec2c))
         self.play(Create(VecRCL))

         # ValueTrackers
         vt1 = ValueTracker(1)

         # Primera función para cambios de Vec2.
         def upd_for_vec2_1(obj):
               t = vt1.get_value()
               NewVec2 = Arrow((0,0,0),(t*B1,t*B2,0),buff=0, color = Vec2.get_color()).shift(2.5*LEFT+1.5*UP).shift(2.5*LEFT+1.5*UP)
               obj.become(NewVec2)
         # Primera función para cambios de Vec2c.
         def upd_for_vec2c_1(obj):
               t = vt1.get_value()
               NewVec2c = DashedArrow(Vec1.get_end(),Vec1.get_end()+(t*B1,t*B2,0), buff=0, color = Vec2.get_color()).set_fill(opacity=0.5).shift(2.5*LEFT+1.5*UP)
               obj.become(NewVec2c)
         # Primera función para cambios de VecRCL.
         def upd_for_vecrcl_1(obj):
               t = vt1.get_value()
               NewVecRCL = DashedArrow((0,0,0),(A1+B1*t)*RIGHT+(A2+B2*t)*UP, buff=0, color = MAGENTA).set_fill(opacity=1).shift(2.5*LEFT+1.5*UP)
               obj.become(NewVecRCL)
         
         # Primera línea usada.
         Linea1 = Line(Vec2c.get_end()+(0.001,0.001,0), Vec2c.get_end(), color = MAGENTA).set_fill(opacity=0.5).shift(2.5*LEFT+1.5*UP)
         # Segunda línea usada.
         Linea2 = Line(Vec2.get_end(), Vec2.get_end()-(0.01*B1,0.01*B2,0), color = MAGENTA).set_fill(opacity=0.5).shift(2.5*LEFT+1.5*UP)
        
         # Función para cambiar tamaño de las líneas.
         def upd_for_linea(obj):
               t = vt1.get_value()
               new_linea = Line(Copia1.get_end()+(0.001,0.001,0)+B1*RIGHT+B2*UP,Vec1.get_end()+(t*B1,t*B2,0), color = MAGENTA).set_fill(opacity=0.5).shift(2.5*LEFT+1.5*UP)
               obj.become(new_linea)

         # Animación del movimiento del primer vector
         self.play(Create(Linea2))
         self.bring_to_back(Linea1)
         self.bring_to_back(Linea2)
         Vec2.add_updater(upd_for_vec2_1)
         Vec2c.add_updater(upd_for_vec2c_1)
         VecRCL.add_updater(upd_for_vecrcl_1)
         Linea1.add_updater(upd_for_linea)
         Linea2.add_updater(upd_for_linea)
         self.play(vt1.animate.set_value(4),run_time=1.3) # HERE 
         Linea1.remove_updater(upd_for_linea)
         self.play(vt1.animate.set_value(1))
         self.play(vt1.animate.set_value(-3.5),run_time=1.3) # HERE 
         Linea2.remove_updater(upd_for_linea)
         self.play(vt1.animate.set_value(1),run_time=1)
         Vec2.remove_updater(upd_for_vec2_1)
         Vec2c.remove_updater(upd_for_vec2c_1)
         VecRCL.remove_updater(upd_for_vecrcl_1)
         self.play(FadeOut(Vec2c))
         
         self.play(Create(Vec1c))
         # Primera función para cambios de Vec1.
         def upd_for_vec1_1(obj):
               t = vt1.get_value()
               NewVec1 = Arrow((0,0,0),(t*A1,t*A2,0),buff=0, color = Vec1.get_color()).shift(2.5*LEFT+1.5*UP)
               obj.become(NewVec1)
         # Primera función para cambios de Vec1c.
         def upd_for_vec1c_1(obj):
               t = vt1.get_value()
               NewVec1c = DashedArrow(Vec2.get_end(),Vec2.get_end()+(t*A1,t*A2,0), buff=0, color = Vec1.get_color()).set_fill(opacity=0.5).shift(2.5*LEFT+1.5*UP)
               obj.become(NewVec1c)
         # Segunda función para cambios de VecRCL.
         def upd_for_vecrcl_2(obj):
               t = vt1.get_value()
               NewVecRCL = DashedArrow((0,0,0),(A1*t+B1)*RIGHT+(A2*t+B2)*UP, buff=0, color = MAGENTA).set_fill(opacity=1).shift(2.5*LEFT+1.5*UP)
               obj.become(NewVecRCL)

         # Rectangulos usados para rellenar plano.
         Vertice1 = Linea1.get_end()
         Vertice2 = Linea2.get_end()
         Vertice3 = Linea2.get_end()+(0.05*A1,0.025*A2,0)
         Vertice4 = Linea1.get_end()+(0.05*A1,0.025*A2,0)
         Vertice5 = Linea2.get_end()-(0.05*A1,0.025*A2,0)
         Vertice6 = Linea1.get_end()-(0.05*A1,0.025*A2,0)
         Plano1 = Polygon(Vertice1,Vertice2,Vertice3,Vertice4,stroke_width=1)
         Plano2 = Polygon(Vertice1,Vertice2,Vertice5,Vertice6,stroke_width=1)

         # Función que rellena plano.
         def upd_for_plano(obj):
               t = vt1.get_value()
               vert1 = Linea1.get_end()
               vert2 = Linea2.get_end()
               vert3 = Linea2.get_end()+((t-1)*A1,(t-1)*A2,0)
               vert4 = Linea1.get_end()+((t-1)*A1,(t-1)*A2,0)
               New_plano = Polygon(vert1,vert2,vert3,vert4,stroke_width=0).set_fill(MAGENTA_CLARO, opacity = 1)
               obj.become(New_plano)
               self.bring_to_back(obj)

         Vec1.add_updater(upd_for_vec1_1)
         Vec1c.add_updater(upd_for_vec1c_1)
         VecRCL.add_updater(upd_for_vecrcl_2)
         Plano1.add_updater(upd_for_plano)

         # Animación del movimiento del segundo vector y creación del plano
         self.play(Create(Plano1), run_time = 0.05)
         self.play(Create(Plano2), run_time = 0.05)
         self.play(vt1.animate.set_value(8),run_time=1.3) # HERE 
         Plano1.remove_updater(upd_for_plano)
         self.play(vt1.animate.set_value(1))
         Plano2.add_updater(upd_for_plano)
         self.bring_to_back(Plano2)
         self.play(vt1.animate.set_value(-8),run_time=1.3) # HERE 
         Plano2.remove_updater(upd_for_plano)
         self.play(vt1.animate.set_value(1),run_time=1.3)
         self.play(FadeOut(Linea1), FadeOut(Linea2), Write(gamma_gen))
         Vec1.remove_updater(upd_for_vec1_1)
         Vec1c.remove_updater(upd_for_vec1c_1)
         VecRCL.remove_updater(upd_for_vecrcl_2)


         self.wait(0.65)
         self.play(FadeOut(Vec1c))
         self.remove_foreground_mobject(VecRCL)
         self.play(FadeOut(VGroup(Plano1,Plano2)),FadeOut(VGroup(VecRCL)))

      ###########
      # OBJETOS #
      ###########

   ###### OBJETOS  Sección introductoria, planteamiento del problema

      grid = NumberPlane(x_range = [-9,9,1],y_range = [-7,4,1],
         background_line_style={"stroke_width": 1, "stroke_opacity": 0.5}).scale(0.5)
      borde_der = Line(start = [4.5,2.75,0], end = [4.5,-2.75,0], stroke_width = 1)
      borde_izq = Line(start = [-4.5,2.75,0], end = [-4.5,-2.75,0], stroke_width = 1 )
      borde_sup = Line(start = [-4.5,2.75,0], end = [4.5,2.75,0], stroke_width = 1 )
      borde_inf = Line(start = [-4.5,-2.75,0], end = [4.5,-2.75,0], stroke_width = 1 )
      lilgrid = VGroup(grid, borde_sup, borde_der, borde_inf, borde_izq).shift(2.5*LEFT).shift(0.75*UP)

      cuadro_1 = Polygon([2.05,8,0],[2.05,-8,0],[10,8,0],[10,-8,0], color  = BLACK, fill_opacity = 1)
      cuadro_2 = Polygon([-7.05,8,0],[-7.05,-8,0],[-8,-8,0],[-8.5,8,0], color  = BLACK, fill_opacity = 1)
      cuadro_3 = Polygon([-7.05,-2.06,0],[2.05,-2.06,0],[2.05,-5,0],[-7.05,-5,0], color  = BLACK, fill_opacity = 1)
      cuadro_4 = Polygon([-7.05,3.55,0],[2.05,3.55,0],[2.05,6,0],[-7.05,6,0], color  = BLACK, fill_opacity = 1)

      marco = VGroup(cuadro_1, cuadro_2, cuadro_3, cuadro_4)

      # Textos planteamiento del problema
      vec_obj_tex = MathTex(r" \vec{v} = \begin{pmatrix} -8 \\ -4 \end{pmatrix}").shift(6*LEFT+2.5*DOWN).scale(0.4)
      vec_obj_tex[0][:2].set_color(NARANJA)

      gamma_tex = MathTex(r" \Gamma = \{ \vec{g}_1, \vec{g}_2\} = \Bigg\{\begin{pmatrix} 1 \\ -1 \end{pmatrix},\
          \begin{pmatrix} -2 \\ -2 \end{pmatrix} \Bigg\}").next_to(vec_obj_tex, DOWN).scale(0.4).shift(1*RIGHT + 0.5*UP)
      gamma_tex[0][3:6].set_color(RED)
      gamma_tex[0][7:10].set_color(BLUE)

      comblin_abs = MathTex(r" \vec{v} " , r"=" ,r"c_1" ,r"\vec{g}_1" ,r"+" ,r"c_2", r"\vec{g}_2")\
         .shift(2.5*DOWN).scale(0.5)
      comblin_abs[0].set_color(NARANJA)
      comblin_abs[3].set_color(ROJO)
      comblin_abs[6].set_color(AZUL)

      # Objetos para indicar que no conocemos los coeficientes c_1, c_2
      coefs_incog = MathTex(r"\text{¿}c_i\text{?}").next_to(comblin_abs, DOWN).scale(0.4).shift(0.2*UP)
      c2_incog = MathTex( r" ", r"c_1 = -2,  ", r"\text{¿}c_2\text{?}").next_to(comblin_abs, DOWN).scale(0.4).shift(0.2*UP)
      no_incog = MathTex( r" ", r" c_1 = -2, ", r"\   c_2 = 3").next_to(comblin_abs, DOWN).scale(0.4).shift(0.2*UP)

      # Objetos para la ecuación en términos de 2-tuplas, cada vez con menos incognitos
      comblin_R2 = MathTex(r"\begin{pmatrix} -8 \\ -4 \end{pmatrix}\ " , r"\ =" ,r"c_1\ ", r"\begin{pmatrix} 1 \\ -1 \end{pmatrix}", r"\ +", r"\ c_2 \ " ,r"\begin{pmatrix} -2\\ -2 \end{pmatrix}")\
         .next_to(coefs_incog, DOWN).scale(0.4).shift(0.4*UP)
      comblin_R2_1 = MathTex(r"\begin{pmatrix} -8 \\ -4 \end{pmatrix}\ " , r"\ =" ,r"(-2)\ ", r"\begin{pmatrix} 1 \\ -1 \end{pmatrix}", r"\ +", r"\ c_2 \ " ,r"\begin{pmatrix} -2\\ -2 \end{pmatrix}")\
         .next_to(coefs_incog, DOWN).scale(0.4).shift(0.4*UP)
      comblin_R2_2 = MathTex(r"\begin{pmatrix} -8 \\ -4 \end{pmatrix}\ " , r"\ =" ,r"(-2)\ ", r"\begin{pmatrix} 1 \\ -1 \end{pmatrix}", r"\ +", r"\ (3) \ " ,r"\begin{pmatrix} -2\\ -2 \end{pmatrix}")\
         .next_to(coefs_incog, DOWN).scale(0.4).shift(0.4*UP)
      

      grupo_intro = VGroup(vec_obj_tex, gamma_tex, comblin_abs, comblin_R2, coefs_incog)

      # Vectores que se muestran en el NumberPlane

      vec_obj = Arrow((0, 0, 0), (-4,-2,0), buff = 0, color = NARANJA, max_tip_length_to_length_ratio=0.4).shift(2.5*LEFT+1.5*UP)
      v_label = MathTex(r"\vec{v}").move_to(vec_obj.get_end()+(0.3/(np.linalg.norm(v)))*v)\
         .scale(0.7)
      v_label[0][:2].set_color(NARANJA)
      v_label2 = MathTex(r"\vec{v}", "=", r"c_1",r"\vec{g}_1", r"+", r"c_2", r"\vec{g}_2").move_to(vec_obj.get_end()+(0.3/(np.linalg.norm(v)))*v)\
         .scale(0.5).shift(RIGHT+0.1*DOWN)
      v_label2[0].set_color(NARANJA)
      v_label2[3].set_color(RED)
      v_label2[6].set_color(BLUE)
      v_label3 = MathTex(r"-2",r"\vec{g}_1", r"+", r"3", r"\vec{g}_2").move_to(vec_obj.get_end()+(0.3/(np.linalg.norm(v)))*v)\
         .scale(0.5).shift(RIGHT+0.1*DOWN)   
      v_label3[0][2:4].set_color(RED)
      v_label3[0][6:8].set_color(BLUE)

      vec_g1 = Arrow((0, 0, 0),(0.5,-0.5,0), buff = 0, color = ROJO, max_tip_length_to_length_ratio=0.4).shift(2.5*LEFT+1.5*UP)
      g1_label = MathTex(r"\vec{g}_1").move_to(vec_g1.get_end()+(0.4/(np.linalg.norm(g1)))*g1).scale(0.5).set_color(RED)

      vec_g2 = Arrow((0, 0, 0), (-1,-1,0), buff = 0, color = AZUL, max_tip_length_to_length_ratio=0.4).shift(2.5*LEFT+1.5*UP)
      g2_label = MathTex(r"\vec{g}_2").move_to(vec_g2.get_end()+(0.4/(np.linalg.norm(g2)))*g2).scale(0.5).set_color(BLUE)

      c1g1_label_1 = MathTex(r"c_1\vec{g}_1 = -2\vec{g}_1").move_to(np.array([-1,1,0])+(0.4/(np.linalg.norm(-2*g1)))*(-2)*g1).scale(0.5)\
         .shift(2.5*LEFT+1.5*UP)
      c1g1_label_1[2:4].set_color(RED)
      c1g1_label_1[7:9].set_color(RED)
      c2g2_label_1 = MathTex(r"c_2\vec{g}_2 = 3\vec{g_2}").move_to(np.array([-3,-3,0])+(0.4/(np.linalg.norm(3*g2)))*3*g2).scale(0.5)\
         .shift(1.5*LEFT+1.75*UP)
      c2g2_label_1[2:4].set_color(BLUE)
      c2g2_label_1[6:8].set_color(BLUE)

      c1g1_label_2 = MathTex(r"\begin{pmatrix} -2 \\ 2 \end{pmatrix}").move_to(np.array([-1,1,0])+(0.5/(np.linalg.norm(-2*g1)))*(-2)*g1).scale(0.4)\
         .shift(2.5*LEFT+1.5*UP)

      c2g2_label_2 = MathTex(r"\begin{pmatrix} -6 \\ -6 \end{pmatrix}").move_to(np.array([-3,-3,0])+(0.5/(np.linalg.norm(3*g2)))*3*g2).scale(0.4)\
         .shift(1.5*LEFT+1.75*UP)
      
      g1_gen = Arrow((0, 0, 0),(0.5,-0.5,0), buff = 0, color = ROJO, max_tip_length_to_length_ratio=0.4)
      
      g2_gen = Arrow((0, 0, 0), (-1,-1,0), buff = 0, color = AZUL, max_tip_length_to_length_ratio=0.4)


      ###### OBJETOS conj_ortogonal
      gamma_c_og = MathTex(r"\Gamma \text{ es }", r"\text{un conjunto \textit{ortogonal}}")\
         .scale(0.6).shift(4.5*RIGHT + DOWN)


      ppunto_1 = MathTex(r" \langle \vec{g}_1, \vec{g}_2 \rangle").shift(3*RIGHT + 2*UP).scale(0.6)
      ppunto_1[0][1:4].set_color(RED)
      ppunto_1[0][5:8].set_color(BLUE)
      ppunto_2 = MathTex(r" = \begin{pmatrix} 1 \\ -1 \end{pmatrix} \cdot \
          \begin{pmatrix} -2 \\ -2 \end{pmatrix}").next_to(ppunto_1,RIGHT).scale(0.6).shift(0.6*LEFT)
      ppunto_3 = MathTex(r"= (1)(-2) + (-1)(-2)").scale(0.6)
      ppunto_4 = MathTex(r"= 0 ").scale(0.6)
      ppunto_5 = MathTex(r"= \langle \vec{g}_2 , \vec{g}_1 \rangle ").scale(0.6)
      ppunto_5[0][2:5].set_color(BLUE)
      ppunto_5[0][6:9].set_color(RED)

      ppunto = VGroup(ppunto_2, ppunto_3, ppunto_4, ppunto_5)\
         .arrange(DOWN, center=False, aligned_edge=LEFT)


         # Se declaran los vectores que aparecen en el grid para usarlos posteriormente
         # y dibujar su generado

      g1_n = np.array([1,-1,0])
      g2_n = np.array([-2,-2,0])

      # OBJETOS base_ortogonal
      gamma_li = MathTex(r"\vec{g}_1\ \text{y}\ \vec{g}_2\ \text{son \textit{l.i.}}").shift(4.5*RIGHT+2*UP).scale(0.6)

      ld_g1 = DashedLine(-2*g1_n, 3.5*g1_n).set_color(MAGENTA).set_opacity(0.5).shift(2.5*LEFT+1.5*UP)
      ld_g2 = DashedLine(-1*g2_n, 1.75*g2_n).set_color(MAGENTA).set_opacity(0.5).shift(2.5*LEFT+1.5*UP)

      gamma_gen = MathTex(r"\langle \Gamma \rangle = \mathbb{R}^2").shift(4.5*RIGHT+0.5*UP).scale(0.6)

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
      c1_11 = MathTex(r" c_1 = ", r" \frac{-4}{2} ").next_to(c1_eq1).scale(0.6).shift(0.4*LEFT)
      c1_fbk1 = MathTex(r" c_1 = ", r" \frac{\langle \vec{v}, \vec{g}_1 \rangle}{\langle \vec{g}_1 , \vec{g}_1 \rangle} ").next_to(c1_eq1).scale(0.6).shift(0.4*LEFT)
      c1_11_r = MathTex(r" c_1 = ", r" \frac{-4}{2} ").next_to(c1_eq1).scale(0.6).shift(0.4*LEFT)
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
      c1_fbk2 = MathTex(r" c_2 = ", r" \frac{\langle \vec{v}, \vec{g}_2 \rangle}{\langle \vec{g}_2, \vec{g}_2 \rangle} ").next_to(c1_eq2).scale(0.6).shift(0.4*LEFT)
      c1_12_r = MathTex(r" c_2 = ", r" \frac{24}{8} ").next_to(c1_eq2).scale(0.6).shift(0.4*LEFT)
      c12 = MathTex(r" c_2 = " , r" 3 ").next_to(c1_eq2).scale(0.6).shift(0.4*LEFT)


      srct_1 = SurroundingRectangle(c12, color = AMARILLO)

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

   # PALOMA PARA ACOMPAÑAR A LA PROPIEDAD PROBADA
      p1 = Line(ORIGIN, [1,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
      p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
      paloma = VGroup(p1,p2).scale(0.2).set_opacity(0).next_to(comblin_R2_2,RIGHT)

      ###############
      # ANIMACIONES #
      ###############

      #self.next_section(skip_animations=True)
      self.play(Create(lilgrid), run_time=2.5)
      self.add(marco)
      self.add_foreground_mobjects(marco)
      self.play(FadeIn(vec_obj))
      self.play(FadeIn(v_label)) # Agregar label v_obj
      self.add_foreground_mobjects(vec_obj,v_label)
      self.add_foreground_mobjects(vec_obj_tex)
      self.play(Write(vec_obj_tex))
      self.wait(2)
      self.add_foreground_mobjects(vec_g1 , vec_g2, g1_label, g2_label)
      self.play(Create(vec_g1), Create(vec_g2), Create(g1_label), Create(g2_label))
      self.wait(1.5)
      self.add_foreground_mobjects(gamma_tex)
      self.play(Write(gamma_tex))
      self.wait(3)
      self.add_foreground_mobjects(comblin_abs)
      self.play(Write(comblin_abs), run_time=1.5)
      self.wait()
      self.add_foreground_mobjects(comblin_R2)
      self.play(Write(comblin_R2))
      self.wait(1.5)
      self.add_foreground_mobjects(coefs_incog)
      self.play(Write(coefs_incog))
      self.wait()
      
      #self.play(ReplacementTransform(v_label,v_label2))

      ########## ANIMACIONES conj_ortog
      #self.next_section(skip_animations=True)
      self.wait(2)
      self.add_foreground_mobjects(ppunto_1)
      self.play(Write(ppunto_1))
      self.add_foreground_mobjects(ppunto_2)
      self.play(Write(ppunto_2))
      self.add_foreground_mobjects(ppunto_3)
      self.play(Write(ppunto_3))
      self.wait(1.5)
      self.add_foreground_mobjects(ppunto_4)
      self.play(Write(ppunto_4))
      self.add_foreground_mobjects(ppunto_5)
      self.play(Write(ppunto_5), run_time=0.5)
      self.add_foreground_mobjects(gamma_c_og)
      self.play(Write(gamma_c_og))
      self.wait()
      self.play(gamma_c_og.animate.shift(9.5*LEFT+2.75*DOWN).scale(0.7), FadeOut(ppunto_1), FadeOut(ppunto_2), FadeOut(ppunto_3), FadeOut(ppunto_4), FadeOut(ppunto_5))
      self.wait(3)


      # # ANIMACIONES base_ortogonal
      #self.next_section(skip_animations=True)
      self.play(Create(ld_g1), run_time=0.5)
      self.play(Create(ld_g2), run_time=0.5)
      self.add_foreground_mobjects(gamma_li)
      self.play(Write(gamma_li), run_time=0.5)
      self.play( FadeOut(ld_g1), FadeOut(ld_g2))
      self.play(FadeOut(v_label), FadeOut(vec_obj),FadeOut(g1_label), FadeOut(g2_label))
      gen_simple(g1_gen, g2_gen)  # Animación del espacio generado
      self.play(FadeOut(marco))
      self.play(FadeIn(vec_obj))
      self.add_foreground_mobjects(g1_label,g2_label,v_label2)
      self.play(Write(g1_label), Write(g2_label), Write(v_label2))
      self.play(gamma_c_og.animate.shift(9.5*RIGHT+2.75*UP).scale(1/0.7))
      self.wait()
      self.play(FadeOut(gamma_c_og[1]))
      self.play(Write(gamma_b_og))
      self.wait()
      self.play(FadeOut(gamma_c_og[0]), gamma_b_og.animate.shift(9.5*LEFT+2.75*DOWN).scale(0.7))
      self.play(FadeOut(gamma_li), FadeOut(gamma_gen))

      ##### ANIMACIONES calc_c1
      #self.next_section(skip_animations=True)
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

      # Flashback
      #self.next_section(skip_animations=True)
      self.play(ReplacementTransform(c1_11, c1_fbk1))
      self.wait()
      self.play(ReplacementTransform(c1_fbk1, c1_11_r))
      self.play(ReplacementTransform(c1_11_r, c11))
      self.play(Write(srct_11))

      # Actualización de los coeficientes incógnitos y la ecuación en tuplas

      #self.next_section(skip_animations=True)
      self.play(ReplacementTransform(coefs_incog,c2_incog))
      self.add_foreground_mobjects(c2_incog) 
      self.play(ReplacementTransform(comblin_R2[0],comblin_R2_1[0]), ReplacementTransform(comblin_R2[1],comblin_R2_1[1]),
      ReplacementTransform(comblin_R2[2],comblin_R2_1[2]), ReplacementTransform(comblin_R2[3],comblin_R2_1[3]),
      ReplacementTransform(comblin_R2[4],comblin_R2_1[4]), ReplacementTransform(comblin_R2[5],comblin_R2_1[5]),
      ReplacementTransform(comblin_R2[6],comblin_R2_1[6]))
      self.add_foreground_mobjects(comblin_R2_1)
      

      self.play(FadeOut(vg1_11),FadeOut(vg1_21),FadeOut(pp31), FadeOut(ppl1),
       FadeOut(c1_eq1), FadeOut(c11), FadeOut(srct_11), FadeOut(ppig1), FadeOut(pp41),
       FadeOut(ppl_51), FadeOut(ppl_81))

      ##### ANIMACIONES calc_c2

      #self.next_section(skip_animations=True)
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

      # Flashback
      #self.next_section(skip_animations=True)
      self.play(ReplacementTransform(c1_12, c1_fbk2))
      self.wait()
      self.play(ReplacementTransform(c1_fbk2, c1_12_r))
      self.play(ReplacementTransform(c1_12_r, c12))
      self.play(Write(srct_1))

      self.play(ReplacementTransform(c2_incog,no_incog))
      self.add_foreground_mobjects(no_incog) 
      self.play(ReplacementTransform(comblin_R2_1[0],comblin_R2_2[0]), ReplacementTransform(comblin_R2_1[1],comblin_R2_2[1]),
      ReplacementTransform(comblin_R2_1[2],comblin_R2_2[2]), ReplacementTransform(comblin_R2_1[3],comblin_R2_2[3]),
      ReplacementTransform(comblin_R2_1[4],comblin_R2_2[4]), ReplacementTransform(comblin_R2_1[5],comblin_R2_2[5]),
      ReplacementTransform(comblin_R2_1[6],comblin_R2_2[6]))
      self.add_foreground_mobjects(comblin_R2_2)


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
      self.play(Create(paloma))
      self.add_foreground_mobjects(paloma)
      self.play(paloma.animate.set_opacity(1))
      self.wait(3)

      self.play(FadeOut(vec_g1), FadeOut(vec_g2))
      self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1)


      ###### OBJETOS  Sección Final

      #esunprod = Tex(" es un producto escalar en ").scale(0.7).shift(2*RIGHT)

      #pe_r2_a = MathTex(r"= u_1v_1 + u_2v_2").next_to(esunprod, LEFT).scale(0.9)
      #pe_r2_b = MathTex(r"= \sum_{i=1}^2 u_i v_i" ).next_to(esunprod, LEFT).scale(0.9)
      #pe_r3= MathTex(r"= \sum_{i = 1}^3 u_i v_i").next_to(esunprod, LEFT).scale(0.9)
      #pe_rn= MathTex(r"= \sum_{i = 1}^n u_i", r" v_i").next_to(esunprod, LEFT).scale(0.9)
      #pe_cn= MathTex(r"= \sum_{i = 1}^n u_i ",r"\bar{v}_i").next_to(esunprod, LEFT).scale(0.9)

      #dos_tupla = MathTex(r" \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}").next_to(pe_r2_a, LEFT).scale(0.9)
      #tres_tupla = MathTex(r" \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}").next_to(pe_r3, LEFT).scale(0.9)
      #n_tupla = MathTex(r" \begin{pmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \\  \vdots \\ v_n \end{pmatrix}").next_to(pe_rn, LEFT).scale(0.9)
      #erre2 = MathTex(r"\mathbb{R}^2").next_to(esunprod, RIGHT).scale(0.9)
      #erre3 = MathTex(r"\mathbb{R}^3").next_to(esunprod, RIGHT).scale(0.9)
      #erren = MathTex(r"\mathbb{R}^n").next_to(esunprod, RIGHT).scale(0.9)
      #cn = MathTex(r"\mathbb{C}^n").next_to(esunprod, RIGHT).scale(0.9)

      ##### ANIMACIONES Sección Final

      #self.play(Write(dos_tupla), Write(pe_r2_a), Write(esunprod), Write(erre2))
      #self.wait()

      ## R2 notación sigma
      #self.play(ReplacementTransform(pe_r2_a,pe_r2_b),dos_tupla.animate.next_to(pe_r2_b, LEFT), runtime = 2)
      #self.wait()

      ##R3
      #self.play(ReplacementTransform(dos_tupla,tres_tupla), ReplacementTransform(pe_r2_b,pe_r3)\
      #   , ReplacementTransform(erre2, erre3), runtime = 2)
      #self.wait()

      ##RN
      #self.play(ReplacementTransform(tres_tupla,n_tupla), ReplacementTransform(pe_r3,pe_rn)\
      #   , ReplacementTransform(erre3, erren), runtime = 2)
      #self.wait()
      #
      ##CN
      #self.play( ReplacementTransform(pe_rn[1],pe_cn[1])\
      #   , ReplacementTransform(erren, cn), runtime = 2)
      #self.wait()

      #self.play(
      #      *[FadeOut(mob) for mob in self.mobjects],
      #      run_time=1)
