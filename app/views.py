from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "TSUBOKURS SHUHEI WEB DESIGNER"
        return ctxt


class AboutView(TemplateView):
    template_name = "design.html"

    # def get_context_data(self):
    #     ctxt = super().get_context_data()
    #     ctxt["skills"] = [
    #         "Python",
    #         "C++",
    #         "Javascript",
    #         "Rust",
    #         "Ruby",
    #         "PHP"
    #     ]
    #     ctxt["num_services"] = 1234567
    #     return ctxt

class WorkView(TemplateView):
    template_name = "work.html"

class BusinessView(TemplateView):
    template_name = "business.html"

class Business_serviceView(TemplateView):
    template_name = "business_service.html"

class Business_newsView(TemplateView):
    template_name = "business_news.html"

class Business_magazineView(TemplateView):
    template_name = "business_magazine.html"

class ProfileView(TemplateView):
    template_name = "profile.html"

# def main(request):
#     params = {
#         'msg':'安芸大学',
#         'name':'安芸大学',
#         'link':'http://limeokapi95.sakura.ne.jp/work/academy',
#         'image01':'work/image01.png',
#     }
#     return render(request, 'main.html', params)

def work_page1(request):
    params = {
        'name':'安芸大学',
        'msg':'Planning / Design / HTML,CSS,JavaScript /',
        'link':'http://limeokapi95.sakura.ne.jp/work/academy',
        'info':'安芸大学は、国際交流や経済活動を中心に学ぶことのできる大学です。広い世界観を意識した空間とシンプルな作りのWEBサイトにさせていただきました。ロゴは、地球と人々の繋がりを意識して作成させていただきました。',
        'image_sp':'work/sp/image_sp_01.png',
        'image01':'work/page01/image01.png',
        'image02':'work/page01/image02.jpg',
        'image03':'work/page01/image03.jpg',
        'image04':'work/page01/image04.jpg',
    }
    return render(request, 'main.html', params)

def work_page2(request):
    params = {
        'name':'ふじさき歯科医院',
        'msg':'Planning / Design / HTML,CSS,JavaScript /',
        'link':'http://limeokapi95.sakura.ne.jp/work/dental_clinic',
        'info':'緑色の蛍光色を取り入れた"ふじさき歯科医院"のWEBサイトは、清潔感とナチュラルなイメージを意識して制作させて頂きました。丸みのあるコンテンツにすることで柔らかさを表現しています。安心感を持って受診して頂けるように意識しました。',
        'image_sp':'work/sp/image_sp_02.png',
        'image01':'work/page02/image01.png',
        'image02':'work/page02/image02.jpg',
        'image03':'work/page02/image03.jpg',
        'image04':'work/page02/image04.jpg',
    }
    return render(request, 'main.html', params)

def work_page3(request):
    params = {
        'name':'日光・鬼怒川週末フリーデー',
        'msg':'Design / HTML,CSS,JavaScript /',
        'link':'http://limeokapi95.sakura.ne.jp/work/nikko_freeday2022',
        'info':'日光・鬼怒川のスポットをモチーフにしたイラストを多く取り入れて、お出かけをしたくなるイメージで制作させていただきました。フォントサイズを大きくすることで視認性と協調性を高めています。また、開催期間が2月と言うこともあり寒さを連想させないオレンジ色をベースに暖かい気持ちでお出かけしていただきたいと思いを込めております。',
        'image_sp':'work/sp/image_sp_03.png',
        'image01':'work/page03/image01.png',
        'image02':'work/page03/image02.jpg',
        'image03':'work/page03/image03.jpg',
        'image04':'work/page03/image04.jpg',
    }
    return render(request, 'main.html', params)

def work_page4(request):
    params = {
        'name':'ポイント倍増キャンペーン',
        'msg':'Design / HTML,CSS,JavaScript /',
        'link':'http://limeokapi95.sakura.ne.jp/work/noritoku2022',
        'info':'WEBサイト内に傾斜のあるラインを取り入れて、スピード感あるサイトに仕上げています。閲覧いただいたユーザーの方に早めの購買意識を持たせています。お得感を表現するためにフォントを大きめに調整し、ボタンのサイズも大きくしています。',
        'image_sp':'work/sp/image_sp_04.png',
        'image01':'work/page04/image01.png',
        'image02':'work/page04/image02.jpg',
        'image03':'work/page04/image03.jpg',
        'image04':'work/page04/image04.jpg',
    }
    return render(request, 'main.html', params)


def work_page5(request):
    params = {
        'name':'野岩鉄道株式会社',
        'msg':'Planning / Design / HTML,CSS,JavaScript /',
        'link':'http://limeokapi95.sakura.ne.jp/work/yagan',
        'info':'野岩鉄道株式会社は、福島・栃木両県ならびに関係地方団体、民間企業の合資により運営されています。沿線は過疎化現象傾向にあり、観光客を中心に利用されています。観光でご利用いただくユーザーの方に自然を満喫いただきたと思いを込めて、自然と空間をモチーフに、濃い緑色をアクセントに使用しています。また、フォトギャラリー等の写真を取り入れることで野岩鉄道の魅力をアピールしています。',
        'image_sp':'work/sp/image_sp_05.png',
        'image01':'work/page05/image01.png',
        'image02':'work/page05/image02.jpg',
        'image03':'work/page05/image03.jpg',
        'image04':'work/page05/image04.jpg',
    }
    return render(request, 'main.html', params)


def work_page6(request):
    params = {
        'name':'MENS MART',
        'msg':'Planning / Design / HTML,CSS,JavaScript,Python /',
        'link':'https://mensmart-main7295-lowlands.herokuapp.com/',
        'info':'メンズの洋服を取り揃えた"MENS MART"のWEBサイトは、男性ユーザー向けにスタイリッシュでシンプルな作りに仕上げています。また、白と黒を使い分けることで商品を際立たせています。ECサイト仕様に多様な機能を追加し、決済システムを導入しています。',
        'image_sp':'work/sp/image_sp_06.png',
        'image01':'work/page06/image01.png',
        'image02':'work/page06/image02.jpg',
        'image03':'work/page06/image03.jpg',
        'image04':'work/page06/image04.jpg',
    }
    return render(request, 'main.html', params)


def work_page7(request):
    params = {
        'name':'東武アーバンパークライン',
        'msg':'Design / HTML,CSS,JavaScript /',
        'link':'http://limeokapi95.sakura.ne.jp/work/urban',
        'info':'東武アーバンパークラインのイメージカラーである、黄緑色と青色のラインを使用したWEBサイトに仕上げています。イラストや文字にモーションを取り入れることで関心を高めアーバンパークラインに興味を持っていただけるように仕上げました。',
        'image_sp':'work/sp/image_sp_07.png',
        'image01':'work/page07/image01.png',
        'image02':'work/page07/image02.jpg',
        'image03':'work/page07/image03.jpg',
        'image04':'work/page07/image04.jpg',
    }
    return render(request, 'main.html', params)


def work_page8(request):
    params = {
        'name':'OPERA(オペラ)',
        'msg':'Design / HTML,CSS,JavaScript /',
        'link':'http://limeokapi95.sakura.ne.jp/work/cosmetic/',
        'info':'',
        'image_sp':'work/sp/image_sp_08.png',
        'image01':'work/page08/image01.png',
        'image02':'work/page08/image02.jpg',
        'image03':'work/page08/image03.jpg',
        'image04':'work/page08/image04.jpg',
    }
    return render(request, 'main.html', params)




