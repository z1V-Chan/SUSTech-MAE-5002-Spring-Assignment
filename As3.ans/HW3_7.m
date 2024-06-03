clear all
clc

exact_res = exp(3)-exp(0);
fx = @(x) exp(x);
a = 0;
b = 3;
h = 1 ./ 2.^(linspace(1,10,10));

%% composite midpoint
compmid_error  = abs(compMid(a,b,h,fx)-exact_res);


p=polyfit(log(h),log(compmid_error),1);
C=exp(p(2));
order=p(1);
X = ['Midpoint rule:',' C = ',num2str(C),' h =',num2str(order)];
disp(X)

%% composite Trapezoid
comptrap_error = abs(compTrap(a,b,h,fx)-exact_res);

p=polyfit(log(h),log(comptrap_error),1);
C=exp(p(2));
order=p(1);
X = ['Trapezoid rule:',' C = ',num2str(C),' h =',num2str(order)];
disp(X)
%% composite Simpson
compsimp_error = abs(compSimp(a,b,h,fx)-exact_res);

p=polyfit(log(h),log(compsimp_error),1);
C=exp(p(2));
order=p(1);
X = ['Simpson rule:',' C = ',num2str(C),' h =',num2str(order)];
disp(X)

%% composite 3pGauss
comp3pgauss_error = abs(comp3pGauss(a,b,h,fx)-exact_res);

p=polyfit(log(h(1:5)),log(comp3pgauss_error(1:5)),1);
C=exp(p(2));
order=p(1);
X = ['3point Gaussian rule:',' C = ',num2str(C),' h =',num2str(order)];
disp(X)
%% plot
figure;
loglog(h,compmid_error,'ko--',h,comptrap_error,'ks-.',h,compsimp_error,'kd-',h(1:5),comp3pgauss_error(1:5),'kp-')
legend(["Midpoint", "Trapz", "Simpson","3-Point Gauss",'Location','northwest'])
xlabel("h")
ylabel("Error")

%% Composite
function res = compMid(a,b,h,f)
    res = zeros(length(h),1);
    for k = 1:length(h)
        interval = a:h(k):b;
        ai_list  = interval(1:end-1);
        bi_list  = interval(2:end);
        for i = 1:length(ai_list)
            res(k) = res(k) + (bi_list(i)-ai_list(i))*f((bi_list(i)+ai_list(i))/2);
        end
    end
end

function res = compTrap(a,b,h,f)
    res = zeros(length(h),1);
    for k = 1:length(h)
        interval = a:h(k):b;
        ai_list  = interval(1:end-1);
        bi_list  = interval(2:end);
        for i = 1:length(ai_list)
            res(k) = res(k) + (bi_list(i)-ai_list(i))/2*(f(ai_list(i))+f(bi_list(i)));
        end
    end
end

function res = compSimp(a,b,h,f)
    res = zeros(length(h),1);
    for k = 1:length(h)
        interval = a:h(k):b;
        ai_list  = interval(1:end-1);
        bi_list  = interval(2:end);
        for i = 1:length(ai_list)
            res(k) = res(k) + (bi_list(i)-ai_list(i))/6*(f(ai_list(i))+4*f((ai_list(i)+bi_list(i))/2)+f(bi_list(i)));
        end
    end
end

%% 3-points Gaussian quadrature

function res = comp3pGauss(a,b,h,f)
%%get nodes and weight
alpha=-1; beta=1;
syms x1 x2 x3 w1 w2 w3
eq1= w1+w2+w3==2;
eq2= w1*x1+w2*x2+w3*x3==0;
eq3= w1*x1^2+w2*x2^2+w3*x3^2==2/3;
eq4= w1*x1^3+w2*x2^3+w3*x3^3==0;
eq5= w1*x1^4+w2*x2^4+w3*x3^4==2/5;
eq6= w1*x1^5+w2*x2^5+w3*x3^5==0;
sol=solve(eq1,eq2,eq3,eq4,eq5,eq6,x1,x2,x3,w1,w2,w3);
x(1)=double(sol.x1(1));
x(2)=double(sol.x2(1));
x(3)=double(sol.x3(1));
w(1)=double(sol.w1(1));
w(2)=double(sol.w2(1));
w(3)=double(sol.w3(1));

res = zeros(length(h),1);    
for k = 1:length(h)
    
    interval = a:h(k):b;
    ai_list  = interval(1:end-1);
    bi_list  = interval(2:end);
    
    for i = 1:length(ai_list)
        for l=1:length(x)
        res(k) = res(k)+(bi_list(i)-ai_list(i))/(beta-alpha)*w(l)*f(((bi_list(i)-ai_list(i))*x(l)+ai_list(i)*beta-bi_list(i)*alpha)/(beta-alpha));
        end
    end
    
end

end

