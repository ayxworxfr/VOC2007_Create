# 制作VOC2007数据集

1. 使用格式工厂或其他工具格式化自己的图片为jpg格式，大小为640X480

2. 将自己的图片保存到".\VOC2007\JPEGImages"目录下

3. 运行以下代码将图片名称规格化

   ```
   python rename.py
   ```

   

4. 使用[labellImg](https://github.com/tzutalin/labelImg)工具生成xml文件到".\VOC2007\Annotations"目录下

   | labellImg工具快捷键 |                功能                 |
   | :-----------------: | :---------------------------------: |
   |       Ctrl+R        |      修改默认的XML文件保存位置      |
   |      Ctrl + s       |                保存                 |
   |      Ctrl + d       | Copy the current label and rect box |
   |        Space        |         标记当前图片已标记          |
   |          w          |            创建一个矩形             |
   |          d          |             下一张图片              |
   |          a          |             上一张图片              |

5. 运行以下代码生成txt文件

```
python text.py
```


