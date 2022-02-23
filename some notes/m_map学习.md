## 地理图(MATLAB的M_MAP库)

官网https://www.eoas.ubc.ca/~rich/map.html

欲画昨天的图(时间... )

发现了M_MAP库, 过了一遍相应的内容, 现在能画的地理方面的图(学习了已有的example code)

- 直接画个球

  ![image-20220109202752348](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220109202752348.png)

  但是用到的地方应该不多

  m_proj的时候选择ortho , coast选择patch

  后面提及的所有代码都是example code , 用来备忘

  ```matlab
  m_proj('ortho','lat',48','long',-123');
  m_coast('patch','r');
  m_grid('linest','-','xticklabels',[],'yticklabels',[]);
  
  patch(.55*[-1 1 1 -1],.25*[-1 -1 1 1]-.55,'w'); 
  text(0,-.55,'M\_Map','fontsize',25,'color','b',...
      'verticalalignment','middle','horizontalalignment','center');
  ```

- 等高线图/地形图

  ![image-20220109203013816](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220109203013816.png)

  m_elev函数用来画等高线, 颜色可以通过换colormap解决, flipud函数是将一个矩阵行元素上下颠倒, 经测试没太大区别, 暂不知道作者flipud的用意.

  ```matlab
  m_proj('lambert','long',[-160 -40],'lat',[30 80]);
  m_coast('patch',[1 .85 .7]);
  m_elev('contourf',[500:500:6000]);
  m_grid('box','fancy','tickdir','in');
  colormap(flipud(copper));
  ```

- 水中的等高线

  ![image-20220109203435525](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220109203435525.png)

  这个就是和上面的m_elev中的level不同以及, m_proj选择stereographic

  代码略

- 不知道有什么用的错位图

  ![image-20220109203616012](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220109203616012.png)

  .... 不知道这种图干嘛的.... 但是代码还是过了一下, subplot两个子图, 然后每个子图其实包含六个部分, 循环一下

- **风向/洋流/有标注的等高线图**

  ![image-20220109203804054](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220109203804054.png)

  虽然代码很长, 但是还是贴一手, 觉得很重要

  与直接画图相同 , 用的是quiver函数, 但是是在地图之上, 所以是m_quiver函数, 用法区别不大. 换颜色啥的用set 配合句柄换.

  等高线也是和contour, 地图上就是m_contour, 然后在地图上标注数据使用clabel, 用法

  ```matlab
  [cs,h]=m_contour(lon,lat,sqrt(u.*u+v.*v));
  clabel(cs,h,'fontsize',8);
  ```

  类似于句柄? 或者这个应该也叫句柄

  ```matlab
  [lon,lat]=meshgrid([-136:2:-114],[36:2:54]);
  u=sin(lat/6);
  v=sin(lon/6);
  
  m_proj('oblique','lat',[56 30],'lon',[-132 -120],'aspect',.8);
  subplot(121);
  m_coast('patch',[.9 .9 .9],'edgecolor','none');
  m_grid('tickdir','out','yaxislocation','right',...
              'xaxislocation','top','xlabeldir','end','ticklen',.02);
  hold on;
  m_quiver(lon,lat,u,v);
  xlabel('Simulated surface winds');
  subplot(122);
  m_coast('patch',[.9 .9 .9],'edgecolor','none');
  m_grid('tickdir','out','yticklabels',[],...
                'xticklabels',[],'linestyle','none','ticklen',.02);
  hold on;
  [cs,h]=m_contour(lon,lat,sqrt(u.*u+v.*v));
  clabel(cs,h,'fontsize',8);
  xlabel('Simulated something else');
  ```

- 地图上画曲线, 点, 气泡

  ![image-20220109204443415](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220109204443415.png)

  画曲线就是用m_line , 用法类似于plot, 事实上两者的介绍都是一样的

  ![image-20220109204617605](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220109204617605.png)

  ```matlab
  % Plot a circular orbit
  lon=[-180:180];
  lat=atan(tan(60*pi/180)*cos((lon-30)*pi/180))*180/pi;
  m_proj('miller','lat',82);
  m_coast('color',[0 .6 0]);
  m_line(lon,lat,'linewi',3,'color','r');
  m_grid('linestyle','none','box','fancy','tickdir','out');
  m_northarrow(-150,0,40,'type',4,'linewi',.5);
  ```

  m_track画轨迹, m_streamline一般也是画线, m_pcolor画热力图

- 还有一些更长的组合使用没有看完, 但是本质是在map上进行正常的作画...

- 个人觉得两个缺点

  - 图有点丑

    ![image-20220109205012203](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220109205012203.png)

    就.... 看起来不

### code7

重新看了7的代码,然后打算学习一下函数用法

```matlab
m_proj('lambert','lon',[-10,20],'lat',[33 48]);
[CS,CH] = m_etopo2('contourf',[-5000:500:0 250:250:3000],'edgecolor','none');
% 问题, contourf用法, 如上的矩阵拼接结果如何?
m_grid('linestyle','none','tickdir','out','linewidth',3);
% 问题, tickdir的out/in/both的区别
colormap([m_colmap('blues',80);m_colmap('gland',48)]);
brighten(.5);
ax=m_contbar(1,[.5 .8],CS,CH);
title(ax,{'Level/m',''});
% 问题, title函数怎么用
```

contourf用法

![image-20220110114739310](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220110114739310.png)



[-5000:500:0 250:250:3000] 拼接出来就是正常的一个行向量



tickdir的用法

![image-20220110115210928](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220110115210928.png)

区别很大吗, 看了一遍感觉没啥区别

### code10

```matlab
 	m_proj('UTM','long',[-72 -68],'lat',[40 44]);
    m_gshhs_i('color','k');
    m_grid('box','fancy','tickdir','in');
    m_ruler(1.2,[.5 .8]);
    
    % fake up a trackline
    lons=[-71:.1:-67];
    lats=60*cos((lons+115)*pi/180);
    dates=datenum(1997,10,23,15,1:41,zeros(1,41));

    m_track(lons,lats,dates,'ticks',0,'times',4,'dates',8,...
           'clip','off','color','r','orient','upright');
    
    m_northarrow(-68.5,43.4,.4,'type',2);
```

m_grid中的box属性有  'box',( 'on' | 'fancy' | 'off' )

经验证box就是这个框框 , 分别对应fancy,on,off

![image-20220110120426482](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220110120426482.png)

### code11

```matlab
m_proj('hammer','clong',170);
m_grid('xtick',[],'ytick',[],'linestyle','-');
m_coast('patch','g');
m_line(100.5,13.5,'marker','square','color','r');
m_range_ring(100.5,13.5,[1000:1000:15000],'color','b','linewi',2);
xlabel('1000km range rings from Bangkok');
```

此处的xtick, ytick取消了坐标轴

m_coast的g是什么?, m_coast里的patch参数和标准库中的patch参数是相同的

是颜色green.

### code12

```matlab
	bndry_lon=[-128.8 -128.8 -128.3 -128 -126.8 -126.6 -128.8];
    bndry_lat=[49      50.33  50.33  50   49.5   49     49];
    
    clf;
    m_proj('lambert','long',[-130 -121.5],'lat',[47 51.5],'rectbox','on');

    m_gshhs_i('color','k');              % Coastline...
    m_gshhs_i('speckle','color','k');    % with speckle added

    m_line(bndry_lon,bndry_lat,'linewi',2,'color','k');     % Area outline ...
    m_hatch(bndry_lon,bndry_lat,'single',30,5,'color','k'); % ...with hatching added.

    m_grid('linewi',2,'linest','none','tickdir','out','fontsize',12);
    title({'Speckled Boundaries','for nice B&W presentation','(best in postscript format)'});
    m_text(-128,48,{'Pacific','Ocean'},'fontsize',18);
    
    m_northarrow(-122.5,50.2,.8,'type',3,'linewi',2);    
```

m_proj中的rectbox: on为将整个图的变成一个矩形, 忽略地球的球形, 但是并不会让坐标格子变成正方形

这里的m_hatch就是打阴影, 效果如右所示

![image-20220110122104154](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220110122104154.png)

### code13

```matlab
	m_proj('miller','lat',[-77 77]);   
    m_coast('patch',[.7 1 .7],'edgecolor','none'); 
    m_grid('box','fancy','linestyle','-','gridcolor','w','backcolor',[.2 .65 1]);
    
    cities={'Cairo','Washington','Buenos Aires'}; 
    lons=[ 30+2/60  -77-2/60   -58-22/60];
    lats=[ 31+21/60  38+53/60  -34-45/60]; 
    for k=1:3
      [range,ln,lt]=m_lldist([-123-6/60 lons(k)],[49+13/60  lats(k)],40); 
      m_line(ln,lt,'color','r','linewi',2); 
      m_text(ln(end),lt(end),sprintf('%s - %d km',cities{k},round(range)));
    end;
    title('Great Circle Routes','fontsize',14,'fontweight','bold');
    
    set(gcf,'color','w');   % Need to do this otherwise 'print' turns the lakes black
```

backcolor是什么? 是背景颜色, 整张图的背景颜色,也就是后面的蓝色.

m_lldist是什么,  计算两个坐标之间的球形距离.

最后的set(gcf, 'color', 'w'); 是什么, 在本地跑时没有特别的影响.

此处的m_text使用了格式化字符串输出

### code14

colormap的使用 , 虽然我觉得自己以后也不会用到,

caxis怎么用? 

axis是设置坐标轴的范围和纵横比, caxis则是设置当前坐标去的颜色图范围.

> `caxis(limits)` 设置当前坐标区的颜色图范围。`limits` 是 `[cmin cmax]` 形式的二元素向量。[颜色图索引数组](https://www.mathworks.com/help/releases/R2020b/matlab/ref/caxis.html#mw_262386a0-0173-40a5-b123-7b5834c1d396)中小于或等于 `cmin` 的所有值映射到颜色图的第一行。大于或等于 `cmax`的所有值映射到颜色图的最后一行。介于 `cmin` 和 `cmax` 之间的所有值以线性方式映射到颜色图的中间各行。

m_elev的image参数和其他等等参数

>  OPTN: 'contour' -  contour lines are drawn.
>              'contourf' -  filled contours are drawn. 
>                               LEVELS are the levels used, and ARGS
>                               are optional patch arguments of line types, 
>                               colors, etc. 
>              'pcolor'    - pcolor call
>              'image'     - displays pixellated image
>              'shadedrelief' - shaded relief map.

有这么些参数, 但是呢, 并不能直接顾名思义.

>figure(2)
>m_elev('image')
>figure(3)
>m_elev('contour')
>figure(4)
>m_elev('contourf')
>figure(5)
>m_elev('pcolor')
>figure(6)
>m_elev('shadedrelief')

![image-20220110151659035](C:/Users/86176/Desktop/2022年1月10日的美赛学习/image-20220110151659035.png)

作者主要是秀了一波自己的这个projection, 专门为大洋设置.

```matlab
    %  This projection shows all the oceans connected to each other - the outside ring
    %  is the Asian coastline (Thanks to M B-O for this idea)
    % otherwise its just an example of different map types.
    
     m_proj('azimuthal equal-area','radius',156,'lat',-46,'long',-95,'rot',30);

     ax1=subplot(2,2,1,'align');
      m_coast('patch','r');
      m_grid('xticklabel',[],'yticklabel',[],'linestyle','-','ytick',[-60:30:60]);
        
     ax2=subplot(2,2,2,'align');
      m_elev('contourf',[-7000:1000:0 500:500:3000],'edgecolor','none');
      colormap(ax2,[m_colmap('blues',70);m_colmap('gland',30)]);  
      caxis(ax2,[-7000 3000]);       
      m_grid('xticklabel',[],'yticklabel',[],'linestyle','-','ytick',[-60:30:60]);

        
     ax3=subplot(2,2,3,'align');
      colormap(ax3,[m_colmap('blues',70);m_colmap('gland',30)]);  
      caxis(ax3,[-7000 3000]);       
      m_elev('image');
      m_grid('xticklabel',[],'yticklabel',[],'linestyle','-','ytick',[-60:30:60]);

        
     ax4=subplot(2,2,4,'align');
      colormap(ax4,[m_colmap('blues')]);  
      caxis(ax4,[-8000 000]);       
      m_elev('shadedrelief','gradient',.5);
      m_coast('patch',[.7 .7 .7],'edgecolor','none');
      m_grid('xticklabel',[],'yticklabel',[],'linestyle','-','ytick',[-60:30:60]);

     ha = axes('Position',[0 0 1 1],'Xlim',[0 1],'Ylim',[0  1],'Box','off',...
               'Visible','off','Units','normalized', 'clipping' , 'off');
      text(0.5, 0.98,'This projection shows all oceans connected to each other',...
               'horiz','center','fontsize',20);

```

### code15

```matlab
 
    % get delta-SA data from the TEOS-10 gsw atlas at 2500 dbar

    [LG,LT]=meshgrid(0:360,-86:89);
    dSA=ones(size(LG));
    dSA(:)=gsw_deltaSA_atlas(3000*dSA(:),LG(:),LT(:));


    % Rearrange data to lie in the longitude limits I give for the
    % projection

    ind=[31:361 1:30]; % Move left side to right
    dSA=dSA(:,ind);
    LT=LT(:,ind);
    LG=LG(:,ind);LG(LG>30)=LG(LG>30)-360; %...and subtract 360 to some longitudes

    clf;
    m_proj('robinson','lon',[-330 30]);

    m_pcolor(LG,LT,dSA*1000);

    m_coast('patch',[.7 .7 .7],'edgecolor','none');
    m_grid('tickdir','out','linewi',2);

    % This is a perceptually uniform jet-like color scale, but in m_colmap
    % we can add some simple graduated steps to make the pcolor look a little
    % more like a contourf
    colormap(m_colmap('jet','step',10));

    h=colorbar('northoutside');
    title(h,'\deltaSA/(g/kg) at 2000 dbar','fontsize',14);
    set(h,'pos',get(h,'pos')+[.2 .05 -.4 0],'tickdir','out')

    set(gcf,'color','w');   % Need to do this otherwise 'print' turns the lakes black
```

emmmm, 没看懂上面的数据处理, 但是函数都认识, 暂且跳过

### code 16

没有数据集,

### code17

```matlab
m_proj('lambert','lat',[5 24],'long',[105 125]);

set(gcf,'color','w')   % Set background colour before m_image call

caxis([-6000 0]);
colormap(flipud([flipud(m_colmap('blues',10));m_colmap('jet',118)]));
m_etopo2('shadedrelief','gradient',3);
 
m_gshhs_i('patch',[.8 .8 .8]);
 
m_grid('box','fancy');

ax=m_contfbar(.97,[.5 .9],[-6000 0],[-6000:100:000],'edgecolor','none','endpiece','no');
xlabel(ax,'meters','color','k');
```

没啥特别的

### code18

```matlab
m_proj('utm','ellipse','grs80','zone',10,'lat',[49+15.7/60 49+21/60],...
        'long',[-123-15/60 -123-3/60]);      

% Uses multibeam bathymetry with 10m horizontal resolution
% Already regularly gridded in UTM coords with vector x2/y2, and
% matrix Z2.
caxis([-150 0]);
colormap([m_colmap('water',128)]);
m_shadedrelief(x2,y2,-Z2,'lightangle',-45,'gradient',8,'coord','z');

% Add some contours
hold on;

[cs,h]=contour(x2,y2,Z2,[0:20:150],'color','k');
clabel(cs,h,'fontsize',6);
hold off;

% Land parts from a previously saved high-resolution coastline
col=[255 214 140]/255; % CHS chart land colour

m_usercoast('/ocean/rich/more/mmapbase/bcgeo/PNW.mat','patch',col);
m_usercoast('/ocean/rich/more/mmapbase/bcgeo/PNWrivers.mat','patch',col);

% Lat/long AND a UTM grid
 
m_grid('tickdir','out','fontsize',12,'linest','none','xaxisloc','top','yaxisloc','right');
m_utmgrid('xcolor','b','ycolor','b','linest','-'); 

m_ruler([.5 .8],.9,'tickdir','out','ticklen',[.007 .007]);
m_northarrow(-123-4.5/60,49+19.5/60,1/60,'type',4,'aspect',1.5);

xlabel('Vancouver Harbour','color','k'); 
```

后面的代码...... 不想看了...... m_map学很久了, 看点别的....

### 画行政版图

m_map不支持 , matlab 好像有mapping tools, 但是暂时还没有找到方法画 ,文档太少, 先埋个坑

