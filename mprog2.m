%opens C program output file and reads all values using fileread
pixelString = fileread("input.txt");
%convert to numbers from 1D array string
%will split along every comma
pixelArray = str2num(pixelString);
%convert to char values
pixelCharArray = uint8(pixelArray);
%convert to 2D array, dimensions are 256 x 256
imageMatrix = reshape(pixelCharArray, [256,256]);
%output image
imshow(imageMatrix);