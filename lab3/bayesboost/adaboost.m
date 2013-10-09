function [mu, sigma, p, alpha, classes] = adaboost(data, T)
[M, ~] = size(data);
mu = zeros(2,2,T);
sigma = zeros(2,2,T);
p = zeros(2,T);
alpha = zeros(1,T);
w = zeros(M,T);
w(1:M,1) = 1/M;
err = zeros(1,T);
classes = [0,1];
for t = 1:T
    [mu(:,:,t), sigma(:,:,t)] = bayes_weight(data,w(:,t));
    p(:,t) = prior(data, w(:,t));
    tmp = 0;
    for m = 1:M
        tmp = tmp + w(m,t)*delta(mu(:,:,t), sigma(:,:,t), p(:,t), data(m,:));
    end
    err(1,t) = 1 - tmp;
    alpha(1,t) = 0.5*log((1-err(1,t))/err(1,t));
    if t ~= T
        for m = 1:M
            if delta(mu(:,:,t), sigma(:,:,t), p(:,t), data(m,:)) == 1
                w(m,t+1) = w(m,t) * exp(-alpha(1,t));
            else
                w(m,t+1) = w(m,t) * exp(alpha(1,t));
            end
        end
        w(:,t+1) = w(:,t+1)/sum(w(:,t+1));
    end
end
end

