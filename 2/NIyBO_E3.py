from manim import *
#####################################################################################
######################  Norma inducida y bases ortonormales  ########################
#####################################################################################

#####################################################################################
###############################  Tercera escena  ####################################
######################  versión: Manim Community v0.17.3   ##########################
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

SKIP_DEFAULT = False #Útil para lo siguiente: si sólo quieres renderizar una sección, cambia esta variable a 'True' y cambia el valor de 'skip_animations' de esa sección a 'not SKIP_DEFAULT'


class E3(MovingCameraScene):
    def construct(self):

        texto0 = Tex("\\mbox{*", "Ver el ", "Ejercicio 1.2 ", "del video ", "\\emph{Producto escalar, bases ortogonales y proyecciones vectoriales }", "de Animathica.}").scale(0.55).to_edge(DOWN)
        texto0[0].set_color(AMARILLO)
        texto0[2].set_color(AZUL)
        texto0[4].set_color(AMARILLO)

        texto1 = MathTex(r"(V,K)").scale(0.6)
        texto2 = MathTex(r" \langle \cdot , \cdot \rangle : V\times V\to K \ \text{es un producto escalar en} \ V ").scale(.6)

        texto_1=VGroup(texto1, texto2).arrange(direction=1.5*DOWN).shift(2.3*UP)

        texto3=MathTex(r"||\vec{v}||:=\sqrt{\langle \vec{v} , \vec{v} \rangle} \quad \forall \ \vec{v}\in V").scale(.6)
        texto4=MathTex(r"||\cdot||:V \to", "\mathbb{R}^{\geq0}").scale(.6)
        texto5=MathTex(r"\forall \ \vec{u}\in V,", r" \ \forall \ a \in K,").scale(.6)
        texto3.next_to(texto_1, 3*DOWN)
        texto_2=VGroup(texto4, texto5).arrange(direction=1.5*DOWN, center=True).next_to(texto3, 3*DOWN)

        texto6=MathTex(r"||a\vec{u}||", r" = \sqrt{\langle a\vec{u} , a\vec{u} \rangle}", r"= \sqrt{ a\overline{a}\langle \vec{u} , \vec{u} \rangle}", r" = \sqrt{a\overline{a}} \sqrt{\langle \vec{u} , \vec{u} \rangle}", r" = |a| \ ||\vec{u}||").scale(.6)
        texto7=MathTex(r"|| \vec{u} ||= 0", r" \Longleftrightarrow", r"\sqrt{\langle \vec{u} , \vec{u} \rangle} = 0", r"\Longleftrightarrow", r" \langle \vec{u} , \vec{u} \rangle = 0", r" \Longleftrightarrow ",  r"\vec{u} = \vec{0}").scale(.6)

        texto_3=VGroup(texto6, texto7).arrange(direction=1.5*DOWN, center=False, aligned_edge=RIGHT).next_to(texto_2, 1.5*DOWN)
        texto_3.shift(2.5*LEFT)

        texto8=Tex("Escalabilidad absoluta").scale(.6)
        texto9=Tex("Distinción del vector nulo").scale(.6)
        texto10=Tex("Desigualdad del triángulo").scale(.6)

        texto11=MathTex(r"||\cdot||:V \to \mathbb{R}^{\geq0} \text{ es una \emph{norma inducida por un producto escalar.}").scale(.6).shift(3.7*DOWN)

        texto_4=VGroup(texto8, texto9, texto10).arrange(direction=1.9*DOWN, center=False, aligned_edge=LEFT).next_to(texto_2, 1.5*DOWN).shift(3.5*RIGHT+0.125*DOWN)

        p1 = Line(ORIGIN, [1,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma1 = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(5.5*RIGHT+2.1*DOWN)
        paloma2 = paloma1.copy().shift(0.7*DOWN)
        paloma3 = paloma1.copy().shift(1.4*DOWN)

        #Animaciones
        self.next_section("...operaciones positivo definidas que distinguen al vector nulo", skip_animations=SKIP_DEFAULT)
        self.play(Write(texto0), run_time=2.5)
        self.wait(3)
        self.play(FadeOut(texto0), run_time=0.5)
        self.wait()

        self.next_section("Supongamos que tenemos un espacio vectorial con producto escalar...", skip_animations=SKIP_DEFAULT)
        self.camera.frame.shift(0.4*DOWN) #Ajusta la altura de la cámara para el encuadre
        self.play(Write(texto1))
        self.play(Write(texto2), run_time=0.9)
        self.wait()

        self.next_section("...siguiente manera.", skip_animations=SKIP_DEFAULT)
        self.play(Write(texto3[0][:17]), run_time=2.25)
        self.wait(0.25)
        self.play(Write(texto3[0][17:]), run_time=1.25)
        self.wait()

        self.next_section("...a cada vector del espacio un número real no negativo....", skip_animations=SKIP_DEFAULT)#En el futuro, cambiar a "número real MAYOR O IGUAL QUE 0" para no entrar en posibles controversias
        self.play(Write(texto4[0]), run_time=2)
        self.play(Write(texto4[1]), run_time=1.5)
        self.wait()

        self.next_section("...siguientes propiedades:", skip_animations=SKIP_DEFAULT)
        self.play(Write(texto5), run_time=2)
        self.play(Write(texto6[0]))
        self.wait(0.5)
        self.play(Write(texto6[1]))
        self.wait(0.5)
        self.play(Write(texto6[2]))
        self.wait(0.5)
        self.play(Write(texto6[3]))
        self.wait(0.5)
        self.play(Write(texto6[4]))
        self.wait()
        self.play(Write(texto7[0]))
        self.wait(0.5)
        self.play(Write(texto7[1]))
        self.wait(0.5)
        self.play(Write(texto7[2]))
        self.wait(0.5)
        self.play(Write(texto7[3]))
        self.wait(0.5)
        self.play(Write(texto7[4]))
        self.wait(0.5)
        self.play(Write(texto7[5]))
        self.wait(0.5)
        self.play(Write(texto7[6]))
        self.wait()

        self.next_section("...escalabilidad absoluta y distinción del vector nulo.", skip_animations=SKIP_DEFAULT)
        self.add(paloma1, paloma2, paloma3)
        self.play(Write(texto8), Indicate(texto6[0], rate_func=there_and_back_with_pause), Indicate(texto6[4], rate_func=there_and_back_with_pause))
        self.play(paloma1.animate.set_opacity(1), run_time=0.5)
        self.play(Write(texto9), Indicate(texto7[0], rate_func=there_and_back_with_pause), Indicate(texto7[5], rate_func=there_and_back_with_pause), Indicate(texto7[6], rate_func=there_and_back_with_pause))
        self.play(paloma2.animate.set_opacity(1), run_time=0.5)

        self.next_section("...desigualdad del triángulo.", skip_animations=SKIP_DEFAULT)
        self.play(Write(texto10))
        self.play(paloma3.animate.set_opacity(1), run_time=0.5)
        self.play(Indicate(texto3), run_time=6.5)
        self.wait(6.5)
        sub = Tex("Si deseas recibir la notificación, \emph{¡subscríbete!}", color=AMARILLO).scale(0.6).next_to(texto10, 2.8*LEFT)
        self.play(Write(sub))
        self.wait()

        self.next_section("...norma inducida por un producto escalar.", skip_animations=SKIP_DEFAULT)
        self.play(Write(texto11), run_time=4)
        self.play(Circumscribe(texto3))
        self.wait()
