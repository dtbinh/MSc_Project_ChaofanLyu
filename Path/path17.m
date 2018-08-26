X = [0, 0.0, -0.0, -0.1, -0.2, -0.2, -0.2, -0.2, -0.1, -0.1, -0.1, -0.2, -0.3, -0.2, -0.2, -0.1, -0.2, -0.3, -0.3, -0.3];
Y = [0, -0.1, -0.0, 0.0, -0.1, -0.0, -0.1, -0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, -0.1, -0.1, -0.1, -0.1, -0.0, -0.0];
Z = [3.0, 2.9, 3.0, 3.0, 3.0, 3.0, 2.9, 2.9, 3.0, 3.1, 3.2, 3.2, 3.3, 3.3, 3.3, 3.3, 3.2, 3.3, 3.2, 3.3];
t = [0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0, 27.0, 30.0, 33.0, 36.0, 39.0, 42.0, 45.0, 48.0, 51.0, 54.0, 57.0];
Psi = [0, -0.5, -0.1, 0.9, -0.7, -0.5, -0.7, -0.9, 0.7, 0.9, -0.9, -0.9, 0.2, 0.9, 0.1, -0.3, 0.1, 0.5, 0.2, 1.0];
Psi = Psi * pi / 180;
path.x = timeseries(X,t);
path.y = timeseries(Y,t);
path.z = timeseries(Z,t);
path.psi = timeseries(Psi,t);
clear X Y Z t Psi
uisave('path', 'Path_Project_test_17')