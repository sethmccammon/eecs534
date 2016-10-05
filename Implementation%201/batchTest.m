function [ err ] = batchTest( w,h,y )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

    yHat = h'*w;
    err = sum(abs(y - yHat));
end

