function [ w wSum gSum ] = batchGradient( w,h,y, epsilon, learningRate, lamda )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

    flag = 1;
    i=0;
    while flag
        i = i+1;
        yHat = h'*w;
        err = y - yHat;
        gradient = h*err / length(w);
        gSum(i) = sum(gradient);
        wSum(i) = sum(w);

        w = w+learningRate*gradient - 2*lamda*w;
        
        if abs(gSum(i)) < epsilon
            flag = 0;
        end
        
        if i > 200
            flag = 0;
        end
    end

end
