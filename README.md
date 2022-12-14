# alganim

Repositorio con los guiones y códigos de animación creados para elaborar los [videos de álgebra lineal](https://www.youtube.com/watch?v=GxcXCLAiQO0&list=PL91agCMqt_mdAgHZkxyn-tscoNpu7ZHvl) del canal de YouTube [Animathica](https://www.youtube.com/@Animathica/featured).

## Objetivo

Generar material educativo audiovisual para apoyar el curso de [Álgebra Lineal](http://www.fciencias.unam.mx/licenciatura/asignaturas/2016/1330) de la Licenciatura en Física Biomédica de la UNAM, así como a estudiantes de otras licenciaturas de la Facultad de Ciencias.

## Serie: Producto escalar y descomposición espectral

Serie de videos de álgebra lineal sobre la teoría de espacios vectoriales con producto escalar, con un enfoque especial hacia entender la descomposición espectral.

### Videos de la serie

1. Producto escalar y bases ortogonales [[finalizado]](https://www.youtube.com/watch?v=GxcXCLAiQO0)
2. Norma inducida y bases ortonormales [[en producción]](https://github.com/animathica/alganim/tree/main/2)
3. Ortogonalización y ortonormalización (Teorema de Gram-Schmidt) [[finalizado]](https://www.youtube.com/watch?v=7oO6xXpaTLk)
4. Descomposición espectral (Introducción al Teorema espectral) [[en preproducción]](https://github.com/animathica/alganim/tree/main/4)

## Acerca del código

El código de este repositorio está escrito principalmente en Python(3), utilizando la biblioteca [Manim](https://github.com/3b1b/manim) para hacer la mayoría de las animaciones. Por el momento, existen varias versiones de esta biblioteca; en este repositorio se han utilizado las siguientes:
- [manimlib 0.2.0](https://pypi.org/project/manimlib/)  (también conocido como ManimCairo)
- [Manim Community v0.8.0](https://docs.manim.community/en/v0.8.0/index.html) y [v0.15.2](https://docs.manim.community/en/v0.15.2/) (también conocido como manim/manimCE)

Adicionalmente, algunas escenas están escritas en Haskell, utilizando la biblioteca [Reanimate](https://github.com/reanimate/reanimate). En este repositorio se ha utilizado la versión [reanimate 1.1.4.0](https://hackage.haskell.org/package/reanimate-1.1.4.0/docs/Reanimate.html); una introducción a esta biblioteca se encuentra disponible [aquí](https://reanimate.readthedocs.io/en/latest/).
