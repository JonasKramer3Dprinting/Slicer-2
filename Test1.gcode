;FLAVOR:Marlin 
;Layer height: 0.12 
;Generated with Cura_SteamEngine 4.9.0 
M140 S70.0
M105 
M190 S70.0
M104 S210.0
M105 
M109 S210.0
M83 ;relative extrusion mode 
; Ender 3 Custom Start G-code 
G92 E0 ; Reset Extruder 
G28 ; Home all axes 
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed 
G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position 
G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line 
G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little 
G1 X0.4 Y20 Z0.3 F1500.0 E15 ; Draw the second line 
G92 E0 ; Reset Extruder 
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed 
G1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish 
G92 E0 
G92 E0 
G1 F3000 E-8 
M104 S210.0
M140 S70.0
G0 X109.8 Y104.8 Z0.24 F1200.0
G1 E8
G1 X90.2 Y104.8 Z0.24 E0.7822783762852838 F1200.0
G1 X90.2 Y95.2 Z0.24 E0.3831567557315675 F1200.0
G1 X109.8 Y95.2 Z0.24 E0.7822783762852838 F1200.0
G1 X109.8 Y104.8 Z0.24 E0.3831567557315675 F1200.0
G1 X109.4 Y104.4 Z0.24 E0.022577728352935273 F1200.0
G1 X90.6 Y104.4 Z0.24 E0.7503486466409872 F1200.0
G1 X90.6 Y95.6 Z0.24 E0.35122702608727085 F1200.0
G1 X109.4 Y95.6 Z0.24 E0.7503486466409872 F1200.0
G1 X109.4 Y104.4 Z0.24 E0.35122702608727085 F1200.0
G1 X109.0 Y104.0 Z0.24 E0.022577728352936078 F1200.0
G1 X91.0 Y104.0 Z0.24 E0.7184189169966894 F1200.0
G1 X91.0 Y96.0 Z0.24 E0.3192972964429731 F1200.0
G1 X109.0 Y96.0 Z0.24 E0.7184189169966894 F1200.0
G1 X109.0 Y104.0 Z0.24 E0.3192972964429731 F1200.0
G1 X108.6 Y103.6 Z0.24 E0.022577728352936078 F1200.0
G1 X91.4 Y103.6 Z0.24 E0.6864891873523916 F1200.0
G1 X91.4 Y96.4 Z0.24 E0.2873675667986753 F1200.0
G1 X108.6 Y96.4 Z0.24 E0.6864891873523916 F1200.0
G1 X108.6 Y103.6 Z0.24 E0.2873675667986753 F1200.0
G1 X108.2 Y103.2 Z0.24 E0.022577728352935273 F1200.0
G1 X91.8 Y103.2 Z0.24 E0.654559457708095 F1200.0
G1 X91.8 Y96.8 Z0.24 E0.2554378371543787 F1200.0
G1 X108.2 Y96.8 Z0.24 E0.654559457708095 F1200.0
G1 X108.2 Y103.2 Z0.24 E0.2554378371543787 F1200.0
G1 X107.8 Y102.8 Z0.24 E0.022577728352936078 F1200.0
G1 X92.2 Y102.8 Z0.24 E0.6226297280637973 F1200.0
G1 X92.2 Y97.2 Z0.24 E0.22350810751008096 F1200.0
G1 X107.8 Y97.2 Z0.24 E0.6226297280637973 F1200.0
G1 X107.8 Y102.8 Z0.24 E0.22350810751008096 F1200.0
G1 X107.39999999999999 Y102.4 Z0.24 E0.022577728352935676 F1200.0
G1 X92.60000000000001 Y102.4 Z0.24 E0.5906999984194996 F1200.0
G1 X92.60000000000001 Y97.6 Z0.24 E0.1915783778657843 F1200.0
G1 X107.39999999999999 Y97.6 Z0.24 E0.5906999984194996 F1200.0
G1 X107.39999999999999 Y102.4 Z0.24 E0.1915783778657843 F1200.0
G1 X107.0 Y102.0 Z0.24 E0.022577728352935676 F1200.0
G1 X93.0 Y102.0 Z0.24 E0.558770268775203 F1200.0
G1 X93.0 Y98.0 Z0.24 E0.15964864822148656 F1200.0
G1 X107.0 Y98.0 Z0.24 E0.558770268775203 F1200.0
G1 X107.0 Y102.0 Z0.24 E0.15964864822148656 F1200.0
G1 X106.6 Y101.6 Z0.24 E0.022577728352936078 F1200.0
G1 X93.4 Y101.6 Z0.24 E0.5268405391309051 F1200.0
G1 X93.4 Y98.4 Z0.24 E0.12771891857718878 F1200.0
G1 X106.6 Y98.4 Z0.24 E0.5268405391309051 F1200.0
G1 X106.6 Y101.6 Z0.24 E0.12771891857718878 F1200.0
G1 X106.2 Y101.2 Z0.24 E0.022577728352935273 F1200.0
G1 X93.8 Y101.2 Z0.24 E0.4949108094866085 F1200.0
G1 X93.8 Y98.8 Z0.24 E0.09578918893289215 F1200.0
G1 X106.2 Y98.8 Z0.24 E0.4949108094866085 F1200.0
G1 X106.2 Y101.2 Z0.24 E0.09578918893289215 F1200.0
G1 X105.8 Y100.8 Z0.24 E0.022577728352936078 F1200.0
G1 X94.2 Y100.8 Z0.24 E0.46298107984231074 F1200.0
G1 X94.2 Y99.2 Z0.24 E0.06385945928859439 F1200.0
G1 X105.8 Y99.2 Z0.24 E0.46298107984231074 F1200.0
G1 X105.8 Y100.8 Z0.24 E0.06385945928859439 F1200.0
G1 X105.39999999999999 Y100.4 Z0.24 E0.022577728352935676 F1200.0
G1 X94.60000000000001 Y100.4 Z0.24 E0.431051350198013 F1200.0
G1 X94.60000000000001 Y99.6 Z0.24 E0.03192972964429776 F1200.0
G1 X105.39999999999999 Y99.6 Z0.24 E0.431051350198013 F1200.0
G1 X105.39999999999999 Y100.4 Z0.24 E0.03192972964429776 F1200.0