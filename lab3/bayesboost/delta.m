function d = delta(mu, sigma, p, m)
    g = discriminant(m(1:2), mu, sigma, p);
    [~, class] = max(g, [], 2);
    class = class - 1;
    d = class == m(:,end);
end

