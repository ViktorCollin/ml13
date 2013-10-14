function c = adaboost_discriminant(data, mu, sigma, p, alpha, classes, T)
[M, ~] = size(data);
c = zeros(M,1);

for m = 1:M
    tmp = zeros(2,1);
    for class = classes
        for t = 1:T
            tmp(class+1,1) = tmp(class+1,1) + alpha(1,t)*delta(mu(:,:,t), sigma(:,:,t), p(:,t), [data(m,1:2), class]);
        end
    end
    if tmp(1,1) > tmp(2,1)
        c(m,1) = 0;
    else
        c(m,1) = 1;
    end
   
end
end

