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

  -- Este bloque genera una lista con los objetos de texto (SVGs) que serán utilizados en la primera parte de la escena.
  
  texts1 <- mapM oNew [ e1p0, e1p1, e1p2, e1p3, e1p4, e1p5, e2p0, e2p1 ]

  -- Este bloque genera una lista con los objetos de texto (SVGs) que serán utilizados en la segunda parte de la escena.

  texts2 <- mapM oNew [ c1p0, e3p0, e3p1, e3p2, e3p3, e4p0, e4p1, e4p2, e4p3 ]

  -- Este bloque genera una lista con los objetos de texto (SVGs) que serán utilizados en la tercera parte de la escena.

  texts3 <- mapM oNew [ p5p0, p5p1, p5p2, p5p3, p5p4 ]

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
    
  forM_ (zip5 texts3 leftXs3 topYs3 durationFunctions3 waitDurations3) $    -- Creamos una lista de 5-tuplas a partir de las
    \(obj, xPos, yPos, dFunc, wDur) -> do                              -- listas de parámetros;
    oModify obj $ oLeftX .~ xPos                                       -- modificamos la posición horizontal del objeto;
    oModify obj $ oTopY .~ (yPos - 0.5)                                        -- modificamos la posición vertical del objeto;
    oShowWith obj $ adjustDuration dFunc . oDraw                       -- dibujamos el objeto ajustando la velocidad;
    wait wDur                                                          -- esperamos una cantidad indicada de tiempo.

  forM_ texts3 $
    \obj -> fork $ do
    oHideWith obj oFadeOut
    

-----------------------------------------------------------------------------
-- Listas de parámetros utilizados en la escena para cada objeto de texto. --
-----------------------------------------------------------------------------

leftXs1 :: [Double]
leftXs1 = [-7.75, -5.5, -7.75, -2.25, -7.75, -7.75, -7.75, -7.75]

topYs1 :: [Double]
topYs1 = [3.5, 3.525, 3.5, 2.5, 1.5, 1.5, 0, 0]

durationFunctions1 :: [(Duration -> Duration)]
durationFunctions1 = [(*0.3), (*0.33), (*0.4), (*0.75), (*0.5), (*0.33), (*0.3), (*0.33)]

waitDurations1 :: [Double]
waitDurations1 = [0.5, 0.25, 0, 0, 0, 0.5, 0.5, 2.5]

leftXs2 :: [Double]
leftXs2 = [-7.25, -7.75, -5.5, -7.75, -7.75, -7.75, -7.75, -2.25, -7.75]

topYs2 :: [Double]
topYs2 = [4.75, 3.25, 3.25, 2.25, 1.5, -0.25, -0.25, -1.25, -2.75]

durationFunctions2 :: [(Duration -> Duration)]
durationFunctions2 = [(*0.4), (*0.3), (*0.3), (*0.33), (*0.5), (*0.3), (*0.33), (*0.5), (*0.4)]

waitDurations2 :: [Double]
waitDurations2 = [0.5, 0.5, 0, 0.5, 2, 0, 0, 0, 2.5]

leftXs3 :: [Double]
leftXs3 = [-7.75, -7.75, -7.75, -7.75, -4]

topYs3 :: [Double]
topYs3 = [3.25, 3.25, 2.3, 1.85, -0.175]

durationFunctions3 :: [(Duration -> Duration)]
durationFunctions3 = [(*0.3), (*0.33), (*0.33), (*0.33), (*0.33)]

waitDurations3 :: [Double]
waitDurations3 = [0.5, 0.25, 0.5, 0, 0]

------------------------------------------------------------------------------------------------------------------
-- Aquí va el texto que escribiremos, separado en pedazos; usamos "\\hfill\\break" para romper líneas en LaTeX. --
------------------------------------------------------------------------------------------------------------------

ejercicio1 :: SVG    -- Definimos el SVG del primer ejercicio con los atributos deseados.
ejercicio1 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 2.1 Sea $V$ un espacio vectorial con norma $||\\cdot||:V\\to \\mathbb{R}^{\\ge0}$. Para $\\vec{u}\\in V$, demuestra que $$\\vec{u}\\neq\\vec{0} \\implies ||\\vec{u}||>0,$$ es decir, que la norma es positivo definida. Adicionalmente, demuestra que la implicación contraria también se verifica."

e1p0 :: SVG
e1p0 = split [0..11] ejercicio1

e1p1 :: SVG
e1p1 = split [12..53] ejercicio1

e1p2 :: SVG
e1p2 = split [54..74] ejercicio1

e1p3 :: SVG
e1p3 = split [75..91] ejercicio1

e1p4 :: SVG
e1p4 = split [92..127] ejercicio1

e1p5 :: SVG
e1p5 = split [128..200] ejercicio1

ejercicio2 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latexCfg myTexConfig "Ejercicio 2.2 Demuestra que todo conjunto ortonormal finito es linealmente independiente."

e2p0 :: SVG
e2p0 = split [0..11] ejercicio2

e2p1 :: SVG
e2p1 = split [12..78] ejercicio2

c1p0 :: SVG      -- Definimos el SVG de la cabecera con los atributos deseados.
c1p0 = withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ center $ scale 0.4 $
         latex "Sean $(V,K)$ un espacio vectorial con producto escalar $\\langle \\cdot , \\cdot \\rangle:V\\times V\\to K$, $\\text{dim}(V)<\\infty$ y $N=\\{\\hat{n}_1, \\hat{n}_2, \\dots, \\hat{n}_k\\}\\subseteq V$ considerando la norma inducida."

ejercicio3 :: SVG    -- Análogo a lo anterior.
ejercicio3 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 2.3 Demuestra que las siguientes condiciones son equivalentes. \\hfill \\break \\break (a) $N$ es una base ortonormal de $V$. \\hfill \\break \\break (b) $\\langle N \\rangle = V$ y $\\langle \\hat{n}_i, \\hat{n}_j \\rangle = \\begin{cases} 1 \\ \\ \\text{si} \\ j=i, \\\\ 0 \\ \\ \\text{si} \\ j\\neq i. \\end{cases}$"

e3p0 :: SVG
e3p0 = split [0..11] ejercicio3

e3p1 :: SVG
e3p1 = split [12..63] ejercicio3

e3p2 :: SVG
e3p2 = split [64..90] ejercicio3

e3p3 :: SVG
e3p3 = split [91..125] ejercicio3

ejercicio4 :: SVG    -- Análogo a lo anterior.
ejercicio4 = withSubglyphs [0..11] (withStrokeColorPixel miAzul) $ withSubglyphs [0..11] (withFillColorPixel miAzul) $
            withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
                latex "Ejercicio 2.4 Demuestra que $N=\\{\\hat{n}_1,\\hat{n}_2,\\dots,\\hat{n}_k\\}$ es una base \\emph{ortonormal} de $V$ si, y sólo si, $$\\vec{v} = \\sum_{i=1}^k \\langle\\vec{v}, \\hat{n}_i\\rangle \\hat{n}_i \\quad \\forall \\ \\vec{v}\\in V.$$ Más aún, demuestra que en este caso $\\big \\langle \\langle \\vec{v} , \\hat{n}_i \\rangle \\hat{n}_i, \\langle \\vec{v} , \\hat{n}_j \\rangle \\hat{n}_j \\big \\rangle = 0$ si $i\\neq j$." 

e4p0 :: SVG
e4p0 = split [0..11] ejercicio4

e4p1 :: SVG
e4p1 = split [12..76] ejercicio4

e4p2 :: SVG
e4p2 = split [77..101] ejercicio4

e4p3 :: SVG
e4p3 = split [102..166] ejercicio4
e4p4 = split [102..166] ejercicio4

pregunta5 :: SVG    -- Análogo a lo anterior.
pregunta5 = withSubglyphs [0..10] (withStrokeColorPixel miRojo) $ withSubglyphs [0..10] (withFillColorPixel miRojo) $
           withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ scale 0.4 $ 
           latexCfg myTexConfig "Pregunta 2.5 Por la propiedad de \\emph{escalabilidad absoluta} de la norma, multiplicar a un vector arbitrario por un escalar con valor absoluto $1$ deja invariante su norma. ¿Cómo se interpreta esto geométricamente en espacios vectoriales reales y complejos? (Sugerencia: Considera vectores de $\\mathbb{R}^2$ multiplicados por escalares de $\\{x\\in \\mathbb{R} \\mid |x| = 1\\}$ y vectores de $\\mathbb{C}$ multiplicados por escalares de $\\{z\\in\\mathbb{C} \\mid |z|=1\\}$. En cada caso, la multiplicación de vectores por escalares de valor absoluto 1 se interpreta como un tipo de operación geométrica bajo la cual la norma es invariante. ¿Cuáles son?)"

p5p0 :: SVG
p5p0 = split [0..10] pregunta5

p5p1 :: SVG
p5p1 = split [11..138] pregunta5

p5p2 :: SVG
p5p2 = split [139..214] pregunta5

p5p3 :: SVG
p5p3 = split [215..477] pregunta5

p5p4 :: SVG
p5p4 = split [478..490] pregunta5

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
