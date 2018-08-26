X = [0, -1.5, 1.4, 1.3, -2.5, -5.4, -3.8, -7.8, -8.4, -10.0];
Y = [0, 1.0, 1.2, 3.2, 3.7, 6.5, 10.4, 14.0, 13.9, 14.7];
Z = [3.0, 3.1, 5.4, 9.4, 10.7, 15.4, 16.0, 19.6, 20.6, 22.9];
t = [ 0.  5. 10. 15. 20. 25. 30. 35. 40. 45.];
Psi = [0, 104.3, 82.0, 138.2, 164.9, 43.3, 73.5, 67.0, 35.9, 157.7];
Psi = Psi * pi / 180;
path.x = timeseries(X,t);
path.y = timeseries(Y,t);
path.z = timeseries(Z,t);
path.psi = timeseries(Psi,t);
clear X Y Z t Psi
uisave('path', 'Path_Project_test_5')