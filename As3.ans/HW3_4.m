clear
clc
ft = @(t) 1./(1+25*t.^2);
n1 = 5;
n2 = 10;
intv = [-1,1];

draw_t = linspace(intv(1),intv(2),100);
%% equally spaced
t1 = linspace(intv(1),intv(2),n1+1);
f1 = ft(t1);

t2 = linspace(intv(1),intv(2),n2+1);
f2 = ft(t2);

p5 = LagInt(draw_t,t1,f1);
p10 = LagInt(draw_t,t2,f2);
realf = ft(draw_t);

figure;
plot(draw_t,p5,'b--',draw_t,p10,'m-.',draw_t,realf,'k-')
legend(["$p_5(t)$","$p_{10}(t)$","$f(t)=1/(1+25t^2)$"],"Interpreter","latex")
title("Equally spaced interpolaton points")
%% Chebyshev points
t1Che = Chebyshevpoints(n1+1);
f1Che = ft(t1Che);

t2Che = Chebyshevpoints(n2+1);
f2Che = ft(t2Che);

p5Che = LagInt(draw_t,t1Che,f1Che);
p10Che = LagInt(draw_t,t2Che,f2Che);
realf = ft(draw_t);
figure;
plot(draw_t,p5Che,'b--',draw_t,p10Che,'m-.',draw_t,realf,'k-')
legend(["$p_5(t)$","$p_{10}(t)$","$f(t)=1/(1+25t^2)$"],"Interpreter","latex")
title("Chebyshev points")

%% Lagrange interpolation
function res = LagInt(t,tlist,flist)
    res = 0;
    n = length(tlist);
    for i = 1:n
        li = 1;
        for j = 1:i-1
            li = li.*(t-tlist(j))./(tlist(i)-tlist(j));
        end
        for j = i+1:n
            li = li.*(t-tlist(j))./(tlist(i)-tlist(j));
        end
        res = res + flist(i)*li;
    end
end
%% Chebyshev points
function t = Chebyshevpoints(k)
    for i = 1:k
        t(i) = cos((2*i-1)*pi/(2*k));
    end
end





