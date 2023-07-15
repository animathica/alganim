from manim import *
#####################################################################################
######################  Norma inducida y bases ortonormales  ########################
#####################################################################################

#####################################################################################
###############################  Tercera escena  ####################################
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

class E3(MovingCameraScene):
    def construct(self):

        texto1 = MathTex(r"(V,K)").scale(0.6)
        texto2 = MathTex(r" \langle \cdot , \cdot \rangle : V\times V\to K \ \text{es un producto escalar en} \ V ").scale(.6)

        texto_1=VGroup(texto1, texto2).arrange(direction=1.5*DOWN).shift(2*UP)

        texto3=MathTex(r"||\vec{v}||:=\sqrt{\langle \vec{v} , \vec{v} \rangle} \quad \forall \ \vec{v}\in V").scale(.6)
        texto4=MathTex(r"||\cdot||:V \to \mathbb{R}^{\geq0}").scale(.6)
        texto5=MathTex(r"\forall \ \vec{u}\in V,", r" \forall \ a \in K,").scale(.6)

        texto_2=VGroup(texto3, texto4, texto5).arrange(direction=1.5*DOWN, center=True).next_to(texto_1, 1.5*DOWN)

        texto6=MathTex(r"||a\vec{u}|| = \sqrt{\langle a\vec{u} , a\vec{u} \rangle}", r"= \sqrt{ a\overline{a}\langle \vec{u} , \vec{u} \rangle}", r" = \sqrt{a\overline{a}}", r"\sqrt{\langle \vec{u} , \vec{u} \rangle}", r" = |a| \ ||\vec{u}||").scale(.6)
        texto7=MathTex(r"|| \vec{u} ||= 0", r" \Longleftrightarrow" r"\sqrt{\langle \vec{u} , \vec{u} \rangle}", r" = 0", r"\Longleftrightarrow", r" \langle \vec{u} , \vec{u} \rangle = 0", r" \Longleftrightarrow ",  r"\vec{u} = \vec{0}").scale(.6)

        texto_3=VGroup(texto6, texto7).arrange(direction=1.5*DOWN, center=False, aligned_edge=RIGHT).next_to(texto_2, 1.5*DOWN)
        texto_3.shift(2.5*LEFT)

        texto8=Tex("Escalabilidad absoluta").scale(.6)
        texto9=Tex("Distinción del vector nulo").scale(.6)
        texto10=Tex("Desigualdad del triángulo").scale(.6)

        texto11=MathTex(r"||\cdot||:V \to \mathbb{R}^{\geq0} \text{ es una \emph{norma inducida por un producto escalar}").scale(.6).shift(3.25*DOWN)

        texto_4=VGroup(texto8, texto9, texto10).arrange(direction=1.9*DOWN, center=False, aligned_edge=LEFT).next_to(texto_2, 1.5*DOWN).shift(3.5*RIGHT+0.125*DOWN)

        p1 = Line(ORIGIN, [1,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma1 = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(5.5*RIGHT+1.65*DOWN)
        paloma2 = paloma1.copy().shift(0.7*DOWN)
        paloma3 = paloma1.copy().shift(1.4*DOWN)

        #Animaciones

        self.camera.frame.shift(0.4*DOWN)

        self.play(Write(texto1, run_time=0.5))
        self.play(Write(texto2))

        self.wait()

        self.play(Write(texto3))

        self.wait(3)

        self.play(Write(texto4))

        self.wait()

        texto5.shift(2.5*LEFT)
        self.play(Write(texto5))

        self.play(Write(texto6))

        self.play(Write(texto7))

        self.wait()

        self.play(Write(texto8))

        self.play(Write(texto9))

        self.add(paloma1, paloma2, paloma3)
        self.play(paloma1.animate.set_opacity(1),
                  paloma2.animate.set_opacity(1))

        self.play(Write(texto10))

        self.play(paloma3.animate.set_opacity(1))

        self.play(Write(texto11[0][0:21]))

        self.wait(7)

        self.play(Write(texto11[0][21:]))
