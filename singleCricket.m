
    x(1) = 0;
    y(1) = 0;
   for i=2:1000
      d = 0.1^(i-1);
      theta = 2*pi*rand();
      dx = d*cos(theta);
      dy = d*sin(theta);
      x(i) = x(i-1) + dx;
      y(i) = y(i-1) + dy;
   end 
   
   plot(x, y)


