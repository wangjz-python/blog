from django.urls import path,re_path
from first import views
from django.conf import settings
from django.views.static import serve


app_name = 'first'    # 视图函数命名空间，说明这个 urls.py 模块属于 blog（这个是first） 应用

urlpatterns = [
    path('',views.index,name='index'),      # 首页
    path('list<int:lid>.html',views.list,name='list'),   # 列表页
    path('show<int:sid>.html',views.show,name='show'),   # 内容页
    path('tag/<str:tag>',views.tags,name='tags'),  # 标签页
    path('s/',views.search,name='search'),  #  搜索 列表页
    path('about/',views.about,name='about'),#  关于博主页

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # 此行代码是能使<img src="/media/booktest/jobs.png" width="100px">能在客户端页面上显示的关键所在
]