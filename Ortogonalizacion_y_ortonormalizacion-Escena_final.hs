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

main :: IO ()
main = reanimate $ addStatic (mkBackground "black") $ scene $ do

  -- Este bloque genera una lista con los objetos (SVGs) que serán utilizados en la escena.
  
  texts <- mapM oNew [ cabecera, ejercicio1Titulo, ejercicio1Cuerpo, ejercicio1Cuerpo', ejercicio1Cuerpo''
                     , ejercicio2Titulo, ejercicio2Cuerpo, ejercicio2Cuerpo', ejercicio2Cuerpo''
                     , preguntaTitulo, preguntaCuerpo, preguntaCuerpo', preguntaCuerpo'' ]

  -- Este bloque describe lo que sucederá en la escena.
  
  forM_ (zip5 texts leftXs centerYs durationFunctions waitDurations) $    -- Creamos una lista de 5-tuplas a partir de las
    \(obj, xPos, yPos, dFunc, wDur) -> do                                 -- listas de parámetros;
    oModify obj $ oLeftX .~ xPos                                          -- modificamos la posición horizontal del objeto;
    oModify obj $ oCenterY .~ yPos                                        -- modificamos la posición vertical del objeto;
    oShowWith obj $ adjustDuration dFunc . oDraw                          -- dibujamos el objeto ajustando la velocidad;
    wait wDur                                                             -- esperamos una cantidad indicada de tiempo.

-----------------------------------------------------------------------------
-- Listas de parámetros utilizados en la escena para cada objeto de texto. --
-----------------------------------------------------------------------------

leftXs :: [Double]
leftXs = [-4.7, -5.5, -3.25, -3.2, -5.5, -5.5, -3.2, -5.5, -5.5, -5.5, -3.75, -5.5, -5.5]

centerYs :: [Double]
centerYs = [3.5, 2.5, 2.5, 1.5, 0.5, -0.5, -0.5, -1, -1.5, -2.5, -2.5, -3, -3.5]

durationFunctions :: [(Duration -> Duration)]
durationFunctions = [(*0.3), (*0.3), (*0.3), (*0.33), (*0.33), (*0.3), (*0.3), (*0.33), (*0.3), (*0.3), (*0.3), (*0.3), (*0.33)]

waitDurations :: [Double]
waitDurations = [0.5, 0.5, 0, 0, 0.5, 0.5, 0, 0, 0.5, 0.5, 0, 0, 3]

------------------------------------------------------------------------------------------------------------------
-- Aquí va el texto que escribiremos, separado en pedazos; usamos "\\hfill\\break" para romper líneas en LaTeX. --
------------------------------------------------------------------------------------------------------------------

cabecera :: SVG    -- Definimos el SVG de la cabecera con los atributos deseados.
cabecera = withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ center $ scale 0.4 $
         latex "Sea V un espacio vectorial con producto escalar."

ejercicio1 :: SVG    -- Definimos el SVG de la primera pregunta con los atributos deseados.
ejercicio1 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 2.1 Para $\\vec{u},\\vec{v}\\in V$, con $\\vec{u},\\vec{v}\\neq 0$, demuestra que $$\\bigg\\langle\\bigg\\{\\vec{u},\\vec{v}-\\frac{\\langle\\vec{v},\\vec{u}\\rangle}{||\\vec{u}||}\\hat{u}\\bigg\\}\\bigg\\rangle = \\langle\\{\\vec{u},\\vec{v}\\}\\rangle,$$ y dibuja un ejemplo en $\\mathbb{R}^2$."

ejercicio1Titulo :: SVG
ejercicio1Titulo = split [0..11] ejercicio1        -- Separamos el título del ejercicio.

ejercicio1Cuerpo :: SVG
ejercicio1Cuerpo = split [12..47] ejercicio1       -- Separamos la parte del ejercicio que va en la misma línea que el título.

ejercicio1Cuerpo' :: SVG
ejercicio1Cuerpo' = split [48..84] ejercicio1      -- Separamos la parte de en medio del ejercicio.

ejercicio1Cuerpo'' :: SVG
ejercicio1Cuerpo'' = split [85..105] ejercicio1    -- Separamos la última parte del ejercicio.

ejercicio2 :: SVG    -- Análogo a lo anterior.
ejercicio2 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 2.2 Supongamos que $V$ tiene dimensión finita. \\hfill\\break Demuestra que, para $1\\leq k\\leq \\text{dim}(V)$, cualquier conjunto \\hfill\\break ortogonal de $k$ vectores es linealmente independiente."

ejercicio2Titulo :: SVG
ejercicio2Titulo = split [0..11] ejercicio2

ejercicio2Cuerpo :: SVG
ejercicio2Cuerpo = split [12..46] ejercicio2

ejercicio2Cuerpo' :: SVG
ejercicio2Cuerpo' = split [47..91] ejercicio2

ejercicio2Cuerpo'' :: SVG
ejercicio2Cuerpo'' = split [92..139] ejercicio2

pregunta :: SVG    -- Análogo a lo anterior.
pregunta = withSubglyphs [0..7] (withStrokeColorPixel miRojo) $ withSubglyphs [0..7] (withFillColorPixel miRojo) $
           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
           latex "Pregunta ¿Qué sucedería si aplicáramos el proceso de \\hfill\\break Gram-Schmidt a un conjunto linealmente \\emph{dependiente} \\hfill\\break de $k$ vectores?"

preguntaTitulo :: SVG
preguntaTitulo = split [0..7] pregunta

preguntaCuerpo :: SVG
preguntaCuerpo = split [8..47] pregunta

preguntaCuerpo' :: SVG
preguntaCuerpo' = split [48..92] pregunta

preguntaCuerpo'' :: SVG
preguntaCuerpo'' = split [93..104] pregunta

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
