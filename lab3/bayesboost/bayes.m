function [mu,sigma] = bayes(data)
[r,~] = size(data);
mu = zeros(2,2);
for i = [1,2]
    for n = [1,2]
        count = 0.0;
        sum = 0.0;
        for m = 1:r
            if data(m,3) == i-1
                count = count + 1;
                sum = sum + data(m,n);
            end
        end
        mu(i,n) = sum/count;
    end
end

sigma = zeros(2,2);
for i = [1,2]
    for n = [1,2]
        count = 0;
        sum = 0.0;
        for m = 1:r
            if data(m,3) == i-1
                count = count + 1;
                sum = sum + (data(m,n) - mu(i,n))^2;
            end
        end
        sigma(i,n) = sqrt(sum/count);
    end
end



end

