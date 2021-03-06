X = [0, 0.8, 0.8, 1.6, 1.4, 1.6, 1.9, 2.3, 2.1, 1.7, 1.5, 1.0, 0.2, 0.1, -0.5, -1.5, -1.1, -1.1, -0.6, -0.1];
Y = [0, 1.8, 2.2, 5.3, 1.3, -0.8, -3.1, -2.9, -1.2, 2.2, 1.3, 3.8, 0.7, 3.4, 6.9, 10.5, 10.0, 7.9, 4.3, 6.0];
Z = [3.0, 2.4, 2.5, 1.6, 2.3, 2.4, 1.6, 0.9, 0.5, 0.5, 0.9, 0.5, 0.5, 0.6, 1.3, 1.9, 1.0, 0.5, 1.2, 1.6];
t = [0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0, 27.0, 30.0, 33.0, 36.0, 39.0, 42.0, 45.0, 48.0, 51.0, 54.0, 57.0];
Psi = [0, 73.6, 170.5, 30.2, 99.4, 125.0, 44.3, 55.6, 29.7, 150.9, 74.6, 175.6, 120.6, 157.5, 26.7, 69.7, 79.6, 48.0, 124.5, 33.2];
Psi = Psi * pi / 180;
path.x = timeseries(X,t);
path.y = timeseries(Y,t);
path.z = timeseries(Z,t);
path.psi = timeseries(Psi,t);
clear X Y Z t Psi
uisave('path', 'Path_Project_test_12')