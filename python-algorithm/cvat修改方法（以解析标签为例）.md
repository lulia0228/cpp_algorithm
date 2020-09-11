### 条件

cvat正在运行中，docker启动了4个容器，其中一个叫cvat的容器是我们要修改的对象。

### 进入容器

```
docker exec -it cvat bash
```

### 修改labelme文件

```
vim cvat/apps/annotation/labelme.py
```

第94行改为:

```
ET.SubElement(obj_elem, 'attributes').text = '♥'.join(attrs)
```

第167行改为:

```
read = attributes_string.split("♥")
```

保存退出

### 重启容器

按住ctrl + p + q退出容器

重启容器:

```
docker stop cvat
docker start cvat
```

重新进入页面，进行验证。



### 永久保存文件

验证成功后，可提交容器覆盖原有镜像。