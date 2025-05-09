from manim import *
from math import (cos, sin)
#####################################################################################
######################  Norma inducida y bases ortonormales  ########################
#####################################################################################

#####################################################################################
###############################  Primera escena  ####################################
######################  versión: Manim Community v0.19   ##########################
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
CARTÓN = "#CD9F61"
CARTÓN_BORDE = "#C08F4F"

SKIP_DEFAULT = False #Útil para lo siguiente: si sólo quieres renderizar una sección, cambia esta variable a 'True' y cambia el valor de 'skip_animations' de esa sección a 'not SKIP_DEFAULT'


class SE1(Scene):
    def construct(self):
        #Empujando la caja: Mobjects
        plano = NumberPlane()
        caja = Square(fill_opacity=1, fill_color=CARTÓN, stroke_color=CARTÓN_BORDE, stroke_width=8, side_length=1)
        vec_u = Arrow(start=ORIGIN, end=3*UP, color=AZUL, buff=0)
        label_u = MathTex("\\vec{u}", color=AZUL).next_to(vec_u, 0.8*LEFT)
        vec_v = Arrow(start=ORIGIN, end=5*RIGHT, color=ROJO, buff=0)
        label_v = MathTex("\\vec{v}", color=ROJO).next_to(vec_v, 0.75*DOWN)

        vec_u_fantasma = Arrow(start=vec_v.get_end(), end=vec_v.get_end()+vec_u.get_end(), color=AZUL, buff=0)
        label_u_fantasma = MathTex("\\vec{u}", color=AZUL).next_to(vec_u_fantasma, 0.8*RIGHT)
        vec_v_fantasma = Arrow(start=vec_u.get_end(), end=vec_v.get_end()+vec_u.get_end(), color=ROJO, buff=0)
        label_v_fantasma = MathTex("\\vec{v}", color=ROJO).next_to(vec_v_fantasma, 0.75*UP)
        desplazamiento = Arrow(start=ORIGIN, end=vec_v.get_end()+vec_u.get_end(), color=MAGENTA, buff=0)
        label_desplazamiento_1 = MathTex("\\vec{u}+\\vec{v}").move_to(4*RIGHT+1.5*UP)
        label_desplazamiento_1[0][0:2].set_color(AZUL)
        label_desplazamiento_1[0][3:].set_color(ROJO)
        label_desplazamiento_1_box = SurroundingRectangle(label_desplazamiento_1, color=BLACK, fill_opacity=1)
        label_desplazamiento_2 = MathTex("\\vec{v}+\\vec{u}").move_to(RIGHT+1.5*UP)
        label_desplazamiento_2[0][0:2].set_color(ROJO)
        label_desplazamiento_2[0][3:].set_color(AZUL)
        label_desplazamiento_2_box = SurroundingRectangle(label_desplazamiento_2, color=BLACK, fill_opacity=1)
        igual = MathTex("=").move_to(3*DOWN)
        igual_box = SurroundingRectangle(igual, color=BLACK, fill_opacity=1, buff=0.25)

        #Empujando la caja: Animaciones
        self.next_section("Por ejemplo, supongamos que podemos colocar una caja...", skip_animations=SKIP_DEFAULT)
        self.play(Create(plano), run_time=1.5)
        self.wait()
        self.play(FadeIn(caja))
        self.wait()

        self.next_section("...hacia el frente, con una fuerza que llamaremos u...", skip_animations=SKIP_DEFAULT)
        self.play(caja.animate.shift(3*UP), Create(vec_u)) #ARREGLAR sincronización con rate functions
        self.play(FadeIn(label_u))
        self.wait()

        self.next_section("...hacia un lado con una fuerza mayor, que llamaremos v", skip_animations=SKIP_DEFAULT)
        self.play(caja.animate.shift(5*RIGHT), Create(vec_v_fantasma), run_time=1.5)
        self.play(FadeIn(label_v_fantasma))
        self.wait()

        self.next_section("Observemos el desplazamiento obtenido...", skip_animations=SKIP_DEFAULT)
        self.play(FadeIn(desplazamiento, label_desplazamiento_1_box))
        self.play(FadeIn(label_desplazamiento_1[0][0:2]))
        self.play(FadeIn(label_desplazamiento_1[0][2]), run_time=0.5)
        self.play(FadeIn(label_desplazamiento_1[0][3:]))
        self.wait()

        self.next_section("Ahora, imaginemos que desde el mismo punto de partida...", skip_animations=SKIP_DEFAULT)
        self.play(FadeOut(vec_u, label_u, vec_v_fantasma, label_v_fantasma, desplazamiento, label_desplazamiento_1_box, label_desplazamiento_1))
        self.wait()
        self.play(caja.animate.shift(3*DOWN+5*LEFT))
        self.wait()

        self.next_section("...hacia el mismo lado con la miasma fuerza v antes...", skip_animations=SKIP_DEFAULT)
        self.play(caja.animate.shift(5*RIGHT), Create(vec_v), run_time=1.5)
        self.play(FadeIn(label_v))
        self.wait()

        self.next_section("...hacia el frente con fuerza u.", skip_animations=SKIP_DEFAULT)
        self.play(caja.animate.shift(3*UP), Create(vec_u_fantasma))
        self.play(FadeIn(label_u_fantasma))
        self.wait()

        self.next_section("...es el mismo, a pesar de haber aplicado las fuerzas...", skip_animations=SKIP_DEFAULT)
        self.play(FadeIn(desplazamiento, label_desplazamiento_2_box))
        self.wait(2)
        self.play(FadeIn(label_desplazamiento_2[0][0:2]), run_time=0.5)
        self.play(FadeIn(label_desplazamiento_2[0][2]), run_time=0.5)
        self.play(FadeIn(label_desplazamiento_2[0][3:]), run_time=0.5)
        self.wait(1.5)
        self.play(FadeIn(vec_u, label_u, vec_v_fantasma, label_v_fantasma, label_desplazamiento_1_box, label_desplazamiento_1), run_time=1.5)
        self.wait()

        self.next_section("...en las mismas direcciones y con las mismas fuerzas en cada dirección...", skip_animations=SKIP_DEFAULT)
        self.play(label_desplazamiento_1.animate.move_to(LEFT+3*DOWN), label_desplazamiento_1_box.animate.move_to(LEFT+3*DOWN), run_time=1.25)
        self.play(FadeIn(igual_box, igual), run_time=0.5)
        self.play(label_desplazamiento_2.animate.move_to(RIGHT+3*DOWN), label_desplazamiento_2_box.animate.move_to(RIGHT+3*DOWN), run_time=1.25)
        self.wait(2)
        self.play(igual.animate.set_color(MAGENTA), run_time=1.5)
        self.wait()

        #Ley del Paralelogramo: Mobjects
        forall = MathTex("x \\ \\forall \\ \\vec{u}, \\vec{v} \\in \\mathbb{R}^2").move_to(1.6*RIGHT+3*DOWN)
        forall[0][0].set_color(BLACK)
        forall[0][2:4].set_color(AZUL)
        forall[0][5:7].set_color(ROJO)
        V = MathTex("V^2").move_to(forall[0][8:].get_center())
        V[0][1].set_color(BLACK)
        forall_box = SurroundingRectangle(forall, color=BLACK, fill_opacity=1)
        equation = VGroup(label_desplazamiento_1_box, igual_box, label_desplazamiento_2_box, label_desplazamiento_1, igual,  label_desplazamiento_2)

        #Ley del Paralelogramo: ValueTrackers y updaters
        nu, au, nv, av = ValueTracker(3), ValueTracker(PI/2), ValueTracker(5), ValueTracker(0) #Normas y ángulos de u y v
        vec_u.add_updater( lambda v: v.become(Arrow(start=ORIGIN, end=[nu.get_value()*cos(au.get_value()), nu.get_value()*sin(au.get_value()), 0], color=AZUL, buff=0)) ) 
        vec_v.add_updater( lambda v: v.become(Arrow(start=ORIGIN, end=[nv.get_value()*cos(av.get_value()), nv.get_value()*sin(av.get_value()), 0], color=ROJO, buff=0)) ) 
        vec_u_fantasma.add_updater( lambda v: v.become(Arrow(start=vec_v.get_end(), end=vec_v.get_end()+[nu.get_value()*cos(au.get_value()), nu.get_value()*sin(au.get_value()), 0], color=AZUL, buff=0)) ) 
        vec_v_fantasma.add_updater( lambda v: v.become(Arrow(start=vec_u.get_end(), end=vec_v.get_end()+vec_u.get_end(), color=ROJO, buff=0)) ) 
        desplazamiento.add_updater( lambda v: v.become(Arrow(start=ORIGIN, end=vec_v.get_end()+[nu.get_value()*cos(au.get_value()), nu.get_value()*sin(au.get_value()), 0], color=MAGENTA, buff=0)) )

        #Ley del Paralelogramo: Animaciones
        #self.next_section(skip_animations=True)
        self.next_section("...[La Ley del] Paralelogramo no es más que una generalización de esta observación...", skip_animations=SKIP_DEFAULT)
        self.play(FadeOut(label_u, label_v, label_u_fantasma, label_v_fantasma), caja.animate.set_opacity(0))
        self.wait()
        self.play(equation.animate.shift(1.5*LEFT))
        self.play(FadeIn(forall_box, forall))
        self.play(Circumscribe(Group(label_desplazamiento_1, forall)))
        self.wait()

        self.next_section("...dirección que sea...", skip_animations=SKIP_DEFAULT)
        self.play(au.animate.set_value(PI),
                  av.animate.set_value(-PI/6),
                  run_time=0.5
                  )
        self.play(au.animate.set_value(9*PI/8),
                  av.animate.set_value(PI/4),
                  run_time=0.5
                  )
        self.play(au.animate.set_value(PI/2),
                  av.animate.set_value(0),
                  run_time=0.5
                  )
        self.wait()

        self.next_section("...además de poder ser arbitrariamente grandes o pequeñas.", skip_animations=SKIP_DEFAULT)
        self.play(nu.animate.set_value(3.5),
                  nv.animate.set_value(6.5),
                  run_time=0.5
                  )
        self.play(nu.animate.set_value(0.5),
                  nv.animate.set_value(0.75),
                  run_time=0.5
                  )
        self.play(nu.animate.set_value(3),
                  nv.animate.set_value(5),
                  run_time=0.5
                  )
        self.wait()

        self.next_section("...conmutatividad de la suma vectorial...", skip_animations=SKIP_DEFAULT)
        self.play(Transform(forall[0][8:], V))
        self.play(Circumscribe(Group(label_desplazamiento_1, forall))) 
        self.play(Circumscribe(Group(label_desplazamiento_1, forall))) 
        self.wait()

        self.next_section("...más intuitivas.", skip_animations=SKIP_DEFAULT)
        vec_u.clear_updaters()          #Es necesario quitar todos los updaters
        vec_v_fantasma.clear_updaters() #para tener un FadeOut correcto.
        self.play(FadeOut(equation), FadeOut(forall), FadeOut(forall_box), FadeOut(vec_u), FadeOut(vec_v_fantasma))
        self.wait()

        #Magnitud: Mobjects
        brace_v = BraceBetweenPoints(ORIGIN, vec_v.get_end())
        brace_v.add_updater(lambda v:
                           (brace_v.become( BraceBetweenPoints(ORIGIN, vec_v.get_end()) )) if (nv.get_value() > 0)
                            else brace_v.become( BraceBetweenPoints(vec_v.get_end(), ORIGIN) )
                           )
        brace_u_fantasma = BraceBetweenPoints(vec_v.get_end(), vec_v.get_end()+vec_u.get_end())
        brace_u_fantasma.add_updater(lambda v:
                                    brace_u_fantasma.become(BraceBetweenPoints(vec_v.get_end(), vec_v.get_end()+[nu.get_value()*cos(au.get_value()), nu.get_value()*sin(au.get_value()), 0]))
                                    )
        brace_desplazamiento = BraceBetweenPoints(vec_v.get_end()+[nu.get_value()*cos(au.get_value()), nu.get_value()*sin(au.get_value()), 0], ORIGIN)
        brace_desplazamiento.add_updater(lambda v:
                                    brace_desplazamiento.become(BraceBetweenPoints(vec_v.get_end()+[nu.get_value()*cos(au.get_value()), nu.get_value()*sin(au.get_value()), 0], ORIGIN))
                                    )
        span_v_1 = Line(start=ORIGIN, end=[7.1,0,0], color=RED).set_z_index(0.5).set_opacity(0.95)
        span_v_2 = Line(start=ORIGIN, end=[-7.1,0,0], color=RED).set_z_index(0.5).set_opacity(0.95)
        circ_u = Circle(radius=nu.get_value(), color=AZUL, stroke_opacity=0.5, fill_opacity=0)
        circ_v = Circle(radius=3.5, color=ROJO, stroke_opacity=0.5, fill_opacity=0)

        #Magnitud: Animaciones
        self.next_section("Dado que un aumento o disminución de fuerza...", skip_animations=SKIP_DEFAULT)
        self.play(FadeIn(brace_v, brace_u_fantasma))
        self.play(nu.animate.set_value(3.5),
                  nv.animate.set_value(6.5),
                  run_time=0.75
                  )
        self.play(nu.animate.set_value(1.5),
                  nv.animate.set_value(3),
                  run_time=0.75
                  )
        self.play(nu.animate.set_value(3),
                  nv.animate.set_value(5),
                  run_time=0.5
                  )
        self.wait(0.25)
        self.play(FadeIn(brace_desplazamiento))
        self.play(nu.animate.set_value(3.5),
                  nv.animate.set_value(6.5),
                  run_time=0.75
                  )
        self.play(nu.animate.set_value(1.5),
                  nv.animate.set_value(3),
                  run_time=0.75
                  )
        self.play(nu.animate.set_value(3),
                  nv.animate.set_value(5),
                  run_time=0.5
                  )
        self.wait()

        self.next_section("...asociar la longitud de la flecha que representa a un vector", skip_animations=SKIP_DEFAULT)
        desplazamiento.clear_updaters() #Es necesario quitar todos los updaters
        vec_u_fantasma.clear_updaters() #para tener un FadeOut correcto.
        self.play(FadeOut(desplazamiento), FadeOut(brace_desplazamiento), FadeOut(vec_u_fantasma), FadeOut(brace_u_fantasma))
        self.wait()

        self.next_section("...nos dice qué tan cerca o lejos están del vector nulo...", skip_animations=SKIP_DEFAULT)
        self.play(nv.animate.set_value(0.75), run_time=0.75)
        self.play(nv.animate.set_value(-0.75), run_time=0.75)
        self.play(nv.animate.set_value(7), run_time=0.75)
        self.play(nv.animate.set_z_index(-7), nv.animate.set_value(-7), run_time=0.75)
        self.play(nv.animate.set_value(5), run_time=0.75)
        self.wait(1.5)
        self.play(Write(span_v_1), Write(span_v_2))
        self.play(nv.animate.set_value(-7), run_time=0.75)
        self.play(nv.animate.set_value(3.5), run_time=0.75)
        self.wait()

        self.next_section("...o incluso con los vectores de todo el espacio, sin importar las direcciones.", skip_animations=SKIP_DEFAULT)
        self.play(FadeIn(vec_u), FadeOut(span_v_1), FadeOut(span_v_2), run_time=2)
        self.play(FadeIn(circ_v), run_time=1.25)
        self.play(FadeIn(circ_u), run_time=1.25)
        self.wait()
        circ_v.add_updater( lambda c: c.become(Circle(radius=nv.get_value(), color=ROJO, stroke_opacity=0.5, fill_opacity=0)) )
        self.play(nv.animate.set_value(0.75), run_time=1.5)
        self.play(nv.animate.set_value(-3.75), run_time=1.5)
        self.play(nv.animate.set_value(1), run_time=1.5)
        self.play(nv.animate.set_value(3), run_time=3)
        self.wait()


class SE2(MovingCameraScene):
    def propiedades(self):

        #Texto
        t0 = Tex("Norma")
        t1 = MathTex("||\\cdot||:V \\to", "\\mathbb{R}^{\\geq0}").scale(0.7)

        p1 = MathTex("\\forall \ \\vec{u},\\vec{v}\\in V, \ \\forall \ a\\in K,").scale(0.6)
        p1_C = MathTex("\\forall \ \\vec{u},\\vec{v}\\in V, \ \\forall \ a\\in \\mathbb{C},").scale(0.6).shift(0.725*UP+0.02*LEFT)
        p1_copy = p1.copy().shift(0.725*UP+0.02*LEFT)
        p2 = MathTex("||a\\vec{u}||", "=", "|a| \ ||\\vec{u}||").scale(0.6).move_to(1.5*LEFT).shift(0.25*DOWN)
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
        t5 = Tex("*", "Ver la ", "Pregunta 2.5 ", "al final del video.").scale(.55).to_edge(DOWN).shift(0.25*DOWN)
        t5[0].set_color(AMARILLO)
        t5[2].set_color(ROJO)
        t6 = Tex("*", "Ver el ", "Ejercicio 2.1", ".").scale(.55).to_edge(DOWN).shift(0.25*DOWN)
        t6[0].set_color(AMARILLO)
        t6[2].set_color(AZUL)

        g = VGroup(t2,t3,t4).arrange(direction=2.5*DOWN, aligned_edge=LEFT)
        g.next_to(tinv, RIGHT).shift(0.25*LEFT)
        t0.move_to(2*UP)
        t1.move_to(1.4*UP)
        p1.move_to(0.75*UP)
        p3.shift(0.15*LEFT)

        #Geometría
        grid = NumberPlane(x_range=[-3.25, 3.25, 1], y_range=[-3.25, 3.25, 1],
                           background_line_style={
                               "stroke_width": 1, "stroke_opacity": 0.5}
                           ).shift(6.75*LEFT)

        u1, u2, v1, v2 = ValueTracker(1.5), ValueTracker(-1), ValueTracker(0.5), ValueTracker(2.5) #Coordenadas de los vectores u y v

        vt_u = ValueTracker(1)
        vec_u = Vector(direction = [u1.get_value(), u2.get_value(), 0], color=AZUL).shift(6.75*LEFT)
        vec_u.add_updater(lambda v:
                          vec_u.become( (Vector([vt_u.get_value()*u1.get_value(), vt_u.get_value()*u2.get_value(), 0], buff=0, color=AZUL).shift(6.75*LEFT)) )
                          )
        vec_u_null = Circle(radius=0.025, color=AZUL).set_opacity(1).shift(6.75*LEFT)
        norm_u = MathTex(r"||\vec{u}||").scale(0.6)
        norm_u[0][2:4].set_color(AZUL)
        brace_u = BraceBetweenPoints(ORIGIN, [u1.get_value(), u2.get_value(), 0]).shift(6.75*LEFT)
        brace_u.put_at_tip(norm_u, buff=0)
        brace_u.add_updater(lambda v:
                            brace_u.become( BraceBetweenPoints(ORIGIN, [value*u1.get_value(), value*u2.get_value(), 0]).shift(6.75*LEFT) ) if ((value := vt_u.get_value()) > 0)
                            else ( ( brace_u.become( BraceBetweenPoints([value*u1.get_value(), value*u2.get_value(), 0], ORIGIN).shift(6.75*LEFT) ) ) if (value < 0) else ( brace_u.become( Line(start=6.75*LEFT - [0.175, 0.175, 0], end=6.75*LEFT - [0.35, 0.35, 0])) )
                                  )
                          )
        norm_u.add_updater(lambda n: (brace_u.put_at_tip(n, buff=0)) if (vt_u.get_value() != 0)
                           else n.set_opacity(1).move_to(7.225*LEFT+0.53*DOWN)
                           )
        geq0 = MathTex(r"0\leq").scale(0.6).next_to(norm_u, LEFT, buff=0.1)
        geq0.add_updater(lambda n: n.next_to(norm_u, LEFT, buff=0.1))

        vec_u_2 = Vector(direction = [u1.get_value(), u2.get_value(), 0], color=AZUL).shift(6.75*LEFT)
        norm_u_2 = MathTex(r"||\vec{u}||").scale(0.6)
        norm_u_2[0][2:4].set_color(AZUL)
        brace_u_2 = BraceBetweenPoints(ORIGIN, [u1.get_value(), u2.get_value(), 0]).shift(6.75*LEFT).shift([u1.get_value(), u2.get_value(), 0])
        brace_u_2.put_at_tip(norm_u_2, buff=0)

        vt_2u = ValueTracker(1)
        vec_2u = Vector(direction = [u1.get_value(), u2.get_value(), 0], color=AZUL).shift(6.75*LEFT)
        vec_2u.add_updater(lambda v:
                          vec_2u.become( Vector([vt_2u.get_value()*u1.get_value(), vt_2u.get_value()*u2.get_value(), 0], buff=0, color=AZUL).shift(6.75*LEFT) )
                          )
        norm_2u = MathTex(r"||2\vec{u}||").scale(0.6)
        norm_2u[0][3:5].set_color(AZUL)
        brace_2u = BraceBetweenPoints([u1.get_value(), u2.get_value(), 0], ORIGIN).shift(6.75*LEFT).put_at_tip(norm_2u, buff=0.1)
        brace_2u.put_at_tip(norm_2u, buff=0)
        brace_2u.add_updater(lambda v:
                            brace_2u.become( BraceBetweenPoints([value*u1.get_value(), value*u2.get_value(), 0], ORIGIN).shift(6.75*LEFT) ) if ((value := vt_2u.get_value()) > 0)
                            else brace_2u.become( BraceBetweenPoints(ORIGIN, [value*u1.get_value(), value*u2.get_value(), 0]).shift(6.75*LEFT) )
                            )
        norm_2u.add_updater(lambda n: brace_2u.put_at_tip(n, buff=0))
        norm_m2u = MathTex(r"||-2\vec{u}||").scale(0.6)
        norm_m2u[0][4:6].set_color(AZUL)
        norm_m2u.add_updater(lambda n: brace_2u.put_at_tip(n, buff=0))

        norm_u_copy = MathTex(r"||\vec{u}||").scale(0.6)
        norm_u_copy[0][2:4].set_color(AZUL)
        brace_u_copy = BraceBetweenPoints(ORIGIN, [u1.get_value(), u2.get_value(), 0]).shift(6.75*LEFT)
        brace_u_copy.put_at_tip(norm_u_copy, buff=0)
        norm_u_copy_2 = MathTex(r"||\vec{u}||").scale(0.6)
        norm_u_copy_2[0][2:4].set_color(AZUL)
        brace_u_copy_2 = BraceBetweenPoints(ORIGIN, [u1.get_value(), u2.get_value(), 0]).shift(6.75*LEFT)
        brace_u_copy_2.put_at_tip(norm_u_copy_2, buff=0)

        vt_v = ValueTracker(0)
        vec_v = Arrow(start = ORIGIN, end = [v1.get_value(), v2.get_value(), 0], buff=0, color=ROJO).shift(6.75*LEFT)
        vec_v.add_updater(lambda v:
                          vec_v.become( Arrow(start = [vt_v.get_value()*u1.get_value(), vt_v.get_value()*u2.get_value(), 0], end = [v1.get_value()+vt_v.get_value()*u1.get_value(), v2.get_value()+vt_v.get_value()*u2.get_value(), 0], buff=0, color=ROJO).shift(6.75*LEFT) )
                          )
        norm_v = MathTex(r"||\vec{v}||").scale(0.6)
        norm_v[0][2:4].set_color(ROJO)
        brace_v = BraceBetweenPoints(ORIGIN, [v1.get_value(), v2.get_value(), 0]).shift(6.75*LEFT).put_at_tip(norm_v, buff=0)
        brace_v.add_updater(lambda v:
                          brace_v.become( BraceBetweenPoints([vt_v.get_value()*u1.get_value(), vt_v.get_value()*u2.get_value(), 0], [v1.get_value()+vt_v.get_value()*u1.get_value(), v2.get_value()+vt_v.get_value()*u2.get_value(), 0]).shift(6.75*LEFT) )
                          )
        norm_v.add_updater(lambda n: brace_v.put_at_tip(norm_v, buff=0))

        vec_upv = Vector(direction = [u1.get_value()+v1.get_value(), u2.get_value()+v2.get_value(), 0], buff=0, color=MAGENTA).shift(6.75*LEFT)
        vec_upv.add_updater(lambda v:
                          vec_upv.become( Vector(direction = [u1.get_value()+v1.get_value(), u2.get_value()+v2.get_value(), 0], buff=0, color=MAGENTA).shift(6.75*LEFT) )
                          )
        brace_upv = BraceBetweenPoints([u1.get_value()+v1.get_value(), u2.get_value()+v2.get_value(), 0], ORIGIN).shift(6.75*LEFT)
        norm_upv = MathTex(r"||\vec{u}+\vec{v}||").scale(0.6)
        norm_upv[0][2:7].set_color(MAGENTA)
        brace_upv.put_at_tip(norm_upv, buff=0)
        brace_upv.add_updater(lambda v:
                          brace_upv.become( BraceBetweenPoints([u1.get_value()+v1.get_value(), u2.get_value()+v2.get_value(), 0], ORIGIN).shift(6.75*LEFT) )
                          )
        norm_upv.add_updater(lambda n: brace_upv.put_at_tip(norm_upv, buff=0))

        #Animaciones
        self.next_section("...llamada norma, que a cada vector del espacio le asigna...", skip_animations=SKIP_DEFAULT)
        grid.shift(3.75*LEFT)
        vec_u.shift(3.75*LEFT)
        self.play(Write(t0))
        self.wait(0.25)
        self.play(Write(t1[0]))
        self.wait()

        self.next_section("...representados gométricamente como flechas...", skip_animations=SKIP_DEFAULT)
        self.add(grid, vec_u)
        self.play(self.camera.frame.animate.move_to(3*LEFT), grid.animate.shift(3.75*RIGHT), vec_u.animate.shift(3.75*RIGHT), run_time=1.5)
        self.wait()
        self.play(Write(brace_u))
        self.wait()
        self.play(Write(norm_u), reverse=True)
        self.wait()

        self.next_section("longitud negativa, la cantidad asignada a cada vector...", skip_animations=SKIP_DEFAULT)
        self.play(Write(geq0), reverse=True)
        self.wait()
        self.play(vt_u.animate.set_value(2.05))
        self.play(vt_u.animate.set_value(-2.05))
        self.play(vt_u.animate.set_value(1))
        self.wait(0.5)
        self.play(Write(t1[1]), run_time=2)
        self.wait(0.5)
        self.play(Unwrite(geq0))
        self.wait()

        self.next_section("...sumamos a un vector consigo mismo...", skip_animations=SKIP_DEFAULT)
        vec_u_2.set_opacity(0)
        vec_2u.set_opacity(0)
        self.add(vec_u_2, vec_2u)
        self.play(vec_u_2.animate.set_opacity(1), vec_2u.animate.set_opacity(1))
        self.play(vec_u_2.animate.shift([u1.get_value(), u2.get_value(), 0]))
        self.play(FadeIn(brace_u_2, norm_u_2), run_time = 0.5)
        self.wait()
        self.play(Write(brace_2u))
        self.wait(0.5)
        self.play(vt_2u.animate.set_value(2))
        self.wait()
        self.play(Write(norm_2u), run_time=1.5)
        self.wait()

        self.next_section("Lo mismo ocurre si, en vez de reescalar por 2, reescalamos por -2...", skip_animations=SKIP_DEFAULT)
        self.play(Unwrite(norm_2u))
        self.wait()
        self.play(vt_2u.animate.set_value(1), FadeOut(vec_u_2, brace_u_2, norm_u_2))
        self.wait()
        self.play(vt_2u.animate.set_value(-2))
        self.play(Write(norm_m2u))
        self.wait()

        self.next_section("...nuevamente es el doble de la original.", skip_animations=SKIP_DEFAULT)
        self.add(norm_u_copy, brace_u_copy, norm_u_copy_2, brace_u_copy_2)
        self.play(FadeOut(brace_u, norm_u),
                  brace_u_copy.animate.shift([-u1.get_value(), -u2.get_value(), 0]),
                  norm_u_copy.animate.shift([-u1.get_value(), -u2.get_value(), 0]))
        self.play(brace_u_copy_2.animate.shift([-2*u1.get_value(), -2*u2.get_value(), 0]),
                  norm_u_copy_2.animate.shift([-2*u1.get_value(), -2*u2.get_value(), 0]) #Aquí puede aparecer un salto brusco en renders de baja calidad (con -ql)
                  )
        self.wait()

        self.next_section("Más generalmente, si multiplicamos a un vector por un escalar arbitrario...", skip_animations=SKIP_DEFAULT)
        self.play(Write(p1))
        self.wait()
        self.play(Write(p2[0][3:5]))
        self.wait()
        self.play(Write(p2[0][2]))
        self.wait()
        self.play(Write(p2[0][0:2]), Write(p2[0][5:7]))
        self.play(Write(p2[1]))
        self.play(Write(p2[2][3:]))
        self.wait(1.5)
        self.play(Write(p2[2][:3]))
        self.wait()

        self.next_section("...número complejo.", skip_animations=SKIP_DEFAULT)
        self.play(Transform(p1[0][12], p1_C[0][12]), run_time=1.5)
        self.wait(0.5)
        self.play(Write(t5))
        self.wait()
        self.play(FadeOut(t5), Transform(p1[0][12], p1_copy[0][12]))
        self.wait()

        self.next_section("Esto nos da la primera propiedad de la norma...", skip_animations=SKIP_DEFAULT)
        vec_2u.clear_updaters()
        self.play(FadeOut(vec_2u, brace_2u, norm_m2u, brace_u_copy, norm_u_copy, brace_u_copy_2, norm_u_copy_2))
        self.wait(2)
        self.play(Write(t2))
        self.wait()

        self.next_section("Ahora, notemos que el vector nulo del espacio tiene magnitud cero...", skip_animations=SKIP_DEFAULT)
        self.play(FadeIn(brace_u, norm_u))
        self.wait(1.25)
        self.play(vt_u.animate.set_value(0), FadeIn(vec_u_null), run_time=1.25)
        self.wait()
        cero = MathTex("=0").scale(0.6).next_to(norm_u, buff=0.1)
        self.play(Write(cero))
        self.wait()

        self.next_section("...el que un vector arbitrario tenga norma cero equivale a que...", skip_animations=SKIP_DEFAULT)
        self.play(Write(p3[0]), run_time=2)
        self.wait(0.5)
        self.play(Write(p3[1]))
        self.play(Write(p3[2]), run_time=2)
        self.wait()

        self.next_section("...distinción del vector nulo.", skip_animations=SKIP_DEFAULT)
        t3.shift(0.05*DOWN)
        self.play(Write(t3))
        self.wait()

        self.next_section("[pausa] Por último, observemos que, si consideramos la suma de dos vectores...", skip_animations=SKIP_DEFAULT)
        self.play(Unwrite(cero))
        self.wait(0.5)
        self.play(vt_u.animate.set_value(1), FadeOut(vec_u_null))
        self.wait(0.5)
        self.play(FadeIn(vec_v, brace_v, norm_v))
        self.play(vt_v.animate.set_value(1), run_time=0.75)
        self.play(FadeIn(vec_upv, brace_upv, norm_upv))
        self.wait()
        p4.shift(0.375*LEFT)
        self.play(Write(p4[0]), Indicate(norm_upv, color=MAGENTA), run_time=2.5)
        self.play(Write(p4[1]))
        self.play(Write(p4[2]), Indicate(norm_u, color=AZUL), Indicate(norm_v, color=ROJO), run_time=4)
        self.wait()

        self.next_section("...siempre debe ser mayor o igual a la longitud del tercer lado.", skip_animations=SKIP_DEFAULT)
        self.play(u1.animate.set_value(0.5))
        self.play(u2.animate.set_value(-2))
        self.play(v1.animate.set_value(2))
        self.play(u1.animate.set_value(2.5),
                  u2.animate.set_value(0.5),
                  v1.animate.set_value(-3), 
                  v2.animate.set_value(2)
                  )
        self.play(u1.animate.set_value(1.5),
                  u2.animate.set_value(-1),
                  v1.animate.set_value(0.5), 
                  v2.animate.set_value(2.5)
                  )
        self.wait()

        self.next_section("...desigualdad del triángulo.", skip_animations=SKIP_DEFAULT)
        self.play(Write(t4))
        self.wait()

        self.next_section("...como ejercicio al final del video.", skip_animations=SKIP_DEFAULT)
        self.play(Write(t6))
        self.wait()
        self.play(FadeOut(t6), run_time=0.5)
        self.wait()

        self.next_section("...estas tres propiedades se le cooce como un espacio vectorial normado.", skip_animations=SKIP_DEFAULT)
        self.play(self.camera.frame.animate.move_to(ORIGIN),
                  FadeOut(grid, vec_u, brace_u, norm_u, vec_v, brace_v, norm_v, vec_upv, brace_upv, norm_upv)
                  )
        self.wait()

    def construct(self):
        self.propiedades()
