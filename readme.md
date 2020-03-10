## 效果和动机

效果如下图

![image-20200309224213815](C:\Users\78372\AppData\Roaming\Typora\typora-user-images\image-20200309224213815.png)

主要参考慕课网 "TensorFlow与Flask结合打造手写体数字识别"课程（免费的课，虽然老师只敲代码，但是这个前端我感觉挺厉害的，渣渣的我不会js啊）

> https://www.imooc.com/learn/994

不过课程上线时间已经过长，原课程使用tf1.x。我根据课程介绍，使用tf2来实现了一套，前端还是使用原课程中的，重新写了Web服务以及训练代码

## 项目架构

web框架：flask：提供web服务

深度学习框架：TensorFlow 训练模型，导出模型

模型部署：docker&TensorFlow serving 模型对外提供服务

## 环境

docker：本项目需要docker 也就需要一些基本的docker知识

python3.6+:使用下面的命令就可以快速安装所需要的环境，由于tensorflow依赖过多，建议使用anaconda来进行管理

~~~shell
pip install -r requirement.txt 
~~~



## 运行

项目中已经保存好了训练好的模型，分别：是根据LeNet网络结构进行训练的模型（准确率大约在93%附近）以及使用普通的softmax的线性回归（使用Relu激活函数）

直接将本项目clone到本地后就可以使用docker发布模型，然后运行flask就可以使用浏览器进行访问了。

这一步你可以训练自己的模型，修改一下路径就好了。（可以提高精准度）

如果你是docker新手，看不懂参数，直接修改一下中文路径就好了，docker会自动运行的，如果报错了，就多搜索一下吧。

~~~shell
docker pull tensorflow/serving # 这一句不加也行，没有镜像也会自动去docker.io拉取
docker run --rm -d -p 18502:8501 -v "这里修改成你的项目绝对路径/train/lrmodel:/models/lenet" -e MODEL_NAME=lenet tensorflow/serving
docker run --rm -d -p 18501:8501 -v "这里修改成你的项目绝对路径/train/mymodel:/models/lenet" -e MODEL_NAME=lenet tensorflow/serving
~~~

解释一下这里：因为docker需要绝对距离进行数据卷挂载，所以这里需要手动修改，这里偷懒了一下，发布模型的时候都叫了lenet，运行镜像的时候忘了改了。^~^

运行好docker之后，推荐运行一下代码检查模型是否正确发布

~~~shell
 curl http://localhost:18501/v1/models/lenet/metadata # 返回StatusCode: 200就行了
~~~



这时候只需要启动flask就大功告成了

~~~shell
cd 你的项目路径
python app.py 
~~~

~~~shell
 # 如果出现这个就大功告成了
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 232-107-356
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
~~~



使用浏览器访问 http:localhost:8000 就可以进行愉快的玩耍了

## 改进（TODO）

目前项目中flask只是提供了web服务，因为我不会改js中的代码，所以这还是沿袭了课程中的内容，可以更新成nginx+html页面的方式，这样的话，架构就成了nginx+docker+tensorflow的架构了，这样就没有flask了，可能会更好一些