from django.shortcuts import render
from first.models import Category,Banner,Article,Tui,Tag,Link
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.


def index(request):
    all_category = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui_id=1)[:3]
    # 首页最新文章
    all_article = Article.objects.all().order_by('-id')[0:3]
    # 热门文章排行
    hot = Article.objects.all().order_by('-views')[:6]
    # 右侧热门推荐
    remen = Article.objects.filter(tui_id=2)[:6]
    tags = Tag.objects.all()
    link = Link.objects.all()

    return render(request,'index.html',locals())



# 列表页--点击分类
def list(request,lid):  #该lid是由url传递过来的
    list = Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)
    all_category = Category.objects.all()
    remen = Article.objects.filter(tui_id=2)[:5]  # 右侧热门推荐
    tags = Tag.objects.all()
    #~~~~~~~~ 分页  ~~~~~~~~
    page = request.GET.get("page")  #在url中获取当前页数
    paginator = Paginator(list,5)   #对list对象分页，设置超过5条数据就分页
    try:
        p_list = paginator.get_page(page)  #获取当前页码的记录
        print(p_list.number)
    except PageNotAnInteger:
        p_list = paginator.page(1)  #如果用户输入的页码不是整数时，显示第一页的内容
    except EmptyPage:
        p_list = paginator.page(paginator.num_pages)  #如果用户输入的页码不在该页码列表中，显示最后一页的内容

    return render(request,'list.html',locals())



# 内容页
def show(request,sid):
    show = Article.objects.get(id=sid)
    all_category = Category.objects.all()
    tags = Tag.objects.all()
    remen = Article.objects.filter(tui_id=2)[:5]
    like = Article.objects.all().order_by('?')[:5]    #内容下可能感兴趣的文章--随机推荐
    previous_blog = Article.objects.filter(created_time__lt=show.created_time,category_id=show.category_id).last()
    next_blog = Article.objects.filter(created_time__gt=show.created_time,category_id=show.category_id).first()
    show.views += 1
    show.save()

    return render(request,'show.html',locals())



def tags(request,tag):
    list = Article.objects.filter(tags__name=tag)
    remen = Article.objects.filter(tui_id=2)[:5]
    all_category = Category.objects.all()
    tname = Tag.objects.get(name=tag)
    #---- 分页-----
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list,5)
    try:
        list = paginator.get_page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request,'tags.html',locals())




def search(request):
    ss = request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)
    all_category = Category.objects.all()
    remen = Article.objects.filter(tui_id=2)[:5]
    tags = Tag.objects.all()
    # ------ 分页 -------
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request,'search.html',locals())



def about(request):
    all_category = Category.objects.all()

    return render(request,'about.html',locals())










