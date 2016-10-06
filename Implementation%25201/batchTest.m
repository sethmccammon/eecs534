function [ err ] = batchTest( w,h,y )
%Sum squared error of the given batch
    yHat = h'*w;
    err = sum((y - yHat).^2);
end

