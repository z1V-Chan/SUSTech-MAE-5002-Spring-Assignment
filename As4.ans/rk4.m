function [t,y] = rk4(fhan,y0,h,t0,tf)

npts = round((tf-t0)/h)+1;
dim  = numel(y0);
y    = zeros(dim,npts); t = zeros(npts,1);
y(:,1) = y0; t(end) = tf;
for k=1:npts-1
    yk = y(:,k); tk = t0+(k-1)*h; t(k) = tk;
    k1 = fhan(tk,yk);
    k2 = fhan(tk+h/2,yk+h/2*k1);
    k3 = fhan(tk+h/2,yk+h/2*k2);
    k4 = fhan(tk+h,yk+h*k3);
    y(:,k+1) = yk+h/6*(k1+2*k2+2*k3+k4);
end

end