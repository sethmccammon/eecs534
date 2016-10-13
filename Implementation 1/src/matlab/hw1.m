% machine learning hw

close all
clear
clc

train = csvread('../Implementation 1/data/train p1-16.csv');
test = csvread('../Implementation 1/data/test p1-16.csv');

nTrials = 100;
nPts = 45;

y(1:100,1) = train(:,46);
h(1:45,1:100) = train(:,1:45)';
[h,y] = normalize(h,y);

ty(1:100,1) = test(:,46);
th(1:45,1:100) = test(:,1:45)';
[th,ty] = normalize(th,ty);

w = randn(nPts,1);

lamda = 0.001;
learningRate = 0.5;
epsilon = 0.01;


%% varying the learning rate
lR = [0, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1];%, 1.1, 1.2, 1.3];
clear lR
lR = [0:0.001:1];
for i=1:length(lR)
    w = randn(nPts,1);
    [w wSum gSum] = batchGradient(w,h,y,epsilon, lR(i), lamda);

    err(i) = batchTest(w,h,y);
    errT(i) = batchTest(w,th,ty);
    
    %{
    figure
        subplot(2,1,1)
            plot(gSum)
            title(['LR = ' num2str(lR(i)) ', lamda = ' num2str(lamda) ]);
            ylabel('g sum')
            grid on
        subplot(2,1,2)
            plot(wSum)
            ylabel('w sum')
            xlabel('Iterations')
            grid on
    %}
end

figure
    semilogx(lR,err,'b.', lR, errT, 'r.');
    ylabel('SSE')
    xlabel('Learning Rate')
    legend('Training Error', 'Testing Error');
    grid on
    
%% varryin lamda (L2)
la = [0, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5];%, 1, 10, 100];

clear la
la = [0:0.001:0.5];

clear err errT
err = zeros(length(la));
errT = zeros(length(la));
for i=1:length(la)
    w = randn(nPts,1);
    [w wSum gSum] = batchGradient(w,h,y,epsilon, learningRate, la(i));

    err(i) = batchTest(w,h,y);
    errT(i) = batchTest(w,th,ty);
    
    %{
    figure
        subplot(2,1,1)
            plot(gSum)
            title(['LR = ' num2str(learningRate) ', lamda = ' num2str(la(i)) ]);
            ylabel('g sum')
            grid on
        subplot(2,1,2)
            plot(wSum)
            ylabel('w sum')
            xlabel('Iterations')
            grid on
    %}
end

figure
    loglog(la,err,'b', la, errT, 'r');
    ylabel('SSE')
    xlabel('Lamda')
    legend('Training Error', 'Testing Error');
    grid on
%% for batch testing

errBatch = zeros( size(la) );

for i=1:10
    
    lb = 10*(i-1)+1;
    ub = 10*i;
    
    ws = randn(nPts,1);
    ys = vertcat(y(1:lb,:),y(ub:end,:));
    hs = horzcat(h(:,1:lb),h(:,ub:end));
    
    for j=1:length(la)
    
        [ws wSums gSums] = batchGradient(ws,hs,ys,epsilon, learningRate, la(j));
    
        yt = y(lb:ub,:);
        ht = h(:,lb:ub);
    
        errBatch(j) = errBatch(j) + batchTest(ws,ht,yt)/10; % normalized because 10 validation sets
    end
end

figure
    semilogx(la, errBatch)
    %title('Cross Validation')
    ylabel('SSE')
    xlabel('Lamda')
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











