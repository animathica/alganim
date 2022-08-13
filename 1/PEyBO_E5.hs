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
  
  texts1 <- mapM oNew [ e1p0, e1p1, e1p2, e1p3, e2p0, e2p1 ]

  texts2 <- mapM oNew [ e3p0, e3p1, e3p2, e4p0, e4p1, e5p0, e5p1 ]

  texts3 <- mapM oNew [ e6p0, e6p1, e6p2, e6p3, e6p4 ]

  texts4 <- mapM oNew [ e7p0, e7p1, e7p2, e7p3, e7p4 ]

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
  oShowWith cab' $ adjustDuration (*0.33) . oDraw
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


-----------------------------------------------------------------------------
-- Listas de parámetros utilizados en la escena para cada objeto de texto. --
-----------------------------------------------------------------------------

leftXs1 :: [Double]
leftXs1 = [-7.75, -5.5, -2.75, -7.75, -7.75, -5.4]

topYs1 :: [Double]
topYs1 = [3.5, 3.5, 3, 1.5, 0, 0.1]

durationFunctions1 :: [(Duration -> Duration)]
durationFunctions1 = [(*0.3), (*0.33), (*0.5), (*0.5), (*0.5), (*0.5)]

waitDurations1 :: [Double]
waitDurations1 = [0.5, 0, 0.25, 0, 0, 0]

leftXs2 :: [Double]
leftXs2 = [-7.75, -5.5, -7.75, -7.75, -7.75, -7.75, -7.75]

topYs2 :: [Double]
topYs2 = [3.5, 3.5, 2.5, -0.5, -0.5, -2, -2]

durationFunctions2 :: [(Duration -> Duration)]
durationFunctions2 = [(*0.3), (*0.33), (*0.3), (*0.33), (*0.33), (*0.33), (*0.33)]

waitDurations2 :: [Double]
waitDurations2 = [0.5, 0, 0.5, 2, 0, 0, 0]

leftXs3 :: [Double]
leftXs3 = [-7.75, -7.75, -3.15, -3.15, -1.05, -7.75, -7.75, -7.75, -7.75]

topYs3 :: [Double]
topYs3 = [2.5, 2.5, -0.3, -1, -1, -3, -4, -5, -6]

durationFunctions3 :: [(Duration -> Duration)]
durationFunctions3 = [(*0.3), (*0.3), (*0.33), (*0.3), (*0.33), (*0.33), (*0.33), (*0.33), (*0.33)]

waitDurations3 :: [Double]
waitDurations3 = [0.5, 0, 0, 0.5, 2, 0.5, 0.5, 0.5, 0.5]

leftXs4 :: [Double]
leftXs4 = [-7.75, -7.75, -2, -7.75, -3.75, -7.75, -7.75, -7.75, -7.75]

topYs4 :: [Double]
topYs4 = [2.5, 2.5, 1.25, -0.25, -1.25, -3, -4, -5, -6]

durationFunctions4 :: [(Duration -> Duration)]
durationFunctions4 = [(*0.3), (*0.3), (*0.33), (*0.3), (*0.33), (*0.33), (*0.33), (*0.33), (*0.33)]

waitDurations4 :: [Double]
waitDurations4 = [0.5, 0, 0, 0.5, 2, 0.5, 0.5, 0.5, 0.5]

------------------------------------------------------------------------------------------------------------------
-- Aquí va el texto que escribiremos, separado en pedazos; usamos "\\hfill\\break" para romper líneas en LaTeX. --
------------------------------------------------------------------------------------------------------------------

c1l1 :: SVG      -- Definimos el SVG de la cabecera con los atributos deseados.
c1l1 = withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ center $ scale 0.4 $
         latex "Sea $(V,K)$ un espacio vectorial con producto escalar $\\langle \\cdot, \\cdot \\rangle:V \\times V \\to K$."

ejercicio1 :: SVG    -- Definimos el SVG del primer ejercicio con los atributos deseados.
ejercicio1 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 1.1 Demuestra que $$\\langle \\vec{u} + a\\vec{w}, \\vec{v} \\rangle = \\langle \\vec{u}, \\vec{v} \\rangle + a\\langle \\vec{w}, \\vec{v} \\rangle, $$ $$\\langle \\vec{u}, \\vec{v}  + a\\vec{w} \\rangle = \\langle \\vec{u}, \\vec{v} \\rangle + \\overline{a}\\langle \\vec{u}, \\vec{w} \\rangle$$ para todo $\\vec{u},\\vec{v},\\vec{w}\\in V, a\\in K$, y dibuja un ejemplo no trivial ($\\vec{u}, \\vec{v}, \\vec{w}\\neq\\vec{0}, a\\neq0$) en $\\mathbb{R}^2$ para cada caso."

e1p0 :: SVG
e1p0 = split [0..11] ejercicio1       -- Separamos la primera línea del ejercicio.

e1p1 :: SVG
e1p1 = split [12..23] ejercicio1      -- Separamos la parte de en medio del ejercicio.

e1p2 :: SVG
e1p2 = split [24..81] ejercicio1      -- Separamos el final del ejercicio.

e1p3 :: SVG
e1p3 = split [82..200] ejercicio1      -- Separamos el final del ejercicio.

ejercicio2 :: SVG    -- Definimos el SVG del primer ejercicio con los atributos deseados.
ejercicio2 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 1.2 Sea $\\vec{v}\\in V$. Demuestra que $\\langle \\vec{v}, \\vec{v} \\rangle = 0$ si, y sólo si, $\\vec{v}=\\vec{0}$."

e2p0 :: SVG
e2p0 = split [0..11] ejercicio2

e2p1 :: SVG
e2p1 = split [12..100] ejercicio2

ejercicio3 :: SVG    -- Análogo a lo anterior.
ejercicio3 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 1.3 Demuestra que las siguientes condiciones son equivalentes. \\hfill \\break (a) $\\langle \\vec{u}, \\vec{v} \\rangle = 0$ para todo $\\vec{u}\\in V$. \\hfill \\break \\break (b) $\\vec{v} = \\vec{0}$. \\hfill \\break \\break (c) $\\langle \\vec{v}, \\vec{u} \\rangle = 0$ para todo $\\vec{u}\\in V$."

e3p0 :: SVG
e3p0 = split [0..11] ejercicio3

e3p1 :: SVG
e3p1 = split [12..63] ejercicio3

e3p2 :: SVG
e3p2 = split [64..122] ejercicio3

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
e6p1 = split [12..160] ejercicio6

e6p2 :: SVG
e6p2 = split [161..178] ejercicio6

e6p3 :: SVG
e6p3 = split [179] ejercicio6

e6p4 :: SVG
e6p4 = split [180..200] ejercicio6

ejercicio7 :: SVG    -- Definimos el SVG del primer ejercicio con los atributos deseados.
ejercicio7 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 7 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 1.7 Demuestra que $\\Gamma$ es una base ortogonal de $V$ si, y sólo si, $$\\vec{v} = \\sum_{i=1}^k \\frac{\\langle \\vec{v}, \\vec{g}_i \\rangle}{\\langle \\vec{g}_i, \\vec{g}_i \\rangle} \\vec{g}_i \\quad \\forall \\vec{v}\\in V.$$ Más aún, demuestra que, en este caso, $$ \\bigg \\langle \\frac{\\langle \\vec{v}, \\vec{g}_i \\rangle}{\\langle \\vec{g}_i, \\vec{g}_i \\rangle} \\vec{g}_i, \\frac{\\langle \\vec{v}, \\vec{g}_j \\rangle}{\\langle \\vec{g}_j, \\vec{g}_j \\rangle} \\vec{g}_j \\bigg \\rangle = 0 \\ \\ \\text{si} \\ i\\neq j.$$"

e7p0 :: SVG
e7p0 = split [0..11] ejercicio7       -- Separamos la primera línea del ejercicio.

e7p1 :: SVG
e7p1 = split [12..83] ejercicio7       -- Separamos la primera línea del ejercicio.

e7p2 :: SVG
e7p2 = split [84..113] ejercicio7      -- Separamos la parte de en medio del ejercicio.

e7p3 :: SVG
e7p3 = split [114..134] ejercicio7      -- Separamos el final del ejercicio.

e7p4 :: SVG
e7p4 = split [135..300] ejercicio7      -- Separamos el final del ejercicio.

--pregunta5 :: SVG    -- Análogo a lo anterior.
--pregunta5 = withSubglyphs [0..10] (withStrokeColorPixel miRojo) $ withSubglyphs [0..10] (withFillColorPixel miRojo) $
--           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
--           latex "Pregunta 3.5 El Teorema de Gram-Schmidt \\textbf{no} asegura la \\hfill\\break existencia de bases ortogonales y ortonormales en espacios \\hfill\\break vectoriales con producto escalar de dimensión \\textbf{infinita}, \\hfill\\break ¿por qué?"
--
--p5l1 :: SVG
--p5l1 = split [0..10] pregunta5
--
--p5l2 :: SVG
--p5l2 = split [11..153] pregunta5

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
