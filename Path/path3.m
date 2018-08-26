X = [0, 2.8, 2.7, -0.2, 1.4, 0.8, -0.5, 0.7, 0.4, -1.1];
Y = [0, -2.4, 0.0, 1.2, 3.6, 1.6, 0.4, -2.0, -2.7, -3.6];
Z = [0, 0.9, 0.5, 3.7, 2.8, 3.3, 4.5, 4.1, 3.2, 2.5];
t = [ 0.  5. 10. 15. 20. 25. 30. 35. 40. 45.];
Psi = [0, 48.1, 17.8, 145.8, 85.7, 36.2, 115.4, 121.9, 28.3, 168.9];
Psi = Psi * pi / 180;
path.x = timeseries(X,t);
path.y = timeseries(Y,t);
path.z = timeseries(Z,t);
path.psi = timeseries(Psi,t);
clear X Y Z t Psi
uisave('path', 'Path_Project_test_3')