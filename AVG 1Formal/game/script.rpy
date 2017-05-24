# 您可以在此编写游戏的脚本。

# 下方的image命令可用于定义一个图像。
# 例：image eileen happy = "eileen_happy.png"

# 下方的define命令可定义游戏中出现的角色名称与对应文本颜色。
# 译注：define还可以定义很多功能，具体请参阅官方文档。

image xy = u"images/咲夜.png"
define e = Character('Eileen', color="#c8ffc8")
define n = Character(None, kind=nvl)
define cwy = Character('乘务员', kind=nvl)
define bm = Character('?', kind=nvl)
define pj = Character('平京', kind=nvl)
define mxz = Character('美香紙', kind=nvl)
define txa = Character('同学A', kind=nvl)
define txb = Character('同学B', kind=nvl)
define ss = Character('山神', kind=nvl)
define zs = Character('纸神', kind=nvl)
define nw = Character('诺唯', kind=nvl)
define nx = Character('女性', kind=nvl)
define my = Character('末言', kind=nvl)

init python:
     menu = nvl_menu
init:


 
    $ choice = False
    $ style.nvl_label.minwidth = 150
    $ style.nvl_label.text_align = 1.0    
    $ style.nvl_window.background = "#0008"
    $ style.nvl_window.yfill = True
    $ style.nvl_window.xfill = True
    $ style.nvl_window.xmargin = 640
    $ style.nvl_window.ymargin = 30
    $ style.nvl_window.xpadding = 40
    $ style.nvl_window.ypadding = 60
    $ style.nvl_vbox.box_spacing = 30
# 引用游戏OP视频，在进入程序主菜单显示前自动播放。
# 此处也可以使用图片代替。
# label splashscreen:
    # $ renpy.movie_cutscene('data/op.avi')
    # return

# 游戏从这里开始。
label start:

# 下面的参数用于设定是否允许用户通过点击或快进功能跳过转场特效。
    $ _skipping = True

# 是否允许用户通过点击或快进跳过暂停时间。
# 暂停时间是通过pause命令实现的，具体请参阅官方文档。
    $ _dismiss_pause = True

# 译注：以上两个命令都是出现后生效，并且有跨label继承性，
# 通常我们设置为True以保证用户能够使用快进，
# 但如果您在特殊情况下设置为False后，应在合适的地方重新
# 调整为True，以便用户能够正常进行游戏。
# 此功能包含在最新的每夜版SDK中，当您发现正式版SDK不兼容此命令时，
# 请将SDK的更新通道设置为每夜版，并进行更新。
#    show xy
# 已完成适应章节（纯文本）
# chapter0
# chapter1
# chapter_inconti
    jump chapter0    
label main1:
    jump chapter_inconti

    jump chapter1
label main2:
#    e "您已经创建了一个新的Ren'py游戏。"

#   e "当您给您的游戏加入了故事剧情，图片和音乐，您就能将它与世界分享了。"

    return
