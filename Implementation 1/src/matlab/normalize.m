function [ h,y ] = normalize( h,y )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

    % normalize
    for i=1:length(y)
        [~, mi] = max(abs(h(:,i)));
        mV = h(mi,i);
        h(:,i) = h(:,i)/mV;
        y(i) = y(i) / mV;
    end
end

