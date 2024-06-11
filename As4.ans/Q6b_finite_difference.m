figure;
hold on;

for n = [1, 3, 7, 15]
    h = 1/(n+1);
    mainDiags = -2*ones(n,1);
    subDiags  = ones(n-1,1);
    ts = linspace(0,1,n+2)';
    A = diag(mainDiags)+diag(subDiags,-1)+diag(subDiags,1);
    
    % newton iteration
    y0 = ts/(n+1); % a straight line approximation
    yk = y0(2:end-1);
    k = 1;
    while 1
        [Fk,DFk] = fhan(yk,A,h,ts(2:end-1));
        ykp1 = yk-DFk\Fk;
        fprintf('the residule at %i iteration is %d \n',k,norm(Fk));
        if norm(Fk,"inf")<1e-14
            ys = ykp1;
            break;
        end
        k = k+1;
        yk = ykp1;
    end
    plot(ts,[0;ys;1],'o-', 'DisplayName', ['n = ', num2str(n)])
end

title('Finite Difference Method Solution');
xlabel('t');
ylabel('u(t)');
legend show;

function [F,DF] = fhan(y,A,h,t)
    % evaluate function
    F      = A*y-h^2*(10*y.^3+3*y+t.^2);
    F(end) = F(end)+1; % the last entry
    % evaluate its Jacobian
    DF = A-h^2*diag(30*y.^2+3);
end