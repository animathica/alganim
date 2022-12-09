#!/usr/bin/env stack
-- stack runghc --package reanimate
{-# LANGUAGE OverloadedStrings #-}
module Main(main) where

import Codec.Picture (PixelRGBA8 (..))
import Control.Lens
import Control.Monad
import Reanimate
import Reanimate.LaTeX
import Reanimate.Scene

----------------------------------------------------------------------------------
-- Código principal de la animación, que fue generada usando reanimate-1.1.4.0. --
----------------------------------------------------------------------------------

main :: IO ()
main = reanimate $ addStatic (mkBackground "black") $ scene $ do

  -- Este bloque dibuja la cabecera, asegurándose de que esté centrada; si no es necesario, se puede "comentar" con "--".
  
  cab <- oNew c1l1
  oModify cab $ oCenterX .~ 0
  oModify cab $ oTopY .~ 4.25
  oShowWith cab $ adjustDuration (*0.33) . oDraw
  wait 0.5
  
  -- Este bloque genera dos listas con los demás objetos de texto (SVGs) que serán utilizados en la escena.
  
  texts1 <- mapM oNew [ e1p0, e1p1, e1p2, e1p3, e2p0, e2p1, e2p2 ]

  texts2 <- mapM oNew [ e3p0, e3p1, e3p2, e3p3, e3p4, e4p0, e4p1, e5p0, e5p1 ]

  texts3 <- mapM oNew [ e6p0, e6p1, e6p2, e6p3, e6p4, e6p5, e6p6, e6p7 ]

  texts4 <- mapM oNew [ e7p0, e7p1, e7p2, e7p3, e7p4 ]

  texts5 <- mapM oNew [ p8p0, p8p1, p8p2, p8p3, p9p0, p9p1, p10p0, p10p1, p10p2, p10p3, p10p4 ]

  -- Este bloque describe lo que sucederá en la escena con los demás objetos de texto.

  forM_ (zip5 texts1 leftXs1 topYs1 durationFunctions1 waitDurations1) $    -- Creamos una lista de 5-tuplas a partir de las
    \(obj, xPos, yPos, dFunc, wDur) -> do                                   -- listas de parámetros;
    oModify obj $ oLeftX .~ xPos                                            -- modificamos la posición horizontal del objeto;
    oModify obj $ oTopY .~ (yPos - 0.5)                                             -- modificamos la posición vertical del objeto;
    oShowWith obj $ adjustDuration dFunc . oDraw                            -- dibujamos el objeto ajustando la velocidad;
    wait wDur                                                               -- esperamos una cantidad indicada de tiempo.

  forM_ texts1 $
    \obj -> fork $ do
    oHideWith obj oFadeOut

  wait 1

  forM_ (zip5 texts2 leftXs2 topYs2 durationFunctions2 waitDurations2) $    -- Creamos una lista de 5-tuplas a partir de las
    \(obj, xPos, yPos, dFunc, wDur) -> do                              -- listas de parámetros;
    oModify obj $ oLeftX .~ xPos                                       -- modificamos la posición horizontal del objeto;
    oModify obj $ oTopY .~ (yPos - 0.5)                                        -- modificamos la posición vertical del objeto;
    oShowWith obj $ adjustDuration dFunc . oDraw                       -- dibujamos el objeto ajustando la velocidad;
    wait wDur                                                          -- esperamos una cantidad indicada de tiempo.

  forM_ texts2 $
    \obj -> fork $ do
    oHideWith obj oFadeOut

  wait 1

  cab' <- oNew c1l2
  oModify cab' $ oCenterX .~ 0
  oModify cab' $ oTopY .~ 3.5
  oShowWith cab' $ adjustDuration (*0.6) . oDraw
  wait 0.5

  forM_ (zip5 texts3 leftXs3 topYs3 durationFunctions3 waitDurations3) $    -- Creamos una lista de 5-tuplas a partir de las
    \(obj, xPos, yPos, dFunc, wDur) -> do                              -- listas de parámetros;
    oModify obj $ oLeftX .~ xPos                                       -- modificamos la posición horizontal del objeto;
    oModify obj $ oTopY .~ (yPos - 0.25)                                        -- modificamos la posición vertical del objeto;
    oShowWith obj $ adjustDuration dFunc . oDraw                       -- dibujamos el objeto ajustando la velocidad;
    wait wDur                                                          -- esperamos una cantidad indicada de tiempo.

    wait 1

  forM_ texts3 $
    \obj -> fork $ do
    oHideWith obj oFadeOut

  wait 1

  forM_ (zip5 texts4 leftXs4 topYs4 durationFunctions4 waitDurations4) $    -- Creamos una lista de 5-tuplas a partir de las
    \(obj, xPos, yPos, dFunc, wDur) -> do                              -- listas de parámetros;
    oModify obj $ oLeftX .~ xPos                                       -- modificamos la posición horizontal del objeto;
    oModify obj $ oTopY .~ (yPos - 0.25)                                        -- modificamos la posición vertical del objeto;
    oShowWith obj $ adjustDuration dFunc . oDraw                       -- dibujamos el objeto ajustando la velocidad;
    wait wDur                                                          -- esperamos una cantidad indicada de tiempo.

  forM_ texts4 $
    \obj -> fork $ do
    oHideWith obj oFadeOut

  do fork $ oHideWith cab' oFadeOut
  oHideWith cab oFadeOut

  wait 1

  forM_ (zip5 texts5 leftXs5 topYs5 durationFunctions5 waitDurations5) $    -- Creamos una lista de 5-tuplas a partir de las
    \(obj, xPos, yPos, dFunc, wDur) -> do                              -- listas de parámetros;
    oModify obj $ oLeftX .~ xPos                                       -- modificamos la posición horizontal del objeto;
    oModify obj $ oTopY .~ (yPos - 0.25)                                        -- modificamos la posición vertical del objeto;
    oShowWith obj $ adjustDuration dFunc . oDraw                       -- dibujamos el objeto ajustando la velocidad;
    wait wDur                                                          -- esperamos una cantidad indicada de tiempo.

  forM_ texts5 $
    \obj -> fork $ do
    oHideWith obj oFadeOut


-----------------------------------------------------------------------------
-- Listas de parámetros utilizados en la escena para cada objeto de texto. --
-----------------------------------------------------------------------------

leftXs1 :: [Double]
leftXs1 = [-7.75, -5.5, -2.65, -6, -7.75, -5.5, -3.5]

topYs1 :: [Double]
topYs1 = [3.5, 3.5, 3.5, 2.5, 0.75, 0.75, 0.85]

durationFunctions1 :: [(Duration -> Duration)]
durationFunctions1 = [(*0.3), (*0.33), (*0.4), (*0.5), (*0.3), (*0.33), (*0.4) ]

waitDurations1 :: [Double]
waitDurations1 = [0.5, 0, 0, 0.25, 0.5, 0.5, 2.5]

leftXs2 :: [Double]
leftXs2 = [-7.75, -5.5, -7.75, -7.75, -7.75, -7.75, -7.75, -7.75, -7.75]

topYs2 :: [Double]
topYs2 = [3.5, 3.5, 2.35, 1.6, 0.8, -0.5, -0.5, -2, -2]

durationFunctions2 :: [(Duration -> Duration)]
durationFunctions2 = [(*0.3), (*0.33), (*0.5), (*0.5), (*0.5), (*0.33), (*0.33), (*0.33), (*0.33)]

waitDurations2 :: [Double]
waitDurations2 = [0.5, 0, 0, 0, 0.25, 0.5, 0.25, 0.5, 2.5]

leftXs3 :: [Double]
leftXs3 = [-7.75, -5.4, -7.75, -7.75, -7.75, -3.15, -3.15, -1.05, 0]

topYs3 :: [Double]
topYs3 = [2.5, 2.5, 1.5, 0.5, -0.3, -0.4, -1.1, -1.1]

durationFunctions3 :: [(Duration -> Duration)]
durationFunctions3 = [(*0.3), (*0.3), (*0.33), (*0.33), (*0.5), (*0.5), (*0.3), (*0.3)]

waitDurations3 :: [Double]
waitDurations3 = [0.5, 0.1, 0, 0, 0, 0, 0, 2.5]

leftXs4 :: [Double]
leftXs4 = [-7.75, -5.5, -2.75, -7.75, -3.5, -7.75, -7.75, -7.75, -7.75]

topYs4 :: [Double]
topYs4 = [2.5, 2.5, 1.75, 0, -0.75, -4, -5, -6, -6]

durationFunctions4 :: [(Duration -> Duration)]
durationFunctions4 = [(*0.3), (*0.33), (*0.5), (*0.33), (*0.5), (*0.33), (*0.33), (*0.33), (*0.33)]

waitDurations4 :: [Double]
waitDurations4 = [0.5, 0, 1, 0, 2, 0.5, 0.5, 0.5, 2.5]

leftXs5 :: [Double]
leftXs5 = [-7.75, -7.75, -7.75, -4.7, -7.75, -7.75, -7.75, -5, -7.75, -7.75, -7.75]

topYs5 :: [Double]
topYs5 = [3, 3, 2.55, 2.1, 1, 1, -0.5, -0.5, -0.5, -1.45, -1.9]

durationFunctions5 :: [(Duration -> Duration)]
durationFunctions5 = [(*0.3), (*0.33), (*0.33), (*0.5), (*0.3), (*0.33), (*0.3), (*0.33), (*0.33), (*0.5), (*0.33)]

waitDurations5 :: [Double]
waitDurations5 = [0.5, 0, 0, 1, 0.5, 1, 0.5, 0, 0, 0.5, 2.5]


------------------------------------------------------------------------------------------------------------------
-- Aquí va el texto que escribiremos, separado en pedazos; usamos "\\hfill\\break" para romper líneas en LaTeX. --
------------------------------------------------------------------------------------------------------------------

c1l1 :: SVG      -- Definimos el SVG de la cabecera con los atributos deseados.
c1l1 = withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ center $ scale 0.4 $
         latex "Sea $(V,K)$ un espacio vectorial con producto escalar $\\langle \\cdot, \\cdot \\rangle:V \\times V \\to K$."

ejercicio1 :: SVG    -- Definimos el SVG del primer ejercicio con los atributos deseados.
ejercicio1 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 1.1 Demuestra que, para cualesquiera $\\vec{u},\\vec{v},\\vec{w}\\in V$ y $a\\in K,$ $$\\langle \\vec{u} + a\\vec{w}, \\vec{v} \\rangle = \\langle \\vec{u}, \\vec{v} \\rangle + a\\langle \\vec{w}, \\vec{v} \\rangle \\quad \\text{y} \\quad \\langle \\vec{u}, \\vec{v}  + a\\vec{w} \\rangle = \\langle \\vec{u}, \\vec{v} \\rangle + \\overline{a}\\langle \\vec{u}, \\vec{w} \\rangle.$$"

e1p0 :: SVG
e1p0 = split [0..11] ejercicio1       -- Separamos la primera línea del ejercicio.

e1p1 :: SVG
e1p1 = split [12..24] ejercicio1      -- Separamos la parte de en medio del ejercicio.

e1p2 :: SVG
e1p2 = split [25..55] ejercicio1      -- Separamos el final del ejercicio.

e1p3 :: SVG
e1p3 = split [56..134] ejercicio1      -- Separamos el final del ejercicio.

ejercicio2 :: SVG    -- Definimos el SVG del primer ejercicio con los atributos deseados.
ejercicio2 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 1.2 Sea $\\vec{v}\\in V$. Demuestra que $\\langle \\vec{v}, \\vec{v} \\rangle = 0$ si, y sólo si, $\\vec{v}=\\vec{0}$."

e2p0 :: SVG
e2p0 = split [0..11] ejercicio2

e2p1 :: SVG
e2p1 = split [12..19] ejercicio2

e2p2 :: SVG
e2p2 = split [20..100] ejercicio2

ejercicio3 :: SVG    -- Análogo a lo anterior.
ejercicio3 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 1.3 Demuestra que las siguientes condiciones son equivalentes. \\hfill \\break (a) $\\langle \\vec{u}, \\vec{v} \\rangle = 0$ para todo $\\vec{u}\\in V$. \\hfill \\break \\break (b) $\\vec{v} = \\vec{0}$. \\hfill \\break \\break (c) $\\langle \\vec{v}, \\vec{u} \\rangle = 0$ para todo $\\vec{u}\\in V$."

e3p0 :: SVG
e3p0 = split [0..11] ejercicio3

e3p1 :: SVG
e3p1 = split [12..63] ejercicio3

e3p2 :: SVG
e3p2 = split [64..88] ejercicio3

e3p3 :: SVG
e3p3 = split [89..97] ejercicio3

e3p4 :: SVG
e3p4 = split [98..122] ejercicio3

ejercicio4 :: SVG    -- Análogo a lo anterior.
ejercicio4 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 1.4 Demuestra que, si $K=\\mathbb{R}$, entonces el producto escalar es \\emph{bilineal} (lineal en ambas entradas)."

e4p0 :: SVG
e4p0 = split [0..11] ejercicio4

e4p1 :: SVG
e4p1 = split [12..200] ejercicio4

ejercicio5 :: SVG    -- Análogo a lo anterior.
ejercicio5 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 1.5 Demuestra que todo conjunto ortogonal finito es linealmente independiente si, y sólo si, no contiene al vector nulo."

e5p0 :: SVG
e5p0 = split [0..11] ejercicio5

e5p1 :: SVG
e5p1 = split [12..200] ejercicio5

c1l2 :: SVG      -- Definimos el SVG de la c1l1 con los atributos deseados.
c1l2 = withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ center $ scale 0.4 $
         latex "Sean $\\text{dim}(V)=k<\\infty$ y $\\Gamma = \\{ \\vec{g}_1, \\vec{g}_2, ..., \\vec{g}_k \\} \\subseteq V$."

ejercicio6 :: SVG    -- Análogo a lo anterior.
ejercicio6 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 1.6 Demuestra que las siguientes condiciones son equivalentes. \\hfill \\break \\break (a) $\\Gamma$ es un conjunto ortogonal que no contiene al vector nulo. \\hfill \\break \\break (b) $\\Gamma$ es una base ortogonal de $V$. \\hfill \\break \\break (c) $\\langle \\Gamma \\rangle = V$ y $\\langle \\vec{g}_j, \\vec{g}_i \\rangle = \\left\\{\\rule{0cm}{6mm}\\right. \\langle \\vec{g}_i, \\vec{g}_i \\rangle \\neq 0 \\ \\ \\text{si} \\ j=i, 0 \\text{si} \\ j\\neq i.$"

e6p0 :: SVG
e6p0 = split [0..11] ejercicio6

e6p1 :: SVG
e6p1 = split [12..63] ejercicio6

e6p2 :: SVG
e6p2 = split [64..114] ejercicio6

e6p3 :: SVG
e6p3 = split [115..140] ejercicio6

e6p4 :: SVG
e6p4 = split [141..160] ejercicio6

e6p5 :: SVG
e6p5 = split [161..178] ejercicio6

e6p6 :: SVG
e6p6 = split [179] ejercicio6

e6p7 :: SVG
e6p7 = split [180..200] ejercicio6

ejercicio7 :: SVG    -- Definimos el SVG del primer ejercicio con los atributos deseados.
ejercicio7 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 7 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 1.7 Demuestra que $\\Gamma$ es una base ortogonal de $V$ si, y sólo si, $$\\vec{v} = \\sum_{i=1}^k \\frac{\\langle \\vec{v}, \\vec{g}_i \\rangle}{\\langle \\vec{g}_i, \\vec{g}_i \\rangle} \\vec{g}_i \\quad \\forall \\ \\vec{v}\\in V.$$ Más aún, demuestra que, en este caso, $$ \\bigg \\langle \\frac{\\langle \\vec{v}, \\vec{g}_i \\rangle}{\\langle \\vec{g}_i, \\vec{g}_i \\rangle} \\vec{g}_i, \\frac{\\langle \\vec{v}, \\vec{g}_j \\rangle}{\\langle \\vec{g}_j, \\vec{g}_j \\rangle} \\vec{g}_j \\bigg \\rangle = 0 \\ \\ \\text{si} \\ i\\neq j.$$"

e7p0 :: SVG
e7p0 = split [0..11] ejercicio7       -- Separamos la primera línea del ejercicio.

e7p1 :: SVG
e7p1 = split [12..57] ejercicio7       -- Separamos la primera línea del ejercicio.

e7p2 :: SVG
e7p2 = split [58..92] ejercicio7      -- Separamos la parte de en medio del ejercicio.

e7p3 :: SVG
e7p3 = split [93..125] ejercicio7      -- Separamos el final del ejercicio.

e7p4 :: SVG
e7p4 = split [126..300] ejercicio7      -- Separamos el final del ejercicio.

pregunta8 :: SVG    -- Análogo a lo anterior.
pregunta8 = withSubglyphs [0..10] (withStrokeColorPixel miRojo) $ withSubglyphs [0..10] (withFillColorPixel miRojo) $
           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
           latexCfg myTexConfig "Pregunta 1.8 ¿Se puede extender la interpretación geométrica del producto escalar entre dos vectores, que lo relaciona con la proyección vectorial del primero sobre el segundo, al caso en que cualquiera de ellos es el vector nulo del espacio?"

p8p0 :: SVG
p8p0 = split [0..10] pregunta8

p8p1 :: SVG
p8p1 = split [11..90] pregunta8

p8p2 :: SVG
p8p2 = split [91..154] pregunta8

p8p3 :: SVG
p8p3 = split [155..400] pregunta8

pregunta9 :: SVG    -- Análogo a lo anterior.
pregunta9 = withSubglyphs [0..10] (withStrokeColorPixel miRojo) $ withSubglyphs [0..10] (withFillColorPixel miRojo) $
           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
           latexCfg myTexConfig "Pregunta 1.9 ¿Qué significa que el producto escalar entre dos vectores sea positivo, negativo o cero?"

p9p0 :: SVG
p9p0 = split [0..10] pregunta9

p9p1 :: SVG
p9p1 = split [11..200] pregunta9
 
pregunta10 :: SVG    -- Análogo a lo anterior.
pregunta10 = withSubglyphs [0..11] (withStrokeColorPixel miRojo) $ withSubglyphs [0..11] (withFillColorPixel miRojo) $
           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
           latexCfg myTexConfig "Pregunta 1.10 En un espacio vectorial complejo con producto escalar, ¿qué significa geométricamente que el produco escalar entre dos vectores tenga parte imaginaria positiva, negativa o cero? Más aún. ¿cómo se interpreta la propiedad de simetría conjugada en este caso? (Sugerencia: Considera el espacio vectorial complejo $\\mathbb{C}$.)"

p10p0 :: SVG
p10p0 = split [0..11] pregunta10
 
p10p1 :: SVG
p10p1 = split [12..58] pregunta10

p10p2 :: SVG
p10p2 = split [59..165] pregunta10

p10p3 :: SVG
p10p3 = split [166..234] pregunta10
 
p10p4 :: SVG
p10p4 = split [235..300] pregunta10
 
--------------------------------------------------------------------------------------------------------------
-- Funciones auxiliares. En las primeras líneas se declaran las signaturas y en las siguientes, se definen. --
--------------------------------------------------------------------------------------------------------------

zip5 :: [a] -> [b] -> [c] -> [d] -> [e] -> [(a,b,c,d,e)]
zip5 (a:as) (b:bs) (c:cs) (d:ds) (e:es) = (a,b,c,d,e) : zip5 as bs cs ds es    -- Crea una lista de 5-tuplas a partir de 5
zip5 _      _      _      _      _      = []                                   -- listas, cada una de su propio tipo.

myTexConfig :: TexConfig                                      
myTexConfig = TexConfig LaTeX ["\\usepackage{amssymb}"] []    -- Carga paquetes de LaTeX al ser usado con latexCfg.

miAzul :: PixelRGBA8           
miAzul = PixelRGBA8 0 135 255 0    -- Color azul.

miRojo :: PixelRGBA8            
miRojo = PixelRGBA8 255 0 0 0      -- Color rojo.

split :: [Int] -> SVG -> SVG
split list svg = mkGroup [ ctx glyph | (ctx, _attr, glyph) <- reverse $    -- Separa de un SVG los pedazos indizados por una
                           svgGlyphs $ snd $ splitGlyphs list svg ]        -- lista de enteros dada.
