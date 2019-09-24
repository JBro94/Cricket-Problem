clear
clc

for t = 1:100
for j=1:10000
    x = 0;
    y = 0;
   for i=1:1000
      d = 0.1^(i-1);
      theta = 2*pi*rand();
      dx = d*cos(theta);
      dy = d*sin(theta);
      x = x + dx;
      y = y + dy;
   end 
   x_out(j) = x;
   y_out(j) = y;
end 
for k = 1:10000
    dist(k)= sqrt((x_out(k))^2+(y_out(k))^2);
end
    mean(dist)
end


    
        
        


