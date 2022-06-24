from django.contrib import admin

# Register your models here.
from app.models import User, Course, Grade, Message


class UserAdmin(admin.ModelAdmin):
    fields = (
        'user_name', 'user_pass', 'user_id', 'message_name', 'message_sex', 'message_age', 'message_phone',
        'message_image')
    list_display = (
        'user_name', 'user_pass', 'user_id', 'message_name', 'message_sex', 'message_age', 'message_phone',
        'message_image',
        'add_time')


class CourseAdmin(admin.ModelAdmin):
    fields = ('course_id', 'course_name', 'semester', 'course_teacher')
    list_display = ('course_id', 'course_name', 'semester', 'course_teacher', 'add_time')


class GradeAdmin(admin.ModelAdmin):
    fields = ('user_name', 'course_id', 'grade_value', 'grade_complain')
    list_display = ('user_name', 'course_id', 'grade_value', 'grade_complain', 'add_time')
    actions = ['import_grade']

    def import_grade(self, request):
        pass

    import_grade.short_description = '导入成绩'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    import_grade.type = 'success'

    # 给按钮追加自定义的颜色
    import_grade.style = 'color:black;color:white'

    # 链接按钮，设置之后直接访问该链接
    # 3中打开方式
    # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 设置了action_type，不设置url，页面内将报错
    # 设置成链接类型的按钮后，custom_button方法将不会执行。

    import_grade.action_type = 0
    import_grade.action_url = '/importGrade'


class MessageAdmin(admin.ModelAdmin):
    fields = ('sender', 'receive', 'message', 'read')
    list_display = ('sender', 'receive', 'message', 'read', 'add_time')


admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Message, MessageAdmin)

# 修改网页title和站点header
admin.site.site_title = "学生成绩后台"
admin.site.site_header = "学生成绩管理"
