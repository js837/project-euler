n=100;
x=linspace(0,1600,n);
y=linspace(0,1600,n);
h=zeros(n,n);



for i=1:length(x)
    for j=1:length(x)
       h(i,j)=(5000-0.005*(x(i)*x(i)+y(j)*y(j)+x(i)*y(j))+12.5*(x(i)+y(j)))*exp(-abs(0.000001*(x(i)*x(i)+y(j)*y(j))-0.0015*(x(i)+y(j))+0.7)); 
    end
end

xi=200;
yi=200;
h_start=(5000-0.005*(xi*xi+yi*yi+xi*yi)+12.5*(xi+yi))*exp(-abs(0.000001*(xi*xi+yi*yi)-0.0015*(xi+yi)+0.7)); 

xi=1400;
yi=1400;
h_end =(5000-0.005*(xi*xi+yi*yi+xi*yi)+12.5*(xi+yi))*exp(-abs(0.000001*(xi*xi+yi*yi)-0.0015*(xi+yi)+0.7)); 

contour(x,y,h,[h_start,10396.44998726596,h_end])

%contour(x,y,h,50)

