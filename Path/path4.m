X = [0, -0.9, 1.9, 3.0, 2.0, 2.8, 4.0, 2.8, 3.3, 1.4];
Y = [0, -0.7, -1.6, -1.4, -1.4, -1.1, -4.1, -2.7, -2.0, -0.5];
Z = [1.0, 1.8, 2.2, 3.3, 4.5, 6.8, 5.8, 9.6, 7.9, 8.8];
t = [ 0.  5. 10. 15. 20. 25. 30. 35. 40. 45.];
Psi = [0, 102.2, 174.4, 10.9, 103.4, 74.3, 3.4, 158.8, 155.4, 36.9];
Psi = Psi * pi / 180;
path.x = timeseries(X,t);
path.y = timeseries(Y,t);
path.z = timeseries(Z,t);
path.psi = timeseries(Psi,t);
clear X Y Z t Psi
uisave('path', 'Path_Project_test_4')