figure;
hold on;

t0 = 0; tf = 1;
u0 = 0; gamma0 = 0;
h = 0.1;
fhan = @(t,y) [y(2); 10*y(1)^3 + 3*y(1) + t^2];
myfun = @(gamma) ghan(gamma,t0,tf,h,fhan,u0)-1;
outputFcn = @(gamma, output, state) plotIter(gamma, t0, tf, h, fhan, u0, state);
options = optimoptions('fsolve', 'Display', 'iter', 'OptimalityTolerance', 1e-2, ...
    'OutputFcn', outputFcn);
x = fsolve(myfun, gamma0, options);

title('Shooting Method Solution');
xlabel('t');
ylabel('u(t)');
legend('Interpreter', 'latex');
legend show;

function uf = ghan(gamma,t0,tf,h,fhan,u0)
    y0 = [u0;gamma];
    [~,y] = rk4(fhan,y0,h,t0,tf);
    uf = y(1,end);
end

function stop = plotIter(gamma, t0, tf, h, fhan, u0, state)
    stop = false;
    if strcmp(state, 'iter')
        y0 = [u0;gamma];
        [t,y] = rk4(fhan,y0,h,t0,tf);
        plot(t, y(1,:), 'DisplayName', ['$u''(0)$ = ', num2str(gamma)]);
    end
end