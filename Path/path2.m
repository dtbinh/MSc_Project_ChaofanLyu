X = [0, 1.1, 1.1, -0.9, -2.5, -1.1, -3.5, -6.0, -6.5, -9.1];
Y = [0, -2.0, -1.5, -0.4, -0.7, 0.2, 2.4, 4.8, 3.1, 5.4];
Z = [0, 0.5, 0.5, 2.1, 0.5, 0.5, 2.5, 5.4, 3.2, 3.1];
t = [ 0.  5. 10. 15. 20. 25. 30. 35. 40. 45.];
Psi = [0, 166.8, 165.1, 134.5, 100.4, 90.4, 95.9, 89.0, 74.7, 68.8];
Psi = Psi * pi / 180;
path.x = timeseries(X,t);
path.y = timeseries(Y,t);
path.z = timeseries(Z,t);
path.psi = timeseries(Psi,t);
clear X Y Z t Psi
uisave('path', 'Path_Project_test_2')