figure;
hold on;
ts = linspace(0,1,100);

for n = [3, 4, 5, 6]
    x0 = zeros(n,1);
    t = linspace(0,1,n)';
    myfun = @(x) residual_collocation(x,n,t);
    x = fsolve(myfun,x0,optimoptions('fsolve','Display','iter'));
    ys = polyval(flip(x),ts);
    plot(ts,ys,'-', 'DisplayName', ['n = ', num2str(n)])
end

title('Collocation Method Solution');
xlabel('t');
ylabel('u(t)');
legend show;

function F = residual_collocation(x,n,t)
    % calculate u(t)
    u = zeros(n,1);
    for j=1:n
        u = u+t.^(j-1)*x(j);
    end
    % calculate u''(t)
    upp = zeros(n,1);
    for j=3:n
        upp = upp+(j-1)*(j-2)*t.^(j-3)*x(j);
    end
    % calculate F
    F = upp-(10*u.^3+3*u+t.^2);
    % impose boundary condition
    F(1) = x(1);
    F(end) = sum(x)-1;
end