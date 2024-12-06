%imread stores png data into a 2d array
origArray = imread("mickey-1.png");
%use reshape to convert 2D array to 1D array
% 256 * 256 = 65,536
singleArray = reshape(origArray, [1,65536]);
%write single array to a textfile
dlmwrite("input.txt", singleArray)
