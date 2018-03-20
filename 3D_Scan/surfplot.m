% Matlab program to plot the matrix data from ScanArray

% Initializing Program

clear all

% USER INPUTS -------------------------------------------------------------

contour  = 30;      % # of isolines in plot

% Plot --------------------------------------------------------------------
figure(1)
hold on
Z_matrix = xlsread('Matrices.xlsx', 'Zmatrix')
Y_matrix = xlsread('Matrices.xlsx', 'Ymatrix')
X_matrix = xlsread('Matrices.xlsx', 'Xmatrix')
surf(X_matrix, Y_matrix, Z_matrix)

shading interp
contour3(X_matrix, Y_matrix, Z_matrix, contour,'k')

title('3D Scanner Plot')
xlabel('X-axis')
ylabel('Y-axis')
zlabel('Z-axis')

