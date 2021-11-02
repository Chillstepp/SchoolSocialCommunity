from django.shortcuts import render, redirect
from .models import Comment, User, Topic, Picturewall, Funding, Job, Group, GroupRealation, GroupMessage, GroupComment
from django.db import models
import json

# Create your views here.

def homepage(request):
    if "email" not in request.COOKIES:
        return redirect("login")
    if request.method == "POST":
        if 'del_topic_2' in request.POST:
            topic = Topic.objects.all()
            topic_newest_2 = topic.order_by('-time_created')[1]
            topic_newest_2.delete()
            return redirect("homepage")
        elif 'del_topic_1' in request.POST:
            topic = Topic.objects.all()
            topic_newest_1 = topic.order_by('-time_created')[0]
            topic_newest_1.delete()
            return redirect("homepage")
        elif 'del_topic_3' in request.POST:
            topic = Topic.objects.all()
            topic_newest_3 = topic.order_by('-time_created')[2]
            topic_newest_3.delete()
            return redirect("homepage")
        elif 'post_comment_1' in request.POST:
            now_user = User.objects.get(email=request.COOKIES.get("email")).name
            topic = Topic.objects.all()
            topic_newest = topic.order_by('-time_created')[0]
            content = request.POST.get("post_comment_text_1", None)
            Comment.objects.create(
                creator=now_user,
                topic=topic_newest.title,
                content=content,
                likes=0,
                is_vis=False
            )
            return redirect("homepage")
        elif 'post_comment_2' in request.POST:
            now_user = User.objects.get(email=request.COOKIES.get("email")).name
            topic = Topic.objects.all()
            topic_newest = topic.order_by('-time_created')[1]
            content = request.POST.get("post_comment_text_2", None)
            Comment.objects.create(
                creator=now_user,
                topic=topic_newest.title,
                content=content,
                likes=0,
                is_vis=False
            )
            return redirect("homepage")
        elif 'post_comment_3' in request.POST:
            now_user = User.objects.get(email=request.COOKIES.get("email")).name
            topic = Topic.objects.all()
            topic_newest = topic.order_by('-time_created')[2]
            content = request.POST.get("post_comment_text_3", None)
            Comment.objects.create(
                creator=now_user,
                topic=topic_newest.title,
                content=content,
                likes=0,
                is_vis=False
            )
            return redirect("homepage")
        else:
            img = request.FILES.get("topic_picture", None)
            content = request.POST.get("topic_content", None)
            context = {
                "img": img,
                "content": content
            }
            creator = json.loads(request.COOKIES.get("name"))
            Topic.objects.create(
                title=content,
                creator=creator,
                content=content,
                cover_picture=img,
                is_vis=False
            )
            return redirect("homepage")
    user = User.objects.all()
    topic = Topic.objects.all()
    comment = Comment.objects.all()
    topic_newest_1 = topic.order_by('-time_created')[0]
    topic_newest_2 = topic.order_by('-time_created')[1]
    topic_newest_3 = topic.order_by('-time_created')[2]
    creator_avatar_1 = User.objects.get(name=topic_newest_1.creator).avatar
    creator_avatar_2 = User.objects.get(name=topic_newest_2.creator).avatar
    creator_avatar_3 = User.objects.get(name=topic_newest_3.creator).avatar
    now_user = User.objects.get(email=request.COOKIES.get("email")).name
    now_avatar = User.objects.get(email=request.COOKIES.get("email")).avatar
    comment_list_1 = Comment.objects.filter(topic=topic_newest_1.title)
    comment_list_2 = Comment.objects.filter(topic=topic_newest_2.title)
    comment_list_3 = Comment.objects.filter(topic=topic_newest_3.title)
    comment_avatar_map = {}
    for comment in comment_list_1:
        comment_avatar_map.update({comment.creator: User.objects.get(name=comment.creator).avatar})
    for comment in comment_list_2:
        comment_avatar_map.update({comment.creator: User.objects.get(name=comment.creator).avatar})
    for comment in comment_list_3:
        comment_avatar_map.update({comment.creator: User.objects.get(name=comment.creator).avatar})
    user_1 = user[0]
    user_2 = user[1]
    user_3 = user[2]
    user_4 = user[3]
    context = {
        'now_user': now_user,
        'now_avatar': now_avatar,
        'user': user,
        'topic_newest_1': topic_newest_1,
        'topic_newest_2': topic_newest_2,
        'topic_newest_3': topic_newest_3,
        'creator_avatar_1': creator_avatar_1,
        'creator_avatar_2': creator_avatar_2,
        'creator_avatar_3': creator_avatar_3,
        'user_1': user_1,
        'user_2': user_2,
        'user_3': user_3,
        'user_4': user_4,
        'comment_list_1': comment_list_1,
        'comment_list_2': comment_list_2,
        'comment_list_3': comment_list_3,
        'comment_list_1_len': len(comment_list_1),
        'comment_list_2_len': len(comment_list_2),
        'comment_list_3_len': len(comment_list_3),
        'comment_avatar_map': comment_avatar_map
    }
    return render(request, 'homepage/index.html', context)


def signup(request):

    if request.method == "POST":
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        password_confirm = request.POST.get("password_confirm", None)

        User.objects.create(
            name=name,
            password=password,
            avatar="avatar/default.png",
            email=email,
            is_superuser=False
        )
        context = {
            "name": name,
            "password": password,
            "email": email,
        }

        return redirect("homepage")
    return render(request, 'signup/form-singup.html')

def login(request):
    context = {

    }
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        pw = User.objects.get(email=email).password
        namee = User.objects.get(email=email).name
        if pw == password:
            response = redirect("homepage")
            response.set_cookie("state", "client")
            response.set_cookie("email", email)
            #cookie中文处出现错码，先转json
            tran_name = json.dumps(namee)
            response.set_cookie("name", tran_name)
            return response
        else:
            return redirect("login")

    return render(request, 'login/form-login.html', context)

def album(request):
    if "email" not in request.COOKIES:
        return redirect("login")
    if request.method == "POST":
        img = request.FILES.get("upload_pic", None)
        Picturewall.objects.create(
            picture=img
        )
        return redirect("album")
    pic = Picturewall.objects.all()
    picture = pic.order_by('-time_created')
    now_avatar = User.objects.get(email=request.COOKIES.get("email")).avatar
    now_user = User.objects.get(email=request.COOKIES.get("email")).name
    context = {
        "picture": picture,
        "now_avatar": now_avatar,
        "now_user": now_user,
    }
    return render(request, "album/albums.html", context)

def timeline(request):
    if "email" not in request.COOKIES:
        return redirect("login")
    now_avatar = User.objects.get(email=request.COOKIES.get("email")).avatar
    now_user = User.objects.get(email=request.COOKIES.get("email")).name
    group_relation_all = GroupRealation.objects.all()
    group_all = Group.objects.all()
    user_group = group_relation_all.filter(user=now_user)
    group_info = [group_all.get(group_name=g.group_name) for g in user_group]
    group_num = len(group_info)
    context = {
        "now_user": now_user,
        "now_avatar": now_avatar,
        "group_info": group_info,
        "group_num": group_num,
    }
    return render(request, "timeline/timeline.html", context)

def calendar(request):
    if "email" not in request.COOKIES:
        return redirect("login")
    now_avatar = User.objects.get(email=request.COOKIES.get("email")).avatar
    now_user = User.objects.get(email=request.COOKIES.get("email")).name
    context = {
        "now_user": now_user,
        "now_avatar": now_avatar,
    }
    return render(request, "calendar/calendar.html", context)

def funding(request):
    if "email" not in request.COOKIES:
        return redirect("login")
    now_avatar = User.objects.get(email=request.COOKIES.get("email")).avatar
    now_user = User.objects.get(email=request.COOKIES.get("email")).name
    funding = Funding.objects.all()

    context = {
        "now_user": now_user,
        "now_avatar": now_avatar,
        "funding": funding
    }
    return render(request, "funding/funding.html", context)

def job(request):
    if "email" not in request.COOKIES:
        return redirect("login")
    if request.method == "POST":
        img = request.FILES.get("upload_pic", None)
        company_name = request.POST.get("company_name", None)
        gangwei = request.POST.get("gangwei", None)
        paymin = request.POST.get("paymin", None)
        paymax = request.POST.get("paymax", None)
        label = request.POST.get("label", None)
        where = request.POST.get("where", None)
        discription = request.POST.get("discription", None)
        herf = request.POST.get("herf", None)
        Job.objects.create(
            cover_pic=img,
            creator=company_name,
            title=gangwei,
            pay_min=paymin,
            pay_max=paymax,
            related_label=label,
            where=where,
            discription=discription,
            herf=herf
        )
        return redirect("job")
    now_avatar = User.objects.get(email=request.COOKIES.get("email")).avatar
    now_user = User.objects.get(email=request.COOKIES.get("email")).name
    job_list = Job.objects.all()
    job_list = job_list.order_by('-time_created')
    context = {
        "now_user": now_user,
        "now_avatar": now_avatar,
        "job_list": job_list,
    }
    return render(request, "job/job.html", context)

def group(request):
    if "email" not in request.COOKIES:
        return redirect("login")
    now_avatar = User.objects.get(email=request.COOKIES.get("email")).avatar
    now_user = User.objects.get(email=request.COOKIES.get("email")).name
    lecture_class = Group.objects.filter(is_lecture_group=True)
    lecture_class = lecture_class.order_by('-time_created')
    common_class = Group.objects.filter(is_lecture_group=False)
    common_class = common_class.order_by('-time_created')
    #create group
    for i in range(0, 5):
        if 'look_lecture_'+str(i) in request.POST:
            response = redirect("group_feed")
            tran_name = json.dumps(lecture_class[i].group_name)
            response.set_cookie("group_name", tran_name)
            return response
        elif 'join_lecture_'+str(i) in request.POST:
            response = redirect("group_feed")
            tran_name = json.dumps(lecture_class[i].group_name)
            response.set_cookie("group_name", tran_name)
            group_name = lecture_class[i].group_name
            if GroupRealation.objects.filter(group_name=group_name, user=now_user).count() == 0:
                GroupRealation.objects.create(
                    group_name=group_name,
                    user=now_user
                )
                #update group user number
                now_num = Group.objects.get(group_name=group_name).user_number
                group_obeject = Group.objects.get(group_name=group_name)
                group_obeject.user_number = now_num + 1
                group_obeject.is_active = True
                group_obeject.save()
            return response

    for i in range(0, 8):
        if 'look_class_'+str(i) in request.POST:
            response = redirect("group_feed")
            tran_name = json.dumps(common_class[i].group_name)
            response.set_cookie("group_name", tran_name)
            return response
        elif 'join_class_'+str(i) in request.POST:
            response = redirect("group_feed")
            tran_name = json.dumps(common_class[i].group_name)
            response.set_cookie("group_name", tran_name)
            group_name = common_class[i].group_name
            if GroupRealation.objects.filter(group_name=group_name, user=now_user).count() == 0:
                GroupRealation.objects.create(
                    group_name=group_name,
                    user=now_user
                )
                #update group user number
                now_num = Group.objects.get(group_name=group_name).user_number
                group_obeject = Group.objects.get(group_name=group_name)
                group_obeject.user_number = now_num + 1
                group_obeject.is_active=True
                group_obeject.save()
            return response

    if "publish" in request.POST:
        group_name = request.POST.get("group_name", None)
        is_lecture_group = request.POST.get("is_lecture_group", None)
        if is_lecture_group == "yes":
            is_lecture_group = True
        else:
            is_lecture_group = False
        about = request.POST.get("about", None)
        img = request.FILES.get("upload_pic", None)
        Group.objects.create(
            group_name=group_name,
            user_number=1,
            cover_picture=img,
            is_lecture_group=is_lecture_group,
            about=about,
            is_vis=True,
        )
        GroupRealation.objects.create(
            group_name=group_name,
            user=now_user
        )

    context = {
        "now_user": now_user,
        "now_avatar": now_avatar,
        "lecture_class": lecture_class,
        "common_class": common_class
    }
    return render(request, "group/group.html", context)

def group_feed(request):
    now_avatar = User.objects.get(email=request.COOKIES.get("email")).avatar
    now_user = User.objects.get(email=request.COOKIES.get("email")).name
    group_name = json.loads(request.COOKIES.get("group_name"))
    group_info = Group.objects.get(group_name=group_name)
    if "email" not in request.COOKIES:
        return redirect("login")
    if "publish_group_message" in request.POST:
        img = request.FILES.get("topic_picture", None)
        content = request.POST.get("topic_content", None)
        creator = now_user
        GroupMessage.objects.create(
            group_name=group_name,
            title=content,
            creator=creator,
            content=content,
            cover_picture=img,
            is_vis=True
        )
        return redirect("group_feed")
    group_message = GroupMessage.objects.filter(group_name=group_name)
    group_message = group_message.order_by('-time_created')
    message_avatar = [User.objects.get(name=message.creator).avatar for message in group_message]
    group_message_message_avatar = [[group_message[i], message_avatar[i]] for i in range(0, len(message_avatar))]
    group_user_list = GroupRealation.objects.filter(group_name=group_name)
    group_user_info_list = [User.objects.get(name=userr.user) for userr in group_user_list]
    context = {
        "now_user": now_user,
        "now_avatar": now_avatar,
        "group_name": group_name,
        "group_info": group_info,
        "group_message": group_message,
        "message_avatar": message_avatar,
        "group_message_message_avatar": group_message_message_avatar,
        "group_user_info_list": group_user_info_list,
    }
    return render(request, "group_feed/group_feed.html", context)

