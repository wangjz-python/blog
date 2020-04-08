from django.db import models

from django.contrib.auth.models import User

from DjangoUeditor.models import UEditorField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='文章分类')
    index = models.IntegerField(default=999,verbose_name='分类排序')

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100,verbose_name='文章标签')

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tui(models.Model):
    name = models.CharField(max_length=100,verbose_name='推荐位')

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    excerpt = models.TextField(max_length=200,blank=True,verbose_name='摘要')
    # 一对多
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,
                                 verbose_name='分类',blank=True,null=True)
    # 多对多
    tags = models.ManyToManyField(Tag,verbose_name='标签',blank=True)
                            # upload_to  指定文件存放前缀路径
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/',verbose_name='文章图片',blank=True,null=True)
    # 使用DjangoUedtor----可以使用富文本编辑器添加内容
    body = UEditorField(width=800,height=500,toolbars='full',imagePath='upimg/',filePath='upfile',
                        upload_settings={"imageMaxSize":1204000},settings={},command=None,
                        blank=True,verbose_name='内容')
    # 一对多
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
                   # 正整数
    views = models.PositiveIntegerField(default=0,verbose_name='阅读量')
    tui = models.ForeignKey(Tui,on_delete=models.DO_NOTHING,verbose_name='推荐位',blank=True,null=True)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='发布日期')
    modified_time = models.DateTimeField(auto_now=True,verbose_name='修改日期')

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Banner(models.Model):
    text_info = models.CharField(max_length=50,default='',verbose_name='标题')
    img = models.ImageField(upload_to='banner/',verbose_name='幻灯片')
    link_url = models.URLField(max_length=100,verbose_name='图片链接')
    is_active = models.BooleanField(default=False,verbose_name='是否是active')

    class Meta:
        verbose_name = '幻灯片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text_info


class Link(models.Model):
    name = models.CharField(max_length=20,verbose_name='链接名称')
    linkurl = models.URLField(max_length=100,verbose_name='网址')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



