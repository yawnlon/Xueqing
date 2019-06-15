Xueqing frontend

# install dependency
npm install

# develop
npm run dev

Build
# build for test environment
npm run build:stage

# build for production environment
npm run build:prod


Advanced
# preview the release environment effect
npm run preview

# preview the release environment effect + static resource analysis
npm run preview -- --report

# code format check
npm run lint

# code format check and auto fix
npm run lint -- --fix

# config
因为依赖库默认安装位置是 /home/proj/Xueqing/fronted 所以，自己克隆项目的时候，最好创建相同的目录，否则得吧 node_modules 文件夹删掉，重新安装，并删除两个配置文件 .babelrc 和 postcssrc.js


### 6.15

完成注册等6个页面初始化

其中一些js在下载下来失效，暂时未找到原因，页面还需要微调

赵正品重新整合前端文件
