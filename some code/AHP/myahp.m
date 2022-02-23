A = %判断矩阵
[n, n] = size(A);
[V, D] = eig(A); %求得特征向量和特征值
%求出最大特征值和它所对应的特征向量
temp = diag(A);
[n, index] = max(temp)
pos = index

w = abs(V(:, pos));
w = w / sum(w);
t = D(pos, pos);
disp('准则层特征向量w='); disp(w); disp('准则层最大特征根t='); disp(t);
%以下是一致性检验
CI = (t - n) / (n - 1); RI = [0 0 0.52 0.89 1.12 1.26 1.36 1.41 1.46 1.49 1.52 1.54 1.56 1.58 1.59 1.60 1.61 1.615 1.62 1.63];
CR = CI / RI(n);

if CR < 0.10
    disp('此矩阵的一致性可以接受!');
    disp('CI='); disp(CI);
    disp('CR='); disp(CR);
else disp('此矩阵的一致性验证失败，请重新进行评分!');
end
