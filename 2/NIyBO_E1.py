from manim import *
#####################################################################################
######################  Norma inducida y bases ortonormales  ########################
#####################################################################################

#####################################################################################
###############################  Primera escena  ####################################
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


#class SE1(Scene):
#   def propiedades(self):


class SE2(Scene):
    def propiedades(self):
        t0 = Tex("Norma")
        t1 = MathTex("||\\cdot||:V \\to \\mathbb{R}_{\geq0}").scale(0.6)

        p1 = MathTex("\\forall \ \\vec{u},\\vec{v}\\in V, \ \\forall \ a\\in K,").scale(0.6)
        p2 = MathTex("||a\\vec{u}||", "=", "|a| \ ||\\vec{u}||").scale(0.6).move_to(2*LEFT)
        p3 = MathTex("||\\vec{u}|| = 0 ", " \\Longleftrightarrow", " \\vec{u} = \\vec{0}").scale(0.6).next_to(p2, 2*DOWN)
        p4 = MathTex("||\\vec{u}+\\vec{v}|| ", "\\le", " ||\\vec{u}|| + ||\\vec{v}||").scale(0.6).next_to(p3, 2*DOWN)

        pe2 = p2.get_part_by_tex("=")
        pe3 = p3.get_part_by_tex("\\Longleftrightarrow").align_to(pe2, LEFT)
        pe4 = p4.get_part_by_tex("\\le").align_to(pe3, LEFT)
        p2.get_part_by_tex("||a\\vec{u}||").next_to(pe2, LEFT)
        p2.get_part_by_tex("|a| \ ||\\vec{u}||").next_to(pe2, RIGHT)
        p3.get_part_by_tex("||\\vec{u}|| = 0 ").next_to(pe3, LEFT)
        p3.get_part_by_tex(" \\vec{u} = \\vec{0}").next_to(pe3, RIGHT)
        p4.get_part_by_tex("||\\vec{u}+\\vec{v}|| ").next_to(pe4, LEFT)
        p4.get_part_by_tex(" ||\\vec{u}|| + ||\\vec{v}||").next_to(pe4, RIGHT)

        tinv = Tex("aaaa", color = BLACK).scale(0.6).next_to(p3, RIGHT)
        t2 = Tex("Escalabilidad \\emph{absoluta}").scale(0.6)
        t3 = Tex("Distinción del vector nulo").scale(0.6)
        t4 = Tex("Desigualdad del triángulo").scale(0.6)

        g = VGroup(t2,t3,t4).arrange(direction=2.5*DOWN, aligned_edge=LEFT)
        g.next_to(tinv, RIGHT)
        t0.move_to(2.5*UP)
        self.play(Write(t0))
        t1.move_to(2*UP)
        p1.move_to(0.8*UP+2*LEFT)
        p3.shift(0.15*LEFT)

        #Animaciones
        self.play(Write(t1))
        self.play(Write(p1))

        self.play(Write(p2))
        self.play(Write(p3))
        self.play(Write(p4))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))

    def construct(self):
        self.propiedades()
