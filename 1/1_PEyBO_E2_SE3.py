# -*- coding: utf-8 -*-

from manim import *
#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################


#####################################################################################
###############################  Segunda escena  ####################################
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

# MathTex(r"\alpha") -> Código en LaTeX
# Tex("blabla") -> texto normal
# SurroundingRectangle(self, mobject, color=YELLOW, buff=SMALL_BUFF, **kwargs)
# VGroup(mobjects)
# Line(start=LEFT, end=RIGHT, buff=0, path_arc=None, **kwargs)
# 

class Subescena_3(Scene):
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
        dem_1 = Tex(" Prueba de primer propiedad").shift( 3*RIGHT)
        
        #####################
        ## ANIMACIONES DEMO 1 ###
        #####################
        self.play(Write(dem_1))
        self.wait(1)
        self.play(FadeOut(dem_1))


    def demo_2(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la segunda propiedad del producto punto
        '''
        #----------- OBJETOS
        dem_2 = Tex(" Prueba de segunda propiedad").shift(3*RIGHT)
        
        #####################
        ## ANIMACIONES DEMO 2 ###
        #####################
        self.play(Write(dem_2))
        self.wait(1)
        self.play(FadeOut(dem_2))

    def demo_3(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la tercer propiedad del producto punto
        '''
        #----------- OBJETOS
        dem_3 = Tex(" Prueba de tercer propiedad").shift(3*RIGHT)
        
        #####################
        ## ANIMACIONES DEMO 3 ###
        #####################
        self.play(Write(dem_3))
        self.wait(1)
        self.play(FadeOut(dem_3))

    def demo_4(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la cuarta propiedad del producto punto
        '''
        #----------- OBJETOS
        dem_4 = Tex(" Prueba de cuarta propiedad").shift(3*RIGHT)
        
        #####################
        ## ANIMACIONES DEMO 4 ###
        #####################
        self.play(Write(dem_4))
        self.wait(1)
        self.play(FadeOut(dem_4))
    

    def construct(self):
        '''
        Aquí se definen objetos y animaciones que estarán a lo largo de toda la subescena, por lo que
        se definen en el método principal (construct). Siempre que queramos ver/omitir una de las pruebas
        podemos descomentar/comentar la línea donde se invoca la función.
        '''
        #-------------- DEFINICIÓN DEL PP EN ABSTRACTO: OPERACION Y PROPS (OBJETOS)
        pe_def = MathTex(r" \langle\cdot,\cdot\rangle:",r"V", r"\times ", r"V",r"\to ",r"K").shift(2*UP)
        pe_def_1 = MathTex(r" \forall \ \vec{u}, \vec{v}, \vec{w}&\in V, \ \forall \ a\in K ").next_to(pe_def, 1.1*DOWN)
        pe_def_2 = MathTex(r"  \langle\vec{u}+\vec{w},\vec{v}\rangle &= \langle \vec{u} , \vec{v} \rangle + \langle \vec{w} , \vec{v} \rangle ").next_to(pe_def_1, 1.1*DOWN)
        pe_def_3 = MathTex(r"  \langle a\vec{u} , \vec{v} \rangle &= a \langle \vec{u} , \vec{v} \rangle ").next_to(pe_def_2, 1.1*DOWN)
        pe_def_4 = MathTex(r"  \langle \vec{u} , \vec{v} \rangle &= \overline{ \langle \vec{v} , \vec{u} \rangle} ").next_to(pe_def_3, 1.1*DOWN)
        pe_def_5 = MathTex(r" \langle \vec{u}, \vec{u} \rangle > 0 \ &\ \text{si} \ \ \vec{u}\neq\vec{0} ").next_to(pe_def_4, 1.1*DOWN)

        #VGroup que contiene las propiedades que debe satisfacer el P.E. en abstracto
        pe_group_2 = VGroup(pe_def_1, pe_def_2, pe_def_3, pe_def_4, pe_def_5).scale(0.8).shift(0.5*DOWN)
        
        #---------------- PASANDO DE LO ABSRTACTO AL CASO PARTICULAR en R2 (OJETOS)
        pp_def = MathTex(r" \langle\cdot,\cdot\rangle:",r"\mathbb{R}^2", r"\times ", r"\mathbb{R}^2",r"\to ",r"\mathbb{R}").shift(2*UP) # SE QUEDA
        pp_def[1].set_color(AMARILLO)
        pp_def[3].set_color(AMARILLO)
        pp_def[5].set_color(AZUL_CLARO)
        entries_v = [["v_{1}"], ["v_{2}"]]  
        vec_v = Matrix(entries_v,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(LEFT)
        vec_v_label = MathTex(r"v = ").next_to(vec_v, LEFT)

        entries_w = [["w_{1}"], ["w_{2}"]] 
        vec_w = Matrix(entries_w,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(2*RIGHT)
        vec_w_label = MathTex(r"w = ").next_to(vec_w, LEFT)                    

        vecs_enR2 = VGroup(vec_v_label, vec_v, vec_w_label, vec_w).scale(0.9).shift(0.4*UP) # SE QUEDA
        pp_oper = MathTex(r"\langle \vec{v},\vec{w}\rangle  = \vec{v}\cdot\vec{w} = v_1w_1 + v_2w_2" ).shift(DOWN) #SE QUEDA

        #------------- REACOMODO DE LAS COSAS EN LA PANTALLA, DIBUJAMOS LÍNEAS (OBJETOS)
        
        linea_1 = Line(start = 7*LEFT + 0.5*UP, end = LEFT + 0.5*UP, buff= 0.5)
        linea_2 = Line(start = 4*UP + 1.5*LEFT, end = 4*DOWN + 1.5*LEFT, buff= 0.5)


    #####################
    ## ANIMACIONES   ###
    #####################

        # INTRODUCCION, PLANTEAMIENTO DEL CASO PARTICULAR Y DEFINICIÓN DEL PP 
        self.play(Write(pe_def))
        self.wait()
        self.play(Write(pe_group_2), runtime = 2)
        self.wait()
        self.play(pe_group_2.animate.set_opacity(0))
        self.play(ReplacementTransform(pe_def,pp_def))
        self.play(Write(vecs_enR2))
        self.wait(0.5)
        self.play(Write(pp_oper))

        #------ REACOMODO DE LOS OBJETOS Y DIBUJO DE LÍNEAS 
        self.play(pp_def.animate.shift(4*LEFT+1*UP).scale(0.7))
        self.play(vecs_enR2.animate.shift(4*LEFT+1.6*UP).scale(0.7))
        self.play(pp_oper.animate.shift(4*LEFT+2*UP).scale(0.7))
        self.play(Write(linea_1))
        self.play(Write(linea_2))

        
        self.play(pe_def_1.animate.shift(4*LEFT+0.5*DOWN).scale(0.6))
        self.play(pe_def_1.animate.set_opacity(1))
        self.play(pe_def_2.animate.shift(4*LEFT+0.8*DOWN).scale(0.8))
        self.play(pe_def_2.animate.set_opacity(1))
        self.play(pe_def_3.animate.shift(4*LEFT+0.8*DOWN).scale(0.8))
        self.play(pe_def_3.animate.set_opacity(1))
        self.play(pe_def_4.animate.shift(4*LEFT+0.8*DOWN).scale(0.8))
        self.play(pe_def_4.animate.set_opacity(1))
        self.play(pe_def_5.animate.shift(4*LEFT+0.8*DOWN).scale(0.8))
        self.play(pe_def_5.animate.set_opacity(1))

        #######################
        # ANIM PREVIAS A DEM 1 #
        #######################

        self.play(pe_def_3.animate.set_opacity(0.3), pe_def_4.animate.set_opacity(0.3),
        pe_def_4.animate.set_opacity(0.3), pe_def_5.animate.set_opacity(0.3))
        self.play(pe_def_2.animate.scale(1.2))

        self.demo_1() # Llamamos a la animación completa de la primer demostración

        #######################
        # ANIM PREVIAS A DEM 2 #
        #######################

        self.play(pe_def_2.animate.scale(1/1.2).set_opacity(0.3))
        self.play(pe_def_3.animate.set_opacity(1).scale(1.2))

        self.demo_2() # Llamamos a la animación completa de la segunda demostración

        #######################
        # ANIM PREVIAS A DEM 3 #
        #######################

        self.play(pe_def_3.animate.scale(1/1.2).set_opacity(0.3))
        self.play(pe_def_4.animate.set_opacity(1).scale(1.2))

        self.demo_3() # Llamamos a la animación completa de la tercera demostración

        #######################
        # ANIM PREVIAS A DEM 4 #
        #######################

        self.play(pe_def_4.animate.scale(1/1.2).set_opacity(0.3))
        self.play(pe_def_5.animate.set_opacity(1).scale(1.2))

        self.demo_4() # Llamamos a la animación completa de la cuarta demostración

        #####################
        # ANIMACIONES FINALES
        #####################
        self.play(pe_def_5.animate.scale(1/1.2))

        self.play(pe_def_2.animate.set_opacity(1))
        self.play(pe_def_3.animate.set_opacity(1))
        self.play(pe_def_4.animate.set_opacity(1))
