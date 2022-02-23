nl = 80 ;% 车道长度（偶数）
nc = 2; % nc:双向车道数目
dt= 0.01; % 仿真步长时间
fp = 20; % 车道入口处新进入车辆的概率（列向量）
nt=10000;% 仿真步长数目
chance=0.5;
chance1=0.5;
[ v, d, p ] = multi_driveway_with_crossroad_exit ( nl,nc,dt,fp,nt,chance,chance1);