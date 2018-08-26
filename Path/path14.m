X = [0, 2.9, -0.2, 3.1, 3.3, 4.1, 7.2, 11.0, 7.7, 8.3, 4.7, 5.2, 4.2, 0.6, -3.3, -3.9, -1.1, 2.8, 3.9, 4.4];
Y = [0, -0.3, 0.2, -0.6, 0.2, 1.1, 1.1, 0.7, 0.3, 0.8, 0.0, -0.3, -1.0, -1.6, -1.9, -1.7, -2.0, -1.6, -0.9, -1.1];
Z = [3.0, 3.9, 4.5, 3.7, 2.8, 3.5, 2.5, 3.0, 3.6, 3.6, 3.2, 2.8, 2.0, 1.1, 0.5, 1.2, 0.6, 0.6, 0.5, 0.5];
t = [0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0, 27.0, 30.0, 33.0, 36.0, 39.0, 42.0, 45.0, 48.0, 51.0, 54.0, 57.0];
Psi = [0, 8.2, 57.1, 43.9, 166.5, 6.4, 109.5, 176.5, 56.2, 97.6, 21.5, 61.5, 37.4, 127.7, 127.4, 132.6, 180.0, 108.1, 125.4, 37.5];
Psi = Psi * pi / 180;
path.x = timeseries(X,t);
path.y = timeseries(Y,t);
path.z = timeseries(Z,t);
path.psi = timeseries(Psi,t);
clear X Y Z t Psi
uisave('path', 'Path_Project_test_14')