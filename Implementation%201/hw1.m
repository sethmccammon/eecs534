% machine learning hw

close all
clear x y w m mi yHat err gSum grad gradSumV wSum
clc

nTrials = 100;
nPts = 45;

y(1:100,1) = trainp116(:,46);
h(1:45,1:100) = trainp116(:,1:45)';

[h,y] = normalize(h,y);

w = randn(nPts,1);

lamda = 0.001;
learningRate = 0.5;
epsilon = 0.1;

[w wSum gSum] = batchGradient(w,h,y,epsilon, learningRate, lamda);
err = batchTest(w,h,y);

gSum(end)
subplot(2,1,1)
plot(gSum)
ylabel('g sum')
grid on
subplot(2,1,2)
plot(wSum)
ylabel('w sum')
xlabel('Iterations')
grid on

figure
plot(err)
ylabel('Error')
xlabel('Sample')
grid on

figure
plot(w)
ylabel('w')
xlabel('Pts')
grid on

%% for batch testing

for i=1:10
    
    lb = 10*(i-1)+1;
    ub = 10*i;
    
    ws = randn(nPts,1);
    ys = vertcat(y(1:lb,:),y(ub:end,:));
    hs = horzcat(h(:,1:lb),h(:,ub:end));
    
    [ws wSums gSums] = batchGradient(ws,hs,ys,epsilon, learningRate, lamda);
    
    yt = y(lb:ub,:);
    ht = h(:,lb:ub);
    
    errBatch(i) = batchTest(ws,ht,yt);
end

figure
plot(errBatch)
ylabel('Error')
xlabel('Sample')
grid on


%% this was for developing and testing purposes, ignore for main project
%{ 

clear h y w nPts nTrials wp

nPts = 2;
nTrials = 3;

h = zeros(nPts,nTrials);
y = zeros(1,nTrials);
w = zeros(nPts,1);

for xi =1:nPts
    for xj = 1:nTrials
        h(xi,xj) = xi;%+rand()-0.5;
    end
end

h = h';

for xi=1:nTrials
    for xj = 1:nPts
        y(xi) = y(xi) + h(xi,xj)*xj;
    end
    y(xi) = y(xi);% + rand()-0.5;
end

y = y';
w;


for iter=1:20
    %{
    for pts=1:nPts
        wp(pts) = 0;
        for sets=1:nTrials
            
            h;
            y;
            w;
            h(sets,pts);
            w(pts);
            yHat = h(sets,pts)*w(pts);
            err = y(pts)-yHat;
            rG = h(sets,pts)*err;
            
            wp(pts) = wp(pts) + learningRate*-2*h(sets,pts)'*(y(pts)-h(sets,pts)*w(pts));
        end
        wp
        
    end
    
    w = wp
    %}
    ya = y;
    yHat = h*w;
    err = y-yHat;
    gradient = h'*err;
    avg_gradient = gradient / length(y);
    w = w + 0.1*avg_gradient - 2*lamda*w;
end

w;
%}











