function g = discriminant(data, mu, sigma, p) %g is MxC matrix
    [r,~] = size(data);
    g = zeros(r,2);
    for m = 1:r
        for i = [1,2]
            alpha = log(p(i));
            tmp1=0;
            tmp2 = 0;
            for n = [1,2]
                tmp1 = tmp1 + log(sigma(i,n));
                tmp2 = tmp2 + ((data(m,n)-mu(i,n))^2)/(2*(sigma(i,n)^2));
            end
            g(m,i) = alpha - tmp1 - tmp2;
        end
    end


end

