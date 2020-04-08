import xadmin
from first.models import Banner,Category,Tag,Tui,Article,Link


class ArticleAdmin(object):
    list_display = ['id','category','title','tui','user','views','created_time']
    list_per_page = 50
    style_fields = {'body':'ueditor'}   # 富文本编辑器
    list_editable = []
    list_filter = []

class BannerAdmin(object):
    list_display = ['id','text_info','img','link_url','is_active']

class CategoryAdmin(object):
    list_display = ['id','name','index']
    list_editable = ['name','index']

class TagAdmin(object):
    list_display = ['id','name']

class TuiAdmin(object):
    list_display = ['id','name']

class LinkAdmin(object):
    list_display = ['id','name','linkurl']


xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Tui,TuiAdmin)
xadmin.site.register(Link,LinkAdmin)
