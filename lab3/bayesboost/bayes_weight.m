function [mu,sigma] = bayes_weight(data, w)
[r,~] = size(data);
mu = zeros(2,2);
for i = [1,2]
    for n = [1,2]
        weight = 0;
        sum = 0.0;
        for m = 1:r
            if data(m,3) == i-1
                weight = weight + w(m);
                sum = sum + data(m,n) * w(m);
            end
        end
        mu(i,n) = sum/weight;
    end
end

sigma = zeros(2,2);
for i = [1,2]
    for n = [1,2]
        weight = 0;
        sum = 0.0;
        for m = 1:r
            if data(m,3) == i-1
                weight = weight + w(m);
                sum = sum + w(m)*((data(m,n) - mu(i,n))^2);
            end
        end
        sigma(i,n) = sqrt(sum/weight);
    end
end



end

