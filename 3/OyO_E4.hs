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
  
  -- cab <- oNew cabecera
  -- oModify cab $ oCenterX .~ 0
  -- oModify cab $ oTopY .~ 3.75
  -- oShowWith cab $ adjustDuration (*0.33) . oDraw
  -- wait 0.5
  
  -- Este bloque genera dos listas con los demás objetos de texto (SVGs) que serán utilizados en la escena.
  
  texts1 <- mapM oNew [ ejercicio1Titulo, ejercicio1Cuerpo, ejercicio1Cuerpo', ejercicio1Cuerpo''
                      , ejercicio1Cuerpo'''
                      , ejercicio2Titulo, ejercicio2Cuerpo, pregunta3Titulo, pregunta3Cuerpo ]

  texts2 <- mapM oNew [ pregunta4Titulo, pregunta4Cuerpo, pregunta5Titulo, pregunta5Cuerpo ]

  -- Este bloque describe lo que sucederá en la escena con los demás objetos de texto.

  forM_ (zip5 texts1 leftXs1 topYs1 durationFunctions1 waitDurations1) $    -- Creamos una lista de 5-tuplas a partir de las
    \(obj, xPos, yPos, dFunc, wDur) -> do                                   -- listas de parámetros;
    oModify obj $ oLeftX .~ xPos                                            -- modificamos la posición horizontal del objeto;
    oModify obj $ oTopY .~ yPos                                             -- modificamos la posición vertical del objeto;
    oShowWith obj $ adjustDuration dFunc . oDraw                            -- dibujamos el objeto ajustando la velocidad;
    wait wDur                                                               -- esperamos una cantidad indicada de tiempo.

  forM_ texts1 $
    \obj -> fork $ do
    oHideWith obj oFadeOut

  wait 1

  forM_ (zip5 texts2 leftXs2 topYs2 durationFunctions2 waitDurations2) $    -- Creamos una lista de 5-tuplas a partir de las
    \(obj, xPos, yPos, dFunc, wDur) -> do                              -- listas de parámetros;
    oModify obj $ oLeftX .~ xPos                                       -- modificamos la posición horizontal del objeto;
    oModify obj $ oTopY .~ yPos                                        -- modificamos la posición vertical del objeto;
    oShowWith obj $ adjustDuration dFunc . oDraw                       -- dibujamos el objeto ajustando la velocidad;
    wait wDur                                                          -- esperamos una cantidad indicada de tiempo.

  forM_ texts2 $
    \obj -> fork $ do
    oHideWith obj oFadeOut

-----------------------------------------------------------------------------
-- Listas de parámetros utilizados en la escena para cada objeto de texto. --
-----------------------------------------------------------------------------

leftXs1 :: [Double]
leftXs1 = [-5.75, -5.75, -5.45, -1.35, -5.75, -5.75, -5.75, -5.75, -5.75]

topYs1 :: [Double]
topYs1 = [3.5, 3.5, 2.25, 2.25, 1, 0, 0, -1.25, -1.25]

durationFunctions1 :: [(Duration -> Duration)]
durationFunctions1 = [(*0.3), (*0.33), (*0.5), (*0.5), (*0.5), (*0.3), (*0.33), (*0.3), (*0.33)]

waitDurations1 :: [Double]
waitDurations1 = [0.5, 0, 0.25, 0, 0.5, 0.5, 0.5, 0.5, 2]

leftXs2 :: [Double]
leftXs2 = [-5.75, -5.75, -5.75, -5.75]

topYs2 :: [Double]
topYs2 = [3.5, 3.5, 1.75, 1.75]

durationFunctions2 :: [(Duration -> Duration)]
durationFunctions2 = [(*0.3), (*0.33), (*0.3), (*0.33)]

waitDurations2 :: [Double]
waitDurations2 = [0.5, 0, 0.5, 2]

------------------------------------------------------------------------------------------------------------------
-- Aquí va el texto que escribiremos, separado en pedazos; usamos "\\hfill\\break" para romper líneas en LaTeX. --
------------------------------------------------------------------------------------------------------------------

cabecera :: SVG      -- Definimos el SVG de la cabecera con los atributos deseados.
cabecera = withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ center $ scale 0.4 $
         latex "Sea $V$ un espacio vectorial con producto escalar."

ejercicio1 :: SVG    -- Definimos el SVG del primer ejercicio con los atributos deseados.
ejercicio1 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 3.1 Sea $V$ un espacio vectorial con producto escalar. \\hfill\\break Demuestra que $$\\bigg\\langle \\vec{u}, \\vec{v} - \\frac{\\langle \\vec{v}, \\vec{u} \\rangle}{\\langle \\vec{u}, \\vec{u} \\rangle} \\vec{u} \\bigg\\rangle = 0 \\quad \\text{y} \\quad \\bigg\\langle\\bigg\\{\\vec{u},\\vec{v}-\\frac{\\langle\\vec{v},\\vec{u}\\rangle}{||\\vec{u}||}\\hat{u}\\bigg\\}\\bigg\\rangle = \\langle\\{\\vec{u},\\vec{v}\\}\\rangle$$ para $\\vec{u},\\vec{v}\\in V$ con $\\vec{u},\\vec{v}\\neq\\vec{0}$, y dibuja un ejemplo en $\\mathbb{R}^2$."

ejercicio1Titulo :: SVG
ejercicio1Titulo = split [0..11] ejercicio1        -- Separamos el título del ejercicio.

ejercicio1Cuerpo :: SVG
ejercicio1Cuerpo = split [12..64] ejercicio1      -- Separamos el principio de la parte de en medio del ejercicio.

ejercicio1Cuerpo' :: SVG
ejercicio1Cuerpo' = split [65..91] ejercicio1      -- Separamos el principio de la parte de en medio del ejercicio.

ejercicio1Cuerpo'' :: SVG
ejercicio1Cuerpo'' = split [92..128] ejercicio1     -- Separamos el final de la parte de en medio del ejercicio.

ejercicio1Cuerpo''' :: SVG
ejercicio1Cuerpo''' = split [129..173] ejercicio1   -- Separamos la última parte del ejercicio.

ejercicio2 :: SVG    -- Análogo a lo anterior.
ejercicio2 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 3.2 Usa la intuición geométrica generada por este \\hfill\\break video para demostrar el Teorema de Gram-Schmidt."

ejercicio2Titulo :: SVG
ejercicio2Titulo = split [0..11] ejercicio2

ejercicio2Cuerpo :: SVG
ejercicio2Cuerpo = split [12..94] ejercicio2

pregunta3 :: SVG    -- Análogo a lo anterior.
pregunta3 = withSubglyphs [0..10] (withStrokeColorPixel miRojo) $ withSubglyphs [0..10] (withFillColorPixel miRojo) $
           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
           latex "Pregunta 3.3 ¿Qué sucedería si aplicáramos el proceso de \\hfill\\break Gram-Schmidt a un conjunto de vectores linealmente \\hfill\\break \\emph{dependiente}?"

pregunta3Titulo :: SVG
pregunta3Titulo = split [0..10] pregunta3

pregunta3Cuerpo :: SVG
pregunta3Cuerpo = split [11..106] pregunta3

pregunta4 :: SVG    -- Análogo a lo anterior.
pregunta4 = withSubglyphs [0..10] (withStrokeColorPixel miRojo) $ withSubglyphs [0..10] (withFillColorPixel miRojo) $
           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
           latex "Pregunta 3.4 ¿Qué sucedería si, en el proceso de Gram-Schmidt \\hfill\\break modificado, normalizáramos a alguno de los vectores \\emph{antes} de \\hfill\\break ortogonalizarlo, y no \\emph{después}?"

pregunta4Titulo :: SVG
pregunta4Titulo = split [0..10] pregunta4

pregunta4Cuerpo :: SVG
pregunta4Cuerpo = split [11..133] pregunta4

pregunta5 :: SVG    -- Análogo a lo anterior.
pregunta5 = withSubglyphs [0..10] (withStrokeColorPixel miRojo) $ withSubglyphs [0..10] (withFillColorPixel miRojo) $
           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
           latex "Pregunta 3.5 El Teorema de Gram-Schmidt \\textbf{no} asegura la \\hfill\\break existencia de bases ortogonales y ortonormales en espacios \\hfill\\break vectoriales con producto escalar de dimensión \\textbf{infinita}, \\hfill\\break ¿por qué?"

pregunta5Titulo :: SVG
pregunta5Titulo = split [0..10] pregunta5

pregunta5Cuerpo :: SVG
pregunta5Cuerpo = split [11..153] pregunta5

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
