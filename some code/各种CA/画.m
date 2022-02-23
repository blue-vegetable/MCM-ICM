Map = [1 1 1; 0 0 0];
colormap(Map);
% 设置网格大小
S = 121;
L = zeros(S);
% 把中间一个数设置为 1 作为元胞种子
M = (S+1)/2;
L(M, M) = 1;
Temp = L;
imagesc(L);
% 计算层数
Layer = (S-1)/2 + 1;

for t=2:Layer
    for x=M-t+1:M+t-1
       if x==M-t+1 || x==M+t-1

          for y=M-t+1:M+t-1
            SUM = 0;
            for m=-1:1
               for n=-1:1
                  if x+m>0 && x+m<=S && y+n>0 && y+n<=S
                     SUM = SUM + L(x+m, y+n); 
                  end
               end
            end
            SUM = SUM - L(x, y);
            Temp(x, y) = mod(SUM, 2);
          end
          
       else
            y = M-t+1;
            SUM = 0;
            for m=-1:1
               for n=-1:1
                  if x+m>0 && x+m<=S && y+n>0 && y+n<=S
                     SUM = SUM + L(x+m, y+n); 
                  end
               end
            end
            SUM = SUM - L(x, y);
            Temp(x, y) = mod(SUM, 2);
            
            y = M+t-1;
            SUM = 0;
            for m=-1:1
               for n=-1:1
                  if x+m>0 && x+m<=S && y+n>0 && y+n<=S
                     SUM = SUM + L(x+m, y+n); 
                  end
               end
            end
            SUM = SUM - L(x, y);
            Temp(x, y) = mod(SUM, 2);
       end
    end
    L = Temp;
    imagesc(L);
    % 速度控制
    pause(0.2);
end