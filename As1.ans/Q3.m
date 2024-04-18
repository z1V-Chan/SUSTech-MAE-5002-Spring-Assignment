x = 1;
k = 0:1:16;
h = 10.^(-k);
f1x = (cos(x+h)-cos(x))./h;
f2x = (cos(x+h)-cos(x-h))./(2*h);
y = -sin(x);
e1 = abs(f1x-y);
e2 = abs(f2x-y);
loglog(h,e1,h,e2);
legend finite-difference 'centered difference';
xlabel('h');
ylabel('error');
grid on
