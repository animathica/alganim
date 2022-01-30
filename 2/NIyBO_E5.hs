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
  
--  cab <- oNew c1l1
--  oModify cab $ oCenterX .~ 0
--  oModify cab $ oTopY .~ 4.25
--  oShowWith cab $ adjustDuration (*0.33) . oDraw
--  wait 0.5
  
  -- Este bloque genera dos listas con los demás objetos de texto (SVGs) que serán utilizados en la escena.
  
  texts1 <- mapM oNew [ e1p0, e1p1, e2p0, e2p1, e2p2, e2p3, e2p4, e2p5, e2p6, e3p0, e3p1 ]

--  texts2 <- mapM oNew [ e3p0, e3p1, e3p2, e4p0, e4p1, e5p0, e5p1 ]

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

--  wait 1
--
--  forM_ (zip5 texts2 leftXs2 topYs2 durationFunctions2 waitDurations2) $    -- Creamos una lista de 5-tuplas a partir de las
--    \(obj, xPos, yPos, dFunc, wDur) -> do                              -- listas de parámetros;
--    oModify obj $ oLeftX .~ xPos                                       -- modificamos la posición horizontal del objeto;
--    oModify obj $ oTopY .~ (yPos - 0.5)                                        -- modificamos la posición vertical del objeto;
--    oShowWith obj $ adjustDuration dFunc . oDraw                       -- dibujamos el objeto ajustando la velocidad;
--    wait wDur                                                          -- esperamos una cantidad indicada de tiempo.
--
--  forM_ texts2 $
--    \obj -> fork $ do
--    oHideWith obj oFadeOut

-----------------------------------------------------------------------------
-- Listas de parámetros utilizados en la escena para cada objeto de texto. --
-----------------------------------------------------------------------------

leftXs1 :: [Double]
leftXs1 = [-7.75, -5.5, -2.75, -7.75, -7.75, -5.4, -7.75, -7.75, -7.75, -7.75, -7.75]

topYs1 :: [Double]
topYs1 = [3.5, 3.5, 3, 1.5, 0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

durationFunctions1 :: [(Duration -> Duration)]
durationFunctions1 = [(*0.3), (*0.33), (*0.5), (*0.5), (*0.5), (*0.5), (*0.5), (*0.5), (*0.5), (*0.5), (*0.5)]

waitDurations1 :: [Double]
waitDurations1 = [0.5, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0]

leftXs2 :: [Double]
leftXs2 = [-7.75, -5.5, -7.75, -7.75, -7.75, -7.75, -7.75]

topYs2 :: [Double]
topYs2 = [3.5, 3.5, 2.5, -0.5, -0.5, -2, -2]

durationFunctions2 :: [(Duration -> Duration)]
durationFunctions2 = [(*0.3), (*0.33), (*0.3), (*0.33), (*0.33), (*0.33), (*0.33)]

waitDurations2 :: [Double]
waitDurations2 = [0.5, 0, 0.5, 2, 0, 0, 0]

------------------------------------------------------------------------------------------------------------------
-- Aquí va el texto que escribiremos, separado en pedazos; usamos "\\hfill\\break" para romper líneas en LaTeX. --
------------------------------------------------------------------------------------------------------------------

ejercicio1 :: SVG    -- Definimos el SVG del primer ejercicio con los atributos deseados.
ejercicio1 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 2.1 Sean $V$ un espacio normado y $\\vec{u}\\in V$. Demuestra que $||\\vec{u}||>0$ si $\\vec{u}\\neq\\vec{0}$, es decir, que la norma es positivo definida."

e1p0 :: SVG
e1p0 = split [0..11] ejercicio1

e1p1 :: SVG
e1p1 = split [12..23] ejercicio1

e1p2 :: SVG
e1p2 = split [24..81] ejercicio1

e1p3 :: SVG
e1p3 = split [82..200] ejercicio1

e1p4 :: SVG
e1p4 = split [82..200] ejercicio1

e1p5 :: SVG
e1p5 = split [82..200] ejercicio1

e1p6 :: SVG
e1p6 = split [82..200] ejercicio1

ejercicio2 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
ejercicio2 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
ejercicio2 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
ejercicio2 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 2.2 Una \\emph{métrica} o \\emph{función de distancia} en un conjunto $X$ es una función $f(\\cdot,\\cdot):X\\times X\\to [0,\\infty)$ que cumple las siguientes propiedades: \\hfill \\break (i) $d(x,y) = 0$ si, y sólo si, $x=y$; \\hfill \\break \\break (ii) $d(x,y) = d(y,x)$ para cualesquiera $x,y\\in X$; \\hfill \\break \\break (iii) $d(x,y) \\leq d(x,z) + d(z,y)$ para cualesquiera $x,y,z\\in X$. \\hfill \\break Demuestra que si $(V,K)$ es un espacio vectorial con norma $||\\cdot||:V\\to\\mathbb{R}$, entonces la función dada por $$d(\\vec{x},\\vec{y}) = ||\\vec{x}-\\vec{y}|| \\quad \\forall \\ \\vec{x}, \\vec{y}\\in V$$ es una métrica en $V$. Por ende, toda norma \emph{induce} una métrica y, en particular, todo producto escalar positivo definido induce una métrica; sin embargo, existen métricas que no son inducidas por normas ni productos escalares."

e2p0 :: SVG
e2p0 = split [0..11] ejercicio2

e2p1 :: SVG
e2p1 = split [12..100] ejercicio2

ejercicio3 :: SVG    -- Análogo a lo anterior.
ejercicio3 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 2.3 Demuestra que todo conjunto ortonormal finito es linealmente independiente."

e3p0 :: SVG
e3p0 = split [0..11] ejercicio3

e3p1 :: SVG
e3p1 = split [12..63] ejercicio3

e3p2 :: SVG
e3p2 = split [64..122] ejercicio3

--pregunta4 :: SVG    -- Análogo a lo anterior.
--pregunta4 = withSubglyphs [0..10] (withStrokeColorPixel miRojo) $ withSubglyphs [0..10] (withFillColorPixel miRojo) $
--           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
--           latex "Pregunta 2.3 "
--
--p4p0 :: SVG
--p4p0 = split [0..10] pregunta5
--
--p4p1 :: SVG
--p4p1 = split [11..153] pregunta5

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
