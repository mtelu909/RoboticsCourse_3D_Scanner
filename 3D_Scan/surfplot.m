% Matlab program to plot the matrix data from ScanArray

% Initializing Program

clear all

% USER INPUTS -------------------------------------------------------------

contour  = 30;      % # of isolines in plot

% Plot --------------------------------------------------------------------

Z_matrix = xlsread('matrix.xlsx')
surf(Z_matrix)
shading interp
%contour3(X,Y,Z,controur,'b')


