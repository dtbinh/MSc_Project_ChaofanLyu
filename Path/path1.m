X = [0, 1.5, 0.7, 2.5, 1.4, 1.0, 1.2, 2.7, 1.5, 2.5];
Y = [0, 1.1, 0.0, -0.2, 0.8, 1.5, 2.7, 1.0, 0.2, -0.1];
Z = [0.5, 1.4, 1.9, 1.2, 1.7, 3.7, 6.4, 9.3, 11.1, 12.4];
t = [ 0.  5. 10. 15. 20. 25. 30. 35. 40. 45.];
Psi = [0, 30.5, 104.1, 160.5, 41.1, 51.0, 131.1, 147.9, 149.7, 60.7];
Psi = Psi * pi / 180;
path.x = timeseries(X,t);
path.y = timeseries(Y,t);
path.z = timeseries(Z,t);
path.psi = timeseries(Psi,t);
clear X Y Z t Psi
uisave('path', 'Path_Project_test_1')