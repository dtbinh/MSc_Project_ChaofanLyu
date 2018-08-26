X = [0, 2.6, 2.6, 5.4, 6.8, 9.7, 13.0, 11.9, 12.6, 10.0];
Y = [0, -2.4, 0.2, -3.1, -6.4, -7.5, -9.5, -8.3, -8.2, -9.1];
Z = [4.0, 1.8, 0.8, 0.5, 0.6, 0.5, 0.5, 0.5, 1.2, 0.5];
t = [ 0.  5. 10. 15. 20. 25. 30. 35. 40. 45.];
Psi = [0, 8.3, 94.5, 83.4, 114.7, 58.7, 74.4, 40.0, 31.1, 17.0];
Psi = Psi * pi / 180;
path.x = timeseries(X,t);
path.y = timeseries(Y,t);
path.z = timeseries(Z,t);
path.psi = timeseries(Psi,t);
clear X Y Z t Psi
uisave('path', 'Path_Project_test_6')